import time

def log_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        with open('execution_log.txt', 'a') as f:
            f.write(f"{func.__name__} took {end - start:.4f} seconds\n")
        return result
    return wrapper
