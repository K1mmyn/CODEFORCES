n = int(input())
cubes = list(map(int, input().split(" ")))

for x in range(n):
  for y in range(n - 1 - x):
    if cubes[y] > cubes[y + 1]:
      cubes[y], cubes[y+1] = cubes[y+1], cubes[y] 
      
print(" ".join([str(cube) for cube in cubes]))
             