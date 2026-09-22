from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
  return '<h1> 메인페이지 </h1>'

@app.route('/about')
def about():
  return '<h1>소개 페이지</h1>'

@app.route("/test/<uuid:text>")
def route_sample(text) :
  return f'<h1>{text}</h1> <p> 타입은 {type(text).__name__}</p>'

