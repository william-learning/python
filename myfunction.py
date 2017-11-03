def minutes_to_hours(minutes):
    hours = minutes / 60.0      # float needed for Python 2
    return hours 
    
def seconds_to_hours(seconds):
    hours = seconds / 3600.0      # float needed for Python 2
    return hours 
    
print(type(minutes_to_hours(70)))    

def minutes_to_hours2(seconds, minutes=70):
    hours = minutes/60.0 + seconds/3600.0
    return hours
    
print(minutes_to_hours2(300, 200))