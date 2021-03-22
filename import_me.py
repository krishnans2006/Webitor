import os

def read_file(method='w'):
    global f
    f = open('src/templates/Trial.html', method)
read_file('a')
def make_sth(q,type='button',x=str(0),y=str(0),text=''):
    global f
    button_template = '''
    <style>
    .'''+str(type)+str(q)+''' {
      position: relative;
      top: '''+y+'''; 
      left: '''+x+'''; 
    }
    </style>
    <'''+str(type)+''' class='''+str(type)+str(q)+'''>
    '''+str(text)+'''
    </'''+str(type)+'''>
    '''
    f.write(button_template)

def close_time():
    global f
    f.close()
    read_file('a')
def change_color(color='white'):
    global f
    f.close()
    f = open('src/templates/Trial.html', 'r')
    q=f.read()
    print(q)
    z=''
    a=q.split('\n')

    print(a)
    b=0
    for i in a:
        if 'bgcolor' in i:
            a[b] = f"<body bgcolor='{color}'>"
        b+=1

    print(a)
    f = open('src/templates/Trial.html', 'w')
    f.write('\n'.join(a))
    print('\n'.join(a))
    close_time()
change_color()