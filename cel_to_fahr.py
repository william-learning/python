def cel_to_fahr(C):
    if C < -273.15:
        return "That temperature doesn't make sense!"
    else:
        F = C * 9 / 5 + 32
        return F
   
temperatures = [10,-20,-289,100]
        
for c in temperatures:   
    print(cel_to_fahr(c))