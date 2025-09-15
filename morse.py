import codigos

def morse():
    resposta = ""

    print("> Bem vindo ao (De)codificador!")
    print(">")
    print("> 0 - Alfanumérico -> Morse")
    print("> 1 - Morse -> Alfanumérico")
    print(">")

    i = int(input("> Digite 0 ou 1: "))
    
    if i == 0:
        msg = input("> Insira sua mensagem em Alfanumérico: ")
        for letra in msg: 
            resposta += codigos.morse.get(letra) + " "

        resposta = resposta[:-1]
        
    elif i == 1:
        msg = input("> Insira sua mensagem em Morse: ")
        lista_msg = msg.split(" ")

        for item in lista_msg:        
            for chave, valor in codigos.morse.items():
                if valor == item:
                    resposta += chave
    else:
        return
 
    print(f"> {resposta}")

morse()







