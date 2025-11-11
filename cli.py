from typing import Callable


def input_error(func: Callable):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            # implementation
            pass
        except KeyError:
            # implementation
            pass
        except IndexError:
            # implementation
            pass

    return inner


def parse_input(user_input):
    # your implementation!
    # cmd, *args = user_input.split()
    # cmd = cmd.strip().lower()
    # return cmd, *args
    pass
