# Nginx Log Aggregator Django Application

## Overview

This project is a Django application designed to process and aggregate Nginx logs. The application includes a Management command that accepts a URL to a log file in a specific format, parses the log entries, and stores them in the database.

### Example Log Entry

```
{
  "time": "17/May/2015:08:05:32 +0000",
  "remote_ip": "93.180.71.3",
  "remote_user": "-",
  "request": "GET /downloads/product_1 HTTP/1.1",
  "response": 304,
  "bytes": 0,
  "referrer": "-",
  "agent": "Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.21)"
}
```

### Key Features

- **Management Command**: A command to parse and import log data into the database.
- **Database Model**: A Django model representing the parsed log data with fields for IP address, log date, HTTP method (GET, POST, etc.), request URI, response code, and response size.
- **Admin Interface**: Display and manage the parsed data via Django Admin.
- **API**: Access and manipulate the log data through a RESTful API using Django REST Framework (DRF).
  - Includes pagination, filtering, and searching capabilities.
  - Swagger documentation for API endpoints.

## Getting Started

### Setup

1. **Environment Configuration**:Rename the `.env.template` file to `.env` in the root directory of the project. Ensure all necessary environment variables are configured.
2. **Running the Application**:Use Docker Compose to build and start the application. Run the following command in your terminal:

   ```bash
   docker compose -f "docker-compose.yml" up -d --build
   ```
3. **Accessing the Application**:

   - **Main page:** `http://127.0.0.1`
   - **Admin Interface**: Navigate to `http://127.0.0.1/admin` to access the Django admin interface.
   - **API Endpoints**: Visit `http://127.0.0.1/api/logs` to explore the API.
   - **Swagger** documentation is available at `http://127.0.0.1/swagger`.

## Features

- **Django Admin**:

  - Filter and search log data with ease.
  - Intuitive interface for managing aggregated log data.
- **API**:

  - Comprehensive API with pagination, filtering, and searching.
  - Easily explore API endpoints with Swagger documentation.

## Additional Features

- Fully containerized using Docker and Docker Compose.
- Implements Django admin filters and search functionality.
- Supports DRF pagination, filtering, search, and Swagger documentation for easy API exploration.

## Contribution

Feel free to fork this repository, create a new branch, and submit a pull request with your changes. Any improvements or enhancements are welcome.

## License

This project is licensed under the MIT License.
