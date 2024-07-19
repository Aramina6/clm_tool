# clm_tool
Compliance Management System (CLM Tool)


- `app.py`: Main file that initializes and runs the Dash application.
- `data/sample_data.py`: Contains the function to generate sample data for the dashboard.
- `layout/layout.py`: Defines the layout of the dashboard.
- `assets/custom_styles.css`: Contains custom CSS styles for the dashboard (optional).
- `requirements.txt`: Lists the dependencies required for the project.

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/your-username/compliance_dashboard.git
    cd compliance_dashboard
    ```

2. **Create a virtual environment (optional but recommended):**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```sh
    pip install -r requirements.txt
    ```

## Running the Dashboard

1. **Run the Jupyter Notebook server:**

    ```sh
    jupyter notebook
    ```

2. **Open the `app.py` file in Jupyter Notebook and run all cells.**

   The dashboard should display inline within the Jupyter Notebook.

## Customization

- **Data**: Modify the `data/sample_data.py` file to change the sample data or connect to a real data source.
- **Layout**: Adjust the layout in the `layout/layout.py` file to change the appearance of the dashboard.
- **Styles**: Add custom styles in the `assets/custom_styles.css` file to change the look and feel of the dashboard.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with any improvements or new features.

## License

None
