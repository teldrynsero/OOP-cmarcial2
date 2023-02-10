area = 0.0
test = [3, 1, 1, 2, 1, 2, 2]
x = []
y = []
counter = 0
for i in test:
    if (counter == 0):
        pass
    elif (counter % 2 == 0):
        y.append(i)
    else:
        x.append(i)
    counter = counter + 1
print(x)
print(y)