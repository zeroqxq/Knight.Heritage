import keyboard 
import os 
import time 
import random
from tqdm import tqdm


# Параметры игрока
osn_s = False
stels = 0 
exp = 0
lvl = exp//100
money = 0
reyting = 0
brym_gg_save = 0
gg_save = 0 
no_save = 0
plusdeystv = 0
minusdeystv = 0
save = "0"

# -----------
armor = 3 + lvl*5
attack  = 10 + lvl*20
hp = 150 + 50*lvl + armor
yved =[]
temp = 0
vin = False
make_ring = False
#слежка
sumtempsl = 0
sumrad = 0
yspesno_sleska = False
chel_yshla = False
vas_poimali = False
seckret_razvedchil_altaris = 400 ; maxsecret_razvedcik_altairs = 1000
# ------------------------
profile_name = 0
lprofile = 0
#----------------------------
#Игровые враги
hpki1 = 35 ; opki1 = 10
hpki2 = 46 ; apki2 = 10 ; opki2 = 15
hpki3 = 60 ; apki3 = 13 ; opki3 = 20
hkn1 = 30 ;akn1 = 5 ;  okn1 = 20
hkn2 = 40 ; akn2 = 10 ; okn2 = 25
hkn3 = 55 ; akn3 = 10 ; okn3 = 25
hdki1 = 60 ; adki1 = 12 ; odki1 = 50
hbandit_classic = 35 ; abandit_classic = 13 ;obandit_classic = 20
#------------------------------
#Боссы 
hknight_boss = 100 ; aknight_boss = 17 ; oknight_boss = 100
#----------------------------
#Игровые оружия
bone_sword = False ; bs = 1
gigant_sword = False ; gs = 3
blood_sword = False ; bls = 8
elegant_sword = False ; es = 10
iron_sword = False ; irs = 15
military_sword = False ; ms = 21
diamond_sword = False ; ds = 28
legendary_sword =False ; ls = 35
grom_armor = False ; ga = 5
plor = []
#----------------------------
study = False
ykr = False
study1 = False
study3 =False
esccl = False
karta = False
inblackman = False
altaris_free = False
yspesno_sleska = False
ispesh_dvish =0
peshe_vibor = 0
slran = 0
popitkacod = 0
dvish = 0
needwalk = 0
#улики 
class Proof():
    title = None
    description = None
    city = None

class BlackMan(Proof):
    name = None
    age = None
    national = None
    plan = None
    rassa = None
    info1 = None
    info2 = None
    info3 = None
    info4 = None
    info5 = None   
    def proof_get(self):
        print("Название" , self.title)
        print("Общая характеристика:" , self.description)
        print("Город обнаружения:" , self.city)
        print("--------------------------------------------------")
        print("Имя: " ,self.name)
        print("Возраст: " , self.age)
        print("Национальность: ", self.national)
        print("Замысел: " , self.plan )
        print("Расса: " , self.rassa)
        print("Информация: " , self.info1)
        print("Информация: " , self.info2)
        print("Информация: " , self.info3)
        print("Информация: " , self.info4)
        print("Информация: " , self.info5)

class People:
    name = "Имя не удается определить"
    age = "Возраст не удается определить"
    national = "Национальность не удается определить"
    description = "Обычный человек"
    rassa = "Человек"
    statys = "Нейтральный" 

    def set_data(self, name , age , national , description , rassa, statys):
        self.name = name
        self.age = age
        self.national = national
        self.description = description
        self.rassa = rassa
        self.statys = statys

    def get_data(self):
        print("Имя: " + self.name ,  "Возраст: " + self.age , "Национальность: " + self.national , "Описание: " + self.description , "Расса: " + self.rassa ,  "Cтатус: " + self.statys , sep="\n")

class Monsters:
    name = "Имя не удается определить"
    age = "Возраст не удается определить"
    statys = "Агресивный"

def reyting_system():
    global reyting
    global tempplus
    global tempminus
    global plusdeystv
    global minusdeystv
    if plusdeystv > minusdeystv:
        if minusdeystv >= 1:
            minusdeystv = minusdeystv -1
        tempplus = plusdeystv*20
        tempplus = tempplus/20
        reyting = reyting + tempplus
        if plusdeystv >= 3:
            plusdeystv = plusdeystv - 3
        elif plusdeystv >= 1:
            plusdeystv = plusdeystv - 1
    elif minusdeystv > plusdeystv:
        tempminus = minusdeystv * 20
        tempminus = tempminus / 2
        reyting = reyting - tempminus
    if reyting  <= -900:
        plusdeystv = 0
    elif  reyting >= 2400:
        minusdeystv = 0

def sled(radiys , maxradiys):
    global slran
    global dvish
    global gg_dvish
    global pos
    global needwalk
    global vas_poimali
    global chel_yshla
    global sumtempsl
    global sumrad
    global yspesno_sleska
    global stels
    global ispesh_dvish
    int(radiys)
    int(stels)
    radiys = radiys - stels
    ispesh_dvish = 0
    print("Радиус подозрения данного персонажа после применения всех парметров" , radiys)
    while True:
        if ispesh_dvish >= 3:
            print("Успешная слежка")
            ypesno_sleska = True
            stels = stels + 10
            break
        time.sleep(1.2)        
        slran = random.randint(1,200)
        print("Цель отошла на  " , slran)
        sumrad = sumrad + slran
        sumtempsl = sumtempsl + slran
        print("Расстояние до цели:" , sumtempsl)
        time.sleep(1)
        print("Двигаемся? (Вы можете двигаться на расстояние от 100 до 200. Убедитесь что цель далеко. \n Введите значение на которое необходимо двигаться): ")
        dvish = input("w - двигаемся, s (или любая другая клавиша)- ждем: ")
        if dvish =="w":
            while True:
                znch = int(input("Введите занчение: "))
                if znch >=18 and znch<=200:
                    break
                else:
                    print("Неверно введено значение")
                    continue
            rand = random.randint(1,98)
            gg_dvish = znch + rand
            sumtempsl = sumtempsl - gg_dvish
            time.sleep(1)
            print("Расстояние до цели:" , sumtempsl)
            if sumtempsl >= radiys and sumtempsl <= maxradiys:
                ispesh_dvish = ispesh_dvish + 1
                print("Успешно")
                time.sleep(1.5)
                continue
            if sumtempsl < radiys:
                print("Вас поймали!!")
                vas_poimali = True
                break
            if sumtempsl > maxradiys:
                print("Цель ушла")
                chel_yshla = False
                break
        elif dvish =="s":
            continue
        else:
            continue
    sumtempsl = 0
    
