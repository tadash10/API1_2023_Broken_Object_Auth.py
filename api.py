from data_source import DataSource
from authorization import is_authorized

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
