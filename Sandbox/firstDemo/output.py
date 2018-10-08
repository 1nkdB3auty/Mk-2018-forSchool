def main():
    # 1. Output and variables
    salary = float(input("What is your weekly salary? "))
    bonus = float(input("What is your bonus? "))

    # 2. Processing
    totalPay = salary + bonus

    # 3. Output
    print("Your total weekly pay with bonus of {:.2f} is: {:.2f}".format(bonus,totalPay))
	
	
if __name__ == "__main__":
    main()