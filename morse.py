def morse():
    
    morse = {' ':'',
             'a':'.-',
             'b':'-...',
             'c':'-.-.',
             'd':'-..',
             'e':'.',
             'f':'..-.',
             'g':'--.',
             'h':'....',
             'i':'..',
             'j':'.---',
             'k':'-.-',
             'l':'.-..',
             'm':'--',
             'n':'-.',
             'o':'---',
             'p':'.--.',
             'q':'--.-',
             'r':'.-.',
             's':'...',
             't':'-',
             'u':'..-',
             'v':'...-',
             'w':'.--',
             'x':'-..-',
             'y':'-.--',
             'z':'--..',
             '1':'.----',
             '2':'..---',
             '3':'...--',
             '4':'....-',
             '5':'.....',
             '6':'-....',
             '7':'--...',
             '8':'---..',
             '9':'----.',
             '0':'------'}

    print('|0 - Alfanumérico -> Morse, 1 - Morse -> Alfanumérico |')
    i = int(input('Digite 0 ou 1: '))
    
    resposta = ''
    

    if i == 0:
        msg = input('Insira sua mensagem em Alfanumérico: ')
        for letra in msg: 
            resposta += morse.get(letra) + ' '

        resposta = resposta[:-1]
        
    if i == 1:
        msg = input('Insira sua mensagem em Morse: ')
        lista_msg = msg.split(' ')

        for item in lista_msg:        
            for chave, valor in morse.items():
                if valor == item:
                    resposta += chave
 
    return resposta







