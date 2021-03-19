
f=open(f'templates/{file_name}', 'r')
q=f.read()
i=0
a=[]
z={}
for i in q.split('\n'):
    if '.' in i:
        a.append(z)
        z={}
        z['name']=i[5:].split(' ')[0]
    elif 'top' in i:
        z['y']=i.replace(' ', '')[4:-3]
    elif 'left' in i:
        z['x'] = i.replace(' ', '')[5:-3]
    elif '</style>' in i:
        a.append(z)
        break
b=[]
c={}
for i in q.split('\n'):
    if '<' in i and 'style' not in i and '/' not in i:
        g=i.replace(' ','').split('class')
        c['Function']=g[0][1:]
        c['Class']=g[1].replace('=','').split('>')[0]
        b.append(c)
print(b)
a=a[1:]
f.close()
f=open('templates/Trial2.html', 'w')
f.write('<style>')
for i in a:
    f.write(f'.{i["name"]}'+"{"+f'''position: relative;
    top: {i['y']}px;
    left: {i['x']}px;'''
    +'}'+'\n')
f.write('</style>')
for i in b:
    f.write('\n')
    f.write(f'<{i["Function"]} class={i["Class"]}>button</button>')
f.close()
