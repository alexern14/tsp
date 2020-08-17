import random

n = 7

txt_file = open("testn.txt", "w")
txt_file.write("{}\n".format(n))

for z in range(n):
    x = random.randint(0, 50)
    y = random.randint(0, 50)
    txt_file.write("{} {}\n".format(x, y))

txt_file.close()