def sleska_vostan():
    global yspesno_sleska
    global chel_yshla 
    global vas_poimali
    global ispesh_dvish
    yspesno_sleska = False
    chel_yshla = False
    vas_poimali = False
    ispesh_dvish = False
    

def gl2_altaris_night_vstr():
    global popitkacod
    global gg_save
    global kodnaskale
    global peshe_vibor
    time.sleep(1.5)
    print("Слежка за странным человек. Ночная встреча")
    time.sleep(2)
    os.system("cls")
    print("Ночь. Герои подходят к конюшне и прячутся за углом. Герои ожидают прибытия странного человека")
    time.sleep(1.5)
    print("Появляется странный человек в черном(***). Через некоторое время подходит и и человек за которым вы следили")
    time.sleep(1.5)
    print("*** - Приветствую, альтаир. Что нового?")
    time.sleep(1.5)
    print("Альтаир --- Штаб борьбы с колдуньей собирает о ней информацию, собирает силы и готовится к атаке")
    time.sleep(1.5)
    print("*** - Хммм, понятно.\n Колдунья говорит что появился 2 наследник хоть с первого она и нейтрализовала, но он может помочь 2")
    time.sleep(1.5)
    print("*** - Сможешь узнать о нем?")
    time.sleep(1.5)
    print("Альтаир - Я ничего подобного не слышал.")
    time.sleep(1.5)
    print("*** - К тебе не подходил никакой человек с летающем существом рядом?")
    time.sleep(1.5)
    print("Альтаир -- Стоп! На это мы не договаривались. Ты мне обещал отдать кольцо? Где оно?")
    time.sleep(1.5)
    print("*** --- Его украли. Прости")
    time.sleep(1.5)
    print("Человек достаем нож и .....")
    time.sleep(1.5)
    print("Брум - Он уходит! За ним!")
    time.sleep(2.5)
    print("Человек в черном выхидит за городские ворота подходит к скале")
    print("Пишет на скале 128528")
    time.sleep(2.5)
    os.system("cls")
    print("Вы дежурите возле скалы и дожидаетесь ухода странного человека")
    time.sleep(1.5)
    print("Герои подходят к скале")
    while True:
        kodnaskale = input("Введите код:")
        if kodnaskale == "128528":
            break
        else:
            print('Неверный код')
            popitkacod = popitkacod + 1
            if popitkacod >= 3:
                print("Брум - Код вроде бы 128528")
                gg_save = + gg_save + 10
            continue
    print("Открывается вход в небольшую комнатку со свечой на столе, кроватью в углу и странным зеркалом на стене")
    time.sleep(1.5)
    print("Герои решают изучить комнату")
    time.sleep(1.5)
    print("Брум находит дневник странного человека")
    time.sleep(1.5)
    print("-----------------------------------------")
    time.sleep(1.5)
    print("Вчера был мой день рождения мне исполнилось 481 год. Ровно 460 лет назад меня заколдавала кольдунья \n. Теперь я обязан ей прислуживать 500 лет")
    time.sleep(1.5)
    print("Если я верно отслужу 500 лет то она меня расколдует и я снова смогу жить своей жизнью, мне снова станет 21 год")
    time.sleep(1.5)
    print("Осталось 40 лет, еще немного")
    time.sleep(1.5)
    blackman.age = "481 год"
    blackman.plan = "Он вынужден прислуживать колдунье чтобы с него сняли проклятье"
    blackman.rassa = "Заколдованное существо. Ранее - человек"
    print("Раньше я жил в маленьком городишке рядом с Эмеральдом")
    time.sleep(1.5)
    blackman.national = "Город Эмеральд"
    print("Как я счучаю по тем временам.")
    time.sleep(1.5)
    print("Еще эта колдунья.")
    time.sleep(1.5)
    print("Она требует от меня невыполнимого хочет от меня получить кольцо  и требует узнать что происходит в штабе")
    time.sleep(1.5)
    print("Я пообещал члену штаба это кольцо в обмен на информацию. Но я его потерял, даже не знаю где. Колдунья меня убьет")
    time.sleep(1.5)
    print("Вдруг свет в комнате гаснет и в зеркале появляется силуэт колдуньи")
    time.sleep(1.5)
    print('Колдунья - Ардин! Докладывай')
    time.sleep(1.5)
    blackman.name = "Ардин"
    time.sleep(1.5)
    print("Колдунья --- Так это не Ардин, это Брум со вторым наследником, добыча сама пришла к охотнику")
    time.sleep(1.5)
    peshe_vibor = input("y - бежать , n или любая другая клавиша - остаться")
    if peshe_vibor == "y":
        print("КОНЕЦ ПОБОЧНОГО СЮЖЕТА АЛЬТАРИСА")
    elif peshe_vibor == "n":
        print("Ардин - Вы не выйдите отсуда живыми!")
        time.sleep(1.5)
        print("Брум --- Ардин, постой тв помнишь меня я брум. Я помог твоей семье 459 лет назад. Ардин!")
        time.sleep(1.5)
        print("Колдунья --- Не выйдет. Я заколдовала его окончательно!!")
        time.sleep(1.5)
        print("Герои начинают сражаться с Ардином. Но проигрывают и колдунья их отбрасывает далеко от пещеры")
        time.sleep(1.5)
        print("КОНЕЦ ПОБОЧНОГО СЮЖЕТА АЛЬТАРИСА")
        yved.remove("2 - Побочный сюжет. Слежка за странным человек. Ночная встреча")
