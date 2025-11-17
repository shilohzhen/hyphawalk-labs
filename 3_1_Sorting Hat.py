# 作者: 科研哥NeverWise
# 2025年11月14日23时57分32秒
# 523110197@qq.com
# Write code below 💖
a=0
Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0
Q1 = int(input('Do you like Dawn or Dusk?\n1) Dawn\n2) Dusk'))
if Q1 == 1:
  Gryffindor = a + 1
  Ravenclaw = a + 1
elif Q1 == 2:
  Hufflepuff = a + 1
  Slytherin = a + 1
else:
  print('Wrong input')
Q2 = int(input('When I’m dead, I want people to remember me as:\n1) The Good\n2) The Great\n3) The Wise \n4) The Bold'))
if Q2 == 1:
  Hufflepuff = Hufflepuff + 2
elif Q2 == 2:
  Slytherin = Slytherin + 2
elif Q2 == 3:
  Ravenclaw = Ravenclaw + 2
elif Q2 == 4:
  Gryffindor = Gryffindor + 2
else:
  print('Wrong input')
Q3 = int(input('Which kind of instrument most pleases your ear?\n1) The violin\n2) The trumpet\n3) The piano\n4) The drum'))
if Q3 == 1:
  Slytherin = Slytherin + 4
elif Q3 == 2:
  Hufflepuff = Hufflepuff + 4
elif Q3 == 3:
  Ravenclaw = Ravenclaw + 4
elif Q3 == 4:
  Gryffindor = Gryffindor + 4
else:
  print('Wrong input')
print(f'🦁 Gryffindor={Gryffindor}\n🦅 Ravenclaw={Ravenclaw}\n🦡 Hufflepuff={Hufflepuff}\n🐍 Slytherin={Slytherin}')
if Gryffindor > Slytherin and Gryffindor > Hufflepuff and Gryffindor > Ravenclaw:
  print(f'the house with the most points is 🦁 Gryffindor={Gryffindor}')
elif Slytherin > Gryffindor and Slytherin > Hufflepuff and Slytherin > Ravenclaw:
  print(f'the house with the most points is 🐍 Slytherin={Slytherin}')
elif Hufflepuff > Gryffindor and Hufflepuff > Gryffindor and Hufflepuff > Ravenclaw:
  print(f'the house with the most points is 🦡 Hufflepuff={Hufflepuff}')
else:
  print(f'the house with the most points is 🦅 Ravenclaw={Ravenclaw}')
##更好的写法
houses = {
    "🦁 Gryffindor": Gryffindor,
    "🦅 Ravenclaw": Ravenclaw,
    "🦡 Hufflepuff": Hufflepuff,
    "🐍 Slytherin": Slytherin
}

winner = max(houses, key=houses.get)

print(f'The house with the most points is {winner} = {houses[winner]}')