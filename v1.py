class DataSource:
    def __init__(self):
        self.objects = {
            1: {'id': 1, 'name': 'Object1', 'owner_id': 100},
            2: {'id': 2, 'name': 'Object2', 'owner_id': 200},
            # Add more objects here
        }

    def get_object_by_id(self, obj_id):
        return self.objects.get(obj_id)

class User:
    def __init__(self, user_id):
        self.user_id = user_id

def is_authorized(user, object_owner_id):
    return user.user_id == object_owner_id

def api_function_get_object(user, obj_id):
    try:
        data_source = DataSource()
        obj = data_source.get_object_by_id(obj_id)

        if obj is None:
            raise ValueError("Object not found.")
        
        if not is_authorized(user, obj['owner_id']):
            raise PermissionError("You are not authorized to access this object.")
        
        return obj

    except Exception as e:
        raise RuntimeError(f"Error while processing the request: {str(e)}")

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
