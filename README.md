The TransportHub is a web application designed to help users find detailed information about transport options between their selected source and destination locations. 
Users can choose to prioritize fare, travel time, or a balance of both, to receive recommendations tailored to their preferences.

Features
1) Source and Destination Selection: Users can easily input their starting point and destination.
2) Choice of Priority: Users can choose between prioritizing fare, travel time, or a combination of both.
3) Detailed Transport Info: The app provides comprehensive details about the recommended transport options, including routes and costs.

Installation
1) Clone the repository:
   git clone https://github.com/ThanmaiGR/TransportHub.git
   cd TransportHub
   
2) Create a virtual environment:
   python -m venv env
   source env/bin/activate  # On Windows, use `env\Scripts\activate`
   
3) Install dependencies:
   pip install -r requirements.txt
   
4) Apply migrations:
   python manage.py migrate

5) Run the development server:
   python manage.py runserver

6) Access the application:
   Open your web browser and go to http://127.0.0.1:8000/
