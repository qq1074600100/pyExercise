import sympy

x, y = sympy.symbols('x y')
f = (x+y)**2 + (x+1)**2 + (y+3)**2
# 赋值: 注意x_tmp的名字一定不能与符号x同名！！
x_tmp = 1
y_tmp = -1
print(f.evalf(subs={x: x_tmp, y: y_tmp}))
