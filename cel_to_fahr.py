def cel_to_fahr(C):
    if C < -273.15:
        print("That temperature doesn't make sense!")
    else:
        F = C * 9 / 5 + 32
        print(str(C) + " degrees C is " + str(F) + " Fahrenheit")
        
    
cel_to_fahr(-273.16)