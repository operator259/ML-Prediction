import os
import shutil
import requests
import subprocess
import pandas as pd
from pathlib import Path

def download_file(url, save_path):
    response = requests.get(url)
    with open(save_path, 'wb') as file:
        file.write(response.content)
        
def copy_file_to_http_directory(source, destination="./http_directory/"):
    # Ensure destination directory exists
    os.makedirs(destination, exist_ok=True)

    # Construct the full destination file path
    dest_path = os.path.join(destination, os.path.basename(source))

    shutil.copy2(source, dest_path)  # Overwrites if the file exists
    print(f"Copied {source} to {dest_path}")

    

def main():
    url = "https://prediction.webinteractive.co.nz/raw_data"
    excel_file_path = Path("nrl.xlsx")
    csv_script_path = Path("Convert_Spreadsheet_XSLS_TO_CSV.py")
    train_model_script_path = Path("Train_Model.py")
    convert_to_Onnx = Path("Convert_to_ONNX.py")
    Webserver_run = Path("Python_Web_Server.py")

    print(f"Downloading {url}...")
    download_file(url, excel_file_path)
    print("Download complete.")

    # Run the Convert_Spreadsheet_XSLS_TO_CSV.py script using subprocess
    print(f"Running {csv_script_path}...")
    subprocess.run(["python", str(csv_script_path), str(excel_file_path)])

    # Remove the top row (header) from the generated CSV file
    csv_file_path = Path("NRL_matches.csv")
    data = pd.read_csv(csv_file_path, skiprows=1)
    data.to_csv(csv_file_path, index=False)
    
    # Train using subprocess
    print(f"Running {train_model_script_path}...")
    subprocess.run(["python", str(train_model_script_path)])

    # Convert to ONNX format for wordpress using subprocess
    print(f"Running {convert_to_Onnx}...")
    subprocess.run(["python", str(convert_to_Onnx)])
    
    # Copy to Http Directory and overwrite if existing
    copy_file_to_http_directory ('model_away.onnx')
    copy_file_to_http_directory ('model_home.onnx')
    copy_file_to_http_directory ('scaler.json')
    
    # Launch the Webserver 
    print(f"Running {Webserver_run}...")
    subprocess.run(["python", str(Webserver_run)])

if __name__ == "__main__":
    main()