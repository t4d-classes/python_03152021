def safe_open(*args, **kwargs):

    file_handle = None

    try:
        file_handle = open(*args, **kwargs)
    except IOError as exc:
        yield None, exc  # return for an exception
    else:
        try:
            yield file_handle, None  # return for success
            # func(file_handle, None)
        finally:
            print("clean things up")
            if file_handle:
                file_handle.close()


safe_handle = safe_open("colors.txt", "r")

(colors_file, exc) = next(safe_handle)

if exc:
    print(exc)
else:
    for color in colors_file:
        print(color.rstrip())

print("time to wrap up the file reading")

# end of the with block
next(safe_handle)

# def do_it(colors_file, exc):
#     if exc:
#         print(exc)
#     else:
#         for color in colors_file:
#             print(color.rstrip())

# safe_open(do_it, "colors.txt", "r")
