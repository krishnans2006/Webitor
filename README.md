# Webitor

Webitor is a website maker, using complex visualisation, and live updating web pages.

You can host it on a subdomain on our website, and download the source code for yourself.

And the best part, is that this is all completely free! We believe making a website should be free of charge, and a great experience.

## Installation for developers

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the required modules.

```bash
git clone https://github.com/KrishnanS2006/AlgoExperts.git
pip install requirements.txt
python main.py
echo Wow this is an amazing application.
```

## Usage

### Backend Construction

```python

modules = ["Flask", "firebase-admin", "Authlib", "werkzeug-security", "gunicorn"]

def backend_construction(modules, web_provider, database):
    for module in modules:
        print(f"Yes! {module} is a great tool for constructing the backend of our web application!")

    if web_provider == "Heroku" and database == "firebase":
        print("""
        Heroku is a great, free web provider that we have used for our project. It is reliable, and a amazing temporary home for our project. Firebase is also something that we love to use in our project, and we advise for you to use it too! It's documentation is amazing, and it's api is easy to understand, and so useful for managing, and storing schemas in your databases!
        """)

    else:
        print("Why would we use anything else other than something like Heroku and Firebase?")

```

### Frontend Construction

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" content="How we made the Frontend for Webitor!" />
  </head>
  <body>
    <div class="First of all">
      <div class="We used many different things to supply our Frontend">
        <div class="These things can range from: ">
          <ul>
            <li>Using Pure HTML and CSS</li>
            <li>Bootstrap</li>
            <li>Javascript to format our text editor and websites</li>
            <li>HTML5Print module to format html from python!</li>
          </ul>
          <a class="Link to Bootstrap" href="https://getbootstrap.com/">
          <a class="Link to HTML5Print" href="https://pypi.org/project/html5print/">
        </div>
        <div id="it-was-tricky">It was tough</div>
      </div>
    </div>
  </body>
  <footer>
    <script>
        const difficulty = document.getElementById('it-was-tricky')

        const showDifficulty = (difficulty) => {
            console.log(`${difficulty}`)
        };

        const theRealDifficulty = () => {
            difficulty.innerHTML = "But we pushed through!";
        }
    </script>
  </footer>
</html>
```

## Resources

[Heroku](https://www.heroku.com/)

[Firebase](https://firebase.google.com/)

[Python](https://www.python.org/)

[Javascript](https://www.javascript.com/)

[Google-Auth](https://cloud.google.com/cloud-console/)

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure it is a neccessary change!

## License

[MIT](https://choosealicense.com/licenses/mit/)
