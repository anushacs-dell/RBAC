## Role-Based Access Control (RBAC) Django Project

## Overview

This is a Django-based project demonstrating Role-Based Access Control (RBAC) implemented using Django REST Framework (DRF). 
The project features JWT authentication for user login, token management, and role-based access restrictions for different types of users (Admin, User, Moderator).
It includes user registration, login, and logout functionality along with protected views that require specific user roles to access.

## Features

- **User Registration**: Users can register using a username, email, password, and role (User, Admin, or Moderator).
- **Login & JWT Authentication**: The project uses JSON Web Tokens (JWT) for authentication. Upon successful login, users receive an access token and refresh token.
- **Role-Based Access**: Different roles (Admin, User, Moderator) are implemented, with users only allowed to access resources permitted by their role.
- **Logout & Token Blacklisting**: Upon logout, the refresh token is blacklisted, preventing it from being used again.
- **Protected Views**: Certain views are protected and can only be accessed based on the user's role.
  
  - Admin view: Accessible only by users with the `Admin` role.
  - User view: Accessible only by users with the `User` role.
  - Moderator view: Accessible only by users with the `Moderator` role.

## Tech Stack

- **Backend**: Python 3.x, Django 4.x
- **Database**: SQLite (for development purposes)
- **Authentication**: JWT (using `rest_framework_simplejwt`)
- **Permissions**: Role-Based Permissions using Django REST Framework's built-in permission classes.

## Project Setup

### Prerequisites

1. Python 3.x
2. Django 4.x
3. Django REST Framework
4. `rest_framework_simplejwt` for JWT Authentication

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/anushacs-dell/RBAC.git
   cd RBAC

## Api Endpoints

### Register User
   POST /register

Request Body:(JSON)
{
    "username": "testuser",
    "email": "test@example.com",
    "password": "password123",
    "role": "User"
}

Response:
{
    "message": "Registered successfully"
}

### Login
POST /login

Request Body:(JSON)
{
    "username": "testuser",
    "password": "password123"
}
Response:
{
    "message": "Login successfully",
    "access_token": "<access_token>",
    "refresh_token": "<refresh_token>"
}
### Logout
POST /logout

Request Body:
{
    "refresh_token": "<refresh_token>"
}
Response:
{
    "message": "Logout Successful"
}
### Access Admin View
GET /admin

Requires the Admin role.

Response:
{
    "message": "Welcome Admin"
}
### Access User View
GET /user

Requires the User role.

Response:
{
    "message": "Welcome User"
}
### Access Moderator View
GET /moderator

Requires the Moderator role.

Response:
{
    "message": "Welcome Moderator"
}
### Token Refresh
POST /api/token/refresh/

Request Body:(JSON)
{
    "refresh": "<refresh_token>"
}
Response:
{
    "access": "<new_access_token>"
}

## Future Improvements
Implementing email verification during registration.
Adding password reset functionality.
set custom permissions : (permissions.py)
    from rest_framework.permissions import BasePermission
    
    class IsAdmin(BasePermission):
        def has_permission(self, request, view):
            return request.user.role == 'Admin'
(views.py)
    from .permissions import IsAdmin

    @api_view(['GET'])
    @permission_classes([IsAdmin])
    def admin_view(request):
        return Response({"message": "Welcome Admin"})
