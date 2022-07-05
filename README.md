# Django Demo Application

This is a sample application that represents a movie and tv-shows search engine.

## Running

To run this project just run `docker compose up --build`
This will start the Django backend at http://localhost:8000
and the React frontend at http://localhost:3000/app

## Configuration

You can configure the Sentry SDK of the Django Backend and the React frontend with environment variables.

For the backend you can set the following environment variables:

- `SENTRY_DSN_BACKEND` (must be set)
- `SENTRY_RELEASE_BACKEND` (optional, defaults to "0.0.1")
- `SENTRY_ENVIRONMENT_BACKEND` (optional, defaults to "dev")
- `SENTRY_TRACES_SAMPLE_RATE_BACKEND` (optional, defaults to "1.0")

To see all env variables have a look at the Dockerfile: https://github.com/getsentry/demo-app-django-react/blob/main/Dockerfile#L4-L10

The React frontend can be configured with following environment variables:

- `REACT_APP_SENTRY_DSN_FRONTEND` (must be set)
- `REACT_APP_SENTRY_RELEASE_FRONTEND` (optional, defaults to "0.0.1")
- `REACT_APP_SENTRY_ENVIRONMENT_FRONTEND` (optional, defaults to "dev")
- `REACT_APP_SENTRY_TRACES_SAMPLE_RATE_FRONTEND` (optional, defaults to "1.0")

To see all env variables have a look at the index.js: https://github.com/getsentry/demo-app-django-react/blob/main/app/src/index.js

## API

**HINT:** There is a browsable API, so you can open all the following example URLs in your browser and inspect the behaviour of the API.

- You can list all movies (in a paginated fashion) with the endpoint: http://localhost:8000/api/shows/
- You can search for movies by supplying a `q` query parameter: http://localhost:8000/api/shows/?q=spielberg (it is searched in the title, the director and the cast)
- You can retrieve the details of a movie with its `id`: http://localhost:8000/api/shows/330/
- Movies by Martin Scorsese trigger a unhandled exception. For example: http://localhost:8000/api/shows/6827/
