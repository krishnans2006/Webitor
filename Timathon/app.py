from flask import Flask, render_template, request, redirect, url_for
from main import *
import os
app = Flask(__name__)
@app.route('/',methods=['POST','GET'])
def basicStuff():
    if request.method=="POST":
        color = request.form.get('color')
        print(color)
        add_color(color)
        return redirect(url_for('front'))
    return render_template('index.html')

@app.route('/home2',methods=['POST','GET'])
@app.route('/2',methods=['POST','GET'])
def front():
    q=0
    if request.method == "POST":
        data = request.form['js_data']
        x,y = data.split(' ')
        use_button(q=q,text='button',x=x,y=y)
        q+=1
        os.system("start templates\Trial.html")
        return redirect(url_for('basicStuff'))
    return render_template('dragndrop_trial.html')

@app.route('/edit',methods=['POST','GET'])
def edit():
    q=0
    if request.method == "POST":
        data = request.form['js_data']
        print(request.form.get('b'))
        x,y = data.split(' ')
        print(data)
        use_button(q=q,text='button',x=x,y=y)
        q+=1
    return render_template('edit.html',)

app.run(debug=True)