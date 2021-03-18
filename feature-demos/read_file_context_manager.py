from contextlib import contextmanager


@contextmanager
def safe_open(*args, **kwargs):

    file_handle = None

    try:

        file_handle = open(*args, **kwargs)

    except IOError as exc:
        yield None, exc  # return for an exception

    else:
        try:
            yield file_handle, None  # return for success
        finally:

            if file_handle:
                file_handle.close()


with safe_open("colors.txt", "r") as (colors_file, exc):

    if exc:
        print(exc)
    else:
        for color in colors_file:
            print(color.rstrip())
