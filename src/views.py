from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/', methods=["GET", "POST"])
def index():
    return render_template('Index/index.html')

@views.route('/about', methods=["GET", "POST"])
def about():
    return render_template('About/about.html')

