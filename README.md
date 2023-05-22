# blockstak_social_media
The project is a social media application built using Django and Django REST Framework.

# Project Description
The social media application allows users to create profiles, make posts, comment on posts, like posts, share posts, and establish connections with other users. It provides APIs for various operations such as creating and updating profiles, creating and retrieving posts, commenting on posts, liking posts, sharing posts, searching for posts, and managing user connections.

# Installation
To set up the project locally, follow these steps:
1. Go to your cmd of particular floder and write the following instructions without quatations
2. `git clone https://github.com/evana27perveen/blockstak_social_media.git`
3. `cd blockstak_social_media`
4. `myenv\Scripts\activate`
5. `pip install -r requirements.txt`
6. `python manage.py migrate`
7. `python manage.py runserver`
The application will be accessible at http://localhost:8000.

# Features
User Authentication: Users can create accounts and authenticate using their email or phone number.
Profiles: Users can create profiles with their full name, profile picture, bio, and social media accounts.
Posts: Users can create posts with a title, text, and an optional image.
Comments: Users can comment on posts.
Likes: Users can like posts.
Shares: Users can share posts.
Connections: Users can establish connections with other users.

# API Endpoints
The project provides the following API endpoints:

1. POST /api/auth/user/create/: Create a user account.
2. POST /api/auth/login/: Login and obtain an access token.
3. POST /api/auth/login/refresh/: Refresh the access token.
4. GET /api/main/profiles/: List all profiles.
5. POST /api/main/profiles/: Create a profile.
6. GET /api/main/profiles/my-operations/: Retrieve the authenticated user's profile.
7. PUT /api/main/profiles/my-operations/: Update the authenticated user's profile.
8. GET /api/main/posts/: List all posts.
9. POST /api/main/posts/create/: Create a post.
10. GET /api/main/posts/{id}/: Retrieve a post by ID.
11. GET /api/main/comments/: List all comments.
12. POST /api/main/comments/create/: Create a comment.
13. GET /api/main/likes/: List all likes.
14. POST /api/main/likes/create/: Like a post.
15. GET /api/main/shares/: List all shares.
16. POST /api/main/shares/create/: Share a post.
17. GET /api/main/posts/search/: Search posts by title.
18. GET /api/main/connections/: List all connections.
19. POST /api/main/connections/: Create a connection.
20. GET /api/main/connections/{id}/: Retrieve a connection by ID.

# Technologies Used
Django
Django REST Framework
MongoDB (as the database)
Python

# Credits
The project was developed by **Evana Perveen Eva**



