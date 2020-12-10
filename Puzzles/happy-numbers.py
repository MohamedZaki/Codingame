def isHappy(x):
    checked = []
    nums = str(x)
    while nums != '1' and not (nums in checked):
        checked.append(nums)
        result = 0
        for num in nums:
            result += int(num)**2
        nums = str(result)
    if (nums == '1'):
        print("{} :)".format(x))
    else:
        print("{} :(".format(x))

n = int(input())
for i in range(n):
    x = input()
    isHappy(x)