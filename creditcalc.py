import math
import sys
args = sys.argv


def error():
    print('Incorrect parameters')
    quit()


def extraction(a):
    return a.split('=')[1]


if len(args) != 5 or args[1] not in ['--type=diff', '--type=annuity']\
        or not args[4].startswith('--interest='):
    error()

i = abs(float(extraction(args[4])) / (100 * 12))
total = 0

if args[2].startswith('--principal='):
    if not args[3].startswith('--payment=') and not args[3].startswith('--periods='):
        error()

    P = abs(int(extraction(args[2])))

    if args[3].startswith('--payment='):
        if args[1] != '--type=annuity':
            error()

        A = abs(float(extraction(args[3])))
        n = math.ceil(math.log(A / (A - i * P), 1 + i))
        years = n // 12

        if n % 12 != 0:
            if n < 12:
                print(f'You need {n} months to repay this credit!')
            else:
                print(f'You need {years} years and {n % 12} months to repay this credit!')
        elif n == 12:
            print(f'You need {years} year to repay this credit!')
        else:
            print(f'You need {years} years to repay this credit!')
        total = A * n

    elif args[3].startswith('--periods='):
        n = abs(int(extraction(args[3])))
        m = 1
        if args[1] == '--type=annuity':
            A = math.ceil(P * ((i * math.pow(1 + i, n)) / (math.pow(1 + i, n) - 1)))
            print(f'Your annuity payment = {A}!\n')
            total = A * n

        elif args[1] == '--type=diff':
            while m <= n:
                D = math.ceil((P / n) + i * (P - ((P * (m - 1)) / n)))
                print(f'Month {m}: paid out {D}')
                m += 1
                total += D
    print(f'\nOverpayment = {total - P}')


elif args[2].startswith('--payment='):
    if args[1] != '--type=annuity':
        error()
    if not args[3].startswith('--periods=') and not args[4].startswith('--interest='):
        error()

    A = abs(float(extraction(args[2])))
    n = abs(int(extraction(args[3])))
    P = math.ceil(A / ((i * math.pow(1 + i, n)) / (math.pow(1 + i, n) - 1)))
    total = A * n

    print(f'Your credit principal = {P}!\n'
          f'Overpayment = {total - P}')

else:
    error()
