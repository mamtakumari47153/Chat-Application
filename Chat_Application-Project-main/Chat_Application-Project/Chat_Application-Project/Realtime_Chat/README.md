Real-Time Team Chat Application - Django Based

This is a real-time team collaboration platform built with Django and Django REST Framework, enabling users to create teams, participate in channels, exchange direct messages, and view user presence in real-time.

Tasks Completed

Authentication & Users

User registration (/api/register/)

JWT authentication (login/logout via tokens)

List users (/api/users/)


Teams & Channels

Create teams (/api/teams/create/)

List teams for authenticated user (/api/teams/)

Create channels under teams (/api/channels/create/)

List channels in a team (/api/channels/<team_id>/)

Messaging

Send messages to channels (/api/messages/create/)

View message list (/api/messages/)

Search messages with filters (/api/messages/search/?q=hello)

Direct messaging via thread (/api/dm-threads/create/, /api/dm-threads/)


WebSocket Support (Real-Time Messaging)

Integrated Django Channels

Configured Redis as channel layer backend

Created ASGI application

WebSocket endpoint: /ws/chat/<room_name>/

Technologies Used

Django & Django REST Framework

Channels + Daphne (for WebSocket support)

Redis (for scalable channel layers)

JWT Authentication (SimpleJWT)

PostgreSQL / SQLite

WebSocket Testing UI (basic HTML + JS)

How to Run
# 1. Create and activate a virtual environment
python -m venv myenv
source myenv/bin/activate  #On Windows: env\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run migrations
python manage.py migrate

# 4. Run development server
python manage.py runserver

# 5. Run Daphne server for WebSocket
# (in a new terminal)
daphne Realtime_Chat.asgi:application

 Contact
Mamta KumariPython / Django Developer
mamtakumari47153@gmail.com


