import pgzrun
import random

城管_1 = Actor("城管_1")
城管_2 = Actor("城管_2")
城管_3 = Actor("城管_3")
张三 = Actor("张三_1")
顾客_1 = Actor("顾客_1")
顾客_2 = Actor("顾客_2")
顾客_3 = Actor("顾客_3")
顾客_4 = Actor("顾客_4")
标语 = Actor("标语")
广告牌 = Actor("广告牌")
商品_1 = Actor("低_辣条")
商品_2 = Actor("低_气球")
商品_3 = Actor("中_魔方")
商品_4 = Actor("中_雨伞")
商品_5 = Actor("高_党章")
商品_6 = Actor("高_飞机模型")
商品_7 = Actor("低_老干妈")
背景_1 = Actor("1_p大东门_1")
背景_2 = Actor("1_海淀区图书馆_1")
背景_3 = Actor("1_中关村地铁站_1")
背景_4 = Actor("2_工人体育馆_1")
背景_5 = Actor("2_三里屯_1")
背景_6 = Actor("2_广电总局_1")
背景_7 = Actor("3_北海公园门口_1")
背景_8 = Actor("3_胡同_1")
背景_9 = Actor("3_天安门_1")
背景1 = Actor("1_p大东门")
背景2 = Actor("1_海淀区图书馆")
背景3 = Actor("1_中关村地铁站")
背景4 = Actor("2_工人体育馆")
背景5 = Actor("2_三里屯")
背景6 = Actor("2_广电总局")
背景7 = Actor("3_北海公园门口")
背景8 = Actor("3_胡同")
背景9 = Actor("3_天安门")
button_1 = Actor("button_true")
button_2 = Actor("button_1")
初始场景句1 = Actor("1_第一句")
初始场景句2 = Actor("1_第二句")
初始场景句3 = Actor("1_第三句")
初始场景句4 = Actor("1_第四句")
初始场景句5 = Actor("1_第五句")
初始场景句6 = Actor("1_第六句")
初始场景句7 = Actor("1_第七句")
级别提示符1 = Actor("提示符1")
级别提示符2 = Actor("提示符2")
级别提示符3 = Actor("提示符3")
选地提示句 = Actor("2_提示句")
选货提示句 = Actor("3_提示句")
选货弹出1 = Actor("goodss1")
选货弹出2 = Actor("goodss2")
选货弹出3 = Actor("goodss3")
选货弹出4 = Actor("goodss4")
选货弹出5 = Actor("goodss5")
选货弹出6 = Actor("goodss6")
选货弹出7 = Actor("goodss7")
option1 = Actor("option1")
option2 = Actor("option2")
option3 = Actor("option3")
option4 = Actor("option4")
option5 = Actor("option5")
option6 = Actor("option6")
option7 = Actor("option7")
stall = Actor("stall")
bike = Actor("tri-bike")
商品栏 = Actor("商品栏")


WIDTH = 1000
HEIGHT = 600

t = 0
s = 0
客流_概率 = 0
城管出现_概率 = 0
money = 500
级别 = 1
网红概率 = 0
嫉妒概率 = 0
good1_sum = 0
good2_sum = 0
good3_sum = 0
good4_sum = 0
good5_sum = 0
good6_sum = 0
good7_sum = 0
people_sum = 0

