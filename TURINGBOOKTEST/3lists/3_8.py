areas = ['Beijing', 'Shanghai', 'Tokyo', 'Kunming', 'Guangzhou']
print(areas)
# 正向打印
print(sorted(areas))
# 再次打印，确定顺序没变
print(areas)
# 反向打印
print(sorted(areas, reverse=True))
# 再次打印，确定顺序没变
print(areas)
# 反向排序
areas.reverse()
print(areas)
# 再次反向
areas.reverse()
print(areas)
# !!!直接打印 print(areas.reverse())，输出结果为None！！！！
# sort() 永久修改排序
areas.sort()
print(areas)
# 反向
areas.sort(reverse=True)
print(areas)
