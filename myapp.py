# import flask
from flask import Flask, render_template
from flask_mysqldb import MySQL
#main app
app = Flask(__name__)

#database config
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'latihan_flask'
#init mysql
mysql = MySQL(app)
# set route untuk /
@app.route('/')
#function index
def index():
    #print text
    return render_template('index.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/users/')
def users():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users")
    data = cur.fetchall()
    cur.close()
    return render_template('users.html', users=data)
#debug, untuk update server dev otomatis
if __name__ == "__main__":
    app.run(debug=True)