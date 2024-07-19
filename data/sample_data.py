import pandas as pd

def get_data():
    # Sample data
    data = {
        'Department': ['HR', 'Finance', 'IT', 'Operations'],
        'Compliance': [95, 88, 76, 90],
        'Violations': [2, 4, 8, 3]
    }
    df = pd.DataFrame(data)
    return df
