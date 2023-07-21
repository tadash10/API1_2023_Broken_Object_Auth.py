# api.py
from data_source import DataSource
from authorization import is_authorized

def api_function_get_object(user, obj_id):
    try:
        # Input Validation
        if not isinstance(obj_id, int) or obj_id <= 0:
            raise ValueError("Invalid object ID. Please provide a positive integer.")

        if not user or not hasattr(user, 'user_id'):
            raise ValueError("Invalid user information. Please provide a valid user object.")

        data_source = DataSource()
        obj = data_source.get_object_by_id(obj_id)

        if obj is None:
            raise ValueError("Object not found.")
        
        if not is_authorized(user, obj['owner_id']):
            raise PermissionError("You are not authorized to access this object.")
        
        return obj

    except Exception as e:
        raise RuntimeError(f"Error while processing the request: {str(e)}")
