from flask import Flask
app = Flask(__name__)
### simple flask app
@app.route('/')
def hello():
    return 'Hello World!\n'
if __name__ == '__main__':
    app.run()