def gl2_ring_kasimir():
    global osn_s
    print("Казимир -- Ваши украшения готовы")
    time.sleep(1.5)
    print("Брум и ", profile_name , "(вместе) --- Отлично! Спасибо Казимир? Сколько тебе заплатить")
    time.sleep(1.5)
    print("Казимир --- 25000")
    time.sleep(1.5)
    print("У вас не хватает денег. Сказать честно - y. Убежать - n (или любая другая клавиша)")
    time.sleep(1.5)
    ringmoney = input()
    if ringmoney == "y":
            print("Казимир - Хорошо. Тогда пусть это будет подарком.")
    else:
            print("Ах вы!")
            time.sleep(1.5)
            print("Полицеские вас догнали. Штраф - 1000")
            time.sleep(1.5)
            money = money - 1000
            reyting = reyting - 220
            reyting_system()
            no_save = no_save + 200
    print("Отправимся в следующий город")
    time.sleep(1.5)
    print()
    print()
    time.sleep(1.5)
    print("Конец 2 главы")
    osn_s = True
    
def boy(x, y, o ):
    time.sleep(0.5)
    global dm
    global hp
    global exp
    global lvl
    global temp
    global vin
    global armor
    global attack
    temp = x
    armor = 3 + lvl*5
    attack  = 10 + lvl*20
    hp = 150 + 50*lvl + armor
    exp = exp + o
    lvl = exp//100
    print("Нажимай на кнопку 'shift' чтобы атаковать")
    while True:
        nr = random.randint(attack-5, attack)
        keyboard.wait('shift')
        print("Нанесен урон", nr)
        x = x-nr 
        if hp <= 0:
            print("Брум ---- к сожалению вы не справились с врагом. Попробуем еще раз!!")
            hp = 200 + 50*lvl
            x = temp
            continue
        if x <= 0:
            print("Вы победили врага!!")
            hp = 100 + 50*lvl 
            print()
            armor = 3 + lvl*5
            attack  = 10 + lvl*20
            hp = 150 + 50*lvl + armor
            exp = exp + o
            lvl = exp//100
            print("Вы получили опыт:" , o)
            print("Ваш текущий уровень " , lvl)
            x = temp
            vin = True
            time.sleep(3)
            break
        time.sleep(1)
        dm = random.randint(y-5, y)
        print("Вам нанесен урон:", dm)
        hp = hp - dm 

def ex_press(key):
    global money
    global lvl
    global attack
    global armor
    global study1
    global exp
    global study3
    global yvedki
    print("Запрос на вход в командное меню")
    keyboard.wait(key)
    print("---" * 15)
    print("МЕНЮ КОМАНД")
    while True:
        com = input("(h для просмотра всех команд) Введи нужную команду:")
        print("---" * 15)
        if com == "h":
            print("Меню - m")
            print("Помощь  - h")
            print("Инвентарь - e")
            print("Карта - k")
            print("Меню уведомлений - j")
            print("Cбор улик - f")
            print("Выйти из меню команд - q")
            continue
        if com == "j":
            print("-" *10)
            print(*yved , sep="\n")
            time.sleep(1.7)
            yvedki = input()
            if yvedki == "1":
                pass
            if yvedki == "2":
                pass
        if com == "f":
            print("-" *10)
            if inblackman == True:
                print("Новая улика. \n Проходите сюжет побочные задания и основной сюжет чтобы откртывать новую информацию. \n Чтобы перейти к миссиям войдите в меню уведмолений")
                print("-----------------------------------------")
                blackman.proof_get()
          
        if com == "e":
            print("--" *15)
            print(" ИНВЕНАТРЬ ")
            print(*plor , sep="\n")
            global ch
            ch = input("Введите название оружия которое хотите применить. Введите точку для отмены. Чтобы снять все мечи введите drop:")
            if ch == ".":
             continue
            if  ("Костяной меч" or ch == "костяной меч" or ch == "кс" or ch == "ks" ) and "Костяной меч" in plor:
                print("Меч применен")
                attack = attack + bs
                study1 = True
                continue
            if  ("Меч крови" or ch == "меч крови" or ch == "мк" or ch == "bs" ) and "Меч крови" in plor:
                print("Меч применен")
                attack = attack + bls
                continue
            if  ("броня громовежца" or ch == "Броня громовежца" or ch == "бг" or ch == "bg" ) and "Броня громовежца" in plor:
                print("Броня успешно применена")
                armor = armor + ga
                study3 = True
                continue
            
            if ch == "drop":
                attack = 10 + lvl*20
                print("Вы сняли все оружия")
                continue
        if com == "m":
            lvl = exp//100
            print("Меню")
            print("Баланс:" , money )
            print("Уровень:" , lvl )
            print("Опыт:" , exp )
            print("Атака:" , attack )
            print("Броня:", armor)
            continue
        if com == "q":
            time.sleep(1) 
            os.system('cls')
            global study
            study = True
            global esccl
            esccl = True
            break
