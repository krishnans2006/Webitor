from flask import Blueprint, render_template, request, flash, redirect, url_for

auth = Blueprint('auth', __name__)