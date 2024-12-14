class Bharath:
    def init(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def display(self):
        print(self.name)
        print(self.age)
        print(self.gender)
b1=Bharath("bharath",21,"male")
#b.display("bharath",20,"male")
b1.display()