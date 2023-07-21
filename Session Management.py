# main.py
class SessionManager:
    def __init__(self):
        self.sessions = {}

    def create_session(self, user):
        session_token = generate_token(user)
        self.sessions[session_token] = user
        return session_token

    def get_user_from_session(self, session_token):
        return self.sessions.get(session_token)

# Usage
if __name__ == "__main__":
    session_manager = SessionManager()
    authenticated_user = User(user_id=100)
    session_token = session_manager.create_session(authenticated_user)
    print("Session Token:", session_token)

    # Later, when the user makes API requests, you can retrieve the user from the session token
    user_from_session = session_manager.get_user_from_session(session_token)
    print("User from Session:", user_from_session.user_id)
