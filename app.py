from flask import Flask, request, render_template
from datetime import datetime

todaydate = datetime.now()
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")
    # return "Hellow sravan how are you doing \n\nHello, World!"

@app.route('/sravan')
def sravan():
    return render_template("sravan.html")

@app.route('/about')
def about():
    return render_template("about.html")
    
@app.route('/devops')
def devops():
    return render_template("devops.html")

@app.route('/image')
def image():
    return render_template("image.html")
    
if __name__ == "__main__":
    app.run(debug=True)