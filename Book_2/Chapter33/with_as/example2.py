# lock = trheading.Lock()         # после import threading
# with lock:
    # критический раздел кода
    # ...доступ к разделяемым ресурсам...

import decimal
with decimal.localcontext() as ctx:
    ctx.prec = 2
    x = decimal.Decimal('1.00') / decimal.Decimal('3.00')
print(x)