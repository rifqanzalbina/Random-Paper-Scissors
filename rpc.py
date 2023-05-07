import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock,paper,scissors]

user_choice = int(input("Apa yang kamu pilih? Ketik 0 Untuk Batu, 1 Untuk Kertas atau 2 untuk Gunting : "))
if user_choice >= 3 or user_choice < 0:
    print("Kamu mengetik sebuah angka yang tidak jelas, Kamu kalah !!")
else:
    print(game_images[user_choice])
    computer_choice = random.randint(0,2)
    print("Computer Memilih : ")
    print(game_images[computer_choice])


    if user_choice == 0 and computer_choice == 2:
        print("Kamu menang \n")
    elif computer_choice == 0 and user_choice == 2:
        print("Kamu kalah \n")
    elif computer_choice > user_choice:
        print("Kamu kalah \n")
    elif user_choice > computer_choice:
        print("Kamu menang!\n")
    elif computer_choice == user_choice:
        print("Ini seri / seimbang")