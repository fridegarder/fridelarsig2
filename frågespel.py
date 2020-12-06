q1 = "vilket berg var det största innan man upptäckte mounteverest"
a1 = "mounteverest"
poäng = 0

svar = input (q1)

if a1 == svar :
    print("rätt svar")
    poäng = 1
else :
    print("fel svar")
    poäng = 0


print("du har " + str (poäng) + " poäng" )


q2 = "hur många kusiner har jag? "
a2 = "12"
svar = input (q2)

if a2 == svar :
    print("rätt svar")
    poäng = poäng + 1
else :
    print("fel svar")
print("du har " + str (poäng) + " poäng" )



q3 = "vad är summan av mina kusiners åldrar?"
a3 = 20 + 18 + 13 + 12 + 1 + 19 + 24 + 20 + 5
svar = int(input(q3))

if a3 == svar :
    print("exakt rätt svar!")
    poäng = poäng + 2
elif svar <= a3+3 and svar >= a3-3:
    print("nästan rätt. Rätt svar är " + str(a3))
    poäng = poäng + 1
else:
    print("fel svar")


print("du har " + str (poäng) + "poäng " )


























