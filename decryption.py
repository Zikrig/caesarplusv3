import razlich
def menudecr(shifr_book,ret=False):
    alfes = razlich.razl(shifr_book)  # поиск алфавита
    newalf = razlich.vyr(alfes[1])  # выравнивание алфавита в правильном порядке

    newmes = razlich.rashr(shifr_book, newalf)  # расшифровка с помощью нового алфавита
    i = 'a'
    j=0
    while (i != ''):
        print(newmes[100:300])
        print("Если вы догадались о букве, введите ее так:'а б'. Тогда а в сообщении заменится б")
        print("Если вы просто хотите увидеть полную расшифровку, просто нажмите Enter")
        print("Текущий алфавит - " + newalf)
        i = input()
        if len(i) == 3 and i[1] == ' ':  # проверка соответствия формату
            ain = ord(i[0]) - 1072  # порядковый номер буквы в алфавите
            bin = ord(i[2]) - 1072
            if ain >= 0 and ain < 33 and bin >= 0 and bin < 33:
                j += 1
                newalf = razlich.zam(newalf, i[0], i[2])  # новый алфавит (две буквы поменяны)

                newmes = razlich.rashr(shifr_book, newalf)  # заново расшифровываем
                print(str(j)+' букв введено')
    if(ret):
        return(newmes)
    else:
        print(newmes)
        pass