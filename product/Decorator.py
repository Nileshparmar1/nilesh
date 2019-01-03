def devide_decorate(func):
    def check(a,b):
        if b==0:
            print("Division not possible")
            return
        else:
            return func(a,b)
    return check
@devide_decorate
def Devide(a,b):
    return a/b
print("division is:",Devide(10,2))


