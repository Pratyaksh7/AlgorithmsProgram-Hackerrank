def gradingStudents(grades):
   
   for i in grades:
       #checking if grades are greater than or equal to 38
       if i >= 38:
           num = i          #assigning num = 73
           i = i+ (5-(i%5))  # i = 73+ (5-(73%5)) = 73 + (5-3) = 75
           if i-num >= 3:    #if 75-73 >= 3 is true then print 73 
               print(num)
           else:
               print(i)
       else:
           # if grades are lesser than 38
           print(i)
        
                
n = int(input())

grades = []
for i in range(n):
    grades.append(int(input()))
    
gradingStudents(grades)
    