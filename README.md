FastAPI Satellite Company Website

This is a FastAPI-based web application for the Satellite company website. It provides information about the company, its services, portfolio, and contact details.

Requirements

Before running the application, make sure you have the following requirements installed:

Python 3.10 (or compatible version)
FastAPI
Uvicorn
Installation

Clone the repository from GitHub:
bash
Copy code
git clone https://github.com/yourusername/satellite-website.git
cd satellite-website
Create a virtual environment (optional, but recommended):
bash
Copy code
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
Install the required dependencies:
bash
Copy code
pip install -r requirements.txt
Launching the Application

Run the FastAPI application using Uvicorn:

bash
Copy code
uvicorn main:app --reload
The application will be running at http://127.0.0.1:8000.

Swagger Documentation

Once the application is running, you can access the Swagger documentation to explore the available API endpoints and methods. Open your web browser and navigate to the following URL:

Swagger Documentation

The Swagger page provides an interactive interface to test and interact with the API. You can use it to see example requests and responses, execute API methods, and understand the available data 
structures.

Endpoints

The application provides the following endpoints:

/company: Get information about the Satellite company, including a quote, main text, and services offered.
/: Root endpoint that displays a simple message about the website.
/portfolio: Get information about the company's portfolio, including project titles, descriptions, and images.
/contacts: Get contact details for the company, including phone number, address, email, and social media links.
Feel free to explore the API using the provided Swagger documentation or by making requests directly to the endpoints.