def draw():
    global t
    global s
    global 级别,客流_概率,城管出现_概率,网红概率,嫉妒概率,money
    global good1_sum, good2_sum, good3_sum, good4_sum, good5_sum, good6_sum, good7_sum
    screen.fill((0, 0, 0))
    screen.draw.text(str(t / 60) + 's', (800, 0))
    screen.draw.text(str(s), (800, 20))
    screen.draw.text("level: " + str(级别), (800, 40))
    screen.draw.text("keliu： " + str(客流_概率), (800, 60))
    screen.draw.text("chenguan: " + str(城管出现_概率), (800, 80))
    screen.draw.text('money: ' + str(money), (800, 100))
    screen.draw.text('wanghong: ' + str(网红概率), (800, 120))
    screen.draw.text(str(t), (800, 140))
    if t >=0 and t<= 120:
        screen.fill((0, 0, 0))
        标语.center = 500,300
        标语.draw()
    if t > 120 and t <= 240:

        张三.center = 800,300
        张三.draw()
        初始场景句1.center = 250,30
        初始场景句1.draw()
    if t > 240 and t <= 360:
        张三.center = 800, 300
        张三.draw()
        初始场景句1.center = 250, 30
        初始场景句1.draw()
        初始场景句2.center = 250, 90
        初始场景句2.draw()

    if t > 360 and t <= 480:
        张三.center = 800, 300
        张三.draw()
        初始场景句1.center = 250, 30
        初始场景句1.draw()
        初始场景句2.center = 250, 90
        初始场景句2.draw()
        初始场景句3.center = 250, 150
        初始场景句3.draw()
    if t > 480 and t <= 600:
        张三.center = 800, 300
        张三.draw()
        初始场景句1.center = 250, 30
        初始场景句1.draw()
        初始场景句2.center = 250, 90
        初始场景句2.draw()
        初始场景句3.center = 250, 150
        初始场景句3.draw()
        初始场景句4.center = 250, 210
        初始场景句4.draw()
    if t > 600 and t <= 960:
        初始场景句5.center = 250, 30
        初始场景句5.draw()
        初始场景句6.center = 250, 90
        初始场景句6.draw()
        初始场景句7.center = 250, 150
        初始场景句7.draw()

    if  t > 960 and t <= 970:
        选货提示句.center = 250,30
        选货提示句.draw()
        商品_1.center = 75, 200
        商品_1.draw()
        商品_2.center = 225, 200
        商品_2.draw()
        商品_3.center = 375, 200
        商品_3.draw()
        商品_4.center = 525, 200
        商品_4.draw()
        商品_5.center = 300, 500
        商品_5.draw()
        商品_6.center = 500, 500
        商品_6.draw()
        商品_7.center = 700, 500
        商品_7.draw()
        button_1.center = 850,350
        button_1.draw()
        screen.draw.text('goods1:' + str(good1_sum), (600, 0))
        screen.draw.text('goods2:' + str(good2_sum), (600, 20))
        screen.draw.text('goods3:' + str(good3_sum), (600, 40))
        screen.draw.text('goods4:' + str(good4_sum), (600, 60))
        screen.draw.text('goods5:' + str(good5_sum), (600, 80))
        screen.draw.text('goods6:' + str(good6_sum), (600, 100))
        screen.draw.text('goods7:' + str(good7_sum), (600, 120))
        if t == 962:
            选货弹出1.center = 350,370
            选货弹出1.draw()
        if t == 963:
            选货弹出2.center = 350,370
            选货弹出2.draw()
        if t == 964:
            选货弹出3.center = 350,370
            选货弹出3.draw()
        if t == 965:
            选货弹出4.center = 350,370
            选货弹出4.draw()
        if t == 966:
            选货弹出5.center = 350,370
            选货弹出5.draw()
        if t == 967:
            选货弹出6.center = 350,370
            选货弹出6.draw()
        if t == 968:
            选货弹出7.center = 350,370
            选货弹出7.draw()






    if 级别 == 1 and t > 970 and t <=1000:
        级别提示符1.center = 60, 30
        级别提示符1.draw()
        选地提示句.center = 250, 90
        选地提示句.draw()
        背景_1.center = 200,400
        背景_1.draw()
        背景_2.center = 500, 400
        背景_2.draw()
        背景_3.center = 800, 400
        背景_3.draw()
    if 级别 == 2 and t > 970 and t <=1000:
        级别提示符2.center = 60,30
        级别提示符2.draw()
        选地提示句.center = 250, 90
        选地提示句.draw()
        背景_4.center = 200, 400
        背景_4.draw()
        背景_5.center = 500, 400
        背景_5.draw()
        背景_6.center = 800, 400
        背景_6.draw()
    if 级别 == 3 and t > 970 and t <=1000:
        级别提示符3.center = 60,30
        级别提示符3.draw()
        选地提示句.center = 250, 90
        选地提示句.draw()
        背景_7.center = 200, 400
        背景_7.draw()
        背景_8.center = 500, 400
        背景_8.draw()
        背景_9.center = 800, 400
        背景_9.draw()
    if t >= 1001 and t <= 29801:
        背景1.center = 500,300
        背景1.draw()
        screen.draw.text(str(t / 60) + 's', (800, 0))
        screen.draw.text(str(s), (800, 20))
        screen.draw.text("level: " + str(级别), (800, 40))
        screen.draw.text("keliu： " + str(客流_概率), (800, 60))
        screen.draw.text("chenguan: " + str(城管出现_概率), (800, 80))
        screen.draw.text('money: ' + str(money), (800, 100))
        screen.draw.text('wanghong: ' + str(网红概率), (800, 120))
        screen.draw.text(str(t), (800, 140))
        级别提示符1.center = 50, 30
        级别提示符1.draw()
        option1.center = 50, 90
        option1.draw()
        option2.center = 50, 150
        option2.draw()
        option3.center = 50, 210
        option3.draw()
        option4.center = 50, 270
        option4.draw()
        option5.center = 50, 330
        option5.draw()
        option6.center = 50, 390
        option6.draw()
        option7.center = 50, 450
        option7.draw()
        stall.center = 450, 520
        stall.draw()
        bike.center = 700, 520
        bike.draw()
        商品栏.center = 500,500
        screen.draw.text(str(int(480-(t-1001)/60)), (46, 458))










