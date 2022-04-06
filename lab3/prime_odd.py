# prime check
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
count = 0
for i in range(a, b+1):
    # ------------------ Print all the prime numbers in tamge of inputs----------------
    if i > 1:
        for j in range(2, i):
            if (i % j) == 0:
                break
        else:
            print(i)
            count += 1
            print("Total number of prime numbers between",
                  a, "and", b, "is", count, " ", i, j, "\n")
            print("Theis is a prime number")
    # ----------------------------Second Q-----------------------------------
    # if count == 2:
    #     print("There are only two prime numbers between",   a, "and", b, "\n")
    # elif count == 1:
    #     print("There is only one prime number between", a, "and", b, "\n")
    # else:
    #     print("There are no prime numbers between", a, "and", b, "\n")
