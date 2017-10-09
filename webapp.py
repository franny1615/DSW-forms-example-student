from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/response")
def render_response():
    color = request.args['color']
    #The request object stores information that was sent to the server.
    #args is a multi dictionary, it can have multiple values for one key. MultiDict.
    #The information in args is visible in the url for the page being requested(ex. .../response?color=blue) 
    if color == 'green':
        reply = "Thats mine as well, Dawg!"
    else:
        reply = "My fav color is green."
    return render_template('response.html', response = reply)
    
    
if __name__=="__main__":
    app.run(debug=False, port=54321)
