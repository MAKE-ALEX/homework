import random

part_1 = random.randint(1,255)
part_2 = random.randint(1,255)
part_3 = random.randint(1,255)
part_4 = random.randint(1,255)

ipadd = str(part_1)+'.'+str(part_2) + '.' + str(part_3) + '.' + str(part_4)
print("随机生成的IP地址：", ipadd)
