''' Program using for loop, continue and break'''
# import random

# generated_num = random.randint(1,100)

# for i in range(3) :
#     ip = int(input("Enter a Number between 1 to 100:"))

#     if ip>generated_num:
#         print("Your Guss is too High!!!")
#         continue
#     elif ip<generated_num:
#         print("Your Guss is too Low!!!")
#         continue
#     else:
#         print("Your Guss is Correct!!!")
#         break
    
# else:
#     print(f"Ran Out of attempt the correct number is :{generated_num}")

#-----------------------------------------------------------------------------------------------------------------------

# student_info = {
#     'Student_1':{'Name' : 'Hari','Roll_No' : 1,
#                  'Subject' : {
#                     'Sub_1' : 'Python',
#                     'Sub_2' : 'DBMS'
#                  }},
#     'Student_2':{'Name' : 'Jeeva','Roll_No' : 2,
#                  'Subject' : {
#                     'Sub_1' : 'Java',
#                     'Sub_2' : 'Web Dev'
#                  }},
#     'Student_3':{'Name' : 'Prasath','Roll_No' :3,
#                  'Subject' : {
#                     'Sub_1' : 'C',
#                     'Sub_2' : 'Ethicl Hacking'
#                  }}
#     }

# student_info['Student_4'] = {}
# student_info['Student_4']['Name'] = 'Abinesh'
# student_info['Student_4']['Roll_No'] = 4
# student_info['Student_4']['Subject'] = {'Sub_1' : 'Ruby','Sub_2' : 'Frontend','Sub_3' : 'JS'}

# print(student_info['Student_4'])
# del student_info['Student_4']['Subject']['Sub_3']
# print(student_info['Student_4'])

# for s_id,s_info in student_info.items():
#     print("\n",s_id)
#     for key in s_info:
#         print(key + ':',s_info[key])

#-----------------------------------------------------------------------------------------------------------------------

myName = set('HARI')
myName.add('HARI')
print(myName)
myName.remove('HARI')
print(myName)
myName.pop()
print(myName)
