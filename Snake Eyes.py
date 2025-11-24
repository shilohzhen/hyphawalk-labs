# 作者: NeverWise
# 2025年11月24日15时47分01秒
# shilohzhen0315@gmail.com

import random

die1 = random.randint(1, 6)
die2 = random.randint(1, 6)
total = die1 + die2
while total != 2:
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2
    print('Nope')
print('Snake eyes!')