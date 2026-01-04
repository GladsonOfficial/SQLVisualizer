# SQLVisualizer

## Description
SQLVisualizer is a web-based tool designed to help users visualize SQL database schemas and query outputs. It provides an intuitive interface to execute SQL queries and display the results in a clear, readable format.

## Features
- Execute custom SQL queries.
- Visualize database tables and their schemas.
- Display query results in an organized manner.
- Simple and clean user interface.

## Setup and Installation

### Prerequisites
- Python 3.x
- pip (Python package installer)

### Steps
1.  **Clone the repository:**
    ```bash
    git clone https://github.com/GladsonOfficial/SQLVisualizer.git
    cd SQLVisualizer
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv .venv
    ```

3.  **Activate the virtual environment:**
    -   **Windows:**
        ```bash
        .venv\Scripts\activate
        ```
    -   **macOS/Linux:**
        ```bash
        source .venv/bin/activate
        ```

4.  **Install the required Python packages:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  **Start the application:**
    ```bash
    python main.py
    ```

2.  **Access the web interface:**
    Open your web browser and navigate to `http://127.0.0.1:5000` (or the address shown in your console).

3.  **Interact with the application:**
    -   On the homepage, you should be able to interact with the SQL visualization features. This may involve uploading a database file, inputting SQL queries, or browsing existing tables.

## Technologies Used
-   **Backend:** Python (Flask)
-   **Database:** SQLite
-   **Frontend:** HTML, CSS (static/css/style.css), JavaScript (static/js/script.js)

## Project Structure
-   `main.py`: Main application entry point and Flask routes.
-   `requirements.txt`: Python dependencies.
-   `sql_visualizer.db`: Default SQLite database file.
-   `templates/`: HTML template files (e.g., `index.html`, `output.html`, `tables.html`).
-   `static/`: Static assets like CSS and JavaScript.
    -   `static/css/style.css`: Stylesheets for the application.
    -   `static/js/script.js`: Client-side JavaScript.
-   `logging.yaml`: Logging configuration for the application.

## Contributing
(Optional) If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome.

## License
(Optional) This project is licensed under the [Your Chosen License] - see the LICENSE.md file for details.