os.system('cls')
for i in tqdm(range(18)):
        time.sleep(0.1)
os.system('cls')
print("Добро пожаловать в Knight.Neritage. Введите ваш профиль, если его нет автоматически создастся новый.")
profile_name = input()
profile_name = profile_name.lower()
check_file = os.path.exists(str(profile_name) + '.txt')
if check_file == True:
    with open(profile_name + '.txt', "r") as lprofile:
        stels = lprofile.readline()
        exp = lprofile.readline()
        money = lprofile.readline()
        reyting = lprofile.readline()
        brym_gg_save = lprofile.readline()
        gg_save = lprofile.readline()
        no_save = lprofile.readline()
        plusdeystv = lprofile.readline()
        minusdeystv = lprofile.readline()
        save = lprofile.readline().strip()
    lprofile.close()
    stels = int(stels)
    exp = int(exp)
    money = int(money)
    reyting =int(reyting)
    brym_gg_save = int(brym_gg_save)
    gg_save = int(gg_save)
    no_save = int(no_save)
    plusdeystv = int(plusdeystv)
    minusdeystv = int(minusdeystv)
    while True:
            n = input("Чтобы начать игру введите s: ")
            if n == "s" or n == "S":
                time.sleep(1)
                os.system('cls')
                break   
            else:
                continue
else:
    while True:
            n = input("Чтобы начать игру введите s: ")
            if n == "s" or n == "S":
                time.sleep(1)
                os.system('cls')
                break   
            else:
                continue
