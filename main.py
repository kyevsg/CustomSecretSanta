from flask import Flask, render_template
import random
from secret_santa import *

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/secretsanta', methods = ['GET', 'POST'])
def secretsanta():
  return render_template('secretsanta.html')

@app.route('/wishlists')
def wishlists():
  return render_template('wishlists.html')
  
"""
# use if not running on repl
if __name__ == '__main__':
  app.run()
"""

# use if running on repl
if __name__ == "__main__":  
  app.run( # Starts the site
    host='0.0.0.0',  # sStablishes the host, required for repl to detect the site
    port=random.randint(2000, 9000)  # Randomly select the port the machine hosts on.
)