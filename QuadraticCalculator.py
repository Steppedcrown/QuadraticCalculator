#My quadratic calculator. Steppedcrown
a = -0.75
b = 0
c = 0
p = 2
symmetry_x = -b/(2*a)
vertex_y = (a*(symmetry_x**p)) + (b * symmetry_x) + c

def quad_solve (x):
  return str((a*(x**p)) + (b*x) + c)

def spec_y (x):
  return str((a*(x**p)) + (b*x) + c)

point1 = quad_solve(symmetry_x + 1)
point2 = quad_solve(symmetry_x + 2)
pointsTF = point2 > point2

def y0 ():
  if vertex_y > 0 and pointsTF:
    return 'Does not cross x-axis'
  elif vertex_y < 0 and pointsTF:
    return 'Does not cross x-axis'
  elif vertex_y == 0:
    return str(0)
  for i in range (0, 31):
    term1 = a * (i*i)
    term2 = b * i
    term3 = c
    solution = term1 + term2 + term3
    if solution == 0:
      return str(i) + ' and ' + str(-i)
  return 'Not Found'

def x0 ():
  return str(c)
  
print('x-intercept = ' + y0())
print('y-intercept = ' + x0())
print('(' + str(symmetry_x - 2) + ', ' + quad_solve(symmetry_x - 2) + ')')
print('(' + str(symmetry_x - 1) + ', ' + quad_solve(symmetry_x - 1) + ')')
print('(' + str(symmetry_x) + ', ' + quad_solve(symmetry_x) + ')')
print('(' + str(symmetry_x + 1) + ', ' + quad_solve(symmetry_x + 1) + ')')
print('(' + str(symmetry_x + 2) + ', ' + quad_solve(symmetry_x + 2) + ')')
print(spec_y(4))
