import random
import sys
import time
import faker
import random, string
from colorama import Fore
from faker import Faker
fake = Faker()

#getIP, getAddress, getName, sendPizza, getEmail

##########################################################################

randomIP1 = random.randint(1, 255)
randomIP2 = random.randint(1, 255)
randomIP3 = random.randint(1, 255)
randomIP4 = random.randint(1, 255)
class getIP(object):
    def __init__(self, discordUser):
        print(f"{Fore.GREEN}{randomIP1}.{randomIP2}.{randomIP3}.{randomIP4}\n")

##########################################################################

class getAddress(object):
        def __init__(self, discordUser):
            raddress = fake.address()
            print(f'{Fore.GREEN}{raddress}\n')

##########################################################################

class getName(object):
            def __init__(self, discordUser):
                fakename = fake.name()
                print(f"{Fore.GREEN}{fakename}\n")

##########################################################################

class sendPizza(object):
    def __init__(self, discordUser, amount):
        print(f"{Fore.GREEN}Getting the user's address...")
        time.sleep(3)
        print(f"{Fore.GREEN}Sending pizza...")
        time.sleep(random.randint(2, 6))
        print(f"{Fore.GREEN}Sent pizza.\n")

##########################################################################

def random_char(char_num):
       return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))
email = random_char(10)+"@gmail.com"

class getEmail(object):
    def __init__(self, discordUser):
        print(f"{Fore.GREEN}{email}")

##########################################################################

