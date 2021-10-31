import re
print(' '.join(['00 ','0 ']['1'in x]+'0'*len(x)for x in re.findall('0+|1+',''.join(bin(ord(x))[2:].zfill(7)for x in input()))))
