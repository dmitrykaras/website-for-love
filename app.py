from flask import Flask, request, render_template, flash, redirect, url_for
from flask import Flask, render_template, request
import json
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np
import io
import base64
app = Flask(__name__)
app.secret_key = 'your_secret_key'

users = {
    'Вероника': 'я люблю тебя'
}
@app.route('/login', methods=['GET', 'POST'])
def login():
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username in users and users[username] == password:
            return redirect(url_for('transitional'))
        else:
            flash('Неверный логин или пароль!', 'error')
            return redirect(url_for('login'))
    return render_template('login.html',background_image='/static/images/image.jpg')

@app.route('/transitional')
def transitional():
    return render_template('transitional.html')


@app.route('/punishment')
def pipiska():
    return render_template('punishment.html')

@app.route('/love_general_1')
def love_general_1():
    return render_template('love_general_1.html')

@app.route('/love_general_2')
def love_general_2():
    return render_template('love_general_2.html')

if __name__ == '__main__':
    app.run(debug=True)