s ='HH sadsd'

spaces = []
counter = 0
for char in s:
    if char== ' ':
        counter += 1
    elif counter != 0:
        spaces.append(counter)
        counter = 0

print(spaces)
