field = ["",
         "1", "2", "3",
         "4", "5", "6",
         "7", "8", "9"]

def print_field():
    print(field[1] + "|" + field[2] + "|" + field[3])
    print(field[4] + "|" + field[5] + "|" + field[6])
    print(field[7] + "|" + field[8] + "|" + field[9])

def proof():
    if field[1] == field[2] == field[3]:
        return True
    if field[4] == field[5] == field[6]:
        return True
    if field[7] == field[8] == field[9]:
        return True
    if field[1] == field[4] == field[7]:
        return True
    if field[2] == field[5] == field[8]:
        return True
    if field[3] == field[6] == field[9]:
        return True
    if field[1] == field[5] == field[9]:
        return True
    if field[3] == field[5] == field[7]:
        return True

def check_draw():
    if field[1] != "1" and field[2] != "2" and  field[3] != "3"and field[4] != "4" and  field[5] != "5" and  field[6] != "6" and field[7] != "7" and  field[8] != "8" and field[9] != "9":
        return True

where = 0
active_player="O"
run = 1

while run < 2:

    if proof() == True:
        print(f"Spieler {active_player} hat gewonnen!!!!")
        run = 2

    if check_draw() == True:
        print("UNENTSCHIEDEN")
        run = 2

    if run < 2:
        fail=1

        while fail < 2:
         print("\n")
         print_field()
         where = int(input(f"\nWo möchtest du {active_player} platzieren: "))
         fail = 1

         if field[where] != "O" and field[where] != "X":1
         2
             field[where] = active_player

             if proof() == True:
                 print(f"Spieler {active_player} hat gewonnen!!!!")
                 run = 2
                 input('Press ENTER to exit')
                 break

             if check_draw() == True:
                 print("UNENTSCHIEDEN")
                 run = 2
                 break

             if active_player == "X":
                active_player = "O"

             elif active_player == "O":
                  active_player = "X"

             fail = 2
             run = 1
             break


         if field[where] == "O" or field[where] == "X":
          print("\n")
          print("Position ist nicht verfügbar!!")










