import time
import asyncio

name = None
choice = None
deter = 0

def print_letter_by_letter(string):
    for letter in string:
        print(letter, end="")
        time.sleep(0.5)
    print("\n")

def print2(string):
    for letter in string:
        print(letter, end="")
        time.sleep(0.03)
    print("\n")
    


def intro():
    print2("Welcome to the game! Please remember all your answers are case sensitive. Type them exactly as shown inside the parenthesis.")
    print2("You wake up slowly in your bed, the sun shining warmly through your window.")
    print2("Mochi is curled up next to you.")
    print2("After a big stretch and a yawn, you get out of bed, get dressed and walk to the bathroom.")
    print2("After staring at yourself in the mirror for a second, you ponder what the next step is.")
    print2("Do you (1), brush your teeth, then floss. (2), floss, then brush your teeth. Or (3) Neither.")
    choice = input("(1/2/3):")
    if choice == "1":
        print2("You brush your teeth till they shine a bright white then floss between each and every tooth.")
        print2("Even so, it feels a little incorrect.")
        leave()
    if choice == "2":
        print2("You floss between each and every tooth and brush your teeth till they shine a bright white.")
        print2("As this concludes, you feel your determination strengthen just a little bit. (FLOSS BEFORE BRUSHING!)")
        global deter
        deter += 1
        leave()
    if choice == "3":
        print2("You decide to disregard both options, living life as god intended. Oral hygene is overrated anyways.")
        leave()
def leave():
    print2("Soon after, you leave the bathroom, grab your pack, say goodbye to Mochi, and open the door to go explore your new neighborhood once more.")
    print_letter_by_letter("...")
    print2("You walk for a little while and find yourself back at the convinience store.")
    print2("This time, there's someone at the cash register.") 
    print2("It's a tired looking young man who seems to be staring off into space.")
    print2("You peruse the shelves, grab your green beverage, and head over to the cashier.")
    print2("He scans your beverage and in a lazy, monotone voice says 'Do you want a bag for that?'")
    choice = input("(Y/N):")
    if choice == "Y":
        print2("You squeak out a 'yes please!' and he puts your beverage in a flimsy plastic bag.")
        print2("'That'll be 3.87' he says and after you pay for your drink he hands the bag to you.")
        post_store()
    if choice == "N":
        print2("You squeak out a 'No thank you..' and he lets out a sigh.")
        print2("You pay for your drink and he hands you your beverage.")
        print2("It's cold to the touch.")
        post_store()
def post_store():
    print_letter_by_letter("...")
    print2("Happy with your purchase you start to leave the store when the cashier says 'Wait, aren't you new here?'")
    choice = input("(Y/N):")
    if choice == "Y":
        print2("'I thought so..'")
        print2("'Well uh, I've lived here all my life so if you ever need someone to talk to for advice or something, I'm your guy, yeah?'")
        print2("You reflect on what he said for a second and then a smile appears on your face.")
        print2("You've made a new friend.")
        print2("You feel your determination strengthen a little bit.")
        global deter
        deter += 1
        keep_walking()
    if choice == "N":
        print2("'Oh well then uh, nevermind.")
        print2("You feel a little weird about your decision but lying to strangers is always fun I guess.")
        keep_walking()
def keep_walking():
    print_letter_by_letter("...")
    print2("Having left the convinience store, you continue on your walk ")
    print2("The air is cold.")
    print2("Do you rub your hands together to create a little heat?")
    choice = input("(Y/N):")
    if choice == "Y":
        global deter
        deter += 1
        print2("It feels nice.")
        print2("You feel your determination strengthen just a little bit.")
    if choice == "N":
        print("You remain cold.")
    print_letter_by_letter("...")
    print2("After walking for a while you realize the air is getting even colder.")
    print_letter_by_letter("...")
    print2("And colder.")
    print_letter_by_letter("...")
    print2("It's.. almost unbearibly cold.")
    print_letter_by_letter("...")
    if deter >= 3:
        determination()
    if deter < 3:
        faliure()
def faliure():
    print2("You eventually realize that you can't feel your fingers.")
    print_letter_by_letter("...")
    print2("You realize that you can't feel your legs")
    print_letter_by_letter("...")
    print2("Eventually your body can't take it anymore and you pass out from the cold.")
    print_letter_by_letter("...")
    print2("You lack enough determination.")
    print_letter_by_letter("...")
    print2("GAME OVER.")
def determination():
    print2("You feel your as your body succumbs to the cold.")
    print_letter_by_letter("...")
    print2("Wait no..")
    print_letter_by_letter("...")
    print2("This isn't right..")
    print_letter_by_letter("...")
    print2("That's when you feel your inner soul burning within you.")
    print2("You feel..")
    print_letter_by_letter("DETERMINED")
    print2("Suddenly that suffocating cold is melted away in a bright flash of light.")
    print_letter_by_letter("...")
    print2("You stop to think for a second, puzzled by what just happened.
    print2("You hear what sounds like a child giggling.")
    print_letter_by_letter("...")
    print2("From the shadows emerges Mochi, who is now staring at you with cold, devilish eyes.")
    print2("'Maybe next time, human.'")
    print2("Mochi's eyes glow a bright red as he stares at you. You feel yourself getting sleepy.")
    print2("You try to fight it, but it's no use. You're falling asleep.")
    print_letter_by_letter("...")
    print2("'Sleep now, human. Sleep and dream of me.'")
    print_letter_by_letter("TO BE CONTINUED.")
    

if __name__ == "__main__":
  intro()

