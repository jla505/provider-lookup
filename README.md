# Healthcare Provider Search System

The objective of this project is to create a system that allows users to search for and locate Healthcare providers.

## Features

- Search for healthcare providers by name, specialty, and location.
- Display a list of providers matching the search criteria.

## Technologies Used

- Python
- Flask (web framework)
- HTML (for templates)

## Getting Started

### Prerequisites

Make sure you have Python and pip installed on your system.

### Installation

1. Clone the repository:
    ```bash
    https://github.com/jla505/healthcare-provider-search.git
    cd healthcare-provider-search
    ```

2. Install the required Python packages:
    ```bash
    pip install flask
    ```

### Running the Application

1. Navigate to the project directory:
    ```bash
    cd healthcare-provider-search
    ```

2. Run the application:
    ```bash
    python app.py
    ```

3. Open your web browser and go to `http://127.0.0.1:5000/`.

## Project Structure


- `app.py`: Main application file containing the Flask code.
- `templates/`: Directory containing the HTML templates for the application.
  - `index.html`: Home page template.
  - `search.html`: Search page template.
  - `results.html`: Results page template.

## Usage

1. Open the home page and click on "Search for Providers".
2. Enter your search criteria (name, specialty, location) and click "Search".
3. View the list of providers that match your criteria.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request. We welcome any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

