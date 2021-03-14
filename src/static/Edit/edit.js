const checkables = {
    "Navbar": function(text) { return ""; },
    "Contact-Form": function(text) { return ""; },
    "Footer": function(text) { return ""; },
}

const droppables = {
    "Link": function(text) { return '<i>${text}</i>'; },
    "Image": function(source, w=400, h=400, alt="A beautiful image") { return '<img src="${source} width="${w} height="${h}" alt=${alt} />'; },
    "Line-Break": function() { return "<br>"; },
    "Testimonial": function(text) { return ""; },
    "Inner-Section": function() { return ""; },
    "Text-Editor": function() { return ""; },
    "Video": function(link, w=400, h=400) { return ""; },
    "Google-Maps": function() { return ""; }
}


function code_send() {
    console.log("Sending!")
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/edit/"+document.getElementById("sitename").innerHTML);
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.send("code=" + document.getElementById("code").value);
}
