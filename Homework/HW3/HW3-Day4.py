
import numpy as np
import pandas as pd

g1 = np.random.randint(10,size = 4)
g2 = np.random.randint(10,size = 4)
g3 = np.random.randint(10,size = 4)
g4 = np.random.randint(10,size = 4)
g5 = np.random.randint(10,size = 4)

s1 = input("Enter the name of the first student: ")
s2 = input("Enter the name of the second student: ")
s3 = input("Enter the name of the third student: ")
s4 = input("Enter the name of the fourth student: ")
s5 = input("Enter the name of the fifth student: ")

g1[0] = input("Enter the midterm grade of the first sudent: ")
g2[0] = input("Enter the midterm grade of the second sudent: ")
g3[0] = input("Enter the midterm grade of the third sudent: ")
g4[0] = input("Enter the midterm grade of the fourth sudent: ")
g5[0] = input("Enter the midterm grade of the fifth sudent: ")

g1[1] = input("Enter the project grade of the first sudent: ")
g2[1] = input("Enter the project grade of the second sudent: ")
g3[1] = input("Enter the project grade of the third sudent: ")
g4[1] = input("Enter the project grade of the fourth sudent: ")
g5[1] = input("Enter the project grade of the fifth sudent: ")

g1[2] = input("Enter the final grade of the first sudent: ")
g2[2] = input("Enter the final grade of the second sudent: ")
g3[2] = input("Enter the final grade of the third sudent: ")
g4[2] = input("Enter the final grade of the fourth sudent: ")
g5[2] = input("Enter the final grade of the fifth sudent: ")

g1[3] = g1[0]*0.3 + g1[1]*0.3 +g1[2]*0.4
g2[3] = g2[0]*0.3 + g2[1]*0.3 +g2[2]*0.4
g3[3] = g3[0]*0.3 + g3[1]*0.3 +g3[2]*0.4
g4[3] = g4[0]*0.3 + g4[1]*0.3 +g4[2]*0.4
g5[3] = g5[0]*0.3 + g5[1]*0.3 +g5[2]*0.4


d = {s1:g1,s2:g2,s3:g3,s4:g4,s5:g5}
passingGrade = [g1[3],g2[3],g3[3],g4[3],g5[3]]
 
d_table = pd.DataFrame(d)
print(d_table)
