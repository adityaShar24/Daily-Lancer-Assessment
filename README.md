# Job Application System 🌐

## Technologies Used
- Flask 🐍
- Flask-JWT 🌐
- MongoDB 🍃
- Postman 📬
- Cache ⚡

## Features 🚀
### User Registration and Authentication 🔐
- Secure user registration and login functionality using JWT (JSON Web Tokens). The authentication service validates user credentials and generates a JWT for authenticated users. This token is used to authenticate subsequent requests from the client.

## 👥 User Listing

Employers can view a list of all registered users.

---

### Job Posting/Applying 📝
- Users (employers) can post job opportunities with details such as title, description, skills, salary, and company name.
- Job seekers can apply for available job positions by submitting their resumes and cover letters.

## 📄 Job Application Listing

Employers can retrieve and view applications for a specific job.

## Prerequisites 🛠️
### Getting Started
These instructions will help you set up and run the Job Application System Flask Application on your local machine.

### Prerequisites
Before you begin, make sure you have the following installed:
- Python 3.x 🐍
- MongoDB 🍃 (Ensure a MongoDB instance is running, and the connection string is configured)

### Installation 🚀
To run this project, you'll need to set up a Python environment and install its dependencies. Here's how you can do it:

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/adityaShar24/Daily-Lancer-Assessment
    cd Daily-Lancer-Assesment
    cd src
    ```

2. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### Usage 🚀
To run the Job Application System Flask Application, execute the following command:
```bash
python app.py
```

## 📁 Project Structure

- **controllers**: Contains modules handling business logic and interfacing with the database.
- **database**: Includes database connection configurations and models.
- **middlewares**: Houses middleware functions for request processing before reaching the route handlers.
- **routes**: Defines the API endpoints using Flask Blueprints.
- **utils**: Holds utility functions and constants.

#### 🚀 Happy coding! 🌟

Feel free to adjust the emojis or add more to suit your preferences!

