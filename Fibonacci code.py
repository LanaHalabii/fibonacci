number = int(input("Enter a number"))

fst_fib = 0 
snd_fib = 1
print("The first fibonacci numbers are 0 and 1, the rest are:")

for i in range (number):
    next_number = fst_fib + snd_fib 
    fst_fib = snd_fib
    snd_fib = next_number 
    

    print(next_number)
    