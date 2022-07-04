from functools import wraps
import datetime


def loger(log_path):
    def _loger(old_function):
        @wraps(old_function)
        def new_function(*args, **kwargs):
            log = {}
            Key = f"{args}{kwargs}"
            result = old_function(*args, **kwargs)
            log[Key] = f"{result} time-{datetime.datetime.now()}"
            with open(log_path, "a", encoding="utf-8") as f:
                for key, val in log.items():
                    f.write("{}:{}\n".format(key, val))
            return result

        return new_function

    return _loger
