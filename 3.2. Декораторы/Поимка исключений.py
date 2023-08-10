def exception_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            # Handle the exception
            print(f"An exception occurred: {str(e)}")
            # Optionally, perform additional error handling or logging
            # Reraise the exception if needed

    return wrapper


@exception_handler
def divide(x, y):
    result = x / y
    return result


divide(10, 0)
