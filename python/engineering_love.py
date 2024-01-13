def inside_heart(x, y):
  return ((x*0.05)**2 + (y*0.1)**2 - 1)**3 - (x*0.05)**2 * (y*0.1)**3 <= 0

def line(y):
  values = []
  for x in range(-30,30):
    if inside_heart(x, y):
      value = 'Engineer'[(x - y) % 8]
    else:
        value = ' '
    values.append(value)
  return ''.join(values)

lines = [line(y) for y in range(15,-15,-1)]

string = '\n'.join(lines)
print(string)