if save == "0":
    print("*** - Добро пожаловать в игру! Мое имя - брум. Я твой проводник в мир рыцарей и чудовищ", "Как зовут тебя?. Если у тебя уже есть профиль введи его название. ", sep="\n")
    time.sleep(0.5)
    print(profile_name , "---- Я " , profile_name)
    time.sleep(0.5)
    print("Брум - Молодец," , profile_name )
    time.sleep(0.5)
    print("Брум -Так как я твой верный помощник ты можешь нажать кнопку esc для того чтобы попасть в командное  меню."," командном меню введи h чтобы увидеть полный список команд" , "Попробуй сейчас!! Не забудь выйти чтобы продолжить" , sep="\n")
    ex_press("esc")
    if study == True:
        time.sleep(1)
        print("Брум - Нa горизонте приспешник короля империи 1 - ого ранга. Тебе надо победить его!!!")
        print("Нажимай на кнопку shift чтобы атаковать")
        while True:
            nr = random.randint(attack-5, attack)
            keyboard.wait('shift')
            print("Нанесен урон", nr)
            hpki1 = hpki1 - nr
            if hpki1 <= 0:
                print("Отлично!! Вы победели вашего первого монстра")
                print("С него выпал отличный оружие дающие +1 к аттаке. Войди в инвентарь с помощью меню команд и примени меч!!")
                plor.append("Костяной меч")
                hp = 100 + 50*lvl
                hpki1 = 35
                exp = exp + 10
                break
    ex_press("esc")
    if study1 == True and esccl == True:
        esccl = False
        os.system('cls')
        time.sleep(1) 
        print("Брум --- Ты быстро учишься молодец")
        #print("Брум ---" + "")
        print("Брум --- Пришло время рассказать побольше рассказать о нашем мире.")
        time.sleep(1) 
        print("Брум --- Началось все с захвата власти злой короловей Сайрас. Сейчас ее замок находится в царстве бущущих ветров АРАДОН.")
        time.sleep(1) 
        print("Все монстры с которыми ты сражаешься ее приспешники. Она разделила их по рангам от C до S+. Чудовища которых она принесла со своей родины ранга S+")
        time.sleep(1)
        print('Вот полная таблица рангов:')
        print("---" * 15)
        time.sleep(0.5)
        print("Ранг            Монстры ранга")
        print(" S+               Все мировые боссы. Их очень долго перечеслять. Они очень сильные.")
        print("                  С них ты можешь получить + 100 опыта (как раз повысить 1 уровень).")
        print("---" * 15)
        time.sleep(0.5)
        print(" S                Вот некоторые из них: приспешник королевы империи 3 - го ранга.")
        print("                  Главари бандитов. Наемные самураи. C них можно получить + 75 опыта")
        print("---" * 15)
        time.sleep(0.5)
        print(" A                 Приспешники королевы империи 3- го ранга. С них ты сможешь получить + 50 опыта")
        print("---" * 15)
        time.sleep(0.5)
        print(" B                 Приспешники королевы империи 2- го ранга. С них ты сможешь получить + 25 опыта")
        print("---" * 15)
        time.sleep(0.5)
        print(" C                 Приспешники королевы империи 1- го ранга. С них ты сможешь получить + 10 опыта")
        print()
        print("Твоя потанцеальная сила примерно равна уровню C")
        time.sleep(0.5)
        while True:
            prd = input("Чтобы продолжить введи d :")
            if prd != "d":
                continue
            elif prd == "d":
                break
        os.system('cls')
        time.sleep(1)
        print("Брум - Нa горизонте приспешник короля империи 3 - ого ранга. Тебе надо победить его. Он силен.Попробуй. Если ты будешь проигрывать я помогу тебе!!!")
        boy(hpki3, apki3 , opki3)
        time.sleep(1)
        print("Брум --- Ничего себе не все обученные рыцари могут справится с таким чудовищем а ты!!. Кто же ты такой!!!")
        time.sleep(3)
        os.system('cls')
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print("                                     KNIGHT.NERITAGE                                 ")
        print()
        print("                                         ГЛАВА I                                     ")
        print()
        print()
        print()
        print()
        print()
        print()    
        time.sleep(3)
        os.system('cls')
        print()
        print()
        print()
        print()
        print()
        print()
        print("День спустя")
        time.sleep(0.5)
        print("Брум ---" , "Тот монстр которого ты победил был ранга A. Я удивлен. Честно говоря немногие способны на это.")
        time.sleep(1)
        #print("Брум ---" , "")
        print("Брум ---" , "Я советую тебе обратиться в воинскую академию в ближайшем городе. Сейчас я посмотрю ближайший город от нас ...... ")
        time.sleep(1)
        print("Брум ---" , "Итак ближайший город Некреос - город в котором правит Барнет - цестный рыцарь ранга S. Идти минут 10. В путь!")
        time.sleep(1)
        print()
        print()
        print("--------------------------------ВНИМАНИЕ----------------------------")
        print("         2 минуты игрового времени = 1 секунде реального времени    ")
        print("--------------------------------------------------------------------")
        time.sleep(5)
        os.system('cls')
        print("---" * 10)
        print("Добро пожаловать в город Некреос")
        time.sleep(0.5)
        print()
        print("Брум ---" , "Отправимся к начальнику академии")
        time.sleep(1)
        print("*** - Я начальник академии рыцарь Клар ")
        time.sleep(0.5)
        #print("Клар ---" , "")
        print("Клар ---" , "Если ты хочешь вступить в академию нужно пройти испытания. Нооо сейчас проходит турнир готов ли ты участвовать в турнире - приз меч крови?")
        time.sleep(0.5)
        print(profile_name , " --- ДА")
        #print(profile , " --- ")
        print("--------------------------------------------------------------------")
        print("Бой первый")
        print("Противник рыцарь ранга 1")
        boy(hkn1 , akn1 , okn1)
        time.sleep(1)
        os.system('cls')
        print("--------------------------------------------------------------------")
        print("Бой второй ")
        print("Противник рыцарь ранга 2")
        boy(hkn2 , akn2 , okn2)
        time.sleep(1)
        os.system('cls')
        print("--------------------------------------------------------------------")
        print("Бой третий ")
        print("Противник рыцарь ранга 3")
        boy(hkn3 , akn3 , okn3)
        time.sleep(1)
        os.system('cls')
        print()
        print("Клар ---" , "Удивительно этот недавно вступивший в турнир рыцарь прошел в финал")
        time.sleep(1)
        os.system('cls')
        time.sleep(1)
        print()
        print()
        print()
        print()
        print()
        print("                                     BOSS FIGHT                                 ")
        print()
        print()
        print()
        print()
        print()
        print()
        time.sleep(1)
        boy(hknight_boss, aknight_boss, oknight_boss)
        print("Клар ---" , "Удивительно! Это победа!!" , profile_name , " наш победитель он получает меч крови. И титул рыцаря академии")
        plor.append("Меч крови")
        print("Брум ---" , "Как ты их победил! Я удивлен давай попробум применить меч крови")
        money += 1500
        ex_press("esc")
        if esccl == True:
                esccl = False
                print("Брум ---" , "Хороший меч")
                print("Клар ---" , "Вы также получаете 1500 тысячи монет.")
                print("Клар ---" , "Удачи вам!!")
        print("Брум ---" , "Давай отправимся в местный магазин и посмотрим какие там есть товары!")
        time.sleep(1)
        os.system('cls')
        time.sleep(1)
        print("Гейс---" , "Я держатель местоного магазина вы можете посмотреть наличие!!!")
        shop_nekreos = ["Броня громовежца -- 1400" , "Костянной меч -- 300"]
        print("Магазин города Некреос")
        print(*shop_nekreos , sep="\n")
        #print("Брум ---" , "")
        print("Брум ---" , "Давай купим Броню громовежца она как раз стоит 1400")
        print()
        print()
        print()
        print()
        print("--------------------------------ВНИМАНИЕ-----------------------------------------------")
        print("         Для удобства вы можете вводить первые буквы слов для приобретения предметов   ")
        print("---------------------------------------------------------------------------------------")
        print()
        print()
        print()
        print()
        while True:
                buy = input("Введите товар который вы хотите приобрести:")
                if (buy == "броня громовежца" or buy == "bg" or buy == "бг") and money >= 1400 :
                    print("Предмет приобретен")
                    money = money - 1400
                    print("Ваш баланс" , money)
                    plor.append("Броня громовежца")
                    break
                if (buy == "броня громовежца" or buy == "bп" or buy == "бг") and money < 1400 :
                    print("Недостаточно средств")
                    print("Ваш баланс" , money)
                    break
                else:
                    print("Вам необходимо купить другой предмет")
                    continue
        print("Брум ---" , "Хорошая броня. Давай ее применим")
        ex_press("esc")
        if esccl == True and study3 == True:
                print("Брум ---" , "Отличная броня. Давай теперь отправимся в .......")
                print(profile_name , " --- СТОП!!! Мы занимаемся не тем. Мне нужно вернуться домой")
                print("Брум ---" , "Давай тогда отправимся Барнету")
                time.sleep(1)
                os.system('cls')
                time.sleep(1)
                print("Cтражник ----- Вы куда?")
                print("Брум ---" , "Мы пришли к Барнету - впустите.")
                print("Cтражник ----- Барнет спустится к вам сам ожидайте")
                time.sleep(1)
                os.system('cls')
                time.sleep(1)
                #print("Барнет ---") 
                print("Барнет --- Что принесло вас сюда путники?")
                time.sleep(0.5)
                print(profile_name , " --- Мне нужно вернуться домой. Я попал сюда из другого мира. Вы можете мне помочь?")
                time.sleep(0.5)
                print("Барнет --- Хммм.... Я могу помочь только советом. В древних рукописях говорилось что придет странник из мира иного и ....")
                time.sleep(1)
                print("Барнет --- И спасет мир от проклятия. Но может вернуться домой ему поможет. Портал в царстве .... ")
                time.sleep(1)
                print("Барнет --- АРАДОН")
                time.sleep(0.5)
                print(profile_name , " ---  Тогда в путь в царство арадон АРАДОН")
                time.sleep(0.5)
                print("Барнет --- Это опасно! Там правит злая королева с ней придется не легко. Еще тебе надо узгнать больше про портал")
                time.sleep(0.5)
                print(profile_name , " --- Ясно")
                time.sleep(3)
                os.system('cls')
                print()
                print()
                print()
                print()
                print()
                print()
                print()
                print()
                print()
                print()
                print()
                print()
                print("                                     KNIGHT.NERITAGE                                 ")
                print()
                print("                                         ГЛАВА II                                     ")
                print()
                print()
                print()
                print()
                print()
                print()
                save = "gl2ct0"
