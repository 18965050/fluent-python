l1 = [3, [66, 55, 44], (7, 8, 9)]
l2 = list(l1) #
l1.append(100) #
l1[1].remove(55) #
print('l1:', l1)
print('l2:', l2)
l2[1] += [33, 22] # l2[1]为list对象, 直接引用
l2[2] += (10, 11) # l2[2]为tuple对象, +=运算返回新的tuple
print('l1:', l1)
print('l2:', l2)