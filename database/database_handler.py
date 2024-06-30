import sqlite3
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash


def connect_to_database():
    conn = sqlite3.connect('db.sqlite')
    cur = conn.cursor()
    return conn, cur


def create_users_table(conn, cur):
    conn, cur = connect_to_database()

    cur.execute('''
        CREATE TABLE IF NOT EXISTS Users (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Username TEXT NOT NULL,
            Email TEXT NOT NULL,
            PasswordHash TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()


def register_user(username, email, password):
    try:
        # Hash the password
        password_hash = generate_password_hash(password)

        # Connect to the database
        conn, cur = connect_to_database()
        create_users_table(conn, cur)

        # Check if the username already exists
        cur.execute("SELECT * FROM Users WHERE Email = ?", (email,))
        user = cur.fetchone()
        if user:
            print("Username already exists")
            return "Username already exists"
        else:
            # Insert the new user into the Users table
            cur.execute("INSERT INTO Users (Username, Email, PasswordHash) VALUES (?, ?, ?)",
                        (username, email, password_hash))
            print("User registered successfully")

        # Print the last row id to check if the INSERT statement was executed
        print("Last row id:", cur.lastrowid)

        # Commit the changes and close the connection
        conn.commit()
        conn.close()
    except Exception as e:
        print("An error occurred:", e)


def get_email(email):
    try:
        # Connect to the database
        conn, cur = connect_to_database()

        # Fetch the user from the Users table
        cur.execute("SELECT * FROM Users WHERE Email = ?", (email,))
        user = cur.fetchone()
        print(user)
        # Close the connection
        conn.close()

        return user
    except Exception as e:
        print("An error occurred:", e)


def add_password_entry(user_id, account_name, website_url, password, notes):
    try:
        conn, cur = connect_to_database()

        # Insert the data into the PasswordEntries table
        cur.execute("""
            INSERT INTO PasswordEntries (UserID, AccountName, WebsiteURL, PasswordHash, Notes)
            VALUES (?, ?, ?, ?, ?)
        """, (user_id, account_name, website_url, password, notes))

        conn.commit()
        print("Password entry added successfully")

        # Close the connection
        conn.close()

        return True
    except Exception as e:
        print("An error occurred:", e)
        return None


def search_password_entries(user_id, website_url):
    try:
        conn, cur = connect_to_database()

        # Perform the search query
        cur.execute("""
            SELECT * FROM PasswordEntries
            WHERE UserID = ? AND WebsiteURL LIKE ?
        """, (user_id, '%' + website_url + '%'))

        results = cur.fetchall()
        # Remove the user's ID from the results
        results = [result[2:] for result in results]
        results = [results[1:] for results in results]

        # Close the connection
        conn.close()

        return results
    except Exception as e:
        print("An error occurred:", e)
        return None


def get_password_data(user_id):
    try:
        conn, cur = connect_to_database()

        # Initialize a dictionary with keys for all months and values set to 0
        month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        chart_data = {month: 0 for month in month_names}

        # Query the database to get the count of passwords created each month
        cur.execute("""
            SELECT strftime('%m', CreatedAt) as month, COUNT(*) as totalPasswords
            FROM PasswordEntries
            WHERE UserID = ?
            GROUP BY month
        """, (user_id,))

        password_data = cur.fetchall()

        # Update the dictionary with the data returned from the SQL query
        for item in password_data:
            chart_data[month_names[int(item[0])-1]] = item[1]

        # Convert the dictionary to a list of dictionaries in the format needed for the chart
        chart_data = [{'month': month, 'totalPasswords': totalPasswords} for month, totalPasswords in chart_data.items()]

        # Close the connection
        conn.close()

        return chart_data
    except Exception as e:
        print("An error occurred:", e)