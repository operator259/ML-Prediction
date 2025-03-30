Welcome!!!

This project is written in python with an HTML Front end!

Install the requirments.txt file using "pip install -r requirements.txt"

Simply run Prediction_Main.py..

This script will run all the others to make your life easy.. The flow is as follows 

1. Download the latest XSLS File from the repository (Updates every thursday afternoon)
2. Convert it to CSV
3. Train the model 
4. Convert to ONNX (Better format for the webpage to query)
5. Copy over the required Scaler and ONNX files to the Web server directory (Replace if need)
6. Launch the Webserver and serve the content

From there you should be able to access the front end via http://localhost:8000/... If 8000 is in use alreadym then you will need to modify the port in Python_Web_Server.py

Coming Soon - 

Docker container 

The Docker File format will be AMD64