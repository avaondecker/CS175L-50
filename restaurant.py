#CS175L
#Ava Ondecker
#restaurant

vegetarian = input("Is anyone in your party a vegetarian? ")

if vegetarian == "yes" or vegetarian == "no":
    
    vegan = input("Is anyone in your party a vegan? ")
    

    if vegan == "yes" or vegan == "no":
        
        glutenFree = input("Is anyone in your party gluten-free? ")
        

        if glutenFree == "yes" or glutenFree == "no":
            print("\nHere are your restaurant choices:\n")

            if vegetarian == "yes":
                
                if vegan == "yes":

                    if glutenFree == "yes" or glutenFree == "no":
                        print("Corner Cafe\n" + \
                              "The Chef's Kitchen\n")
                else:
                    
                    if glutenFree == "yes":
                        print("Main Street Pizza Company\n" + \
                              "Corner Cafe\n" + \
                              "The Chef's Kitchen\n")
                    else:
                        print("Main Street Pizza Company\n" + \
                              "Corner Cafe\n" + \
                              "Mama's Fine Italian\n" + \
                              "The Chef's Kitchen\n")
            else: # vegetarian == "no"

                if vegan == "yes":

                    if glutenFree == "yes" or gluten_free == "no":
                        print("Corner Cafe\nThe Chef's Kitchen\n")

                else: # vegan == "no"

                    if glutenFree == "yes":
                      print("Main Street Pizza Company\n" + \
                            "Corner Cafe\n" + \
                            "The Chef's Kitchen\n")
                                   
                    else: # glutenFree == "no"
                        print("Joe's Gourmet Burgers\n" + \
                              "Main Street Pizza Company\n" + \
                              "Corner Cafe\n" + \
                              "Mama's Fine Italian\n" + \
                              "The Chef's Kitchen\n")

        
