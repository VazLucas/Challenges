def func():

    nth = int(input("type a natural number: "))
    triangularNumber = int((nth +
                            (nth ** 2))/2)
    print("The {n}th triangular number is {t}" .format(
        n=nth, t=triangularNumber))

    while nth > 0:
        print("°" * nth, sep=' ')
        nth -= 1


func()
