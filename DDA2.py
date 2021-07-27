def display(x1,y1):
# round off values(if required)
# else prints values normally
    if (int(x1)+0.5) <= x1:
        x = int(x1)+1
    else:
        x = int(x1)
    if (int(y1)+0.5) <= y1:
        y = int(y1)+1
    else:
        y = int(y1)
    print(f'({x},{y})')
#function ends


print('Enter first coordinate ')
x1 = int(input('x1 value: '))
y1 = int(input('y1 value: '))

print('Enter second coordinate ')
x2 = int(input('x2 value: '))
y2 = int(input('y2 value: '))

# values of dx and dy
dx = x2 - x1
dy = y2 - y1

# counts the number of steps
steps = 0
if dx > dy:
    steps = abs(dx)
else: 
    steps = abs(dy)    
print(f'\nNo of steps = {steps}')

# calculate x and y increment values
x_inc = dx/steps
y_inc = dy/steps
print('\nIncrement formula used:-')
print(f'x(k+1) = x(k) + {x_inc}')
print(f'y(k+1) = y(k) + {y_inc}')

print("\nIntermediate points are:")
for i in range(steps):
    x1 = x1 + x_inc
    y1 = y1 + y_inc

display(x1,y1)