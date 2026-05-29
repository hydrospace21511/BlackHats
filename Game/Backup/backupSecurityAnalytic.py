Integrity = 125
Defense = 0
Regen = 0

#ataques 
Attacks = {
    "Firewall": Defense + 30,
    "Security Patch": Regen + 30,
    "Weakness View": 30,
    "Punch": 50,
    "God's Hand": 50000000,
#    "God's Wrath": Regen + 100000000,
   "Pneumoultramicroscopicsilicovolcanoconiotic": 'ball cancer'
}

#calculadora de dano (com a defesa)(tenho medo da conta q faz)
def Damage(D, Defense) :
    return D * (1 - Defense / 100)
print("Available attacks:", list(Attacks.keys()))
#print(Attacks["Punch"])

while True :
    Attack = input("Choose an attack: ")

    if Attack in Attacks:

        if Attack in ["Firewall"]:
            Defense += Attacks[Attack]
            print(f"Defense increased to {Defense}%.")
            print(Defense)

        elif Attack in ["Security Patch"] or Attack in ["God's Wrath"]:
            Regen += Attacks[Attack]
            print(f"Regen increased to {Regen}.")

        else:
            print(Integrity)
            final_damage = Damage(Attacks[Attack], Defense) 
            Integrity -= final_damage
            print(f"Integrity left after the attack '{Attack}': {Integrity:.1f}")

        if Regen > 0:
            Integrity += Regen
            print(f"Integrity regenerated to {Integrity}.")  

        if Integrity <= 0:
            print("\n           Error 404 \n < -- You have been hacked. -- >\n")
            break
    else:
        print("Invalid attack, please choose a valid attack from the list.")


