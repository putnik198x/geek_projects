k = int(input("vvedite nomer meseatsa: "))
bbb = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "june", 7: "july", 8:"August", 9:"September", 10:"Octomber", 11:"Nov", 12:"december" }
print(bbb.get(k))
if k == 3 or k == 4 or k == 5:
    print("Spring")
elif k == 6 or k == 7 or k == 8:
    print("Summer")
elif k == 9 or k == 10 or k == 11:
    print("Autumn")
elif k == 12 or k ==1 or k ==2:
    print("Winter")
