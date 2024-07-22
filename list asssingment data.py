data1=['id',     'name',     'age',  'hindi',      'english',  'math', 'science','computer']
data2=['ctr2234','manish',   '16 ',     '90',         '39',     '80',    '70' ,      '60']
data3=['ctr2235','rishi',    '15',    '50',          '77',     '66',    '80' ,      '70']
data4=['ctr3367','priyanshu','14',    '66',          '60',     '77',    '74' ,      '40']
data5=['ctr3367','naman',    '16',    '69',          '33',     '90',    '67' ,      '80']
data6=['ctr3367','prasoon',  '17',    '67',          '60',     '50',    '70' ,      '90']
data7=['ctr3367','navdeep',  '15',    '79',          '40',     '98',    '70' ,      '55']
data8=['ctr3367','shivamdra','14',    '69',          '70',     '86',    '40' ,      '50']
data9=['ctr3367','rishav',   '16',    '68',          '20',     '76',    '70' ,      '70']
data10=['ctr3367','kunal',   '15',    '59',          '70',     '85',    '40' ,      '89']

studentdata=[data1,data2,data3,data4,data5,data6,data7,data8,data9,data10] 
for row in studentdata:
  print(row)


      # question 1
# displaying nAME OF STUDENT whoes marks in english is greaater then 50


print("----------------")
print("name of student whoes marks in english is greaater then" )
for rowindex in range(1,len(studentdata)): 
 english=int(studentdata[rowindex][4])
 if(english>=50):
   print(studentdata[rowindex][1])






            #  question 2

math_scores = [int(i[5]) for i in studentdata[1:]]
names = [student[1] for student in studentdata[1:]]
sorted_scores = sorted(math_scores, reverse=True)
top_4_scores = sorted_scores[:4]
top_scorers_indices = [math_scores.index(score) for score in top_4_scores]
print("Top 4 Math Scorers:")
for index in top_scorers_indices:
  print(names[index])


#                   question 3
# print("display name , id and age of students who are bottom three scorer in computer : ")        https://github.com/manishvishhnoi05050/python.git

computer_scores = [int(student[7]) for student in studentdata[1:]]
names = [student[1] for student in studentdata[1:]]
ids = [student[0] for student in studentdata[1:]]
ages = [student[2] for student in studentdata[1:]]
# Sort the computer scores in ascending order (lowest first)
sorted_scores = sorted(computer_scores)
# Get the bottom 3 computer scores
bottom_3_scores = sorted_scores[:3]
# Find the indices of the bottom 3 scorers
bottom_3_scorers_indices = [computer_scores.index(score) for score in bottom_3_scores]
# Print the names, IDs, and ages of the bottom 3 scorers
for index in bottom_3_scorers_indices:
  print(f"Name: {names[index]}, ID: {ids[index]}, Age: {ages[index]}")






