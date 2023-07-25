from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

# Required
app.config["MYSQL_USER"] = "user"
app.config["MYSQL_PASSWORD"] = "password"
app.config["MYSQL_DB"] = "database"
# Extra configs, optional:
app.config["MYSQL_CURSORCLASS"] = "DictCursor"
app.config["MYSQL_CUSTOM_OPTIONS"] = {"ssl": {"ca": "/path/to/ca-file"}}  # https://mysqlclient.readthedocs.io/user_guide.html#functions-and-attributes

mysql = MySQL(app)

@app.route("/")
def users():
    cur = mysql.connection.cursor()
    cur.execute("""SELECT user, host FROM mysql.user""")
    rv = cur.fetchall()
    return str(rv)

if __name__ == "__main__":
    app.run(debug=True)



    # mysql = MySQL()
# app.config['MYSQL_USER'] = 'user_name'
# app.config['MYSQL_PASSWORD'] = 'user_password'
# app.config['MYSQL_HOST'] = 'sql3.example.net'
# app.config['MYSQL_DB'] = 'Database_name'
# app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
# mysql.init_app(app)