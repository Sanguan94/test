import random
# 玩家参与的猜拳
def caiquan1(player1,player2):
    while 1:
        fuc = ["剪刀", "石头", "布"]
        random1 = random.sample(fuc, 1)
        ans = input("目前正在和%s比赛，请输入你的操作：[剪刀 布 石头]" % player2)
        print("%s出拳：%s,电脑玩家%s出拳：%s" % (player1, ans, player2, random1[0]))
        # print(random1[0])
        if random1[0] == ans:
            print("没有输赢，重来")
            continue
        elif ans == "石头" and random1[0] == "剪刀":
            print("%s赢了" %player1)
            return 1
        elif ans == "剪刀" and random1[0] == "布":
            print("s赢了" %player1)
            return 1
        elif ans == "布" and random1[0] == "石头":
            print("s赢了" %player1)
            return 1
        else:
            print("%s输了"%player1)
            return 2

# 机器参建的猜拳
def caiquan2(player3,player4):
    while 1:
        global random
        fuc = ["剪刀", "石头", "布"]
        random1 = random.sample(fuc, 1)
        random2 = random.sample(fuc, 1)
        print("电脑玩家%s正在和电脑玩家2%s比赛，玩家1出拳：%s，玩家2出拳：%s" % (player3, player4, random1[0], random2[0]))
        if random1[0]== random2[0]:
            print("没有输赢，重来")
            continue
        elif random1[0]== "石头" and random2[0] == "剪刀":
            print("%s赢了" %(player3))

            return player3
        elif random1[0] == "剪刀" and random2[0]== "布":
            print("s赢了" %(player3))

            return player3
        elif random1[0] == "布" and random2[0] == "石头":
            print("s赢了" %(player3))

            return player3
        else:
            print("%s输了" %(player3))

            return player4
# 游戏分组 team1和team2
players_list=["王胜安","李鑫灏" ,"薛佛世", "蔡壮保", "钱勤堃" ,"潘恩依" ,"陈国柏", "魏皑虎", "周卓浩" ,"汤辟邦", "张顺谷", "张悌斯" ,"张灶冲" ,"饶展林", "岳列洋", "时党舒" ,"周迟"]
players=random.sample(players_list,3)
print(players)
player=input("请输入玩家姓名:")
# players.append(str(player))
# print(players)
team1=random.sample(players,1)
team1.append(player)
print("组一是",team1)
for i in team1:
    if i in players:
        players.remove(i)
        team2=players
print("组二是",team2)


if player in team1:
    team1.remove(player)
    user1=str(team1[0])
    user2=str(team2[0])
    user3=str(team2[1])

    game1=caiquan1(player,user1)
    game2=caiquan2(user2, user3)
    team2.remove(game2)
    if game1==1:
        print("组内比赛赢了，进行组外比赛")
        game3=caiquan1(player,game2)
        if game3==1:
            print("%s第一名"%player)
        elif game3==0:
            print("%s第二名"%player)

    elif game1==2:
        print("组内比赛输了，争第三名吧")
        game3=caiquan1(player,str(team2))
        if game3==1:
            print("%s第三名"%player)
        elif game3==2:
            print("%s第四名"%player)
