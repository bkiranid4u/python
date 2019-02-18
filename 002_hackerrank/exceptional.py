from math import log
""" Module for exceptional Handling """

def convert(s):
    """ Convert to an Integer """
    try:
        return (int(s))
    except (TypeError, ValueError):
        raise

# print(convert('33'))
# print(convert('ABC'))
# print(convert('[33]'))

def string_log(s):
    v = convert(s)
    print(log(v))
string_log('33')
string_log('[33]')