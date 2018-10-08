def main():
    #input and variables 
    salary = float(input("What is your weekly salary? "))
    bonus = float(input("What is your bonus? "))


    # processing
    totalPay = salary + bonus

    #output
    print("The total pay for the week is: " + str(totalPay))


if __name__ == "__main__":
    main()