def update():
    global t,money,s
    global 级别, 客流_概率, 城管出现_概率,网红概率,嫉妒概率,商品清单
    t = t + 1
    s = s + 1
    if t == 962 :
        t = 961
    if t == 963 :
        t = 962
    if t == 964 :
        t = 963
    if t == 965 :
        t = 964
    if t == 966 :
        t = 965
    if t == 967 :
        t = 966
    if t == 968 :
        t = 967
    if t == 969 :
        t = 968
    if t == 980:
        t = 971

    if t == 1001:
        s = 0


def on_mouse_down(pos):
    global t
    global 级别, 客流_概率, 城管出现_概率,网红概率,嫉妒概率
    global good1_sum ,good2_sum,good3_sum,good4_sum,good5_sum,good6_sum,good7_sum
    if t >= 961 and t <=970:
        if 商品_1.collidepoint(pos):
            good1_sum += 10
        if 商品_2.collidepoint(pos):
            good2_sum += 10
        if 商品_3.collidepoint(pos):
            good3_sum += 10
        if 商品_4.collidepoint(pos):
            good4_sum += 10
        if 商品_5.collidepoint(pos):
            good5_sum += 10
        if 商品_6.collidepoint(pos):
            good6_sum += 10
        if 商品_7.collidepoint(pos):
            good7_sum += 10
        if button_1.collidepoint(pos):
            t = 971

    if t >=971 and t <= 980:
        if 级别 == 1:
            if 背景_1.collidepoint(pos):
                客流_概率 = 客流_概率 + 2
                城管出现_概率 = 城管出现_概率 + 0.4
                网红概率 = 网红概率 + 0.2
                嫉妒概率 = 0
                t = 1001

            if 背景_2.collidepoint(pos):
                客流_概率 = 客流_概率 + 1.5
                城管出现_概率 = 城管出现_概率 + 0.4
                网红概率 = 网红概率 + 0
                嫉妒概率 = 0
                t = 30000
            if 背景_3.collidepoint(pos):
                客流_概率 = 客流_概率 + 3
                城管出现_概率 = 城管出现_概率 + 0.4
                网红概率 = 网红概率 + 0.2
                嫉妒概率 = 0.5
                t = 60000
        if 级别 == 2:
            if 背景_4.collidepoint(pos):
                客流_概率 = 客流_概率 + 3
                城管出现_概率 = 城管出现_概率 + 0.6
                网红概率 = 网红概率 + 0.2
                嫉妒概率 = 0.1
                t = 1121
            if 背景_5.collidepoint(pos):
                客流_概率 = 客流_概率 + 6
                城管出现_概率 = 城管出现_概率 + 0.6
                网红概率 = 网红概率 + 0.2
                嫉妒概率 = 0.3
                t = 30000
            if 背景_6.collidepoint(pos):
                客流_概率 = 客流_概率 + 3
                城管出现_概率 = 城管出现_概率 + 0.7
                网红概率 = 网红概率 + 0.8
                嫉妒概率 = 0.1
                t = 60000
        if 级别 == 3:
            if 背景_7.collidepoint(pos):
                客流_概率 = 客流_概率 + 9
                城管出现_概率 = 城管出现_概率 + 0.6
                网红概率 = 网红概率 + 0.2
                嫉妒概率 = 0.5
                t = 1121
            if 背景_8.collidepoint(pos):
                客流_概率 = 客流_概率 + 4.5
                城管出现_概率 = 城管出现_概率 + 0.3
                网红概率 = 网红概率 + 0
                嫉妒概率 = 0
                t = 30000
            if 背景_9.collidepoint(pos):
                客流_概率 = 客流_概率 + 15
                城管出现_概率 = 城管出现_概率 + 1
                网红概率 = 网红概率 + 1
                嫉妒概率 = 0
                t = 60000


def on_mouse_move(pos):
    global t
    global 级别, 客流_概率, 城管出现_概率, 网红概率, 嫉妒概率
    global good1_sum, good2_sum, good3_sum, good4_sum, good5_sum, good6_sum, good7_sum

    if t >= 961 and t <=970:
        if 商品_1.collidepoint(pos):
            t = 962
        if 商品_2.collidepoint(pos):
            t = 963
        if 商品_3.collidepoint(pos):
            t = 964
        if 商品_4.collidepoint(pos):
            t = 965
        if 商品_5.collidepoint(pos):
            t = 966
        if 商品_6.collidepoint(pos):
            t = 967
        if 商品_7.collidepoint(pos):
            t = 968



pgzrun.go()
