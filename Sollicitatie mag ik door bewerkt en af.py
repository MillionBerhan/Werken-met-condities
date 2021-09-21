
print("Vacature: Circusdirecteur voor Circus HotelDeBotel")

acrobatiek = int(input("hoeveel jaar heeft u ervaring met acrobatiek?"))
jongleren = int(input("Hoeveel jaar heeft u ervaring met Jongleren?"))
diploma = input("Bent u in het bezit van een Diploma MBO-4 ondernemen?ja/nee")
hoed = input("Bent u in het bezit van een hoge hoed?ja/nee")
man = int(input("Heeft u als man een snor? Zo, ja van hoeveel cm?"))
vrouw = int(input("heeft u als vrouw rood krulhaar, zo ja van hoeveel cm?"))
lengte = int(input("Wat is uw lengte?"))
gewicht = int(input("Wat is uw lichaamsgewicht?"))
praktijkervaring = int(input("Hoeveel jaar praktijkervaring heeft u met dieren-dressuur?"))
certificaat = input("Bent u in het bezit van een certificaat {Overleven met gevaarlijk personeel?}ja/nee")
hobbys = input("heeft u nog hobby's?ja/nee")
toekomst = input("Wilt u kinderen?ja/nee")
partner = input("Heeft u een partner?ja/nee")
clown = input("Houd u ervan om graag de clown uit te hangen?ja/nee")


if acrobatiek>=3:
    print("hoeveel jaar ervaring heeft u met jongleren?")
else:
    print("U bent helaas niet gekwalificeerd voor deze functie, wij wensen u namens Circus HoteldeBotel heel veel succes bij eventuele andere functies!")

if jongleren>=5:
    print("Bent u in het bezit van een MBO-4 diploma ondernemen?")
else:
    print("U bent helaas niet gekwalificeerd voor deze functie, wij wensen u namens Circus HoteldeBotel heel veel succes bij eventuele andere functies!")

if diploma == "ja":
    print("Bent u in het bezit van een hoge hoed?")
else:
    print("U bent helaas niet gekwalificeerd voor deze functie, wij wensen u namens Circus HoteldeBotel heel veel succes bij eventuele andere functies!.")

if hoed == "ja":
    print("Heeft u als man een snor? Zo, ja van hoeveel cm?")
else:
    print("u bent helaas niet gekwalificeerd voor deze functie,wij wensen u namens Circus HotelDeBotel heel veel succes bij eventuele andere functies!")

if man>=10:
    print("heeft u als vrouw rood krulhaar, zo ja van hoeveel cm?")
else:
    print("U bent helaas niet gekwalificeerd voor deze functie, wij wensen u namens Circus HotelDeBotel heel veel succes bij eventuele andere functies!")

if vrouw>=20:
    print("Wat is uw lichaamsgewicht?")
else:
    print("U bent helaas niet gekwalificeerd voor deze functie, wij wensen u namens Circus HotelDeBotel heel veel succes bij eventuele andere functies!")
        
if gewicht>=90:
    print("Hoeveel jaar praktijkervaring heeft u met dieren-dressuur?")
else:
    print("U bent helaas niet gekwalificeerd voor deze functie, wij wensen u namens Circus HotelDeBotel heel veel succes bij eventuele andere functies!")
        
if praktijkervaring>=4:
    print("Bent u in het bezit van een certificaat {Overleven met gevaarlijk personeel}?")
else:
    print("U bent helaas niet gekwalificeerd voor deze functie, wij wensen u namens Circus HotelDeBotel heel veel succes bij eventuele andere functies!")

if certificaat == "ja":
    print("heeft u nog andere hobby's?")
else:
    print ("U bent helaas niet gekwalificeerd voor deze functie, wij wensen u namens Circus HotelDeBotel heel veel succes bij eventuele andere functies!")
                 
if hobbys == "ja":
    print ("Wilt u kinderen?")
else:
    print("Wilt u kinderen?")

if toekomst == "ja":
    print ("Heeft u een partner?")
else:
    print("Heeft u een partner?")

if partner == "ja":
    print("Houd u ervan om graag de clown uit te hangen?")
else:
    print ("Houd u ervan om graag de clown uit te hangen?")

if clown == "ja":
    print("Bedankt voor het beantwoorden van de laatste vraag, u komt in aanmerking voor een de baan bij Circus HotelDeBotel!")
else:
    print("Bedankt voor het beantwoorden van de laatste vraag, u komt in aanmerking voor een de baan bij Circus HotelDeBotel!")
                                                


                                                       




