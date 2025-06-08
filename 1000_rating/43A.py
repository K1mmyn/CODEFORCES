n = int(input())
team1 = []
team2 = []

for x in range(n):
  team = input()
  if not len(team1) or team in team1:
    team1.append(team)
  else:
    team2.append(team)

if len(team1) > len(team2):
  print(team1[0])
else:
  print(team2[0])

