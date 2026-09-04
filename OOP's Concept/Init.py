class Computer:
    def __init__(self,cpu,ram):
        print("This is a Computer class constructor.")
        
        
com1 = Computer("i5, 16") # com1 is an Object for class.
com2 = Computer("Ryzen, 32") # com2 is an Object for class.

com1.__init__()
com2.__init__()