import os
end_template = '''
</body>
</html>
'''
def add_color(color):
    global f
    f = open('templates/Trial.html', 'w')
    html_template = f"""<html> 
        <head> 
        <title>Trial</title> 
        </head> 
        <body bgcolor={color}> 
        """
    f.write(html_template)

def use_button(q,text='button',x=str(0),y=str(0)):
    global f
    print('using')
    button_template = '''
    <style>
    .button'''+str(q)+''' {
      position: relative;
      top: '''+y+'''; 
      left: '''+x+'''; 
    }
    </style>
    <button class=button'''+str(q)+'''>'''+text+'''
    </button>
    '''
    f.write(button_template)
    f.close()
def use_heading(x,y,q,i,t):
    template = '''
    <style>
    .head'''+str(q)+''' {
      position: relative;
      top: '''+y+'''px; 
      left: '''+x+'''px; 
    }
    </style>'''
    template += '<h'+i+' class=head'+q+'>'
    y=input('Text : ')
    template+=y+'</h'+i+'>'
    f.write(template)

def use_form(q):
    f.write('<form>')

    while True:
        i1 = input('What in your form :')
        if 'input' in i1:
            x,y,t = i1.split(' ')[1:]
            input_class = '''
            <style>
            .i'''+q+'''
             {
              position: relative;
          top: '''+x+'''; 
          left: '''+y+'''; 
             }
             </style>'''
            f.write(input_class)
            f.write('<input class=i'+q+' type='+t+'>')
            f.write('</input>')
        else:
            break

def main():
    q =x = y = '0'
    i = input('bg color : ')
    use_temp1(i)
    while True:
        i = input('Command  : ')
        if 'button'in i:
            y,x = i.split(' ')[1:]
            f.write(use_button(x,y,q))

        elif 'form' in i:
            use_form(q)

        elif 'heading'in i:
            y,x = i.split(' ')[1:]
            use_heading(x,y,q)
        else:
            break
        q=str(int(q)+1)
    f.write(end_template)
    f.close()