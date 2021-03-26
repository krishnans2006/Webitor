const items = {
  Navbar: function () {
    return "<div class='topnav'><a class='active' href='/edit/'>Home</a><a href='#about'>News</a><a href='#contact'>Contact</a><a href='#projects'>Projects</a></div>";
  },
  "Contact-Form": function () {
    return "<div class='container'> <form action='POST'> <label for='fname'>First Name</label> <input type='text' id='fname' name='firstname' placeholder='Your name..'> <label for='lname'>Last Name</label> <input type='text' id='lname' name='lastname' placeholder='Your last name..'><label for='subject'>Subject</label> <textarea id='subject' name='subject' placeholder='Write something..' style='height:200px'></textarea> <input type='submit' value='Submit'> </form></div>";
  },
  Footer: function (args) {
    return (
      "<footer> <h3>&copy;" +
      args[0] +
      ". All Rights Reserved.</h3><p>Author: " +
      args[0] +
      "</p> <p><a href='mailto:johndoe@example.com'>johndoe@example.com</a></p></footer>"
    );
  },
  Button: function (args) {
    return "<button>" + args[0] + "</button>";
  },
  Link: function (args) {
    return "<a>" + args[0] + "</a>";
  },
  Image: function (args) {
    return "<img src='" + args[0] + "'";
  },
  "Line-Break": function (args) {
    return "<br />";
  },
  Testimonial: function (args) {
    return (
      '<div class="container"><img src="' +
      args[0] +
      '" alt="Avatar" style="width:90px"><p><span>John Doe.</span> CEO at Mighty Schools.</p><p>John Doe saved us from a web disaster.</p></div>'
    );
  },
  innerSection: function () {
    return '<section> <h1>Example</h1> <p>Cool things to say</p> <section> <h1>Dummy Text</h1> <p>some info....</p> <img src="" /> </section> <section> <h1>Dummy Text</h1> <p>some other info info....</p> <img src="" /> </section></section>';
  },
  "Text-Editor": function (args) {
    return (
      '<label for="text-editor">Your Text Editor</label><textarea id="text-editor" name="text-editor" rows="' +
      args[0] +
      '" cols="' +
      args[1] +
      '">Dummy Text!</textarea>'
    );
  },
  Video: function (args) {
    return (
      '<video width="' +
      args[0] +
      '" height="' +
      args[1] +
      '" controls><source src="' +
      args[2] +
      '" type="video/mp4">'
    );
  },
  "Google-Maps": function (args) {
    return "";
  },
};

function insertAtCursor(item, args = []) {
  myValue = items[item](args);
  myField = document.getElementById("code");
  if (document.selection) {
    myField.focus();
    sel = document.selection.createRange();
    sel.text = myValue;
  } else if (myField.selectionStart || myField.selectionStart == "0") {
    var startPos = myField.selectionStart;
    var endPos = myField.selectionEnd;
    myField.value =
      myField.value.substring(0, startPos) +
      myValue +
      myField.value.substring(endPos, myField.value.length);
    myField.selectionStart = startPos + myValue.length;
    myField.selectionEnd = startPos + myValue.length;
  } else {
    myField.value += myValue;
  }
  document.getElementById("preview").innerHTML = document.getElementById(
    "code"
  ).value;
  createDomTree();
}

function code_send() {
  document.getElementById("preview").innerHTML = document.getElementById(
    "code"
  ).value;
  createDomTree();
  console.log("Sending!");
  var xhr = new XMLHttpRequest();
  xhr.open("POST", "/edit/" + document.getElementById("sitename").innerHTML);
  xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
  xhr.send("code=" + document.getElementById("code").value);
}

window.onload = function () {
  document.getElementById("preview").innerHTML = document.getElementById(
    "code"
  ).value;
  createDomTree();
};

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
  if (currentlyHighlightedItem == element) return;

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

domTree.addEventListener(
  "mousemove",
  function (e) {
    let target = e.target;
    if (target.classList.contains("dom-element")) {
      highlightElement(target.attachedElement, target);
    }
  },
  true
);

domTree.addEventListener(
  "click",
  function (e) {
    let target = e.target;
    if (target.classList.contains("dom-element")) {
      highlightElement(target.attachedElement, target);
    }
  },
  true
);

domTree.addEventListener("mouseleave", function (e) {
  highlight.remove();
  currentlyHighlightedItem = null;
  let selectedDomTreeElement = document.querySelector(".dom-element.selected");
  if (selectedDomTreeElement) {
    selectedDomTreeElement.classList.remove("selected");
  }
});

// on the page itself

page.addEventListener(
  "mousemove",
  function (e) {
    let target = e.target;
    if (target.attachedDomTreeElement) {
      highlightElement(target, target.attachedDomTreeElement);
    }
  },
  true
);

page.addEventListener("mouseleave", function (e) {
  highlight.remove();
  currentlyHighlightedItem = null;
  let selectedDomTreeElement = document.querySelector(".dom-element.selected");
  if (selectedDomTreeElement) {
    selectedDomTreeElement.classList.remove("selected");
  }
});