if save == "gl2ct0":
    print("--------------------------------ВНИМАНИЕ-------------------------------------------------------------------")       
    print('Началась 2 глава. Обучение подходит к концу. Начиная со 2 главы вы можете принимать самостоятельные решения')
    print('Эти решения будут влиять на одну из нескольких концовок. Также ты будеш получать социальный рейтинг       ')
    print("-----------------------------------------------------------------------------------------------------------")
    time.sleep(4.3)
    os.system('cls')
    print(profile_name , ' --Смотри, Брум, какое необычное кольцо! Оно точно обладает какой-то силой')
    time.sleep(1)
    print(" Брум:  Да, ты прав. \n Давай отправимся в Альтарис, там живут лучшие мастера-ювелиры, они помогут нам разобраться с этим кольцом.")
    time.sleep(1)
    print(profile_name, "---Отличная идея! \n В Альтарисе мы сможем узнать больше о свойствах этого кольца и понять, как его использовать.")
    time.sleep(0.5)
    print(" Брум:  Тогда вперёд! Нас ждут приключения!")
    time.sleep(2)
    print(profile_name , "--- Ты уверен, что это кольцо не принесёт нам проблем?")
    print(" Брум:  Не знаю, но я чувствую, что оно может быть полезным. \n Может быть, оно поможет нам в бою или даст нам какие-то способности.")
    time.sleep(1)
    print("Девочка --- Помогите помогите, там монстры. Они напали на наш дом ")
    time.sleep(2.5)
    os.system('cls')
    print("------------------------------------------------------------------------")
    print("Побочное задание: \n принять: (y) \n отказаться: (n или любая другая клавиша)")
    while True:
        pobochka = input()
        if pobochka == "y":
            reyting = reyting + 50
            print(profile_name , "Мы тебе поможем веди!!!")
            time.sleep(1)
            print("Девочка ---- Вот они!!")
            time.sleep(1)
            print("Брум --- хм странно я  незнаю такого монстра. Наверно он очень сильный")
            time.sleep(1)
            print("сразиться (y) \n отступить (n или любая другая клавиша) ")
            popobochka = input()
            if popobochka == "y":
                reyting = reyting + 25
                boy(hdki1,adki1,odki1)
                if vin == True:
                    vin = False
                    print("Родители девочки ---- Спасибо тебе храбрый рыцарь, в награду возьми немнго денег ")
                    brym_gg_save = brym_gg_save + 200
                    plusdeystv += 1
                    gg_save = gg_save - 10
                    no_save = no_save + 0
                    print('Взять деньги (y) \n отказаться (n или любая другая клавиша)')
                    dengiilinet = input()
                    if dengiilinet == "y":
                        print("Получены деньги:3000")
                        time.sleep(1)
                        money = money + 3000
                        print("Брум - Ну идем дальше в Альтарис")
                        break
                    if dengiilinet == "n":
                        brym_gg_save = brym_gg_save + 55
                        gg_save = gg_save - 10
                        no_save = no_save + 0
                        dengiilinet = 0
                        reyting -= 100
                        reyting_system()
                        break
                    else:
                        brym_gg_save = brym_gg_save + 55
                        gg_save = gg_save - 10
                        no_save = no_save + 0
                        dengiilinet = 0
                        reyting -=100
                        reyting_system()
                        break    
            if popobochka == "n":
                brym_gg_save = brym_gg_save - 200
                minusdeystv +=2
                gg_save = gg_save + 30
                no_save = no_save + 150
                popobochka = 0
                break
            else:
                brym_gg_save = brym_gg_save - 200
                gg_save = gg_save + 30
                no_save = no_save + 150
                popobochka = 0
                break    
        if pobochka == "n":
            reyting = reyting - 100
            minusdeystv += 1
            brym_gg_save = brym_gg_save - 100
            gg_save = gg_save + 10
            no_save = no_save + 100
            pobochka = 0
            break
        else:
            reyting = reyting - 100
            brym_gg_save = brym_gg_save - 100
            minusdeystv += 1
            gg_save = gg_save + 10
            no_save = no_save + 100
            pobochka = 0
            pobochka = 0
            break
    print(" Брум:  Вот мы и в Альтарисе. Теперь нужно найти мастера-ювелира.")
    time.sleep(1)
    print(profile_name ,  "Давай спросим у местных жителей, где можно найти хорошего мастера.")
    time.sleep(1)
    print("Брум:  Хорошая идея.")
    time.sleep(1)
    print("Брум: Извините где можно найти самого лучшего ювелира в городе")
    time.sleep(1)
    print("Местный житель --- Обратитесь к Казимиру, он живёт в центре города.")
    time.sleep(3.2)
    os.system("cls")
    print("------------------------ВНИМАНИЕ-------------------------------------")
    print("Вы можете сохранить(рукомендуется) или не сохранять прогресс(не рекомендуется ) \n сохранить(s) \n не сохранять(d или любая другая клавиша)")
    soxranka = input()
    while True:
        if soxranka == "s":
            soxranka = 0
            save = "gl2ct1"
            exp = str(exp)
            money = str(money)
            reyting =str(reyting)
            brym_gg_save = str(brym_gg_save)
            gg_save = str(gg_save)
            no_save = str(no_save)
            with open(profile_name + '.txt' , "w") as lprofile:
                lprofile.write(stels)
                lprofile.write("\n")
                lprofile.write(exp)
                lprofile.write("\n")
                lprofile.write(money)
                lprofile.write("\n")
                lprofile.write(reyting)
                lprofile.write("\n")
                lprofile.write(brym_gg_save)
                lprofile.write("\n")
                lprofile.write(gg_save)
                lprofile.write("\n")
                lprofile.write(no_save)
                lprofile.write("\n")
                lprofile.wrire(plusdeystv)
                lprofile.write("\n")
                lprofile.write(minusdeystv)
                lprofile.write("\n")
                lprofile.write(save)
        elif soxranka == "d":
            save = "gl2ct1"
            soxranka = 0
            break
        else:
            soxranka = 0
            save = "gl2ct1"
            break
