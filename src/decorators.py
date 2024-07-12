from functools import wraps


def log(filename=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                if filename is not None:
                    with open(filename, 'a') as log_file:
                        log_file.write(f'{func.__name__}) ok\n')
                elif filename is None:
                    print(f'{func.__name__} ok')
                return result
            except Exception as e:
                with open(filename, 'a') as log_file:
                    (log_file.write(f'{func.__name__} error:{e}, Inputs: {args}, {kwargs}\n'))
                raise e
        return wrapper

    return decorator
