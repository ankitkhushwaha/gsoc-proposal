import os
import time
import joblib
from functools import wraps

CACHE_DIR = "cache"
EXPIRATION = 86400  # 24 hours

def cache(func):
    @wraps(func)
    def wrapper(param):
        os.makedirs(CACHE_DIR, exist_ok=True)
        cache_file = os.path.join(CACHE_DIR, f"{param}_plot.pkl")

        if os.path.exists(cache_file):
            if time.time() - os.path.getatime(cache_file) > EXPIRATION:
                os.remove(cache_file)
            else:
                return joblib.load(cache_file)

        result = func(param)
        joblib.dump(result, cache_file)
        return result

    return wrapper
