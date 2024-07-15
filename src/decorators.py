from functools import wraps
from typing import Any, Callable


def log(filename: Any) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
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


@log(filename='src/log_file.txt')
# log(filename=None)
def my_function(x: int, y: int) -> int:
    """ Функция складывающая два числа """
    return x + y


if __name__ == "__main__":
    print(my_function(1, 2))
