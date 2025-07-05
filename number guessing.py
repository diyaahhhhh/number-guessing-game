from colorama import Fore, Style
import random
print(Fore.MAGENTA + "🎲Welcome to the Number Guessing Game!"+Style.RESET_ALL)
num=random.randint(1,10)
while True:
      ip = int(input(Fore.CYAN + "Guess your input:" + Style.RESET_ALL))
      if num==ip:
         print(Fore.GREEN+"Hurray!🎉 You guessed correctly!"+Style.RESET_ALL)
         break
      elif ip<num:
         print(Fore.BLUE+"📉Oops! Too low. Try again."+Style.RESET_ALL)
      else:
         print(Fore.RED+"📈Oops! Too high. Try again."+Style.RESET_ALL)
