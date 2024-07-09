# PassPlease

### A simple password manager that uses a master account to encrypt and decrypt passwords. Runs locally on your machine and does not store any data on the cloud.

## Features
- **Add New Passwords**: Store passwords with an account name, website URL, password, and notes.
- **Search Passwords**: Easily find passwords by searching for the website URL.
- **Generate Strong Passwords**: Create random strong passwords (xkcd style).
- **View Statistics**: See the number of passwords stored in the database.
- **Multiple Accounts**: Register multiple accounts with different master passwords and view statistics for each account.

## Note This project is for educational purposes only.
This should not be used. 
It is a simple password manager that uses a master account to encrypt and decrypt passwords. It runs locally on your machine and does not store any data on the cloud. It is a simple project that can be used to learn about basic web development concepts and security practices.

---

## Installation and Running

### Prerequisites
- Python 3.x installed on your machine.

### Steps
1. **Clone the Repository**:
    ```bash
    git clone https://github.com/OscarWiklundJonsson/PassPlease.git
    cd PassPlease
    ```

2. **Install Dependencies**:
    ```bash
    pip install Flask
    ```

3. **Run the Application**:
    ```bash
    flask run
    ```

4. **Access the Application**:
    Open your browser and go to `http://127.0.0.1:5000/`.

---

## Usage

### Creating a New Account
1. Press the "Register" button.
2. Enter a username and a master password.
3. Click "Register" to create a new account.
4. You will be redirected to the login page.

### Logging In
1. Enter your username and master password.
2. Click "Login" to access the password manager.
3. You will be redirected to the home page ( dashboard).

### Adding a New Password
1. Navigate to the "Add Password" section.
2. Fill in the account name, website URL, password, and any notes.
3. Click "Add" to securely store the password in the database.

### Searching for a Password
1. Navigate to the "Search Password" section.
2. Enter the website URL you want to search for.
3. View the matching results.

### Generating a Strong Password
1. Navigate to the "Generate Password" section.
2. Click "Generate" to create a random strong password.

### Viewing Statistics
1. Navigate to the "Statistics" section.
2. See the total number of passwords stored in the database.

---

## What's Next?

- **Update Passwords**: Add a feature to update existing passwords.
- **Delete Passwords**: Add a feature to delete passwords.
- **Update Master Password**: Add a feature to update the master password.
- **Delete Account**: Add a feature to delete the account.
- **Export Passwords**: Add a feature to export passwords to a file.
- **Import Passwords**: Add a feature to import passwords from a file.
- **Hash Passwords**: Hash all the passwords in the database (currently, only the master password is hashed).

---
## What's New?
- *2024-07-09*: Mostly UI stuff. Templates and such.

---
## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
