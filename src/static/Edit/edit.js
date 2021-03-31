const items = {
    Navbar: function () {
        return `<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Navbar</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="#">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Link</a>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Dropdown
          </a>
          <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
            <li><a class="dropdown-item" href="#">Action</a></li>
            <li><a class="dropdown-item" href="#">Another action</a></li>
            <li><hr class="dropdown-divider"></li>
            <li><a class="dropdown-item" href="#">Something else here</a></li>
          </ul>
        </li>
        <li class="nav-item">
          <a class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true">Disabled</a>
        </li>
      </ul>
      <form class="d-flex">
        <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
        <button class="btn btn-outline-success" type="submit">Search</button>
      </form>
    </div>
  </div>
</nav>`;
    },
    "Form": function () {
        return `<form>
  <div class="mb-3">
    <label for="exampleInputEmail1" class="form-label">Email address</label>
    <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
    <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>
  </div>
  <div class="mb-3">
    <label for="exampleInputPassword1" class="form-label">Password</label>
    <input type="password" class="form-control" id="exampleInputPassword1">
  </div>
  <div class="mb-3 form-check">
    <input type="checkbox" class="form-check-input" id="exampleCheck1">
    <label class="form-check-label" for="exampleCheck1">Check me out</label>
  </div>
  <button type="submit" class="btn btn-primary">Submit</button>
</form>`;
    },
    Button: function () {
        return `<button type="button" class="btn btn-primary">Button</button>`;
    },
    Link: function () {
        return `<a class="btn btn-link">Link</a>`;
    },

    Card: function () {
        return `<div class="card" style="width: 18rem;">
  <img src="..." class="card-img-top" alt="...">
  <div class="card-body">
    <h5 class="card-title">Card title</h5>
    <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
    <a href="#" class="btn btn-primary">Go somewhere</a>
  </div>
</div>`;
    },
    Image: function () {
        return "<img src='' alt='' />";
    },
    Video: function () {
        return (`<video width="320" height="240" controls>
  <source src="movie.mp4" type="video/mp4">
  <source src="movie.ogg" type="video/ogg">
Your browser does not support the video tag.
</video>`);
    },
    "Line-Break": function () {
        return "<br />";
    },
    Testimonial: function () {
        return (
            '<div class="container"><img src="" alt="Avatar" style="width:90px"><p><span>John Doe.</span> CEO at Mighty Schools.</p><p>John Doe saved us from a web disaster.</p></div>'
        );
    },
    "Inner-Section": function () {
        return '<section> <h1>Example</h1> <p>Cool things to say</p> <section> <h1>Dummy Text</h1> <p>some info....</p> <img src="" /> </section> <section> <h1>Dummy Text</h1> <p>some other info info....</p> <img src="" /> </section></section>';
    },
    "Text-Editor": function () {
        return (
            '<label for="text-editor">Your Text Editor</label><textarea id="text-editor" name="text-editor" rows="" cols="">Text</textarea>'
        );
    },
};

// THE CULPRITS

var domTree = document.getElementById("dom-tree");
var page = document.getElementById("preview");
var highlight = document.getElementById("highlight");

function insertAtCursor(item) {
    myValue = items[item]();
    editor.insert(myValue);
    document.getElementById("preview").innerHTML = editor.getValue();
    createDomTree();
}

window.onload = function () {
    document.getElementById("preview").innerHTML = document.getElementById(
        "code"
    ).value;
    createDomTree();
    editor = ace.edit(document.getElementById("code"), {
        theme: "ace/theme/tomorrow",
        mode: "ace/mode/html",
        wrap: true,
        autoScrollEditorIntoView: true,
        maxLines: 45,
        minLines: 30
    })
    editor.session.on('change', function(delta) {
        console.log("....")
        newVal = editor.getValue();
        document.getElementById("preview").innerHTML = newVal;
        createDomTree()
        var xhr = new XMLHttpRequest();
        xhr.open("POST", "/edit/" + document.getElementById("sitename").innerHTML);
        xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
        xhr.send("code=" + newVal);
    })
};


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
