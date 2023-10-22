
for i in range(1,4):
    non_client=input("entre le nom du client :")
    y = int(input("svp done le nobre darticle:"))
    t=0
    for j in range(1,y+1):
        prix= int(input("svp done le prix des articles:"))
        tva=(prix*0.15)
        ttc=((prix+tva)-((prix+tva)*0.02))
        print("le prix sons taxe",prix,"le tva",tva)
        s =ttc
        print("le prix total ",s)
        t+=s
    print("le prix total est : ", t)






