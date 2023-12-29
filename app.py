from flask import *

import pymysql

# start 
app=Flask(__name__)
app.secret_key="123ghuutvcrfbngy"

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/homepage')
def homepage():
    return render_template('/index.html')


@app.route('/contact')
def contact():
    return render_template('/contact.html')



@app.route('/women')
def women():
    return render_template('/women.html')

@app.route('/kids')
def kids():
    return render_template('/kids.html')

@app.route('/unisex')
def unisex():
    return render_template('/unisex.html')

@app.route('/men')
def men():
    return render_template('/men.html')

@app.route('/login', methods=['POST','GET'])
def login():
    if request.method =='POST':
        username = request.form['username']
        password = request.form['password']
      
     
        connection = pymysql.connect(host='localhost', user='root', password='', database='perfumecollectiondb')

        cursor = connection.cursor()
        sql = 'select * from users where username =%s and password =%s'
        data = (username, password)
        cursor.execute(sql,data)

        count = cursor.rowcount

     
        if count == 0:
            return render_template('login.html', message ='Invalid Credential')
        else:
            # sessions : Store Information About a specific user
            user_record = cursor.fetchall()
            session['key'] = user_record[1]
            session['user_id'] = user_record[0]
            # session['username'] = user_record[2]
          
            return redirect('/')
    else:
       return render_template('login.html', message = 'Please sign up Here')

@app.route('/sign_up', methods=['POST','GET'])
def sign_up():
    if request.method =='POST':
        username = request.form['username']
        password = request.form['password']
      
     
        connection = pymysql.connect(host='localhost', user='root', password='', database='perfumecollectiondb')

        cursor = connection.cursor()
        sql='insert into users (username,password ) values(%s,%s)'
      
        data = (username, password)
        cursor.execute(sql,data)
        connection.commit()

        return render_template('sign_up.html',message='user registered successfully') 
       
    else:
       return render_template('sign_up.html', message = 'Please Login in Here')






@app.route('/buy')
def buy():
    return render_template('/buy.html')

@app.route('/about')
def about():
    return render_template('/about.html')

@app.route('/shipping')
def shipping():
    return render_template('/shipping.html')







       
app.run(debug=True)