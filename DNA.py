# 作者: NeverWise
# 2026年02月15日14时50分03秒
# shilohzhen0315@gmail.com
dna_sequence = ['GCT', 'AGC', 'AGG', 'TAA', 'ACT', 'CAT',
                'TAT', 'CCC', 'ACG', 'GAA', 'ACC', 'GGA']
item_to_find = 'TAA'
item_found = False

for item in dna_sequence:
    if item == item_to_find:
        item_found = True
        break # 找到了就提前退出循环，节省计算机体力

# 循环结束后统一汇报
if item_found:
    print("Item Found!")
else:
    print("Item not found.")
