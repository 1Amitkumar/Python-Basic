def named_args(name, greeting):
    print(greeting + " " + name)


named_args(name='jim', greeting='Hello')


named_args(greeting='Hello', name='jim')  # you can pass arguments this way too

