from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return('you have successfully used flask route')

@app.route('/get1')
def get():
    return('Accessed the get output')

@app.route('/username/<name>')
def usrname(name):    
    return({'Name':name})

if __name__ == '__main__':
    app.run(debug=True)



