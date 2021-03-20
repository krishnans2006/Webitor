import configparser
config = configparser.ConfigParser()

boilerplate = config['Boilerplate']['boilerplate']

def generator(style, type):
    if style == 'cool-breeze':
        gen_code = str(boilerplate) + str(config['Styles']['cool_breeze'])
    elif style == 'dark-mountains':
        gen_code = str(boilerplate) + str(config['Styles']['dark_mountains'])
    elif style == 'sunrise':
        gen_code = str(boilerplate) + str(config['Styles']['sunrise'])
    else:
        return False

    
    return str(gen_code)
