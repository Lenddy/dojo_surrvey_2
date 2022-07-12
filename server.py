from flask import Flask, redirect, render_template,request, session
app = Flask(__name__)
app.secret_key = "secret"
#to use request you will need to also use .form -> request.fom



#always use the decorator
#show the survey format
@app.route("/")
def show_survey():
    return render_template("index.html")


@app.route("/submit")
def display_submitio_page():

    return render_template("submition.html")


@app.route("/submit",methods = ['post'])
def redirect_submition():
    session["name"] = request.form["name"]
    session["locations"] =request.form["locations"]
    session["fav_stack"] = request.form["fav_stack"]
    session["comment"] = request.form["comment"]
    return redirect("/submit")


if __name__=="__main__":
    app.run(debug= True)