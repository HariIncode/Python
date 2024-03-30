bike = ['Ducati','Jawa','HD','BMW','Pulsar']
car = ["Benz","Ferrari","Jaguar","BMW","Audi"]

print(dir(bike))

print(bike.sort())
print(bike)
bike.reverse()
print(bike)
bike.append("Royal Enfild")
print(bike)
bike.pop(-1)
print(bike)
print(bike.count("BMW"))
bike.insert(3,"Apache")
print(bike)
bike.remove("Apache")
print(bike)
bike.extend(car)
print(bike)
bike.clear()
print(bike)

department = ('CSE','IT','ECE','EEE','MECH')
print(dir(department))

Name = tuple('HARI')
print(Name)

print(department.count('CSE'))
print(Name.index('R'))
print(len(Name))
print(sorted(department))

emp = {'Hari' : 2201,'Jeeva' : 2705,'Prasath' : 2904,'Abinesh' : 3201} # Dictionary
print(emp['Jeeva'])

# emp_info = {
#     'emp1':
#         {'Name' : 'Hari',
#         'Id' : 2201},
#     'emp2':
#         {'Name' : 'Jeeva',
#         'Id' : 2705},
#     'emp3' :
#         {'Name' : 'Prasath',
#         'Id' : 2904},
#     'emp4' :
#         {'Name' : 'Abinesh',
#         'Id' : 3201}
# }       #Nested Dictionary

print(emp_info['emp1']['Name'])
print(emp.get('Jeeva'))
print(emp.items())
print(emp.keys())
print(emp.values())
print(emp.pop('Abinesh'))
print(emp.popitem())
print(emp.clear())