if save == "gl2ct1":
    print(" Казимир: Добро пожаловать в мою мастерскую. Чем я могу вам помочь?")
    time.sleep(1)
    print(profile_name,"Мы нашли это кольцо по пути из города Некреос и решили прийти к вам. \n Вы известный мастер-ювелир, и мы надеемся, что вы сможете нам помочь.")
    time.sleep(1)
    print("Казимир:  Это очень интересное кольцо. \n Оно сделано из редкого металла, который я никогда раньше не видел. \n Я думаю, что оно может иметь большую ценность")
    time.sleep(1)
    print("Брум: Что вы предлагаете? Продать кольцо или обменять его на что-то более полезное?")
    time.sleep(1)
    print(" Казимир:  Я предлагаю создать для вас уникальные украшения из этого кольца. \n Они будут не только красивыми, но и полезными.")
    time.sleep(0.7)
    print(profile_name , "Звучит интересно. Но как вы будете создавать эти украшения?")
    time.sleep(1)
    print("Казимир:  У меня есть мастерская, где я работаю над своими проектами. \n Я буду использовать свои навыки и инструменты, чтобы создать для вас красивые и изысканные изделия.")
    time.sleep(1)
    print("Брум:  А сколько времени это займёт?")
    time.sleep(1.7)
    print("Казимир:  Несколько дней. Я должен тщательно изучить кольцо и разработать дизайн украшений.")
    time.sleep(0.7)
    print()
    print("----------------------------Игровой выбор------------------------------")
    while True:
        ykr = False
        kolvib =  input("Продать кольцо (y) \n  Создать украшения (n или любая другая клавиша): ")
        if kolvib == "y":
            print(profile_name , "Я собераюсь продать кольцо. Сколько оно будет стоить?")
            time.sleep(1)
            print("Казимир: Примерно 8000?")
            time.sleep(1)
            print(profile_name , "Я готов")
            money = money + 8000
            break
        elif kolvib == "n":
            print(profile_name ,  "Хорошо, мы согласны. Давайте начнём работу над кольцом.")
            time.sleep(1)
            print("Казимир:  Отлично! Приходите ко мне через несколько дней, и я покажу вам новые украшения")
            ykr = True
            break
        else:
            print(profile_name ,  "Хорошо, мы согласны. Давайте начнём работу над кольцом.")
            time.sleep(1)
            print("Казимир:  Отлично! Приходите ко мне через несколько дней, и я покажу вам новые украшения")
            yrk = True
            break   
    print("Брум - Мы можем узнать побольше о колдуньии и о других городах распросив местных жителей")
    time.sleep(1)
    print("-------------------------------Выбор местного жителя-------------------")
    time.sleep(0.7)
    print("Вы можете выбрать местного жителя. \n После выбора вы начнете с ним диалог \n Выбирайте жителей исходя из внешнего вида")
    vlad = People()
    vlad.description = "Обычный местный житель, одет в фермурскую одежду"
    altair = People()
    altair.description = "Необычный житель. Одет в военную форму. Брум говорит что это член тайной разведки Альтариса"
    roman = People()
    roman.description = "Человек одетый в  странную форму. С ножом в руках. Видимо это бандит"
    bsesiteky = 0
    while True:
        if bsesiteky == 3:
            altaris_free = True
            break
        os.system('cls')
        print("-------------------------------------", "1 - житель" , vlad.name, vlad.age , vlad.description , sep="\n")
        print("-------------------------------------", "2 - житель" , altair.name ,altair.age, altair.description, sep="\n")
        print("-------------------------------------", "3 - житель" , roman.name , roman.age, roman.description, sep="\n")
        time.sleep(0.7)
        print("------------------------------------------------------------------------------------------------")
        print("В качестве обучения выберите всех жителей, чтобы познакомиться с новыми механиками")
        vibor = input("Введите номер местного жителя: ")
        if vibor == "1":
            print(profile_name, "---- Привет! Я путешественник, можно задать тебе пару вопросов ")
            time.sleep(1.7)
            print("*** - Меня зовут Влад чем я могу быть полезен")
            time.sleep(1.7)
            print(profile_name , " Знаешь ли ты про колдунью которая живет в городе АРАДОН?")
            time.sleep(1.7)
            print("Влад - Нет. Я думаю, что я не смогу вам помочь")
            time.sleep(1.7)
            print(profile_name , " --- До свидания")
            time.sleep(1.7)
            bsesiteky = bsesiteky +1
            time.sleep(1.7)
            continue
        elif vibor == "2":
            print(profile_name, "---- Привет! Я путешественник, можно задать тебе пару вопросов ")
            print("*** - Извините. Я на службе разговаривать с вами не могу")
            print(profile_name , " ---- До свидания")
            print()
            print()
            print("Проследить за членом тайно разведки? \n Проследить (y) \n Уйти (n или любая другая клавиша)")
            sleskain = input()
            if sleskain == "y":
                print("Внимание!!!!! Если вас поймают будет понижение репутации штраф и наказание")
                print("----------------------------------------------------------------------------")
                print("У данного персонажа радиус подозрения - " , seckret_razvedchil_altaris , "\n Если вы подойдете ближе чем этот радиус то вас поймают")
                print("Нажимайте кнопку w чтобы продвигаться и следить")
                sled(seckret_razvedchil_altaris , maxsecret_razvedcik_altairs)
                if vas_poimali == True:
                    print("*** - Ты удумал меня периследовать! Смотрите БАНДИТ!!!")
                    time.sleep(1.7)
                    reyting = reyting - 200
                    print("Штраф - 800")
                    reyting_system()
                    money = money - 800
                    sleska_vostan()
                elif chel_yshla == True:
                    print("Брум --- ну вот теперь мы не узнаем о этом подозрительном человеке ")
                    sleska_vostan()
                elif yspesno_sleska == True:
                    print("Цель стоит за углом рядом с владельцем магазина")
                    time.sleep(1.7)
                    print("Цель --- Встреча ночью рядом с конюшней")
                    time.sleep(1.7)
                    print("Владелец магизна --- я передам")
                    time.sleep(1.7)
                    print("--Цель ушла---")
                    time.sleep(1.7)
                    print("Брум -надо проследить.")
                    yved.append("2 - Побочный сюжет. Слежка за странным человек. Ночная встреча")
                    sleska_vostan()
                    plusdeystv += 1
                bsesiteky = bsesiteky +1
                continue
            if sleskain == "n":
                continue
            else:
                continue
        elif vibor == "3":
            print(profile_name, "---- Привет! Я путешественник, можно задать тебе пару вопросов ")
            print("**** - Ну и какие вопросы? ")
            print("Брум (шепот) ----- " , profile_name , " он какой-то подозрительный тип")
            print("Бандит - Я не услышал, повтори что ты сказал?")
            print()
            print("---------------------")
            print("Бандит наносит удар ножом, но" , profile_name , "уворачивается. \n ---------------- \n  Убежать (y) \n Вступить в драку (n или любая другая клавиша)" )
            banda = input()
            if banda == "y":
                reyting = reyting - 10
                reyting_system()
                time.sleep(2)
                continue
            if banda == "n":
                boy(hbandit_classic , abandit_classic , obandit_classic)
                print("Простите! Я совсем не знаю про колдунью меня нанял странный мужчина в черном плаще. \n Он сказал что будет платить мне деньги если я буду кошмарить население города")
                continue
            else:
                boy(hbandit_classic , abandit_classic , obandit_classic)
                print("Простите! Я совсем не знаю про колдунью меня нанял странный мужчина в черном плаще. \n Он сказал что будет платить мне деньги если я буду кошмарить население города")
                blackman = BlackMan()
                blackman.title = "Мужчина в черном плаще"
                blackman.description = "Странный мужчина в черном плаще, который платит деньги бандитам"
                blackman.city = "Альтарис"
                inblackman = True
                bsesiteky = bsesiteky + 1
                time.sleep(3)
                continue
        elif vibor == ".":
            altaris_free = True
            break   
        else:
            continue
