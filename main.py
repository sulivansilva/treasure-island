print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Seja bem-vindo a ilha do tesouro!")
print("Sua missão é encontrar o tesouro!")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

escolha1 = input("Para qual lado você gostaria de ir? Digite '1' para esquerda ou '2' para direita: \n").lower()

if escolha1 == "1":
    escolha2 = input("Você chegou a um lago, há uma ilha no meio do lago. Gostaria de atravessar nadando ou esperar um bote? Digite '1' para nadar ou '2' para esperar: \n").lower()
    if escolha2 == "2":
        escolha3 = input("O bote chegou e te levou até a casa no meio da ilha. A casa tem três portas: Uma azul, uma amarela e outra vermelha. Qual porta você deseja abrir? Digite '1' para azul, '2' para amarela ou '3' para vermelha: \n").lower()         
        if escolha3 == "1":
            print("Você encontrou o tesouro!")
        elif escolha3 == "2":
            print("Havia um urso atrás da porta que te atacou, fim de jogo.")
        elif escolha3 == "3":
            print("Havia um leão atrás da porta que te atacou, fim de jogo.")
        else:
            print("Essa porta não existe, fim de jogo.")
    else:
        print("Você foi atacado por um cardume de piranhas, fim de jogo.")         
else:
    print("Você caiu em um buraco, fim de jogo.")