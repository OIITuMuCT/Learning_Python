try:
    try:
        raise IndexError()
    except Exception as E:
        raise TypeError() from E
except Exception as E:
    raise SyntaxError() from E