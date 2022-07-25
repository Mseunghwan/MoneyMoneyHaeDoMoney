from flask import Flask, render_template, request
import psycopg2
import json

def connectDB():
    con = psycopg2.connect(
        host = "localhost",
        database = "MMHDM",
        user = "postgres",
        password = "min95440949@"
    )
    return con


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/search', methods=['POST'])
def search():
    if request.method == "POST":
        input = request.form['searchinput']
        connect = connectDB()
        cur = connect.cursor()
        
        cur.execute("SELECT * FROM moneytable where companyname like '%{}%'".format(input))
        descript = cur.fetchall()
        connect.commit()
        cur.close()
        connect.close()
        if len(descript) > 0:
            return render_template("search.html", descript=descript)
        else:
            return render_template("index.html")


if __name__=='__main__':
    app.run('0.0.0.0')