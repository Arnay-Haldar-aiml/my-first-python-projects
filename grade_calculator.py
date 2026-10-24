name=input("enter name of student")
num1=int(input("enter marks of icp"))
num2=int(input("enter marks of act"))
num3=int(input("enter marks of mmla"))
num4=int(input("enter marks of idpt"))
num5=int(input("enter marks of upm"))
total=num1+num2+num3+num4+num5
print("total=",total)
percentage=(total/500)*100
print("percentage=",percentage)
if(percentage>=90 and percentage<=100):
  print("grade : A")
elif(percentage>=80 and percentage<90):
  print("grade : B")
elif(percentage>=70 and percentage<80):
  print("grade : C")
elif(percentage>=60 and percentage<70):
  print("grade : D")
else:
  print("grade : F")
  
