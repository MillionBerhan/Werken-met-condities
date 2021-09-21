invoer = str(input('is de kaas geel?'))
if invoer == "ja":
    invoer = str(input('zitten er gaten in?'))
    if invoer == "ja":
        invoer = str(input('Is de kaas belachelijk duur?'))
        if invoer == "ja":
            print("Emmenthaler")
        else: 
            print("Leerdammer")
    else:
        invoer = str(input('is de kaas hard als steen?'))
        if invoer == "ja":
            print ("Parmagiano Reggiano")
        else:
            print("Goudse kaas")
else:
    invoer = str(input('heeft de kaas blauwe schimmels?'))
    if invoer == "ja":
        print("De kaas heeft blauwe schimmels!")
    else: 
        print("De kaas heeft geen blauwe schimmels!")
        invoer = str(input('heeft de kaas een korst?'))
        if invoer == "nee":
            print("Foume d'Ambert")




    