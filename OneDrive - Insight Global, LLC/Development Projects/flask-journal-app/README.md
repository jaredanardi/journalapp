# Flask Journal App

This is a simple Flask application that allows users to record daily journal entries. Users can submit new entries and view their past entries.

## Project Structure

```
flask-journal-app
├── app
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   └── templates
│       └── journal.html
├── requirements.txt
├── config.py
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd flask-journal-app
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Configuration

Edit the `config.py` file to set up your database URI and any other configuration settings.

## Running the Application

To run the application, use the following command:
```
flask run
```

Make sure to set the `FLASK_APP` environment variable to `app` before running the command.

## Usage

- Navigate to `http://127.0.0.1:5000` in your web browser to access the journal application.
- You can submit new journal entries using the provided form and view all past entries on the same page.

## License

This project is licensed under the MIT License.