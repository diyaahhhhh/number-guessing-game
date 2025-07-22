from colorama import Fore, Style
import time
print(Fore.LIGHTMAGENTA_EX + """
╔════════════════════════════════════════╗
║ 🎲 WELCOME TO NUMBER GUESSING GAME 🎲  ║
╚════════════════════════════════════════╝
""" + Style.RESET_ALL)

time.sleep(1.5)  # Pause for dramatic effect
print(Fore.CYAN + "✨ Guess the number and test your luck! ✨" + Style.RESET_ALL)
time.sleep(1)
import random
num=random.randint(1,10)
count=0
while True:
      ip = int(input(Fore.CYAN + "Guess your input:" + Style.RESET_ALL))
      if num==ip:
         print(Fore.GREEN+"Hurray!🎉 You guessed correctly in",count,"attempts!"+Style.RESET_ALL)
         break
      elif ip<num:
         print(Fore.BLUE+"📉Too low. Try again!"+Style.RESET_ALL)
         count+=1
      else:
         print(Fore.RED+"📈Too high. Try again!"+Style.RESET_ALL)
         count+=1
