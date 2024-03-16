import random
# 存储名字的列表
class Hero:
    def __init__(self,role, name, equipment_init,equipment_first, runes, summoner_skills):
        self.role = role
        self.name = name
        self.equipment_init = equipment_init
        self.equipment_first = equipment_first
        self.runes = runes
        self.summoner_skills = summoner_skills

    def display_info(self):
        print("\033[38;2;255;165;0m位置：", self.role, end="  ")  # 橙色
        print("\033[1;36m英雄姓名：", self.name, end="  ")  # 天蓝色加粗
        print("\033[32m初始装备：", self.equipment_init,end="  ")  # 绿色
        print("\033[33m第一件成装：", self.equipment_first,end="  ")  # 黄色
        print("\033[34m符文：", self.runes,end="  ")  # 蓝色
        print("\033[31m召唤师技能：", self.summoner_skills,end="  ")  # 红色

def random_five():
    #创建五个英雄实例
    # # 随机选择五个不重复的名字
    random_names = random.sample(Hero_names, 5)
    #删除这五个名字
    for i in range(5):
        Hero_names.remove(random_names[i])
    Hero1 = Hero("上单",random_names[0], " ", " "," ", [" ", " "])
    Hero2 = Hero("打野",random_names[1], " ", " "," ", [" ", " "])
    Hero3 = Hero("中单" ,random_names[2]," ", " "," ", [" ", " "])
    Hero4 = Hero("ADC",random_names[3], " ", " "," ", [" ", " "])
    Hero5 = Hero("辅助",random_names[4], " ", " "," ", [" ", " "])
    Heros =[Hero1, Hero2, Hero3, Hero4, Hero5]

    # 随机选择五个不重复的召唤师技能
    for i in range(5):
        Heros[i].summoner_skills = random.sample(Hero_summoner_skills, 2)
    # # 随机选择五个不重复的初始装备
    for i in range(5):
        if Heros[i].summoner_skills[0] == "惩戒" or Heros[i].summoner_skills[1] == "惩戒":
            Heros[i].equipment_init = random.choice(Hero_equipment_init_2)
        else:
            Heros[i].equipment_init = random.choice(Hero_equipment_init)
        
    # 随机选择五个不重复的成装
    for i in range(5):
        Heros[i].equipment_first = random.choice(Hero_equipment_first)
    # 随机选择五个不重复的符文
    for i in range(5):
        Heros[i].runes = random.choice(Hero_runes)

    #随机英雄
    for i in range(5):
        Heros[i].name = random_names[i]
    for i in range(5):
        Heros[i].equipment_init = random.choice(Hero_equipment_init)
    for i in range(5):
        Heros[i].display_info()
        print("\n")
def random_hero():
    #创建一个英雄实例
    # 随机选择一个不重复的名字
    random_name = random.choice(Hero_names)
    #删除这个名字
    Hero_names.remove(random_name)
    Hero1 = Hero("无",random_name, " ", " "," ", [" ", " "])
    # 随机选择一个不重复的召唤师技能
    Hero1.summoner_skills = random.sample(Hero_summoner_skills, 2)
    # 随机选择一个不重复的初始装备
    if Hero1.summoner_skills[0] == "惩戒" or Hero1.summoner_skills[1] == "惩戒":
        Hero1.equipment_init = random.choice(Hero_equipment_init_2)
    else:
        Hero1.equipment_init = random.choice(Hero_equipment_init)
    # 随机选择一个不重复的成装
    Hero1.equipment_first = random.choice(Hero_equipment_first)
    # 随机选择一个不重复的符文
    Hero1.runes = random.choice(Hero_runes)
    Hero1.display_info()
    print("\n")
#英雄
Hero_names = [
    "狂战士", "卡牌大师", "无畏战车", "猩红收割者", "正义天使",
    "牛头酋长", "亡灵战神", "众星之子", "麦林炮手", "雪原双子",
    "寒冰射手", "武器大师", "时光守护者", "痛苦之拥", "死亡颂唱者",
    "殇之木乃伊", "冰晶凤凰", "祖安狂人", "虚空行者", "风暴之怒",
    "英勇投弹手", "瓦洛兰之盾", "巨魔之王", "皮城女警", "熔岩巨兽",
    "永恒梦魇", "荒漠屠夫", "蜘蛛女皇", "齐天大圣", "盲僧",
    "机械公敌", "水晶先锋", "沙漠死神", "兽灵行者", "酒桶",
    "探险家", "牧魂人", "狂暴之心", "曙光女神", "刀锋之影",
    "深渊巨口", "光辉女郎", "龙血武姬", "法外狂徒", "不灭狂雷",
    "惩戒之箭", "机械先驱", "无双剑姬", "仙灵女巫", "战争之影",
    "诺克萨斯之手", "冰霜女巫", "德玛西亚之翼", "铸星龙王", "暮光星灵",
    "虚空之女", "迷失之牙", "疾风剑豪", "岩雀", "影哨",
    "弗雷尔卓德之心", "永猎双子", "暴走萝莉", "狂厄蔷薇", "涤魂圣枪",
    "影流之主", "时间刺客", "皮城执法官", "唤潮鲛姬", "魔法猫咪",
    "魂锁典狱长", "虚空遁地兽", "复仇之矛", "幻翎", "山隐之焰",
    "万花通灵", "镕铁少女", "愁云使者", "腕豪", "灵罗娃娃",
    "不羁之悦", "炽炎雏龙", "异画师"
]

