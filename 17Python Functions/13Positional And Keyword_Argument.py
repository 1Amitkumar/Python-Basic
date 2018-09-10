def myfunc(a, b, c):
    print(a, b, c)


# using positional arguments only
myfunc(12, 13, 14)

# here first argument is passed as positional arguments while other two as keyword argument
myfunc(12, b=13, c=14)

# same as above
myfunc(12, c=13, b=14)

# this is wrong as positional argument must appear before any keyword argument
# myfunc(12, b=13, 14)
