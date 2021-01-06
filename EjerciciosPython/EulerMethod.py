### Euler Method ###

def dy(x):
    return 4*x
def y(x):
    return 2*x*x

x = 1
y = y(x)
h = 0.01

while(x < 10):

    y = y + h*dy(x)
    x = x + h
    yReal = 2*x*x
    print("X: "+str('%.2f' % x)+" | y: "+str('%.2f' % y) + " / yReal: "+str('%.2f' % (2*x*x))) #
    print(str('%.4f' % abs((y-2*x*x))))

input()

#'%.2f' % 1.234
