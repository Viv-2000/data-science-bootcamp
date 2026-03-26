"""
Flask Application Overview:

This app demonstrates basic Flask concepts including routing, templates,
form handling, and dynamic URL parameters.

1. App Initialization:
   - Flask app is created using Flask(__name__)

2. Routes:

   '/' (root):
   - Returns a simple text message guiding the user to /home

   '/home':
   - Renders 'form.html' (a form page for user input)

   '/submit' [POST]:
   - Handles form submission
   - Extracts 'name' from form data using request.form
   - Creates a greeting message
   - Passes the message to 'jinja.html' using render_template
   - 'reference' is the variable used inside the HTML template

   '/var_rule/<int:score>':
   - Demonstrates dynamic routing with URL parameters
   - Accepts an integer 'score' from the URL
   - Uses a conditional expression (ternary operator):
       "pass" if score > 50 else "fail"
   - Returns a formatted string with the result

3. Templates:
   - form.html → contains the input form
   - jinja.html → displays the greeting using {{ reference }}

4. Key Concepts:
   - render_template → renders HTML files from 'templates' folder
   - request.form → retrieves form data (POST requests)
   - Dynamic routes → passing variables via URL
   - Jinja templating → injecting Python variables into HTML

5. App Execution:
   - Runs in debug mode for development (auto-reload + error logs)

Note: render_template(a,b=x)-- here a is the html file to render
                            -- b is the reference passed
                            -- x is the parameter passed in the reference
"""



from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def root():
    return "hey, this is your root directory. go to address bar and add /home to continue with the form"

@app.route('/home')
def home():
    return render_template("form.html")

@app.route('/submit',methods=['POST'])
def submit():
    name = request.form['name']
    greeting = 'hello there mate. nice to meet you ' + name
    return render_template("jinja.html", reference = greeting)

@app.route('/var_rule/<int:score>')
def var_rule(score):
    
    result = "pass" if score>50 else "fail"
    return f"you result based on your score({score}) is {result}. You may try var_rule with other numbers now"

if __name__=="__main__":
    app.run(debug=True)