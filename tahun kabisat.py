tahun = int(input("Input Year: "))

if tahun % 400 == 0:
    print("{} is a leap year".format(tahun))
elif tahun % 100 == 0:
    print("{} is't a leap year".format(tahun))
elif tahun % 4 == 0:
    print("{} is a leap year".format(tahun))
else:
    print("{} is't a leap year".format(tahun))
