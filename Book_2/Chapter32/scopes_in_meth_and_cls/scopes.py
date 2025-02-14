# Scopes in Methods and Classes
# Области видимости в методах и классах это соответствует букве E в правиле LEGB
def generate():
    class Spam:     # Spam - это имя в локальной области видимости generate
        count = 1
        def method(self):
            print(Spam.count)       # Согласно правилу LEGB (E) доступно
                                    # в области видимости generate 
    return Spam()
generate().method()
