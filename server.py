from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)  
app.secret_key = 'fruity'

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout')         
def checkout():
    return render_template("checkout.html")

@app.route('/checkout_counts', methods=['POST'])         
def checkout_counts():
    print(request.form)
    session['strawberry'] = request.form['strawberry']
    session['raspberry'] = request.form['raspberry']
    session['apple'] = request.form['apple']
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['student_id'] = request.form['student_id']
    session['count'] =int(session['strawberry'])+int(session['raspberry'])+int(session['apple'])
    print(f"Charging {session['first_name']} {session['last_name']} for {session['count']} fruits.")
    return redirect('/checkout')

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    