"""
FULL FLOW OF THIS FLASK APP
---------------------------

This app demonstrates:
1. basic routing
2. form submission using POST
3. converting a Python dictionary into a URL-safe string using JSON
4. redirecting to another route dynamically
5. rendering final output using Jinja templates

--------------------------------------------------
STEP-BY-STEP FLOW
--------------------------------------------------

1. App starts:
   - app = Flask(__name__) creates the Flask application object.

2. User visits '/':
   - root() returns a simple HTML welcome message.
   - It tells the user to go to '/info'.

3. User visits '/info':
   - info() renders 'get_result.html'.
   - This page contains a form where the user enters marks.

4. User submits the form:
   - Form sends a POST request to '/submit'.
   - submit() reads values using request.form[...] .
   - request.form looks for the HTML input 'name' attributes:
       e.g. name="science", name="maths", name="english"

5. Dictionary creation:
   - score = {} stores subject names as keys and entered marks as values.
   - Example:
       {'science': 75.0, 'maths': 82.0, 'english': 40.0}

6. Why json is used:
   - A Python dictionary cannot be passed directly in a URL.
   - URL data must be text/string based.
   - json.dumps(score) converts the Python dict into a JSON string.
   - Example:
       '{"science": 75.0, "maths": 82.0, "english": 40.0}'
   - This string can then be passed through the route.

7. Why url_for is used:
   - url_for('results', result=scores) builds the correct URL for the
     'results' function dynamically.
   - Instead of hardcoding '/results/...', Flask creates the route safely.
   - If the route path changes later, url_for still works as long as the
     function name stays the same.

8. Why redirect is used:
   - redirect(...) sends the browser to another route.
   - Here, submit() does not directly render the final page.
   - Instead, it redirects the browser to '/results/<string:result>'.

9. Important redirect behavior:
   - redirect() causes the browser to make a NEW request.
   - That new request is usually a GET request.
   - So even though '/submit' is POST, '/results/...' is accessed after redirection.

10. User reaches '/results/<string:result>':
    - The JSON string from the URL is received as 'result'.
    - json.loads(result) converts the JSON string back into a Python dictionary.

11. Grade calculation:
    - any(int(x) < 50 for x in results.values())
      checks whether any subject mark is below 50.
    - If even one mark is below 50 -> grade = 'fail'
    - Otherwise -> grade = 'pass'

12. Final output:
    - render_template('final_result.html', result=results, grade=grade)
      sends:
        a) the full results dictionary
        b) the final pass/fail grade
      to the HTML template.
    - Jinja then displays these values inside the page.

--------------------------------------------------
KEY IDEAS USED
--------------------------------------------------

request.form
- Reads submitted form data from a POST request.
- The keys must match HTML input name="" attributes.

json.dumps(...)
- Converts Python dict -> JSON string
- Used because dictionaries cannot be passed directly in a URL.

json.loads(...)
- Converts JSON string -> Python dict
- Used after receiving the data in the results route.

url_for(...)
- Dynamically builds the URL for a route using the function name.
- Safer and better than writing URLs manually.

redirect(...)
- Sends the user/browser to another route.
- Commonly used after form submission.

render_template(...)
- Loads an HTML file from the templates folder and passes variables into it.

Jinja
- {{ variable }} prints values
- {% ... %} handles logic such as loops/conditions
- {# ... #} is for comments in templates

--------------------------------------------------
ERROR HANDLING
--------------------------------------------------

- The try block attempts to read and convert all form values to float.
- If the user enters invalid data or a value is missing, the except block runs.
- In that case, the form page is shown again.

--------------------------------------------------
ONE-LINE SUMMARY
--------------------------------------------------

User enters marks -> form sends POST to /submit -> Flask creates a dictionary
-> dictionary is converted to JSON string -> redirect sends user to /results
-> JSON is converted back to dictionary -> pass/fail is calculated -> final
template displays the result.
"""

from flask import Flask,render_template,request,redirect,url_for
import json

###WSGI Application
app=Flask(__name__)

@app.route("/")
def root():
    return "<html><H1>Welcome to building dynamic urls</H1>" \
    "<h2>please go to the address bar and add info, then hit enter</html>"

@app.route('/info')
def info():
    return render_template('get_result.html')

# redirect() always makes a GET request #### VVV IMP
# we are accessing this route via /submit route when the function dynamically builds the url for /results
# it also passes a dictionary as json string under reference result into the /results route
# results function also passes 2 parameters to the final_result.html file
@app.route('/results/<string:result>',methods=['GET','POST'])
def results(result):
    results = json.loads(result)
    grade = 'fail' if any(int(x)<50 for x in results.values()) else 'pass'
    return render_template('final_result.html', result = results, grade = grade)

# you cannot access /submit route directly as the methods specified are only 'POST'
@app.route('/submit',methods=['POST'])
def submit():
    score = {}
    try:

        score['science'] = float(request.form['science'])
        score['maths'] = float(request.form['maths'])
        score['english'] = float(request.form['english'])

        scores = json.dumps(score)
    except Exception as e:
        return render_template('get_result.html')

    return redirect(url_for('results',result = scores))
            

if __name__=="__main__":
    app.run(debug=True)

