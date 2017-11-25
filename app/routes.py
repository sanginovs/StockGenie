# this renders the home page which is start.html
from allImports import *



@app.route("/", methods = ["GET"])
def start():
  return render_template("start.html",
                          cfg = cfg) # Do not worry about cfg, but you need
                                     # to pass that as an argument everytime
                                     # with render_template    


@app.route("/test",methods=['GET'])
def test():
  return "<h1>This is a test</h1>" 