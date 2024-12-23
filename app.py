from flask import Flask, redirect, url_for, render_template, request

app=Flask(__name__)


songs = ["Song by x", "song by y", "song by z"]


@app.route('/result/')
def result():
	uri = request.args.get("URI")
	username = request.args.get("Username")
	results = [uri,username]
	return render_template("result.html", URI = uri, USER=username)


	#content=songs[0][0]
	#return '<h1>Hello {}!</h1>'.format(name)


@app.route('/')
def home():
	return render_template("RecommenderWebsite.html")

if __name__ == "__main__":
	app.debug = True
	app.run()


#@app.route("/login", methods=["POST", "GET"])
#def login():
#	return render_template("login.html")

#@app.route("/<usr>")
#def user(usr):
#	return f"<h1>{usr}</h1>"

