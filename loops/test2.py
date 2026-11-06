def min(values):
    smallest = None
    for value in values:
        if smallest is None or value < smallest:
          smallest = value

        return smallest   


      
def max(values):
    biggest = None
    for value in values:
        if biggest is None or value > biggest:
          biggest = value

        return biggest  
