from flask import Flask, render_template, request, redirect, url_for, redirect
import os

app = Flask(__name__)

tasks = {
	1: {
	    "id": 1,
		"name": "get coffee",
		"description": "none of that cheap stuff",
		"urgent": False,
		"done":	True
	},
	2: {
	    "id": 2,
		"name": "get milk",
		"description": "in a carton",
		"urgent": True,
		"done": False
	},
}

next_id = 3



@app.route("/")
def show_index():
    return render_template("index.html", tasks=tasks.values())
    
    
@app.route("/add", methods=["GET", "POST"])
def show_add_form():
    if request.method == "POST":
    	global next_id
    	new_item = {
    		"id": next_id,
    		"name": request.form["name"],
    		"description": request.form["description"],
    		"urgent": "urgent" in request.form,
    		"done": "done" in request.form
    		
    	}
    	print(new_item)
    	tasks[next_id] = new_item
    	next_id += 1
    	return redirect("/")
    
    else:
        
        return render_template("todo_form.html")
    
    
@app.route("/edit/<int:id>", methods=["GET", "POST"])   
def edit_task(id):
	if request.method == "POST":
		changed_item = {
			"id": id,
			"name": request.form["name"],
			"description": request.form["description"],
			"urgent": "urgent" in request.form,
			"done": "done" in request.form
			
		}
		tasks[id] = changed_item
		return redirect("/")
	else:
		return render_template("edit_form.html", task = tasks[id])
    

if __name__ == "__main__":
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)), debug=True)
    
    
    
    
    