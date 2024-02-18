continueg=True
while continueg==True:
    complete=False
    while not complete:
        greenveg=input("Is the vegetable green? Y/N: ")
        if greenveg.lower()=="y":
            treeveg=input("Does the vegetable look like a tree? Y/N: ")
            if treeveg.lower()=="y":
                print("It must be broccoli!")
                complete=True
                cotinueg=input("Do you want to continue Y/N: ")
                if continueg.lower()=="n":
                    continueg=False
            elif treeveg.lower()=="n":
                print("It must be peas!")
                complete=True
                cotinueg=input("Do you want to continue Y/N: ")
                if continueg.lower()=="n":
                    continueg=False
            else:
                print("input cannot be recognised")
        elif greenveg.lower()=="n":
            orangeveg=input("Is it an orange? Y/N: ")
            if orangeveg.lower()=="y":
                print("It must be Sweetcorn!")
                cotinueg=input("Do you want to continue Y/N: ")
                if continueg.lower()=="n":
                    continueg=False
                complete=True
            elif orangeveg.lower()=="n":
                print("It must be a carrot!")
                complete=True
                cotinueg=input("Do you want to continue Y/N: ")
                if continueg.lower()=="n":
                    continueg=False
            else:
                print("Input cannot be recognised")
        else:
            print("input cannot be recognised")