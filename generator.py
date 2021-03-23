import configparser
from flask import session
from site import *
from html5print import HTMLBeautifier
from exceptions import UnexpectedValue

config = configparser.ConfigParser()

config.sections()

config.read('generator.cfg')


boiler = config['boilerplate']['bp']

def generator(style, type):
    if style == 'Cool-Breeze':
        gen_code = str(HTMLBeautifier.beautify(boiler, 4)) + str(config['Styles']['cool_breeze'])
    elif style == 'Dark-Mountain':
        gen_code = str(HTMLBeautifier.beautify(boiler, 4)) + str(config['Styles']['dark_mountains'])
    elif style == 'Sunrise':
        gen_code = str(HTMLBeautifier.beautify(boiler, 4)) + str(config['Styles']['sunrise'])
    else:
        raise UnexpectedValue('Error! Wrong request type')

    
    return str(gen_code)