from allImports import *
from flask import session


@app.route("/", methods = ["GET"])
def start():
  return render_template("start.html",
                          cfg = cfg)

@app.route("/home", methods=["GET"])
def home():
    return render_template("home.html", cfg=cfg)


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
