
"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Jana Veselá
email: janca.vesela90@gmail.com
"""
#vypiš registrované uživatele
registrovany_uzivatel = ['bob', 'ann', 'mike', 'liz']
#vypis hesla
password = ['123', 'pass123', 'password123', 'pass123']
user = registrovany_uzivatel
#přiřaď user k password
user = {
    "bob":"123",
    "ann":"pass123",
    "mike":"password123",
    "liz":"pass123"
}
#zjisti jestli zadané údaje odpovídají někomu z registrovaných
jmeno = user
input("ussername:")
{"jmeno":"user"}
heslo = password
input("password:")
{"heslo":"password"}
if jmeno.get("registrovany_uzivatel") == password:
    print("Welcome to the app",
    "We have 3 texts to be analyzed")
else:
    print("unregistered user, terminating the program.")
#text obsahujici 3. texty
text_1 = ['''Situated about 10 miles west of Kemmerer 
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley.''']
text_2 = ['''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''']
text_3 = ['''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.''']
texts = [text_1], [text_2], [text_3]
input("Enter a number btw. 1 and 3 to select text:")
{"texts":"texts"}
cislo = [1, 2, 3]
if cislo in texts:
    print("We go analyzed")
else:
    print("is not in our tex, close")