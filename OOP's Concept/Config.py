class Computer:
    def config(self):
        print("i5, 16gb, 1TB.")

com1 = Computer()
com2 = Computer()

Computer.config(com1)  #output: i5, 16gb, 1TB.
Computer.config(com2)  #output: i5, 16gb, 1TB.

com1.config()  #output: i5, 16gb, 1TB.
com2.config()  #output: i5, 16gb, 1TB.