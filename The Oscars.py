# 作者: NeverWise
# 2026年02月15日14时37分02秒
# shilohzhen0315@gmail.com
best_pictures = [
  '2019 - Parasite',
  '2018 - Green Book',
  '2017 - The Shape of Water',
  '2016 - Moonlight',
  '2015 - Spotlight',
  '2014 - Birdman',
  '2013 - 12 Years a Slave',
  '2012 - Argo',
  '2011 - The Artist'
]

# 新搜索到的获奖名单
new_winners = [
    '2024 - Anora',
    '2023 - Oppenheimer',
    '2022 - Everything Everywhere All at Once',
    '2021 - CODA',
    '2020 - Nomadland'
]

# 将新名单添加到前面
best_pictures = new_winners + best_pictures

# 验证结果
for movie in best_pictures:
    print(movie)