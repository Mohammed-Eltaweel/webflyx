from flask import Flask, render_template, request, redirect
app = Flask(__name__)

users = []
@app.route('/')
def home():
    return render_template('login.html')  # your HTML file goes here

@app.route('/signup', methods=["GET", 'POST'])
def signup():
    if request.method == 'POST': 
         # Get form data
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm-password')

        # Simple check
        if password != confirm_password:
            return "Passwords do not match", 400

        # Save user (in memory)
        users.append({
            'name': name,
            'email': email,
            'password': password,  # Don't store plain passwords in real apps
        })

        print("Users:", users)  # For debugging

        return f"Thanks for signing up, {name}!"
    return render_template('signup.html')  # your HTML file goes here

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        return 'login successfuly', 200
    return render_template('login.html')  # your HTML file goes here

if __name__ == '__main__':
    app.run(debug=True)
