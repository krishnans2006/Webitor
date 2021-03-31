import configparser
from flask import session
from site import *
from html5print import HTMLBeautifier
from exceptions import UnexpectedValue

config = configparser.ConfigParser()

config.sections()

config.read('generator.cfg')


boiler = config['boilerplate']['bp']

def generator():
    gen_code = str(HTMLBeautifier.beautify(boiler, 4))
    return str(gen_code)