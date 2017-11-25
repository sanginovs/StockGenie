from allImports import *
from flask import session


@app.route("/", methods = ["GET"])
def start():
  return render_template("start.html",
                          cfg = cfg)


@app.route("/signup", methods=["GET", "POST"])
def signup():
  print "here"
  if 'email' in session:
    return redirect(url_for('home'))
  form = SignupForm()

  if request.method == "POST":
    if form.validate() == False:
      return render_template('signup.html', form=form)
    else:
      newuser = User(form.first_name.data,
                    form.last_name.data,
                    form.email.data,
                    form.password.data)
      session['email'] = newuser.email
      newuser.save()
      return redirect(url_for('home'))

  elif request.method == "GET":
    return render_template('signup.html', form=form, cfg=cfg)

@app.route("/login", methods=["GET", "POST"])
def login():
  if 'email' in session:
    return redirect(url_for('home'))

  form = LoginForm()

  if request.method == "POST":
    if form.validate() == False:
      return render_template("login.html", form=form)
    else:
      email = form.email.data
      password = form.password.data

      user = User.query.filter_by(email=email).first()
      if user is not None and user.check_password(password):
        session['email'] = form.email.data
        return redirect(url_for('home'))
      else:
        return redirect(url_for('login'))

  elif request.method == 'GET':
    return render_template('login.html', form=form)

@app.route("/logout")
def logout():
  session.pop('email', None)
  return redirect(url_for('index'))
