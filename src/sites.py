from flask import Blueprint, flash, redirect, render_template, request, url_for, session, current_app
from .models import *

sites = Blueprint('sites', __name__)

themes = {
    "Cool Breeze": "",
    "Sunrise": "",
    "Dark Mountains": ""
}

types = {
    "Simple Text": "",
    "Cards": ""
}

boilerplate = [
    "",
    "",
    ""
]
# So what I'm thinking is when you make the website, it uses boilerplate[0] + theme_style + boilerplate[1] + type_html + boilerplate[2] - yeah that could work well

# So theme style is just <style>Specific rules for theme</style>
# Type is just some content
# boilerplate is the base html code for each section 
# Yeah exactly So element 1 is all code until the style tag, element 2 is style tag to content, element 3 is content to the end (like scripts) - mkay
# Finally we have elements - Elements should be in JS array and when they drag and drop, 
# it finds out which part of the code they dropped it on and adds that element code right there - yes indeed 
# so we need functionality similar to the Inspect tool... like from Console you can hover over elements and find their code, we can do that by targeting div elements, and giving each main and subsection a div class we already know YEAH, the question is how............................, to be honest their is probably a libary that could do this...



@sites.route('/projects', methods=["GET", "POST"])
def projects():
    if not session.get('logged_in'):
        flash('You must be logged in to view your projects!', category='error')
        return redirect(url_for('auth.login'))
    return render_template('Profile/profile.html', sites=d_get_sites(session.get("username"), session.get("email")))


@sites.route('/create', methods=["GET", "POST"])
def create():
    if not session.get('logged_in'):
        flash("You must login to create a website!", category='error')
        return redirect(url_for("auth.login"))
    else:
        styles = [{'style': 'Cool Breeze'}, {
            'style': 'Sun Rise'}, {'style': 'Dark Mountains'}]
        types = [{'type': 'Test One'}, {
            'type': 'Test Two'}, {'type': 'Test Three'}]

        if request.method == "POST":
            web_name = request.form.get("web-name")
            web_style = request.form.get("web-style")
            web_type = request.form.get("web-type")
            flash("Test Flash Message", category='success')
        else:
            return render_template('Create/create.html', styles=styles, types=types)


@sites.route('/edit/<sitename>', methods=["GET", "POST"])
def edit(sitename=None):
    if not session.get('logged_in'):
        flash("You must be logged in to edit your projects!", category='error')
        return redirect(url_for('auth.login')) 
    if not sitename:
        flash("An Internal Error Occured! This has been reported and will be resolved soon. Thanks for the patience!", category="error")
    if request.method == "POST":
        new_code = request.form.get("code")
        print(new_code)
    site = d_get_site(session.get("Username"), session.get("Email"), sitename)
    return render_template('Edit/edit.html', name=site[0], code=site[1]["HTML"])
