from flask import Flask, render_template, request
from qrcodeMaker import *
import os
import pymysql
from dotenv import load_dotenv
load_dotenv(verbose=True)
USERNAME = "seohyun218"
db = pymysql.connect(host=os.getenv("HOST"), user=os.getenv("USER"), port=int(os.getenv("PORT")), passwd=os.getenv("PASSWD"), db=os.getenv("DB"), charset='utf8')
cursor = db.cursor()
#cursor.execute(f'create table users (id VARCHAR(200) NOT NULL, name VARCHAR(200), period int(50), time varchar(50), water int(50), location varchar(50),PRIMARY KEY(id));')
#cursor.execute(f'insert into {USERNAME} VALUES("seohyun218_flowername_1","rose",70,10,20,"13:10",3)')
db.commit()

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route("/register")
def register():
    return render_template('register.html')

@app.route('/result',methods=['POST','GET'])
def result():
    if request.method == 'POST':
        result = request.form
        name = request.form.get('name')
        period = int(request.form.get('period'))
        time = str(request.form.get('time'))
        water = int(request.form.get('water'))
        location = request.form.get('location')

        id = USERNAME+'_'+name
        insert = 'insert into users VALUES( \"{}\", \"{}\", {}, \"{}\", {}, \"{}\")'.format(id, name, period, time, water, location)
        cursor.execute(insert)
        db.commit()
        result = request.form
    makeQRcode(id)
    return render_template('result.html', result = result)

@app.route("/mypage")
def mypage():
    sql = f'select * from users'
    cursor.execute(sql)
    rows = cursor.fetchall()

    print(rows)
    return render_template('mypage.html', rows=rows)



if __name__ == '__main__':
    app.run()
