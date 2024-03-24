name = input('please enter your name: ')
student_id = input('please enter your 8-digits id: ')
while len(student_id) != 8:
    print('student_id must be a 8-digits number')
    student_id = input('please try again: ')
    
if student_id[0] + student_id[1] == '93':
    print('{0} with the id: {1} '.format(name,student_id))
else:
    print('-')
