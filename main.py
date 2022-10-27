#Библиотека с регулярными выражениями
import re


# Нахождение своего смайлика исходя из номера ИСУ при помощи средств Python(доп. задание)
nomer_isu = 368038
eyes = [":", ";", "X", "8", "="]
nose = ["-", "<", "-{", "<{"]
mouth = ["(", ")", "O", "|", "\ ", "/", "P"]
smile = ""
for i in range(0, 5):
    if nomer_isu % 5 == i:
        smile = smile + eyes[i];
for i in range(0, 4):
    if nomer_isu % 4 == i:
        smile = smile + nose[i];
for i in range(0, 7):
    if nomer_isu % 7 == i:
        smile = smile + mouth[i];
print("")
print("MY SMILE: " + smile)


# Задание первое, нахождение смайлика в строке при помощи регулярных выражений
print("")
print("TASK 1:")
print("")
line1 = "8-{P):<|----postavte-100-ballov-----=-}O8-}P8-{P)"
line2 = "8-P<{PX<\;-}|X<O:<{(---pojaluista---8-(;<)=-O:<{|X-P=-/8-{P=-):<{)X<{|"
line3 = "JGJJFOBDHO*(@V&#T(VFOHJFV80OX-)()()()())/----ya-ochen-staralsya------/rthjhgdfgX-);.;<}.}<=+X-)X-}}"
line4 = "01;<)28GJGKVFDH&(*$COOCKXMV-{P{8()(-)<_)-<>BTOV$()G&V<*@&(DCSG(->==+8-{P8GIFDYVIUDVKJDNCLKJVX-{P8-{P)8-{P)"
line5 = "1-2%=4;{F*DB^Y(*<(*F^DG*&M)F(@*CDLSKU*(#^^GBX-(<}8X-)+6-)8-{P)"
print("Quantity of emojis in lines in order: ", len(re.findall(r'8-{P', line1)), len(re.findall(r'8-{P', line2)),
      len(re.findall(r'8-{P', line3)), len(re.findall(r'8-{P', line4)), len(re.findall(r'8-{P', line5)))


#Задание второе, найти даты в форматах HH:MM:SS или HH:MM, где HH – число от 00 до 23, а MM и SS – число от 00 до 59,
# и заменить их на (TBD)
print("")
print("TASK 2:")
print("")
def RebuildMessage(string):
    pattern = r"(([0-1]{1}[0-9]{1})|([2]{1}[0-3]{1})):[0-5][0-9]:[0-5][0-9]"
    pattern2 = r"(([0-1]{1}[0-9]{1})|([2]{1}[0-3]{1})):[0-5][0-9]"
    stringRe = re.sub(pattern, "(TBD)", string)
    stringRe = re.sub(pattern2, "(TBD)", stringRe)
    return stringRe
print(RebuildMessage("Уважаемые студенты! В эту субботу в 15:00 планируется доп. занятие на 2 часа. "
                     "То есть в 17:00:01 оно уже точно кончится."))
print(RebuildMessage("Уважаемые студенты! Это очень информативное сообщение, в котором соержится ваша"
                     " дата встречи - 21:44:58, ну или может быть 23:22"))
print(RebuildMessage("Уважаемые студенты! Зачем это читать? Я могу конечно просто так вставить даты, но они будут от"
                     " вас скрыты. Вот, смотрите - 11:22:33"))
print(RebuildMessage("Уважаемые студенты! Смотрите, сейчас одна дата скроется, а другая - нет."
                     " Это настоящая магия! Первая дата: 325:76, она не скроется, а вот 15:30 - скроется"))
print(RebuildMessage("Уважаемые студенты! А что здесь писать? Я уже устал придумывать..."
                     " Давайте я вставлю три разные даты: 12:34:56 20:00 11.34 и"
                     " третья не скроется, потому что формат не верен."))

#Задание третье - написать регулярное выражение, которое проверяет корректность email и в качестве
# ответа выдаёт почтовый сервер (почтовый сервер – часть email идущая после «@»)
print("")
print("TASK 3:")
print("")
def PostServer(postServerName):
    pattern = re.compile(r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+")
    pattern2 = re.compile(r"@\S+\.[A-Z|a-z]\w+")
    postServerNameRe = ""
    if re.fullmatch(pattern, postServerName):
        postServerNameRe = pattern2.findall(postServerName)
    else:
        postServerNameRe = "Wrong e-mail or not e-mail."
    return postServerNameRe
print(PostServer("445gsvtv3x@mail.ru"))
print(PostServer("example@example"))
print(PostServer("example@example.com"))
print(PostServer("Pi_pi_Pu_Pu@yandex.rutb"))
print(PostServer("nagibator.princess.cool.boy.barbie.2007@itmo.ru"))