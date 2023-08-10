def validate_input(*validations):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i, val in enumerate(args):
                if i < len(validations):
                    if not validations[i](val):
                        raise ValueError(f"Invalid argument: {val}")
            for key, val in kwargs.items():
                if key in validations[len(args):]:
                    if not validations[len(args):][key](val):
                        raise ValueError(f"Invalid argument: {key}={val}")
            return func(*args, **kwargs)

        return wrapper

    return decorator


@validate_input(lambda x: x > 0, lambda y: isinstance(y, str))
def divide_and_print(x, message):
    print(message)
    return 1 / x


divide_and_print(5, "Hello!")
