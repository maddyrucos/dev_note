# DevNote

DevNote is a simple and efficient web application for managing your notes. It allows you to add, delete, and edit notes with ease. Additionally, it features a robust authentication system to ensure your notes are secure.

## Features

- **Add Notes**: Easily create new notes with a user-friendly interface.
- **Delete Notes**: Remove unwanted notes with a single click.
- **Edit Notes**: Modify existing notes to keep your information up-to-date.
- **Authentication**: Secure your notes with a built-in authentication system.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- Python3.11

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/maddyrucos/dev_note.git
   ```

2. Navigate to the project directory and create virtual enviroment:
   ```sh
   cd dev_note | python3 -m venv venv | . venv/bin/activate
   ```

3. Install the 
   ```sh
   pip install -r requirements.txt
   ```
   
4. Create database:
   ```sh
   python3 manage.py migrate
   ```
   
5. Start the development server:
   ```sh
   python3 manage.py runserver:3000
   ```
   
6. Open your browser and visit `http://localhost:3000` to see the application in action.

## Usage

1. **Sign Up/Login**: Create an account or log in to access your notes.
2. **Add a Note**: Click on the "Create" button to create a new note.
3. **Edit a Note**: Click on the notes field you want to modify, make changes and put cursor away.
4. **Delete a Note**: Click on the red "X" button at the top right corner of the note.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with descriptive commit messages.
4. Push your changes to your fork.
5. Submit a pull request.

## Contact

For any questions or suggestions, feel free to contact me at t.me/madeezy.

---

Thank you for using DevNote! This is my first pet-project on Django. I hope it helps you stay organized and productive.
