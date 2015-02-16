from flask import Flask
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'scrapy'
app.config['MYSQL_DATABASE_PASSWORD'] = 'scrapy'
app.config['MYSQL_DATABASE_DB'] = 'scrapy'
app.config['MYSQL_DATABASE_HOST'] = '52.10.2.102'
mysql.init_app(app)

@app.route("/")
def hello():
    return "Welcome to Python Flask App!"

if __name__ == "__main__":
    app.debug = True  # autoreload
    app.run(host='0.0.0.0')  # allow outside

@app.route("/select")
def list():
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * from scrapy_football_player")
    data = cursor.fetchone()
    if data is None:
        return "Username or Password is wrong"
    else:
        return "Logged in successfully"