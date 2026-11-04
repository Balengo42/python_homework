import logging 

logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))

def logger_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args,**kwargs)

        logger.log(logging.INFO, f"function: {func.__name__}")
        logger.log(logging.INFO, f"positional paramaters: {list(args) if args else 'none'}")
        logger.log(logging.INFO, f"keyword parameters: {kwargs if kwargs else 'none'}")
        logger.log(logging.INFO, f"return: {result}")
        logger.log(logging.INFO, "")
        return result 
    return wrapper 

@logger_decorator
def hello():
    print("Hello, World!")

@logger_decorator
def positional(*args):
    return True

@logger_decorator
def keywords(**kwargs):
    return logger_decorator

hello()
print(positional(1,2,3))
print(keywords(color ="blue"))

