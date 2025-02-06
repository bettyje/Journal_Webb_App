# My Journal Backend

This is the backend for the **My Journal** application, built using Flask and hosted on Render. The backend provides RESTful APIs to manage journal entries, user authentication, and other related functionalities.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup and Installation](#setup-and-installation)
- [Environment Variables](#environment-variables)
- [API Endpoints](#api-endpoints)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## Features

- User authentication (register, login, logout)
- Create, read, update, and delete journal entries
- Secure password hashing
- RESTful API design
- Hosted on Render for scalability and reliability

## Technologies Used

- **Flask**: A lightweight WSGI web application framework in Python.
- **SQLAlchemy**: An ORM for database interactions.
- **Render**: A cloud platform for hosting web applications.
- **JWT (JSON Web Tokens)**: For secure user authentication.
- **Python**: The primary programming language used.
- **PostgreSQL**: The database used for storing user and journal data.

## Setup and Installation

Follow these steps to set up the project locally:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/my_journal_backend.git
   cd my_journal_backend
   ```
2. **Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. **Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4 . **Set up environment variables:
Create a .env file in the root directory and add the following variables:
  ```bash
  SECRET_KEY=your_secret_key
  DATABASE_URL=postgresql://username:password@localhost:5432/my_journal
  JWT_SECRET_KEY=your_jwt_secret_key
  ```
5 . **Run migrations:
  ```bash
  flask db upgrade
  ```
6. **Run the application
   ```bash
   flask run
   ```
The app will be running at http://127.0.0.1:5000/.

# Environment Variables
echo "Setting up environment variables..."
export SECRET_KEY="your_secret_key"
export DATABASE_URL="postgresql://username:password@localhost:5432/my_journal"
export JWT_SECRET_KEY="your_jwt_secret_key"

# API Endpoints
echo "API Endpoints:"
echo "Authentication:"
echo "  POST /api/register: Register a new user."
echo "  POST /api/login: Log in an existing user and return a JWT token."
echo "  POST /api/logout: Log out the current user (invalidate the token)."
echo ""
echo "Journal Entries:"
echo "  GET /api/entries: Get all journal entries for the authenticated user."
echo "  POST /api/entries: Create a new journal entry."
echo "  GET /api/entries/<entry_id>: Get a specific journal entry by ID."
echo "  PUT /api/entries/<entry_id>: Update a specific journal entry by ID."
echo "  DELETE /api/entries/<entry_id>: Delete a specific journal entry by ID."

# Deployment Instructions
echo ""
echo "Deployment Instructions:"
echo "1. Create a Render account: Sign up at https://render.com/."
echo "2. Create a new Web Service:"
echo "   - Connect your GitHub repository."
echo "   - Set the environment variables (SECRET_KEY, DATABASE_URL, JWT_SECRET_KEY)."
echo "   - Choose the appropriate Python version."
echo "3. Deploy:"
echo "   - Render will automatically build and deploy your application."
echo "4. Access your app:"
echo "   - Once deployed, your app will be accessible at the provided Render URL."

# Contributing Guidelines
echo ""
echo "Contributing Guidelines:"
echo "1. Fork the repository."
echo "2. Create a new branch (git checkout -b feature/YourFeatureName)."
echo "3. Commit your changes (git commit -m 'Add some feature')."
echo "4. Push to the branch (git push origin feature/YourFeatureName)."
echo "5. Open a pull request."

# License Information
echo ""
echo "License:"
echo "This project is licensed under the MIT License. See the LICENSE file for details."

echo ""
echo "Setup complete!"

   


   
