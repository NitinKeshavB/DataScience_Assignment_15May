def fib2(val):
    if val == 0:
        return 0
    elif val == 1:
        return 1
    else:
        return fib2(val-1) + fib2(val-2)