# Only in Python 3.X statement nonlocal

def singleton(aClass):
    instance = None
    def onCall(*args, **kwargs):
        nonlocal instance
        if instance is None:
            instance = aClass(*args, **kwargs)
        return instance
    return onCall
