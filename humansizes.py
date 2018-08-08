SUFFIXES = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
            1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}

# Instead of the word `function`, in Python, you use `def`
def approximate_size(size, a_kilobyte_is_1024_bytes=True):

    '''Convert a file size to human-readable form.
    Keyword arguments:
    size -- file size in bytes
    a_kilobyte_is_1024_bytes -- if True (default), use multiples of 1024
                                if False, use multiples of 1000
    Returns: string
    '''
    if size < 0:
        raise ValueError('number must be non-negative')

    multiple = 1024 if a_kilobyte_is_1024_bytes else 1000
    for suffix in SUFFIXES[multiple]:
        size /= multiple
        if size < multiple:
            return '{0:.1f} {1}'.format(size, suffix)

    raise ValueError('number too large')

if __name__ == '__main__':
    print(approximate_size(16384, False))
    print(approximate_size(size=16384, a_kilobyte_is_1024_bytes=True))
    print(approximate_size(-16384))

    # this is an example provided by NSS/bangazon of the style for a ternary condition in Python
    # since they didn't have me do much besides run the code using python humansizes.py 
    # I'll put what I learned here instead...

    # Everything in Python is an object like Javascript without primative forms.
    # The entire module is run as this object in the CLI and given properties called _name_ with
    # a value of _main_

    # print() = console.log()
    # objects are called dictionaries in Python
    # whitespace matters
    # if and for use colons instead with indentation after
    # functions work simarily but are called defintions? they use def instead of function.
    # compliler determines values at runtime