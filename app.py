from flask import Flask, render_template, request, redirect, url_for, jsonify, session
from werkzeug.security import check_password_hash


from functions import generate_password
from database import database_handler
import functions.generators as g

app = Flask(__name__)
app.secret_key = '#qvFSp5A(ziSJ%BI$Q5vaB)|c6jKCCO,?-I_Fs@|h#yX<kdek4RyP0^urB~/z<D'

@app.route('/')
def main_page():
    return render_template('index.html')

@app.route('/privacy')
def privacy_page():
    return render_template('privacy.html')

@app.route('/terms')
def terms_page():
    return render_template('terms.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        # Call the register_user function from database_handler
        print("Registering user")
        result = database_handler.register_user(username, email, password)

        if result == "Username already exists":
            return jsonify({"error": "Username already exists"}), 409

        # Redirect the user to the login page
        return redirect(url_for('login'))
    else:
        return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    print("Logging in")
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        login_email = database_handler.get_email(email)
        print (login_email)

        if login_email is None:
            print("User not found")
            return "Incorrect username or password", 401

        print(check_password_hash(login_email[3], password))

        if check_password_hash(login_email[3], password):
            # Log the user in
            session['username'] = login_email[1]
            session['user_id'] = login_email[0]  # Store user_id in session
            print("User logged in successfully")
            return redirect(url_for('dashboard'))
        else:
            # Return an error message
            return "Incorrect username or password", 401
    else:
        return render_template('login.html')


@app.route('/logout')
def logout():
    # Clear the session
    session.clear()
    return redirect(url_for('login'))


@app.route('/dashboard')
def dashboard():
    # Check if user is logged in
    if 'user_id' not in session:
        # If not logged in, redirect to login page
        return redirect(url_for('login'))

    # If logged in, get the username from the session and proceed
    username = session.get('username', 'User')  # Default to 'User' if not found
    return render_template('dashboard.html', username=username)


@app.route('/generate_password', methods=['GET'])
def generate_password_route():
    password = generate_password.generate_password_word()
    return jsonify(password=password)


@app.route('/add_password', methods=['POST'])
def add_password():
    # Retrieve form data
    account_name = request.form.get('accountName')
    website_url = request.form.get('websiteURL')
    password = request.form.get('password')
    notes = request.form.get('notes')

    # Validate form data
    if not all([account_name, website_url, password]):
        return "All fields are required", 400

    # Get the user's ID from the session
    user_id = session.get('user_id')
    if user_id is None:
        return "User is not logged in", 401

    # Insert data into the database
    result = database_handler.add_password_entry(user_id, account_name, website_url, password, notes)

    if result is not None:
        return "Password entry added successfully", 200
    else:
        return "An error occurred", 500


@app.route('/search_password', methods=['POST'])
def search_password():
    # Retrieve form data
    website_url = request.form.get('searchWebsiteURL')

    # Get the user's ID from the session
    user_id = session.get('user_id')
    if user_id is None:
        return "User is not logged in", 401

    # Perform the search query
    results = database_handler.search_password_entries(user_id, website_url)

    # Return the search results to the client
    return jsonify(results)

@app.route('/get_password_data', methods=['GET'])
def get_password_data():
    # Get the user's ID from the session
    user_id = session.get('user_id')
    if user_id is None:
        return "User is not logged in", 401

    # Get the user's password data
    results = database_handler.get_password_data(user_id)

    return jsonify(results)


# Temp services #

@app.route('/temp-services')
def temp_services():
    return render_template('temp_services.html')

@app.route('/temp-services/name', methods=['GET'])
def temp_service_name():
    name = g.generate_name(gender="any")
    return jsonify({"name": name})

@app.route('/temp-services/address', methods=['GET'])
def temp_service_address():
    address = g.generate_random_address()
    return jsonify({"address": address})


@app.route('/temp-services/id', methods=['GET'])
def temp_service_id():
    identity = g.generate_fake_identity('none', 'en_US', 'safe')
    print (identity)
    return jsonify(identity)



# Error handling 404, 500 and so on #
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run()
