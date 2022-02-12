squares = [1, 2, 4, 9, 16, 25]

print(squares[-1])
# Prints the last element of the list

cubes = [1, 8, 27, 65, 125]
# The cube of 4 is 64, not 65. 
# To correct this, the following operation takes place:
cube_4 = 4 ** 3
cube_4 = cubes[3] = 64
print(cubes)

# Add the cube of 6
cubes.append(216)

# Add the cube of 8 as well
cubes.append(7**3)