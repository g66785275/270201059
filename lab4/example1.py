
#giriş = input("Number:")
#if len(giriş)>1:
 # print("Sum of last digits:",int(giriş[-1]) + int(giriş[-2]))



number = int(input("Enter an integer:"))

ones = number % 10
tens = (number % 100) // 10
total = ones + tens
print(total)