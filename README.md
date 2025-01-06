# "world-travel"

World Travel is a single page web application (SPA) that allows users to explore travel destinations, view their description and manage their information. Users can add new destinations, update their information, or delete existing destinations. Additionally, the app provides weather information for any city using the OpenWeather API. The application is designed to be an interactive platform that makes it easy to explore tourist destinations and check the weather in real time:

1. **Backend**: Application developed with Python and responsible for managing all database operations in Postgres, client requests (frontend) and integration with external services such as the OpenWeather API to obtain weather information..
2. **Frontend**: SPA (Single Page Application) developed with React that allows users to interact with the database of travel destinations, as well as obtain information about the climate of the cities of said destinations..

## Project Structure 

El proyecto está organizado en dos carpetas fundamentales:

- `\world-travel-backend`	: Contains the App in Python.
- `\world-travel-frontend`	: Contains the App in React.js.

https://github.com/GJGE04/world-travel-backend.git

## Technologies used

- **Backend**:
  - Python: Programming language used to develop server logic and manage communication with the database and external APIs. The backend is built in Python using the Flask framework..
  - Flask: Lightweight and flexible framework for Python, used to build RESTful APIs. Provides the structure to handle routes and HTTP requests on the backend.
  - PostgreSQL: Relational database management system. Used to store travel destination information, including name, country and description.
  - psycopg2: Python library to interact with PostgreSQL database. Provides the connection between the Flask application and the database to perform CRUD operations.
  - OpenWeather API: External API that provides real-time weather information. It is used to obtain weather data for cities that are associated with travel destinations.
  - CORS (Cross-Origin Resource Sharing): Mechanism that allows or restricts web resources requested from a domain other than that of the application itself. Ensures that frontend requests to the backend are accepted and not blocked by CORS policies.
  - Heroku/AWS: Cloud deployment services. The backend can be deployed on Heroku or AWS (EC2/RDS) for production, depending on your choice of infrastructure.
  
- **Frontend**:
  - React.js: JavaScript library to build interactive and dynamic user interfaces. The frontend is built with React to create a SPA (Single Page Application), managing the state and logic of the user interface.
  - Redux: JavaScript library to manage the global state of the application in a predictable way. It is used to manage the status of travel destinations and weather data between components.
  - Redux Thunk: Middleware for Redux that allows the execution of asynchronous actions. Used to handle asynchronous requests, such as HTTP requests to the backend to get, create, update, or delete targets.
  - Axios: JavaScript library to make HTTP requests. It is used to make requests to the backend, such as getting destinations or creating new destinations, and receiving weather information from the OpenWeather API
  - HTML5 & CSS3: Standard technologies for the construction and styling of web pages. They are used to structure the content and style the application, respectively
  - JavaScript (ES6+): Programming language used to implement logic on the frontend, including DOM management and interaction with APIs. It is the language used to develop the dynamic behavior of the application in the browser.
  - Create React App: Official tool to create React apps with default settings and optimizations. It is used to initialize the React project, configuring Webpack, Babel and other elements necessary for an efficient development environment.
  - AWS S3 + CloudFront: Amazon S3 is an object storage service, and CloudFront is a content delivery network (CDN). They are used to deploy the frontend, hosting the application's static files (HTML, CSS, JS) in an S3 bucket and distributing them globally through CloudFront.
  
- **Other tools**:
  - Git: Version control system: Used to manage source code and collaborate as a team, ensuring a clear history of changes made to the application.

## Characteristics
- Task CRUD: Create, read, update and delete tasks.
- View destinations and weather in an intuitive and modern interface.
- Select cities to view weather conditions.

## Requisitos
Node.js (v18 or higher version)
Postgres (Local)

### Backend

- **Node.js** 
- **Postgres**		
- **Visual Studio** 

### Frontend

- **Node.js** (v18 or higher version)
- **NPM** (viene con Node.js)
- **Visual Studio Code**
- **Google chrome browser**

## Installation and Configuration

### 1. Clone the Repo

Clone the repositories to the local computer:


### 2. Dependencies 

#### Backend

To create the database structure using Postgres in your backend, follow these steps:

1. Navigate to the backend directory and run the following command:

	npm install

2. Install dependencies
	First, you need to install Postgres and dotenv (to handle environment variables).
	Run the following commands in the terminal:
	
			npm install mongoose dotenv
				
3. Configuration in  the connection to Postgres. In a .db file in the root of the backend directory define the Port and other variables configured. For example:

		dbname="world_travel_db",  # Nombre de tu base de datos
        user="postgres",           # Tu usuario de PostgreSQL
        password="1234",   			# Tu contraseña de PostgreSQL
        host="localhost",           # Si estás en producción, usa la IP de tu servidor
        port="5432"                 # Puerto de PostgreSQL (5432 por defecto)
	
#### Frontend

1. Navigate to the frontend directory and run the following command:

		npm install
	
2. Install other necessary dependencies, e.g:

	- Install axios (for HTTP requests)
	
		npm install axios
	
### 3. Start the applicatio

#### Backend

1. In the backend directory, run the following command to start the server:

	python app.py
	
The backend will run on http://localhost:5000.
	
#### Frontend

1. In the frontend directory, run the following command to start the server:

	npm start

The frontend will be available in http://localhost:3000.

### 4. Endpoints en el Backend

- GET /destinations: Gets a list of all travel destinations stored in the database.
- POST /destination: Create a new destination.
- PUT /destination/:id: Update a destination.
- DELETE /destination/:id: Delete a destination.  

### 4. Considerations

- Tests of the various functionalities were carried out