#初始装备
Hero_equipment_init = [
    "长剑",
    "短剑",
    "多兰盾",
    "多兰剑",
    "红水晶",
    "蓝水晶",
    "布甲",
    "抗魔斗篷",
    "黑暗封印",
    "多兰之戒",
    "萃取",
    "腐败药水",
    "鞋子",
    "仙女护符",
    "仙女护肤*2",
    "治疗宝珠",
    "增幅典籍",
    "莹尘",
    "莹尘*2",
    "云游图鉴",
    "女神之泪"]

#初始装备2
Hero_equipment_init_2 = [
    "长剑",
    "短剑",
    "多兰盾",
    "多兰剑",
    "打野刀*红",
    "打野刀*蓝",
    "打野刀*绿",
    "红水晶",
    "蓝水晶",
    "布甲",
    "抗魔斗篷",
    "黑暗封印",
    "多兰之戒",
    "萃取",
    "腐败药水",
    "鞋子",
    "仙女护符",
    "仙女护肤*2",
    "治疗宝珠",
    "增幅典籍",
    "莹尘",
    "莹尘*2",
    "云游图鉴",
    "女神之泪"]

#成装
Hero_equipment_first = equipment_list = [
    "舒瑞娅的战歌",
    "无终恨意",
    "败魔",
    "薄暮法袍",
    "引路者",
    "大天使之杖",
    "魔宗",
    "炼金科技纯化器",
    "守护天使",
    "无尽之刃",
    "凡性的提醒",
    "多米尼克领主的致意",
    "梅贾的窃魂卷",
    "魔切",
    "幻影之舞",
    "基克的聚合",
    "斯特拉克的挑战护手",
    "振奋盔甲",
    "日炎圣盾",
    "黑色切割者",
    "饮血剑",
    "海克斯注力刚壁",
    "贪欲九头蛇",
    "荆棘之甲",
    "三相之力",
    "狂徒铠甲",
    "心之钢",
    "卢安娜的飓风",
    "斯塔缇克电刃",
    "灭世者的死亡之帽",
    "智慧末刃",
    "疾射火炮",
    "岚切",
    "巫妖之祸",
    "女妖面纱",
    "救赎",
    "骑士之誓",
    "冰霜之心",
    "纳什之牙",
    "瑞莱的冰晶节杖",
    "残疫",
    "凛冬之临",
    "末日寒冬",
    "鬼索的狂暴之刃",
    "虚空之杖",
    "蜕生",
    "水银弯刀",
    "幽梦之灵",
    "兰顿之兆",
    "海克斯科技火箭腰带",
    "破败王者之刃",
    "玛莫提乌斯之噬",
    "中娅沙漏",
    "朔极之矛",
    "莫雷洛秘典",
    "黯影阔剑",
    "破舰者",
    "钢铁烈阳之匣",
    "石像鬼石板甲",
    "米凯尔的祝福",
    "界弓",
    "炽热香炉",
    "夺萃之镰",
    "亡者的板甲",
    "巨型九头蛇",
    "夜之锋刃",
    "符文罗盘",
    "异世珍藏",
    "星界据守",
    "圆梦使者",
    "扎兹沙克的溃口",
    "摩天雪橇",
    "血鸣",
    "帝国指令",
    "自然之力",
    "视界专注",
    "星界驱驰",
    "裂隙制造者",
    "暗夜收割者",
    "恶魔之拥",
    "破碎王后之冕",
    "影焰",
    "风暴狂涌",
    "密银黎明",
    "死亡之舞",
    "炼金朋克链锯剑",
    "焚天",
    "流水法杖",
    "月石再生器",
    "海力亚的回响",
    "黎明核心",
    "渴血战斧",
    "挺进破坏者",
    "兰德里的折磨",
    "卢登的配枪",
    "永霜",
    "时光之杖",
    "冰脉护手",
    "璀璨回响",
    "千变者贾修",
    "辉耀美德",
    "海妖杀手",
    "不朽盾弓",
    "纳沃利迅刃",
    "收集者",
    "德拉克萨的暮刃",
    "星蚀",
    "暗行者之爪",
    "赛瑞尔达的怨恨",
    "巨蛇之牙",
    "公理圆弧",
    "狂妄",
    "亵渎九头蛇",
    "电震涡流剑",
    "拉阔尔之盾",
    "禁忌时机",
    "兰德里的挽歌",
    "厌恨锁链",
    "深渊面具"
]

#符文
Hero_runes = ["强攻", "致命节奏", "迅捷步法", "电刑", "掠食者",
    "黑暗收割", "召唤-艾黎", "奥术彗星", "相位猛冲", "不灭之握",
    "余震", "守护者", "启封的智慧", "冰川增幅", "先攻",
    "从刃", "征服者"]

#召唤师技能
Hero_summoner_skills = ["屏障", "净化", "引燃", "虚弱", "闪现",
    "幽灵疾步", "治疗术", "清晰术", "惩戒", "传送"]

while True:
    print("1.随机五个英雄")
    print("2.随机一个英雄")
    print("3.退出")
    choice = input("请输入你的选择：")
    if choice == "1":
        random_five()
    elif choice == "2":
        random_hero()
    elif choice == "3":
        break
    else:
        print("输入错误，请重新输入！")
        continue