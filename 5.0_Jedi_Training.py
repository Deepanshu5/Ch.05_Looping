  #Sign your name:________________

'''
 1. Make the following program work.
   '''  
     print("This program takes three numbers and returns the sum.")
     total = 0

     for i in range(3):
         x = input("Enter a number: ")
         total = total + i
     print("The total is:", x)
  


'''
  2. Write a Python program that will use a FOR loop to print the even
     numbers from 2 to 100, inclusive.
'''
for i in range(2,101):
  if i%2==0:
    print(i,end=" ")




'''
  3. Write a program that will use a WHILE loop to count from
     10 down to, and including, 0. Then print the words Blast off! Remember, use
     a WHILE loop, don't use a FOR loop.
'''
i=10
while i!=-1:
    print(i)
    i-=1
print("Blast off!")





'''
  4. Write a program that prints a random integer from 1 to 10 (inclusive).
'''
import random
a=random.randint(1,10)
print(a)






'''
  5. Write a Python program that will:
     
     * Ask the user for seven numbers
     * Print the total sum of the numbers
     * Print the count of the positive entries, the count of entries equal to zero,
     and the count of negative entries. Use an if, elif, else chain, not just three
     if statements.
      
'''
print("Input seven numbers")
total_sum=0
positive_count=0
negative_count=0
zero_count=0
for i in range(7):
    a=int(input())
    total_sum+=a
    if a>0:
        positive_count+=1
    elif a<0:
        negative_count+=1
    else:
        zero_count+=1
print(f"Total sum of numbers is {total_sum}")
print(f"Total positive numbers are {positive_count}")
print(f"Total negative numbers are {negative_count}")
print(f"Total zeroes are {zero_count}")
