import time
print("#" * 40)
print("#" * 40)
print("############ADVENTURE GAME##############")
print("#" * 40)
print("#" * 40)
print("")

namn = input("vad ska karaktären heta?:")
time.sleep(1)
print("Det var sen midnatt. Det var den mörkaste dagen på året och vännerna ")
print(namn + ", Kim, Sofia och Kalle sov över med varandra.")
time.sleep(1)
print("Då fick Kim den briljanta idén att gå på en promenad. Så vi gick ut på en kvällspromenad fast det var kolsvart")
time.sleep(4)
print("- Vi går in i skogen. Det blir kul sa Kim.")
print(" Sofia var mörkrädd så hon sa: ")
print("- Aldrig i livet! Det kan finnas monster i skogen, det har jag läst i en bok faktiskt.")
time.sleep(2)
val = input("Vill du gå med in i skogen? (ja/nej) ")

if val == "nej":
    print("Du stannar hemma. Spelet slutar.")
    exit(1)

print("Vi gick in i skogen så långt så vi tappade bort oss i den mörka skogen.")
time.sleep(2)
print("vi komm till ett tempel")
val = input("vill du gå in itemplet? (ja/nej ")
if val == "nej":
    print("du stannar i skogen.")
    time.sleep(2)
    print("Helt plöteligt kommer en björn och äter upp dig. ")
    time.sleep(3)
    print(" GAME OVER.")
    time.sleep(3)






