import pandas as pd

def read_file():
    file_path = open_button.askopenfilename()
    if file_path:
        try:
            if file_path.endswith('.csv'):
                data = pd.read_csv(file_path)
                # Do something with CSV data (e.g., print first 5 rows)
                print(data.head())
            elif file_path.endswith(('.xls', '.xlsx')):
                data = pd.read_excel(file_path)
                # Do something with Excel data (e.g., print first 5 rows)
                print(data.head())
            # Add more formats as needed (e.g., JSON, etc.)
            else:
                print("Unsupported file format")
        except Exception as e:
            print("Error reading file:", e)