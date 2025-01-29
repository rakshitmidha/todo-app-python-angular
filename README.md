# TODO App using Python FastAPI and Angular 19

## Prerequisites

*   Docker installed on your machine.
*   Docker Compose installed.

## Steps to Build and Run the Project

1.  Build and start the Docker containers.

```
docker-compose up --build
```

2.  The following services will be built and started:
    *   Angular app running on `http://localhost:4200`.
    *   FastAPI app running on `http://localhost:8000`.
    *   MongoDB running on `mongodb://localhost:27017`.

3.  To stop the services, use the following command:

```
docker-compose down
```

## Notes

Ensure that the MongoDB URI in the FastAPI app is set correctly in the environment variables:

```
MONGO_URI=mongodb://mongo:27017/todo_db
```