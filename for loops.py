n = int(input("Enter a number:"))
for i in range(1,n+1):
  print(i)  #from 1 to N
  
num = int(input("Enter a number:"))
for i in range(1,11):
  print(num,"x",i,"=",num*i) #multiplication table 

n = int(input("Enter a number:"))
total = 0
for i in range(1,n+1):
  total+=i
  print("Sum is:",total ) #sum of first N numbers

n = int(input("Enter a number:"))
for i in range(1,n+1):
  if i%2==0:
    print(i) #even numbers
