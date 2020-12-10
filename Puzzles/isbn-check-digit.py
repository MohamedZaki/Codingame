import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def validate(isbn):
    #Validate ISBN
    print(isbn, file=sys.stderr)
    if any(x.isalpha() for x in  isbn[:-1]):
        return False

    digits_sum=0
    check = 'X'
    if len(isbn)==10:
        for i, x in enumerate(isbn[:-1]):
            digits_sum += int(x)*(10-i)
        mod = digits_sum%11
        if mod==0:
            check=0
        elif 11-mod<10:
            check = 11-mod
        print('{} with sum= {}, check={}'.format(isbn,digits_sum,check), file=sys.stderr)

    elif len(isbn)==13:
        for i, x in enumerate(isbn[:-1]):
            alt = (1,3)[i%2]
            digits_sum += int(x)*alt
        mod = digits_sum%10
        if mod ==0:
            check=0
        else:
            check = 10-mod
        print('{} with sum= {}, check={}'.format(isbn,digits_sum,check), file=sys.stderr)

    else:
        return False
    return str(check)==isbn[-1]


invalid=[]
n = int(input())
for i in range(n):
    isbn = input()
    if not validate(isbn):
        print(isbn+' not valid', file=sys.stderr)
        invalid.append(isbn)

print(str(len(invalid))+' invalid:')
print('\n'.join(code for code in invalid))
