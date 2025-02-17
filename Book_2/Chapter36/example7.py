""" Отладка с помощью внешних операторов try """
try:
    def startprogramm():
        pass
except:
    import sys
    print('uncaught!', sys.exc_info()[0], sys.exc_info()[1])