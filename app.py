from flask import Flask, request, render_template, redirect, url_for, flash, jsonify

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session management and flashing messages

# Dummy user data (you can replace this with a database later)
users = {
    "test@example.com": {"password": "password123", "name": "Test User"}
}

# Coordinates for locations on Government Engineering College, Thrissur campus
locations = {
        'main entrance': {'lat': 10.555101892944363, 'lng': 76.2253838285237},
        'library': {'lat': 10.554025949121488, 'lng': 76.22478053174801},
        'auditorium': {'lat': 10.553749220961906, 'lng': 76.22442298654245},
        'canteen': {'lat': 10.553362429849095, 'lng': 76.22632869842572},
        'cs': {'lat': 10.5529987623827, 'lng': 76.22201739230731},
        'eee': {'lat': 10.552197792206393, 'lng': 76.22384069067981},
        'ec': {'lat': 10.552929829740812, 'lng': 76.22160029018582},
        'mca': {'lat': 10.553480763544187, 'lng': 76.22059285308711},
        'ccf': {'lat': 10.55378474332099, 'lng': 76.22516978672182},
        'civil': {'lat': 10.554092436922849, 'lng': 76.22515929516514},
        'mech': {'lat': 10.554598579712138, 'lng': 76.22465769900353},
        'chemical': {'lat': 10.552932447085821, 'lng': 76.2235171724627},
        'academic block': {'lat': 10.55347307909898, 'lng': 76.22519752635175},
        'pe': {'lat': 10.55289968747326, 'lng': 76.22249759588999},
        
    }
     


# Route for the Welcome Page
@app.route('/')
def welcome():
    return render_template('welcome.html')

# Route for the Sign-Up Page
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        # Check if the passwords match
        if password != confirm_password:
            flash("Passwords do not match!", 'danger')
            return render_template('signup.html')

        # Check if the email is already registered
        if email in users:
            flash("Email is already registered. Please log in.", 'danger')
            return render_template('signup.html')

        # Add the new user to the dummy data
        users[email] = {"password": password, "name": name}
        flash("Registration successful! You can now log in.", 'success')
        return redirect(url_for('login'))

    return render_template('signup.html')

# Route for the Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Check if the user exists and the password matches
        if email in users and users[email]['password'] == password:
            return redirect(url_for('index'))  # Redirect to the main page if login is successful
        else:
            flash("Invalid credentials, please try again.", 'danger')
            return render_template('login.html')

    return render_template('login.html')

# Route to serve the main page (HTML map page)
@app.route('/index')
def index():
    return render_template('index.html')

# Route to handle the navigation directions
@app.route('/directions', methods=['POST'])
def directions():
    start = request.form['start'].lower()
    end = request.form['end'].lower()

    if start not in locations or end not in locations:
        return jsonify({'error': 'Starting or destination location not found'})

    start_coords = locations[start]
    end_coords = locations[end]

    return jsonify({
        'start': start_coords,
        'end': end_coords
    })

# Start the Flask app
if __name__ == '__main__':
    app.run(debug=True)
