import pandas as pd

def convert_xlsx_to_csv(xlsx_file, csv_file):
    try:
        # Read the Excel file
        df = pd.read_excel(xlsx_file)

        # Convert and save as CSV
        df.to_csv(csv_file, index=False)

        print("Conversion successful! CSV file created.")
    except Exception as e:
        print("Error occurred during conversion:", str(e))

# Example usage
xlsx_file_path = "nrl.xlsx"  # Replace with the path to your .xlsx file
csv_file_path = "NRL_matches.csv"    # Replace with the desired path for the resulting .csv file

convert_xlsx_to_csv(xlsx_file_path, csv_file_path)
