from allImports import *
from flask import session
import time
import operator
import json




@app.route("/", methods = ["GET"])
def start():
  return render_template("start.html",
                          cfg = cfg)


@app.route("/addstock/<name>/<username>/<startd>/<until>")
def addstock(name, username, startd, until):
    user=Users.get(Users.username==username)
    print user.lastName
    favourite=FavoriteStocks(uid=user.uid,sname=name, Field4=startd,Field5=until)
    favourite.save()
    returnlist=["works", "hello"]
    return json.dumps(returnlist)


@app.route("/home", methods=["GET", "POST"])
def home():
    if request.method == 'POST':
        text = request.form['text']
        stockname=text
        print stockname
        values = []
        labels = []
        newdata=[]
        for record in StockData.select().where(StockData.symbol==stockname):
                new_dict={}
                new_dict["date"]=record.date.strftime("%Y-%m-%d")
                new_dict["price"]=record.close
                newdata.append(new_dict)
        newdata.sort(key=operator.itemgetter('date'))
        fake_val=[]
        fake_lab=[]
        for i in newdata:
            fake_val.append(i["price"])
            fake_lab.append(i["date"])
        for i in range(len(fake_val)-60, len(fake_val)-1):
            values.append(fake_val[i])
        for i in range(len(fake_lab)-60, len(fake_lab)-1):
            labels.append(fake_lab[i])

        max_data=values[len(values)-1]
        print values
        print labels
        start=labels[0]
        final=labels[len(labels)-1]

        return render_template("home.html", cfg=cfg, values=values, labels=labels, max_data=max_data, start=start, final=final, stockname=stockname)

    else:
        stockname="AAPL"
        values = []
        labels = []
        newdata=[]
        for record in StockData.select().where(StockData.symbol=="AAPL"):
                new_dict={}
                new_dict["date"]=record.date.strftime("%Y-%m-%d")
                new_dict["price"]=record.close
                newdata.append(new_dict)
        newdata.sort(key=operator.itemgetter('date'))
        fake_val=[]
        fake_lab=[]
        for i in newdata:
            fake_val.append(i["price"])
            fake_lab.append(i["date"])
        for i in range(len(fake_val)-60, len(fake_val)-1):
            values.append(fake_val[i])
        for i in range(len(fake_lab)-60, len(fake_lab)-1):
            labels.append(fake_lab[i])

        max_data=values[len(values)-1]
        print values
        print labels
        start=labels[0]
        final=labels[len(labels)-1]
        return render_template("home.html", cfg=cfg, values=values, labels=labels, max_data=max_data, start=start, final=final, stockname=stockname)



@app.route("/favorites", methods=["GET"])
def favourites():
    allstocks=[]
    for record in FavoriteStocks.select():
            allstocks.append(record)

    return render_template("favourites.html", cfg=cfg, allstocks=allstocks)

@app.route("/signup", methods=["GET", "POST"])
def signup():
  print "here"
  if 'username' in session:
    return redirect(url_for('home'))
  form = SignupForm()

  if request.method == "POST":
    if form.validate() == False:
        print "not validated"
        return render_template('signup.html', form=form, cfg=cfg)
    else:
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(form.password.data.encode('utf-8'), salt)
        newuser = Users(firstName=form.first_name.data,lastName=form.last_name.data,
                  username=form.username.data,password=hashed_password,email=form.email.data)
        session['username'] = newuser.username
        newuser.save()
        return redirect(url_for('home'))

  elif request.method == "GET":
    return render_template('signup.html', form=form, cfg=cfg)

@app.route("/login", methods=["GET", "POST"])
def login():
  if 'username' in session:
    return redirect(url_for('home'))

  form = LoginForm()

  if request.method == "POST":
    if form.validate() == False:
      return render_template("sign.html", form=form)
    else:
      username = form.username.data
      password = form.password.data.encode('utf-8')

      try:
          user = Users.get(Users.username==username)
      except:
          return redirect(url_for('login'))
      if user is not None and bcrypt.hashpw(password, user.password.encode('utf-8')) == user.password:
        session['username'] = form.username.data
        print url_for("home")
        return redirect(url_for('home'))
      else:
        return redirect(url_for('login'))

  elif request.method == 'GET':
    return render_template('signin.html', form=form, cfg=cfg)



@app.route("/logout")
def logout():
  session.pop('username', None)
  return redirect(url_for('start'))
