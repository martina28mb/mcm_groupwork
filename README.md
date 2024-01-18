# FETCHED PROJECT - mcm group
Fetched is web application crafted to streamline the process of finding accommodations within the Veneto region. Beyond its primary function of aiding in accommodation searches, Fetched offers a rich array of supplementary features to enhance the visitor experience.

In addition to a diverse range of lodging options, Fetched acts as a valuable travel companion by furnishing users with insightful suggestions for nearby museums. This feature enables travelers to delve into the vibrant culture of the region, exploring its artistic heritage and historical significance.

Moreover, Fetched goes beyond mere lodging recommendations and museum insights. It paints a vivid portrait of the Veneto region by presenting captivating descriptions complemented by images for each of its provinces.

By seamlessly integrating accommodations, museum recommendations, and evocative snapshots of Veneto's provinces, Fetched provides users with an immersive exploration of this captivating Italian region.

# Flask and FastAPI Dockerized Project
This project demonstrates a simple web application using Flask as the frontend and FastAPI as the backend. The frontend allows to search for a city in Veneto and the result is given by the backend using a search bar.

The project is Dockerized for easy deployment.

## Architecture
The project follows a simple client-server architecture:

1. **Frontend (Flask):**
   - Represents the user interface or client side.
   - Built with Flask, a lightweight web framework for Python.
   - Responsible for rendering web pages and user interaction, including the form for querying the backend.

2. **Backend (FastAPI):**
   - Represents the server or backend of the application.
   - Built with FastAPI, a modern web framework for building APIs with Python.
   - Handles requests from the frontend, including querying birthdays and providing the current date.

3. **Docker Compose:**
   - Orchestrates the deployment of both frontend and backend as separate containers.
   - Ensures seamless communication between frontend and backend containers.
   - Simplifies the deployment and management of the entire application.
