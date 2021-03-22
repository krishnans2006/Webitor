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
    document.getElementById("preview").innerHTML = document.getElementById("code").value
    createDomTree();
    console.log("Sending!")
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/edit/"+document.getElementById("sitename").innerHTML);
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.send("code=" + document.getElementById("code").value);
}

window.onload = function () {
    document.getElementById("preview").innerHTML = document.getElementById("code").value
    createDomTree();
}

// THE CULPRITS

var domTree = document.getElementById("dom-tree");
var page = document.getElementById("preview");
var highlight = document.getElementById("highlight");



// THE CREATION OF THE DOM TREE LOGIC

function createDomTree() {
    domTree.innerHTML = "";

    function walkElement(element, indent = 0) {
        if (!(element.id == "preview")) {
            domTree.appendChild(document.createTextNode("  ".repeat(indent)));

            var span = document.createElement("span");
            span.textContent = "<" + element.tagName.toLowerCase() + ">";
            span.attachedElement = element;
            element.attachedDomTreeElement = span;
            span.className = "dom-element";
            domTree.appendChild(span);

            domTree.appendChild(document.createTextNode("\n"));
        }

        for (let child of element.children) {
            walkElement(child, indent + 1);
        }
    }

    walkElement(page);
}



// THE HIGHLIGHTING LOGIC

let currentlyHighlightedItem = null;

function highlightElement(element, domTreeElement) {
    if (currentlyHighlightedItem == element)
        return;

    let rect = element.getBoundingClientRect();

    highlight.style.left = rect.x + "px";
    highlight.style.top = rect.y + "px";
    highlight.style.width = rect.width + "px";
    highlight.style.height = rect.height + "px";

    page.appendChild(highlight);

    let selectedDomTreeElement = document.querySelector(".dom-element.selected");
    if (selectedDomTreeElement) {
        selectedDomTreeElement.classList.remove("selected");
    }
    domTreeElement.classList.add("selected");

    currentlyHighlightedItem = element;
}



// EVENTS

// on the dom tree elements

domTree.addEventListener("mousemove", function (e) {
    let target = e.target;
    if (target.classList.contains("dom-element")) {
        highlightElement(target.attachedElement, target);
    }
}, true);

domTree.addEventListener("click", function (e) {
    let target = e.target;
    if (target.classList.contains("dom-element")) {
        highlightElement(target.attachedElement, target);
    }
}, true);

domTree.addEventListener("mouseleave", function (e) {
    highlight.remove();
    currentlyHighlightedItem = null;
    let selectedDomTreeElement = document.querySelector(".dom-element.selected");
    if (selectedDomTreeElement) {
        selectedDomTreeElement.classList.remove("selected");
    }
});

// on the page itself

page.addEventListener("mousemove", function (e) {
    let target = e.target;
    if (target.attachedDomTreeElement) {
        highlightElement(target, target.attachedDomTreeElement);
    }
}, true);

page.addEventListener("mouseleave", function (e) {
    highlight.remove();
    currentlyHighlightedItem = null;
    let selectedDomTreeElement = document.querySelector(".dom-element.selected");
    if (selectedDomTreeElement) {
        selectedDomTreeElement.classList.remove("selected");
    }
});
