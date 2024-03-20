from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/results")
def render_page1():
    
    
	name = request.args['name']
	height = request.args['height']
	weight = request.args['weight']
	deadlift = request.args['deadlift']
    
	ratio = (int(height) + int(weight)) / 3
	deadliftRatio = int(deadlift) / 70
	velo1 = ratio + deadliftRatio
	velo2 = round(velo1)
	
	return render_template('page1.html', response1 = name, response2 = height, response3 = weight, response4 = deadlift, velo = velo2)

    
if __name__=="__main__":
    app.run(debug=False)
