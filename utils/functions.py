


def get_environ_vars(environ):
    # Sorting and stringifying the environment key, value pairs
    environ_vars = [
        '%s: %s' % (key, value) for key, value in sorted(environ.items())
    ]
    environ_vars = '\n'.join(environ_vars)
    
    return environ_vars