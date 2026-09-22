from flask import Flask, render_template

app = Flask(__name__)

NAME = '윤효연'
STUDENT_ID = '21011189'
HOBBIES = ['스키', '영화', '볼링']

@app.route('/')
def home():
  return render_template('index.html', name=NAME, student_id=STUDENT_ID)

@app.route('/profile')
def profile():
  return render_template('profile.html', hobbies=HOBBIES)

@app.route('/greet/<name>')
def greet(name):
  return render_template('greet.html', name=name)
