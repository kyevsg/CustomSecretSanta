from flask import Flask, render_template
from secret_santa import *

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/secretsanta')
def secretsanta():
  return render_template('secretsanta.html')

@app.route('/wishlists')
def wishlists():
  return render_template('wishlists.html')

if __name__ == '__main__':
  app.run()