if altaris_free == True:
    print('------------------------------------Внимание открыта механника сбора улик.------------------- \n После сбора достаточного количества улик можно открыть факт \n Чем больше открыто фактов тем больше известно о кольдунье')
    print("Вход в меню уведомлений - через командное меню")
    print()
    print()
    print()
    if ykr == True:
        print("-----------------------------------------")
        print("Украшения изготовлены. Для продолжения основного сюжета войдите в меню уведомлений через командное меню.")
        yved.append(" - Основной сюжет. Кольца у Казимира.")
    ex_press("esc")
if osn_s == True:
    time.sleep(1)
    print("------------------------ВНИМАНИЕ-------------------------------------")
    print("Вы можете сохранить(рукомендуется) или не сохранять прогресс(не рекомендуется ) \n сохранить(s) \n не сохранять(d или любая другая клавиша)")
    soxranka = input()
    while True:
        if soxranka == "s":
            soxranka = 0
            save = "gl3ct0"
            exp = str(exp)
            money = str(money)
            reyting =str(reyting)
            brym_gg_save = str(brym_gg_save)
            gg_save = str(gg_save)
            no_save = str(no_save)
            with open(profile_name + '.txt' , "w") as lprofile:
                lprofile.write(stels)
                lprofile.write("\n")
                lprofile.write(exp)
                lprofile.write("\n")
                lprofile.write(money)
                lprofile.write("\n")
                lprofile.write(reyting)
                lprofile.write("\n")
                lprofile.write(brym_gg_save)
                lprofile.write("\n")
                lprofile.write(gg_save)
                lprofile.write("\n")
                lprofile.write(no_save)
                lprofile.write("\n")
                lprofile.wrire(plusdeystv)
                lprofile.write("\n")
                lprofile.write(minusdeystv)
                lprofile.write("\n")
                lprofile.write(save)
        elif soxranka == "d":
            save = "gl3ct0"
            soxranka = 0
            break
        else:
            soxranka = 0
            save = "gl3ct0"
            break