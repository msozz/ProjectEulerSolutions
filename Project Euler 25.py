nums = [1,1,2]
num = 1
newnum = 2
while len(str(newnum)) < 1000:
    newnum += num
    num = newnum - num
    nums.append(newnum)

print(len(nums))