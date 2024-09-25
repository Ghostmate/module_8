def add_everything_up(a,b):
    try:
        # if isinstance(a,int|float) != isinstance(b,int|float):
        #     raise Exception('let it be string')
        return a + b
    except:
        return str(a) + str(b)

print(add_everything_up(45,'df'))