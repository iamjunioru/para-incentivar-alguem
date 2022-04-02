# não veja o código, apenas execute :)
#       apenas,
#              execute. 
#
#
#
#
#
#
#         ,-,
#        /.(
#        \ {
#         `-`
#
#
#
#      apenas relaxe...
#      .             *        .     .       .
#             .     _     .     .            .       .
#    .     .   _  / |      .        .  *         _  .     .
#             | \_| |                           | | __
#          _ |     |                   _       | |/  |
#         | \      |      ____        | |     /  |    \
#        |  |     \    +/_\/_\+      | |    /   |     \
#     _/____\--...\___ \_||_/ ___...|__\-..|____\____/__
#          .     .      |_|__|_|         .       .
#      .    . .       _/ /__\ \_ .          .
#          .       .    .           .         .
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
from time import sleep

while True:
    description = input("você poderia descrever como você se sente em uma palavra?\nex: triste, feliz, cansado.\n- ")

    list_of_words = description.split()

    feelings_list = []
    encouragement_list = []
    counter = 0

    for each_word in list_of_words:

        if each_word == "triste":
            feelings_list.append("triste")
            encouragement_list.append("que amanhã será um dia melhor.")
            counter += 1
        if each_word == "feliz":
            feelings_list.append("feliz")
            encouragement_list.append("de continuar sorrindo.")
            counter += 1
        if each_word == "cansado":
            feelings_list.append("cansado")
            encouragement_list.append("você é mais forte do que pensa.")
            counter += 1

    if counter == 0:

        output = "eu não entendi, pode usar uma palavra diferente?"

    elif counter == 1:

        output = "parece que você está se sentindo bastante " + \
            feelings_list[0] + ". no entanto, lembre-se " + \
            encouragement_list[0] + " espero que você se sinta melhor :)"

    else:

        feelings = ""
        for i in range(len(feelings_list)-1):
            feelings += feelings_list[i] + ", "
        feelings += "e " + feelings_list[-1]

        encouragement = ""
        for j in range(len(encouragement_list)-1):
            encouragement += encouragement_list[i] + ", "
        encouragement += "e " + encouragement_list[-1]

        output = "parece que você está se sentindo bastante " + feelings + \
            ". por favor, lembre-se sempre " + encouragement + " espero que você se sinta melhor :)"

    print()
    print()
    print()
    sleep(3)
    print("hmmmm")
    sleep(1)
    print("...")
    sleep(1.5)
    print("você se sente " + feelings_list[0] + "?")
    sleep(2)
    print(output)
    sleep(10)
    print()
    print()
    print()