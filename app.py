# Step 1 - To import FLASK
from flask import Flask, request, render_template,request
import re


# Step 2 - Create the object with a parameter __name__
app = Flask(__name__)


###################################################
# Step 3 - Create an END POINT using routes and bind them with a functionality

@app.route('/', methods=['GET','POST'])
def home_page():
    if request.method=='POST':
        pattern=request.form['pattern']
        text=request.form['text']
        matches=re.findall(pattern,text)
        return render_template('home.html',matches=matches,text=text,pattern=pattern)
    else:
        return render_template('home.html')





###################################################

# Step 4 - Run the app
if __name__ == '__main__':
    app.run(debug=True)