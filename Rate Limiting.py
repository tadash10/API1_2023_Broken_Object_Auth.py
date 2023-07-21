# api.py
import time

# Define a decorator for rate limiting
def rate_limit(max_requests=10, period=60):
    requests = []
    
    def decorator(func):
        def wrapper(*args, **kwargs):
            now = time.time()
            requests_in_period = [req for req in requests if now - req < period]
            if len(requests_in_period) >= max_requests:
                raise RuntimeError("Rate limit exceeded. Please try again later.")
            result = func(*args, **kwargs)
            requests.append(now)
            return result
        return wrapper
    return decorator

# Apply rate limiting to the API function
@rate_limit(max_requests=10, period=60)
def api_function_get_object(user, obj_id):
    try:
        # The rest of the code remains the same
    except Exception as e:
        error_message = f"Error while processing the request: {str(e)}"
        logger.error(error_message)
        raise APIError(code=500, message=error_message)
