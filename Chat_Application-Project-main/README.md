💬 Real-Time Team Chat App
A real-time team collaboration chat application built using Django and Django Channels, enabling users to create teams, manage channels, and communicate instantly via direct and group messaging.

🚀 Features
✅ User Registration & Authentication (JWT)

✅ Team & Channel Management

✅ Direct & Channel Messaging

✅ Real-Time Chat via WebSockets

✅ Online/Offline User Status

✅ Message Search by keyword, sender & channel

✅ Scalable & Secure Architecture

🛠️ Tech Stack
Backend: Django, Django REST Framework
Real-time: Django Channels, WebSockets
Database: SQLite
Authentication: JWT (SimpleJWT)
Deployment: ASGI (with Daphne)

📂 Project Structure
Realtime_Chat/
│
├── Message_App/         # Core app (users, teams, channels, messages)
├── templates/           # WebSocket testing HTML
├── Realtime_Chat/       # Project settings
├── manage.py
└── requirements.txt
# 1. Clone the repository
git clone https://github.com/your-username/realtime-chat.git
cd realtime-chat

📦 Setup Instructions
# 2. Create virtual environment
python -m venv env
source env/bin/activate  # on Windows: env\Scripts\activate
# 3. Install dependencies
pip install -r requirements.txt
# 4. Run migrations
python manage.py makemigrations
python manage.py migrate
# 5. Run development server
python manage.py runserver

🔁 For WebSocket Support:
# Start ASGI server
daphne Realtime_Chat.asgi:application

✅ API Endpoints
| Endpoint                   | Method | Description                      |
| -------------------------- | ------ | -------------------------------- |
| `/api/register/`           | POST   | Register new user                |
| `/api/users/`              | GET    | List all users                   |
| `/api/teams/create/`       | POST   | Create a new team                |
| `/api/teams/`              | GET    | List user’s teams                |
| `/api/channels/create/`    | POST   | Create a new channel             |
| `/api/channels/<team_id>/` | GET    | List channels under a team       |
| `/api/messages/create/`    | POST   | Send message to channel/thread   |
| `/api/messages/search/`    | GET    | Search messages                  |
| `/api/dm-threads/create/`  | POST   | Create direct message thread     |
| `/api/dm-threads/`         | GET    | List DM threads for current user |


🧪 Test WebSocket
Open templates/ws_chat.html in browser, connect to:
ws://127.0.0.1:8000/ws/chat/<room_name>/

🔐 Security
Secure JWT authentication
Encrypted WebSocket messages (via WSS)
Role-based access control for channels

👩‍💻 Author
Mamta Kumari
Python Backend Developer

📄 License
This project is licensed under the MIT License.
Feel free to use and contribute!
