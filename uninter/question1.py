def admissions():
    name = str(input('Please, type a name:'))
    age = int(input('Please, type students age: '))
    institution = ''
    if age >= 1 and age <= 5:
        institution = 'kindergarten'
    elif age >= 6 and age <= 10:
        institution = 'elementary school'
    elif age > 10 and age < 15:
        institution = 'middle school'
    elif age > 15 and age < 18:
        institution = 'high school'
    elif age > 18:
        institution = 'college'
    print('The student {} is {} years and is in {}' .format(
        name, age, institution))
    end = int(
        input('Type 0 to continue and another value to stop'))
    if end != 0:
        print('End of program')
    elif end == 0:
        admissions()


admissions()
