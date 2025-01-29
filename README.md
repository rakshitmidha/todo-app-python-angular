  Project Setup Guide body { font-family: Arial, sans-serif; line-height: 1.6; margin: 0; padding: 0; background-color: #f4f4f4; } header { background-color: #333; color: #fff; padding: 10px 20px; text-align: center; } h1 { margin: 0; } section { padding: 20px; margin: 20px; background-color: #fff; border-radius: 8px; } code { background-color: #eee; padding: 2px 4px; border-radius: 4px; } ul { padding-left: 20px; } pre { background-color: #222; color: #fff; padding: 10px; border-radius: 8px; overflow-x: auto; }

# Project Setup and Build Instructions

## Overview

This project contains an Angular frontend, a FastAPI backend, and MongoDB as a database, all running in Docker containers.

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