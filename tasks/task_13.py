import time
from collections import OrderedDict

def cached(max_size=None, seconds=None):
    if not isinstance(max_size, int) and max_size is not None:
        max_size = None
    if not isinstance(seconds, (int, float)) and seconds is not None:
        seconds = None
    
    def decorator(func):
        cache = OrderedDict()
        
        def wrapper(*args, **kwargs):
            key = (args, tuple(sorted(kwargs.items())))
            
            if key in cache:
                result, timestamp = cache[key]
                if seconds is None or (time.time() - timestamp) < seconds:
                    cache.move_to_end(key)
                    return result
            
            result = func(*args, **kwargs)
            
            cache[key] = (result, time.time())
            
            if max_size is not None and len(cache) > max_size:
                cache.popitem(last=False)
            
            return result
        
        return wrapper
    
    return decorator

@cached(max_size=3, seconds=10)
def slow_function(x):
    print(f"Вычисляю для {x}...")
    return x ** 2

print(slow_function(2))  
print(slow_function(2)) 
time.sleep(15)
print(slow_function(2)) 