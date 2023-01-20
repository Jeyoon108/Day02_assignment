# Chap9 # 3

def start2end(func):
    def new_func(*args, **kwargs):
        print(f'start func {func.__name__}')
        result = func(*args, **kwargs)
        print('result: ', result)
        print('end')
        return result
    return new_func


@start2end
def sound():
    print("quak, Quak")


sound()
