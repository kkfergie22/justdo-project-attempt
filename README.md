Personal Task Manager

The Personal Task Manager is a web application that allows users to track and manage their tasks efficiently. It provides a user-friendly interface where users can add, edit, and delete tasks, mark tasks as completed, and organize tasks into different categories or tags. The application also includes features like weather information, gamification elements, collaboration and sharing, and integration with productivity tools.
Features

    User Registration and Authentication: Users can create accounts and log in securely to access their tasks.
    Task Management: Users can create, edit, and delete tasks, mark tasks as completed, and set due dates.
    Task Categorization: Tasks can be organized into different categories or tags for better organization and filtering.
    Weather Information: The application integrates with a weather API to provide real-time weather information.
    Gamification Elements: Users can earn badges, points, or rewards based on their task completion and productivity.
    Collaboration and Sharing: Users can collaborate and share tasks with other users or team members.
    Integration with Productivity Tools: Integration with popular productivity tools like calendars or note-taking apps for enhanced productivity.

Technologies Used

    Backend:
        Flask: Python-based web framework for building the backend server.
        Flask RESTful: Extension for building RESTful APIs with Flask.
        Flask-PyMongo: Integration for MongoDB with Flask.
        PyMongo: MongoDB driver for Python.
        Flask-JWT-Extended: For implementing JSON Web Tokens (JWT) and user authentication/authorization.

    Frontend:
        React: JavaScript library for building the user interface.
        React Router: For handling client-side routing in the React application.
        Axios: HTTP client for making API requests to the backend.
        Bootstrap or Material-UI: UI component libraries for styling and layout.
        Moment.js: For manipulating and formatting dates and times.
        React Icons: Collection of popular icon packs for adding icons to the user interface.
        React Hook Form: Library for handling form validation and state management.

    Database:
        MongoDB: NoSQL document-oriented database for storing task-related data.

Setup Instructions

    Clone the repository:

    bash

git clone <https://github.com/your-username/personal-task-manager.git>

Backend Setup:

    Navigate to the backend directory:

    bash

cd personal-task-manager/backend

Create a virtual environment (optional but recommended):

python -m venv venv

Activate the virtual environment:

    On Windows:

venv\Scripts\activate

On macOS/Linux:

bash

    source venv/bin/activate

Install the backend dependencies:

pip install -r requirements.txt

Set the necessary environment variables (e.g., MongoDB connection URI, JWT secret key).
Run the Flask development server:

    python app.py

Frontend Setup:

    Navigate to the frontend directory:

    bash

cd personal-task-manager/frontend

Install the frontend dependencies:

npm install

Set the API base URL in the .env file.
Start the React development server:

sql

        npm start

    Open the application in your web browser:
        Access the application at http://localhost:3000.

Contributing

Contributions to the Personal Task Manager project are welcome! If you find any issues or have suggestions for improvements, please open
