def spam():
    bacon()


def bacon():
    raise Exception('This is the error message.')


# From the traceback, you can see that the error happened on line 5, in the bacon() function.
# This particular call to bacon() came from line 2, in the spam() function, which in turn was
# called on line 7. In programs where functions can be called from multiple places, the call
# stack can help you determine which call led to the error.
spam()
