n = int(input('no of records: '))
student_marks = {}
for i in range(n):
    name, *line = input('give the name: ').split() # * is used to take multiple inputs
    scores = list(map(float, line)) # it is to convert multiple string input into float
    student_marks[name] = scores # storing in dict
query_name = input('give the name u want percentage: ') 
avg=0
#print(student_marks)
for marks in student_marks[query_name]:
    avg=avg+marks
#avg=avg/len(scores) # instead of scores give len(student_marks[query_name])
#print(scores)
avg=avg/len(student_marks[query_name])
print("%.2f"%avg)# to convert float correct upto 2 decimal point
