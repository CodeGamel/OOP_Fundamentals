class Event:
        def __init__(self, name, date):
            self.name = name
            self.date = date
            self.people = 0
        
        def add_people(self, people):
           num= 30
           num = int(num)
           self.people += num
            
        def get_people_count(self):
            return self.people
        
Affair = Event('Comic-Con', 'August 8th, 2024')

print("uh oh more people are coming")
Affair.add_people(1)
print(Affair.get_people_count())
Affair.add_people(1)
print(Affair.get_people_count())
Affair.add_people(2)
Affair.add_people(1)
Affair.get_people_count()
print("So many weebs coming in jesus hold on to something")
Affair.add_people(5)
Affair.add_people(30)
print(Affair.get_people_count())
Affair.add_people(40)
Affair.add_people(5)
Affair.add_people(5)
print(Affair.get_people_count())
Affair.add_people(3)
Affair.add_people(5)
print("Oh lord they stink so bad")
print(Affair.get_people_count())

