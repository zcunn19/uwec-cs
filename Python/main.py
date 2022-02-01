def printLines(context):
    print(f"--------------------------------------\n{context}\n--------------------------------------")
    
def printLargeLines(context):
    print(f"---------------------------------------------------------------------------------------------------\n{context}\n---------------------------------------------------------------------------------------------------")

printLargeLines("Minecraft Server RAM Calculator - https://github.com/alyamr2006/ram-calculator")
    
def main():
    ram = 0
    jar = "vanilla"
    while True:
        try:
            print("What Minecraft Version would your server be running? E.g. 1.8.8, 1.17.1")
            version = int(str(input("Answer: ")).split(".")[1])
            if version in list(range(8,18)):
                break
            else:
                printLines("Please enter a valid Minecraft version")
        except ValueError:
            printLines("Please enter a valid Minecraft version")
    if version in list(range(8,14)):
        while True:
            try:
                print("What JAR type will your server be running? vanilla, spigot, paper, forge")
                jar = str(input("Answer: ").lower())
                if jar in ['vanilla', 'spigot', 'paper', 'forge']:
                    break
                else:
                    printLines("Please enter a valid JAR type")
            except ValueError:
                printLines("Please enter a valid JAR type")

    else:
        while True:
            try:
                print("What JAR type will your server be running? vanilla, spigot, paper, purpur, forge")
                jar = str(input("Answer: ").lower())
                if jar in ['vanilla', 'spigot', 'paper', 'purpur', 'forge']:
                    break
                else:
                    printLines("Please enter a valid JAR type")
            except ValueError:
                printLines("Please enter a valid JAR type")

    while True:
        try:
            print("How many players maximum would be on the server at once?")
            players = int(input("Answer: "))
            if players > 0:
                break
            else:
                printLines("Please enter an integer")
        except ValueError:
            printLines("Please enter an integer")

    if not jar in ["vanilla", "forge"]:
        while True:
            try:
                print("How many plugins would your server be using?")
                plugins = int(input("Answer: "))
                if plugins > 0:
                    break
                else:
                    printLines("Please enter an integer")
            except ValueError:
                printLines("Please enter an integer")

        while True:
            try:
                print("Are you going to be using any resource intensive plugins on your server? (yes/no)")
                weight = str(input("Answer: ").lower())
                if weight in ['yes', 'no']:
                    break
                else:
                    printLines("Please enter yes or no")
            except ValueError:
                printLines("Please enter yes or no")
    if jar == "forge":
        weight = "no"
        while True:
            try:
                print("How many mods would your server be using?")
                mods = int(input("Answer: "))
                if mods > 0:
                    break
                else:
                    printLines("Please enter an integer")
            except ValueError:
                printLines("Please enter an integer")

    if jar in ['vanilla', 'spigot']:
        if players >= 20:
            ram += 2
            
    else:
        ram += 2

    if not version in list(range(8,13)):
        ram += 3

    if players < 20:
        ram += 1
    elif 20 <= players < 40:
        ram += 2
    elif 40 <= players < 70:
        ram += 3
    elif 70 <= players < 100:
        ram += 5
    elif 100 <= players < 140:
        ram += 6
    elif 140 <= players < 180:
        ram += 8
    elif 180 <= players <= 220:
        ram += 10
    elif players > 220:
        ram += 14

    if jar != "vanilla":
        if jar == "forge":
            plugins = mods
        if weight == "yes":
            ram += 1
        if 40 < plugins < 50:
            ram += 1
        elif 50 <= plugins < 70:
            ram += 2
        elif 70 <= plugins < 90:
            ram += 3
        elif 90 <= plugins < 110:
            ram += 4
        elif 110 <= plugins < 160:
            ram += 5
        elif 160 <= plugins <= 200:
            ram += 6
        elif plugins > 200:
            ram += 8

    print("\033c")
    printLargeLines(f"Approximately, your server will need {ram}GB allocated. Please note this tool is not 100% accurate.")

    

while True:
    main()
    repeat = str(input("Restart? (yes/no) ").lower())
    if repeat != 'yes':
        printLargeLines("Thanks for using this tool, made by aly#1992\nYou can view the other generous contributors here:\nhttps://github.com/alyamr2006/ram-calculator")
        break
