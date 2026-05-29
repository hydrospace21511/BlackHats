# while True :

#     Attack = input("Choose an attack: ")

#     if Attack in Player.Class.Attacks:

#         if Attack in ["Internal Access"]: 
#             Player.Class.Defense += Player.Class.Attacks[Attack][0]
#             print(f"Defense increased to {Player.Class.Defense}%.")

#         elif Attack in ["baiting"]:
#             Player.Class.Defense += Player.Class.Attacks[Attack][0]
#             Player.Class.Regen += Player.Class.Attacks[Attack][1]
#             print(f"Defense increased to {Player.Class.Defense}%.")
#             print(f"Regen increased to {Player.Class.Regen}.")

#         elif Attack in ["Firewall"]:
#             Player.Class.Defense += Player.Class.Attacks[Attack]
#             print(f"Defense increased to {Player.Class.Defense}%.")
#             print(Player.Class.Defense)

#         elif Attack in ["Security Patch"] or Attack in ["God's Wrath"]:
#             Player.Class.Regen += Player.Class.Attacks[Attack]
#             print(f"Regen increased to {Player.Class.Regen}.")

#         else:
#             print(Player.Class.Integrity)
#             final_damage = Damage(Player.Class.Attacks[Attack], Player.Class.Defense)
#             Player.Class.Integrity -= final_damage
#             print(f"Integrity left after the attack '{Attack}': {Player.Class.Integrity:.1f}")

#         if Player.Class.Regen > 0:
#             Player.Class.Integrity += Player.Class.Regen
#             print(f"Integrity regenerated to {Player.Class.Integrity}.")  

#         if Player.Class.Integrity <= 0:
#             print("\n           Error 404 \n < -- You have been hacked. -- >\n")
#             break
#     else:
#         print("Invalid attack, please choose a valid attack from the list.")