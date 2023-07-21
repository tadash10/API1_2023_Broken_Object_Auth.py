from user import User
from api import api_function_get_object

if __name__ == "__main__":
    try:
        # Simulate user authentication (Replace 100 with the actual authenticated user ID)
        authenticated_user = User(user_id=100)

        # Call the API function with the authenticated user and object ID
        object_id_to_retrieve = 1
        result = api_function_get_object(authenticated_user, object_id_to_retrieve)
        print("Object Details:", result)
        
    except PermissionError as e:
        print("PermissionError:", e)
        
    except ValueError as e:
        print("ValueError:", e)
        
    except RuntimeError as e:
        print("RuntimeError:", e)
        
    except Exception as e:
        print("An unexpected error occurred:", e)
