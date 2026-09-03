class Computer:
    def config(self):
        print("i5, 16gb, 1TB.")

com1 = Computer()
com2 = Computer()

Computer.config(com1)  #output: i5, 16gb, 1TB. We can call config using the "object".
Computer.config(com2)  #output: i5, 16gb, 1TB.

com1.config()  #output: i5, 16gb, 1TB. We can call with help of "class" by passing the "object" as an argument.
com2.config()  #output: i5, 16gb, 1TB.

a = 5
print(a.bit_length())  #output: 3