message = 'GIEWIVrGMTLOVrHIQS'  # encrypted message
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(LETTERS)):
    translated = ''
    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            num = num - key
            if num < 0:
                num = num + len(LETTERS)
            translated = translated + LETTERS[num]
        else:
            translated = translated + symbol
    print("正在通过暴力破解Hacking,目前正在暴力破解的Key为： %s,破解后的结果为：%s" % (key, translated))
