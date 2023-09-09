
def func():

    columns = int(input("Enter number of columns of pattern: "))
    lines = int(input("enter number of lines: "))
    for i in range(0, lines):
        if i % 2 == 0:
            for j in range(0, columns):
                if j % 2 == 0:
                    print('1', sep='', end='')
                else:
                    print('0', sep='', end='')
            print()
        else:
             for j in range(0, columns):
                if j % 2 != 0:
                    print('1',sep='', end='')
                else:
                    print('0', sep='', end='')
                    print()


func()
