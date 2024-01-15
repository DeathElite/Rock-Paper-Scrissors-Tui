import random
import time
from rich.console import Console
from rich.text import Text
from rich.table import Table

console = Console()

global users_weapon
users_weapon = "0"

global weapon_choose
weapon_choose = "0"

weapon_table = Table(title="Weapomd Table")

weapon_table.add_column("weapon")
weapon_table.add_column("number")

weapon_table.add_row("rock", "1")
weapon_table.add_row("paper", "2")
weapon_table.add_row("scissors", "3")

console.print(weapon_table)

def start():
    user_choose_weapon()
    print("rock")
    time.sleep(1)
    print("paper")
    time.sleep(1)
    print("scissors")
    time.sleep(1)
    print("shoot")
    time.sleep(0.5)
    comp_choose_weapon()
    play()

def user_choose_weapon():
    users_weapon = input("Choose your weapon: ")
    check_usr_weapon()

def check_usr_weapon():
    if users_weapon == "1":
        print("you choose rock")
    if users_weapon == "2":
        print("you chose paper")
    if users_weapon == "3":
        print("you chose scissors")

def comp_choose_weapon():
    weapon_choose = random.randint(1, 3)
    if weapon_choose == 1:
        print("rock")
    if weapon_choose == 2:
        print("paper")
    if weapon_choose == 3:
        print("scissors")

def play():
    if users_weapon == "1" and weapon_choose == 1:
        print("tie")
    if users_weapon == "1" and weapon_choose == 2:
        print("computer wins!")
    if users_weapon == "1" and weapon_choose == 3:
        print("user wins!")

start()
