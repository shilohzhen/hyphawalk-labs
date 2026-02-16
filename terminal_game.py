# 作者: NeverWise
# 2025年11月25日11时25分49秒
# shilohzhen0315@gmail.com


# terminal_game.py
# 简单的终端文字冒险：项羽击杀苏烈

import random

def line():
    print("-" * 40)

def choose(prompt, options):
    """
    prompt: 提示语
    options: dict, key 为数字字符串, value 为描述
    返回玩家选择的 key
    """
    while True:
        print(prompt)
        for k, v in options.items():
            print(f"{k}. {v}")
        choice = input("请输入选项数字：").strip()
        if choice in options:
            return choice
        else:
            print("选项无效，重来一遍。")

def intro():
    line()
    print("王者峡谷，黑夜将至。")
    print("你是项羽，当前局势：己方高地告急，苏烈正带兵压塔。")
    print("打野在下路清线，中路法师还在回城。此时，能挡住苏烈的只有你。")
    line()

def pre_battle():
    """
    战前分支：影响后面战斗属性
    返回 (extra_hp, extra_attack)
    """
    options = {
        "1": "从正面河道硬刚苏烈",
        "2": "绕自家红 BUFF 草丛埋伏",
        "3": "先去中路清一下兵，再回防高地"
    }
    choice = choose("你决定怎么处理当前局面？", options)
    extra_hp = 0
    extra_attack = 0

    if choice == "1":
        print("你选择正面硬刚，士气高涨，伤害略有提升。")
        extra_attack = 2
    elif choice == "2":
        print("你选择埋伏，先手优势明显，但有些紧张。增加少量生命值。")
        extra_hp = 5
    else:
        print("你选择稳健清线回防，节奏更平稳，攻击和生命都有小幅提升。")
        extra_hp = 3
        extra_attack = 1

    line()
    return extra_hp, extra_attack

def battle(extra_hp, extra_attack):
    # 初始属性
    player_hp = 40 + extra_hp
    player_attack = 8 + extra_attack
    player_defense = 2

    enemy_hp = 45
    enemy_attack = 7
    enemy_defense = 1

    rage = 0  # 项羽怒气，用来开大招

    print("你赶到高地前塔下，苏烈正顶着小兵往前冲。战斗打响！")
    line()
    print(f"项羽 生命值: {player_hp}")
    print(f"苏烈 生命值: {enemy_hp}")
    line()

    while player_hp > 0 and enemy_hp > 0:
        print(f"\n当前状态：项羽HP {player_hp} | 苏烈HP {enemy_hp} | 怒气 {rage}/5")
        action_options = {
            "1": "普攻（稳定输出）",
            "2": "横扫千军（小技能，高伤害，有概率击退）",
            "3": "格挡（本回合减伤，并小幅反击）",
            "4": "大招·破釜沉舟（需要怒气5：高额伤害并获得护盾）"
        }
        action = choose("请选择你的行动：", action_options)

        line()
        # 玩家回合
        if action == "1":
            dmg = max(1, player_attack - enemy_defense + random.randint(-1, 2))
            enemy_hp -= dmg
            rage = min(5, rage + 1)
            print(f"你挥出普攻，对苏烈造成 {dmg} 点伤害，怒气+1。")
        elif action == "2":
            base = player_attack + 3 + random.randint(-1, 3)
            # 20% 几率额外击退伤害
            if random.random() < 0.2:
                extra = 4
                print("横扫命中要害，击退苏烈！额外伤害！")
            else:
                extra = 0
            dmg = max(1, base - enemy_defense + extra)
            enemy_hp -= dmg
            rage = min(5, rage + 1)
            print(f"你释放横扫千军，对苏烈造成 {dmg} 点伤害，怒气+1。")
        elif action == "3":
            print("你举盾格挡，准备承受苏烈的攻击。")
            rage = min(5, rage + 1)
        elif action == "4":
            if rage < 5:
                print("怒气不足，大招落空，只能普攻一次。")
                dmg = max(1, player_attack - enemy_defense + random.randint(-1, 1))
                enemy_hp -= dmg
                print(f"临时普攻，对苏烈造成 {dmg} 点伤害。")
                rage = min(5, rage + 1)
            else:
                rage = 0
                dmg = player_attack + 8 + random.randint(0, 5)
                enemy_hp -= dmg
                shield = 8
                print(f"你怒吼着冲锋，开启破釜沉舟，对苏烈造成 {dmg} 点巨额伤害，并获得 {shield} 点护盾！")
                player_hp += shield  # 简单处理成加血

        # 苏烈是否阵亡
        if enemy_hp <= 0:
            break

        # 敌方回合
        enemy_action = random.random()
        if action == "3":
            # 你选择了格挡，本回合减伤
            if enemy_action < 0.5:
                raw_dmg = max(1, enemy_attack - player_defense)
                dmg = max(0, raw_dmg - 4)  # 格挡额外减伤
                player_hp -= dmg
                counter_dmg = 3
                enemy_hp -= counter_dmg
                print(f"苏烈挥矛猛砸，你成功格挡，大幅减伤，仅受到 {dmg} 点伤害，并反击 {counter_dmg} 点。")
            else:
                raw_dmg = max(1, enemy_attack + 3 - player_defense)
                dmg = max(0, raw_dmg - 4)
                player_hp -= dmg
                print(f"苏烈开大撞击高地，你勉强顶住，受到 {dmg} 点伤害。")
        else:
            if enemy_action < 0.4:
                dmg = max(1, enemy_attack - player_defense + random.randint(-1, 2))
                player_hp -= dmg
                print(f"苏烈挥舞战锤，对你造成 {dmg} 点伤害。")
            elif enemy_action < 0.8:
                dmg = max(1, enemy_attack + 3 - player_defense + random.randint(-1, 1))
                player_hp -= dmg
                print(f"苏烈突进猛撞，你被击退，受到 {dmg} 点伤害。")
            else:
                heal = 5
                enemy_hp += heal
                print(f"苏烈短暂后撤，召唤护盾回复 {heal} 点生命。")

        line()

    # 战斗结果
    if player_hp > 0 and enemy_hp <= 0:
        print("苏烈倒下了！你成功守住了高地，队友赶到，一波反推结束比赛！")
    elif player_hp <= 0 and enemy_hp > 0:
        print("你倒在高地前，苏烈带兵拆掉了水晶，这一局失败了。")
    else:
        print("你和苏烈同时倒地，双方水晶都岌岌可危，这局成了名场面。")

def main():
    intro()
    extra_hp, extra_attack = pre_battle()
    battle(extra_hp, extra_attack)

if __name__ == "__main__":
    main()