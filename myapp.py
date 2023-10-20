# import flask
from flask import Flask, render_template, session, request, redirect, url_for
from flask_mysqldb import MySQL
#main app
app = Flask(__name__)
app.secret_key = 'alhamdulillah'
#database config
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'latihan_flask'
#init mysql
mysql = MySQL(app)

# @app.route('/')
# def index():
#     cur = mysql.connection.cursor()
#     cur.execute("SELECT * FROM users")
#     data = cur.fetchall()
#     cur.close()
#     return render_template('index.html', users=data)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and 'inpEmail' in request.form and 'inpPass' in request.form:
        email = request.form['inpEmail']
        passwd = request.form['inpPass']
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM users WHERE email = %s AND password = %s', (email, passwd))
        result = cur.fetchone()
        if result:
            session['is_logged_in'] = True
            session['username'] = result[1]
            return redirect(url_for('home'))
        else:
            return render_template('login.html')
    else:
        return render_template('login.html')
@app.route('/home')
def home():
    if 'is_logged_in' in session:
        return render_template('home.html')
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('is_logged_in', None)
    session.pop('username', None)
    return redirect(url_for('login'))
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