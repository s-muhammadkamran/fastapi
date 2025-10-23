# This is a play ground for the FastAPI

## How to setup and run in development server on Windows

01. Install python
02. Create a folder
03. Clone the repository in that folder
04. Open Command Prompt
05. Navigate to the root folder after cloning the repository  
    `cd [full path to repo root folder]`
06. Run the following command to create a Virtual Environment  
    `python -m venv .venv`
07. Activate the environment using below command  
    `.\.venv\scripts\activate`
08. Run the following command to install the dependencies  
    `pip install -r requirements.txt`
09. Upgrade PIP using the below command [OPTIONAL]  
    `python -m pip install --upgrade pip`
10. Run the following commands to start the application
    `CD src`  
    `uvicorn main:app --reload`
11. In the browser window open the URL which is shown on the command prompt