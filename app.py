from jupyter_dash import JupyterDash
from data.sample_data import get_data
from layout.layout import create_layout

# Initialize the Dash app
app = JupyterDash(__name__)

# Get the data
df = get_data()

# Define the layout of the dashboard
app.layout = create_layout(df)

# Run the app
if __name__ == '__main__':
    app.run_server(mode='inline')
