import time
a = 1
b = 2
def decor(func):
    def decor2():
        start_time = time.time()
        func()
        print("--- %s seconds ---" % (time.time() - start_time))
    return decor2

def alone_func():
    print(a,b)
function_decorated = decor(alone_func)
function_decorated()


