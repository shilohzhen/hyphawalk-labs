# 作者: NeverWise
# 2026年01月19日22时09分26秒
# shilohzhen0315@gmail.com

import matplotlib.pyplot as plt
import matplotlib.patches as patches

# 设置画布
fig, ax = plt.subplots(figsize=(4, 4))
ax.set_aspect('equal')
ax.axis('off')  # 关闭坐标轴

# 1. 画外圈（辅助裁剪线，极细的浅灰色）
circle = patches.Circle((0.5, 0.5), 0.48, linewidth=1, edgecolor='#D3D3D3', facecolor='white')
ax.add_patch(circle)

# 2. 画坎卦（☵）
# 坎卦结构：上（阴/断）、中（阳/实）、下（阴/断）

# 定义线条样式
line_height = 0.12  # 线条粗细
line_width = 0.6    # 线条总宽度
gap_width = 0.1     # 断开处的间隙
center_x = 0.5
top_y = 0.7
mid_y = 0.5
bot_y = 0.3

# 上爻（阴 - -）
rect_top_left = patches.Rectangle((center_x - line_width/2, top_y - line_height/2), (line_width - gap_width)/2, line_height, facecolor='black')
rect_top_right = patches.Rectangle((center_x + gap_width/2, top_y - line_height/2), (line_width - gap_width)/2, line_height, facecolor='black')
ax.add_patch(rect_top_left)
ax.add_patch(rect_top_right)

# 中爻（阳 —）
rect_mid = patches.Rectangle((center_x - line_width/2, mid_y - line_height/2), line_width, line_height, facecolor='black')
ax.add_patch(rect_mid)

# 下爻（阴 - -）
rect_bot_left = patches.Rectangle((center_x - line_width/2, bot_y - line_height/2), (line_width - gap_width)/2, line_height, facecolor='black')
rect_bot_right = patches.Rectangle((center_x + gap_width/2, bot_y - line_height/2), (line_width - gap_width)/2, line_height, facecolor='black')
ax.add_patch(rect_bot_left)
ax.add_patch(rect_bot_right)

# 保存图片
plt.savefig('kan_trigram_sticker.png', dpi=300, bbox_inches='tight', pad_inches=0.1)