# Restaurant Table Reservation System

A robust Django-based backend system for managing restaurant table reservations. This project is containerized with Docker and uses PostgreSQL for reliable data storage

## 🚀 Features

- **Table Management:** Efficient handling of restaurant tables and availability
- **Reservation Logic:** Backend workflows for booking and client services
- **Dockerized Architecture:** Fully containerized environment for consistent development and deployment
- **Environment Security:** Secure configuration using `.env` files and `python-dotenv`
- **Database:** PostgreSQL integration for production-ready data persistence

## 🛠 Tech Stack

- **Framework:** [Django 5.0+](https://www.djangoproject.com/)
- **Database:** [PostgreSQL 15](https://www.postgresql.org/)
- **Containerization:** [Docker](https://www.docker.com/) & [Docker Compose](https://docs.docker.com/compose/)
- **Language:** [Python 3.12+](https://www.python.org/)
- **Environment Management:** `python-dotenv`

## 📦 Installation & Setup

### Prerequisites
- Docker and Docker Compose installed on your system.
- Git.

### 1. Clone the Repository
```bash
git clone [https://github.com/fotovisp/restaurant_table_reservation_system.git](https://github.com/fotovisp/restaurant_table_reservation_system.git)
cd restaurant_table_reservation_system
```
### 2. Configure Environment Variables

```bash
cp .env.example .env
```

### 3. Build and Run with Docker

``` bash
docker-compose up --build
```

### 4. Apply Migrations

```
docker-compose exec web python manage.py migrate
```

### 5. Access the Application
The server will be running at http://localhost:8000

### 📁 Project Structure

-    **apps/core/: Main application logic**

-    **config/: Project settings and URL configurations**

-    **Dockerfile & docker-compose.yml: Containerization settings**

-   **.env.example: Template for environment variables**

### 🛡 License

This project is open-source and available under the **MIT License**

**Developed by fotovisp**
