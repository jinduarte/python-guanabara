# Create a simple message chat with Python

import os

messages = []
name = input('Nome: ') #Name

while True:
    
    os.system('cls') #Clearning terminal

    if len(messages) > 0:
        for m in messages:
            print(m['nome'], '-', m['texto']) #name - text

    print('_________________')

    text = input('mensagem: ') #message
    if text == 'fim': #end
        break

    messages.append({
                     'nome': name,
                     'texto': text
    })