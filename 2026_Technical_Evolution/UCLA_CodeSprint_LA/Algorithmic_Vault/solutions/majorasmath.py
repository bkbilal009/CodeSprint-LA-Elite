#Problem A Majora's Math
starting_line = input().split()
starting_health = int(starting_line[0])
numbers = int(starting_line[1])

starting_line1 = input().split()
standard_damage = int(starting_line1[0])
fire_damage = int(starting_line1[1])
ice_damage = int(starting_line1[2])
light_damage = int(starting_line1[3])

for i in range(numbers):
  arr_name = input().strip()

  if arr_name == "standard":
    starting_health = starting_health - standard_damage
  elif arr_name == "fire":
    starting_health = starting_health - fire_damage
  elif arr_name == "ice":
    starting_health = starting_health - ice_damage
  elif arr_name == "light":
    starting_health = starting_health - light_damage

if starting_health <= 0:
  print("dead")
else:
  print(starting_health)