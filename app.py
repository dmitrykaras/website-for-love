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

@app.route('/setting')
def setting():
    return render_template('setting.html')

@app.route('/transitional')
def transitional():
    return render_template('transitional.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/punishment')
def punishment():
    return render_template('punishment.html')

@app.route('/love_general_1')
def love_general_1():
    return render_template('love_general_1.html')

@app.route('/love_general_2')
def love_general_2():
    return render_template('love_general_2.html')

@app.route('/love_general_3')
def love_general_3():
    return render_template('love_general_3.html')

@app.route('/love_general_4')
def love_general_4():
    return render_template('love_general_4.html')

@app.route('/love_general_5')
def love_general_5():
    return render_template('love_general_5.html')

@app.route('/love_general_6')
def love_general_6():
    return render_template('love_general_6.html')

@app.route('/love_general_7')
def love_general_7():
    return render_template('love_general_7.html')

@app.route('/proverbs')
def proverbs():
    return render_template('proverbs.html')

@app.route('/together')
def together():
    return render_template('together.html')

@app.route('/space')
def space():
    return render_template('space.html')

@app.route('/video')
def video():
    return render_template('video.html')

@app.route('/counter')
def counter():
    return render_template('counter.html')

@app.route('/subtitles')
def subtitles():
    return render_template('subtitles.html')

@app.route('/stickers')
def stickers():
    return render_template('stickers.html')

@app.route('/end')
def end():
    return render_template('end.html')

if __name__ == '__main__':
    app.run(debug=True)