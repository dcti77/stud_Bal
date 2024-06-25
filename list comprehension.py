# l = [x + ' ggg' for x in 'gradus']
# print(l)


x = input()

lst1 = [float(a) for a in x.split()]
lst = [abs(a) for a in lst1]

print(lst)

