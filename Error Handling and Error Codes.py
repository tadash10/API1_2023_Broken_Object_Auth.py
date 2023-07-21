# api.py
class APIError(Exception):
    def __init__(self, code, message):
        self.code = code
        self.message = message

def api_function_get_object(user, obj_id):
    try:
        # The rest of the code remains the same
    except Exception as e:
        error_message = f"Error while processing the request: {str(e)}"
        logger.error(error_message)
        raise APIError(code=500, message=error_message)
