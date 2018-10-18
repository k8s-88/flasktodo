from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = {
	1: {
		"name": "get coffee",
		"description": "none of that cheap stuff",
		"is_urgent": False
	},
	2: {
		"name": "get milk",
		"description": "in a carton",
		"is_urgent": True
	},
}




@app.route("/")
def todo():
    return render_template("index.html", tasks=tasks.values())

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080, debug=True)