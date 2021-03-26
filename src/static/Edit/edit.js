const items = {
    "Navbar": function (args) { return "<p>A Navbar I guess???</p>"; },
    "Contact-Form": function (args) { return ""; },
    "Footer": function (args) { return ""; },
    "Button": function (args) { return '<button>' + args[0] + '</button>'; },
    "Link": function (args) { return '<a>' + args[0] + '</a>'; },
    "Image": function (args) { return ''; },
    "Line-Break": function (args) { return "<br>"; },
    "Testimonial": function (args) { return ""; },
    "Inner-Section": function (args) { return ""; },
    "Text-Editor": function (args) { return ""; },
    "Video": function (args) { return ""; },
    "Google-Maps": function (args) { return ""; }
}

function insertAtCursor(item, args=[]) {
    myValue = items[item](args);
    myField = document.getElementById("code")
    if (document.selection) {
        myField.focus();
        sel = document.selection.createRange();
        sel.text = myValue;
    } else if (myField.selectionStart || myField.selectionStart == '0') {
        var startPos = myField.selectionStart;
        var endPos = myField.selectionEnd;
        myField.value = myField.value.substring(0, startPos)
            + myValue
            + myField.value.substring(endPos, myField.value.length);
        myField.selectionStart = startPos + myValue.length;
        myField.selectionEnd = startPos + myValue.length;
    } else {
        myField.value += myValue;
    }
    document.getElementById("preview").innerHTML = document.getElementById("code").value
    createDomTree();
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
