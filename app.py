from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'dela'

if __name__ == '__main__':
    print('\nnub\n')
    app.run(debug=True, host='0.0.0.0')