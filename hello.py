#编写一个Python程序pow.py，
# 先导入数学模块math，通过键盘输入一个浮点数x，
# 然后调用math模块中的数学函数pow()计算该数的平方y，
# 分别以浮点数和科学记数法输出结果（均保留2位小数）。
# 要求：给每条语句加上合适的注释。
import math
num = input("please input a number:")
pow(float(num),2)
print(f"{float(num):f}")
print("%e" %float(num))

