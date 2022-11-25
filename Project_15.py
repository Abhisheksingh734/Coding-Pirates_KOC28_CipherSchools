#Project 15:
# In this project you have to enter a positive integer range [A, B] and system will find out the status (Prime or composite) of each number available in the given range. At the end print the count also.
# Note: Make use of efficient approach to check prime status of the number.
# For example:
# Range is (7,10) 
# Then the status of each number in the range is:
# 7 is prime
# 8 is composite or not prime
# 9 is composite
# 10 is composite
# Count: 1 prime and 3 composite numbers in the range.


A=int(input("Enter the starting range: "))
B=int(input("Enter the ending range: "))

# prime=None
countPrime=0
countComposite=0
for i in range(A,B+1):
    if i==1:
        print("1 is neither Prime nor Composite")
        continue
    if i==2:
        print("2 is Prime")
        countPrime+=1
        continue
    for j in range(2,i):
        if i%j!=0:
            prime=True
        else:
            prime=False
            break
    if prime:
        print(f"{i} is Prime")
        countPrime+=1
    else:
        print(f"{i} is Composite")
        countComposite+=1

print(f"Result : {countPrime} Prime and {countComposite} Composite numbers are in the range")

