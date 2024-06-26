# l = [x + ' ggg' for x in 'gradus']
# print(l)

#
# x = input()
#
# lst1 = [float(a) for a in x.split()]
# lst = [abs(a) for a in lst1]
#
# print(lst)

# t = ['qwe', 'dqwd']
# e = [x for x in t]
# print(e)
# print(id(t))
# print(id(e))
# print(type(t))
# print(type(e))


lst_in = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 8, 7, 6],
          [5, 4, 3, 2]]

res = [x
       for row in lst_in
       for x in row]

res.reverse()

print(*res)