from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = {
	1 : {
		"id: 1,
		"name": "get coffee",
		"description": "none of that cheap stuff",
		"is_urgent": False
	},
	
	2 : {
		"id": 2,
		"name": "get milk",
		"description": "in a carton",
		"is_urgent": True
	},
}


task_to_add = {
		"id": next_id,
		"name": request.form['name'],
		"description": request...,
		"is_urgent": True
	}

tasks[????] = task_to_add



@app.route("/")
def show_hi():
    return "Hi"

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080, debug=True)