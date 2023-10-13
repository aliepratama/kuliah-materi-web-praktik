# import flask
from flask import Flask, render_template

#main app
app = Flask(__name__)

# set route untuk /
@app.route('/')
#function index
def index():
    #print text
    return render_template('index.html')

@app.route('/about/')
def about():
    return render_template('about.html')

#debug, untuk update server dev otomatis
if __name__ == "__main__":
    app.run(debug=True)