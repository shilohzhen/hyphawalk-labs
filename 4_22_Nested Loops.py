# 作者: NeverWise
# 2025年11月24日14时28分16秒
# shilohzhen0315@gmail.com

import random

lucky_number = random.randint(1, 9)
not_found = True

while not_found:
  for i in range(1, 10):
    if i == lucky_number:
      not_found = False
      break
    else:
      print(i)

print(f"Yay I got my lucky number {lucky_number}! 🍀")