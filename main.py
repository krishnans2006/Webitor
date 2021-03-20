from src import create_app
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
# Hey # hello for some reason the python extension dooes not work when i join vs shares, i am using vscode insiders so maybe its a new bug or something 
# Ok no problem
# So what I'm thinking is you can keep working on the /create feature
# I can try working on the site builder that Akki started mkay, so what do you want me to do with the /create feature, what needs to be done?
# So when you choose theme/type, it generates basic site, right? site.py so basically i am writing html
# Not really... well sorta but you mainly need to assign the variable and pass it to create_site so I can test that, ok 
# The other part is just making some basic Bootstrap code that works :)
# ok so am i just getting variables from create.js those things from before
# Yeah just using whatever type and style they chose, make a basic template. So like have a different `<style>` section for each style
# And have a different <body> section for each type, and just put it all together and combine it into one long (multiline optional) string, okay i will try............. and do that NOice
# Ok, Good Luck! lmk on Discord (or come to where I am) if you want me to run it, yeah ok