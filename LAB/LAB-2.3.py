import random

total = 0

random_number = [random.randint(1, 100) for i in range(100)]

for ele in range(0, len(random_number)):
    total = total + random_number[ele]

print("生成的100个数字是：", random_number)
print("和：", total)
print("最大值：", max(random_number))
print("最小值：", min(random_number))
