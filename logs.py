import logging


def my_logger(logger: logging.Logger):
    def decorator(original_func):
        def wrapper(*args, **kwargs):
            logger.debug(f'{original_func.__name__} chiamata con args: {args} e kwargs: {kwargs}')
            r = original_func(*args, **kwargs)
            logger.debug(f'{original_func.__name__} ritorna con risultato {r}')
            return r
        return wrapper
    return decorator
