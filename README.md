# shop-api

## **Introduction**

This project is a Django REST API for an e-commerce domain. It provides endpoints for managing products. The API is built using Django Rest Framework and PostgreSQL database. The application is containerized using Docker, and the CI/CD pipeline is set up using GitHub Actions and AWS ECR.

## Technologies

- Python 3.9
- Django Rest Framework 3.14
- PostgreSQL
- Git
- Docker
- GitHub Actions
- AWS ECR

## Usage

The API provides the following endpoints for unauthorized users:

- /products/
    - GET: List all products
- /products/<product_id>/
    - GET: Retrieve a specific product by id

The API provides the following endpoints for superusers:

- /products/
    - GET: List all products
    - POST: Create a new product
- /products/<product_id>/
    - GET: Retrieve a specific product by id
    - PUT: Update a specific product by id
    - DELETE: Delete a specific product by id

To access these endpoints, you need to authenticate using a superuser username and password. Login page: 

For more information on the API endpoints and their usage, refer to the documentation at [http://localhost:8000/openapi](http://localhost:8000/openapi)
.

## Installation

1. Clone the repository
    
    ```bash
    git clone https://github.com/STetiana/shop-api.git
    ```
    
2. Install Docker on your machine if you don't have it already. Visit [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)
 for more information.
3. If needed specify your own value of variables for PostgreSQL connection in .env file.
4. Run the following command to build image and run containers. 
    
    ```bash
    docker-compose up -d --build
    ```
    
5. In docker terminal using the following command create a superuser for adding and updating information about products:
    
    ```bash
    python ./shop/manage.py createsuperuser
    ```
    
6. The project includes integration tests that can be run using the following command:
    
    ```bash
    cd shop
    python manage.py test
    ```
    

Access the API at [http://localhost:8000/products/](http://localhost:8000/products/)

## CI/CD Pipeline

This project consists of two CI pipelines to streamline the development process. The first pipeline is triggered when code is pushed to any branch other than main. This pipeline will automatically build and test the code to ensure its quality before it is merged into the main branch. The second pipeline is triggered when code is pushed to the main branch. This pipeline will build the code, create a Docker image, and deploy it to Amazon Elastic Container Registry (ECR).

To use this pipeline, you need to set up the following:

1. Create an AWS ECR repository
2. Create a GitHub secret called `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` with the AWS access key ID and secret access key, respectively.
3. Set the environment variables in the `.github/workflows/deploy.yml` file.
