# Django REST API CRUD Operations

This project demonstrates the creation of a simple Django REST API capable of performing CRUD (Create, Read, Update, Delete) operations on a "person" resource.

## Getting Started

These instructions will help you set up and run the project on your local machine.

### Prerequisites

- Python (3.x recommended)
- Django
- Django Rest Framework

### Installing

1. Clone the repository:

   ```bash
   git clone https://github.com/priest-tech/django-stage_two_api.git

API Endpoints
Create Person
Endpoint: POST /api/persons/
Request Body: JSON object with a name field
{
  "name": "John Doe"
}

Read Person
Endpoint: GET /api/persons/?name={name}
Parameters: name (string) - The name of the person to fetch.

Update Person
Endpoint: PUT /api/persons/{id}/
URL Parameter: id (integer) - The ID of the person to update.
Request Body: JSON object with a name field.
Example:{
  "name": "Updated Name"
}

Delete Person
Endpoint: DELETE /api/persons/{id}/
URL Parameter: id (integer) - The ID of the person to delete.

Dynamic Parameter Handling
The API is designed to handle dynamic input for CRUD operations. For example, if you pass a specific name, you can perform all CRUD operations on that name.

Validation
The name field is validated to allow only letters and spaces. Other data types are not allowed.

Built With
Django - The web framework for perfectionists with deadlines.
Django Rest Framework - A powerful and flexible toolkit for building Web APIs.