from random import randint


def subscription():
    number = randint(100, 400)
    person['Voucher'] = number
    voucherlist.append(number)
    if len(set(voucherlist)) == len(voucherlist):
        print('This is your voucher: {}' .format(number))
        person['Name'] = input('What is your name?')
        person['Phone'] = input('What is your phone?')
        person['Email'] = input('What is your email?')
        person['Course'] = input('What course?')
        detail()

        subscribed.append(person.copy())
        del mysub[:]
        mysub.append(person)
    else:
        detail()
        print("Voucher invalid, restart")
        detail()
        start()


def detail():
    print('-' * 45)


def start():

    print('choose 1 to make a new subscription')
    print('choose 2 to show the subscription list')
    print('choose 3 to show your subscription')
    print('choose 0 to end the program')
    choose = input('Type your choice')
    detail()
    if choose == '1':
        subscription()
        start()

    elif choose == '2':
        if not subscribed:

            print('No subscriptions')
            detail()
            start()
        else:
            print(*subscribed, sep='\n')
            detail()
            start()
    elif choose == '0':
        print('Program closed')

    elif choose == '3':
        if not mysub:
            print('Subscription not made')
            detail()
            start()
        else:
            print(mysub)
        detail()
        start()
    else:
        print('Invalid option. Please, select 1, 2 or 0')
        detail()
        start()


subscribed = []
mysub = []
voucherlist = []
person = {}

start()
