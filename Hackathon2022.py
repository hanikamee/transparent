# TRANSPARENT - STUDENT FINANCE
def main():
    # mission statement
    print("Welcome to Transparent! \n")
    print("We believe that school should not get in the way of a student's financial future.")
    print("Therefore, we created Transparent to clearly communicate to students their best path(s) to future financial success! \n")
    savings_total = 0
    def savings():
        prompt = input("Do you have any scholarships, FAFSA money, or savings from a 529 or other account? (reply either 'yes' or 'no'). \n")
        if prompt == 'yes':
            print("Below, if the prompt does not apply to you, enter '0'. Do not use commas or any special characters. \n")
            s_529 = input("Enter your 529 savings amount below: \n")
            s_sav = input("Enter the total of any other savings you may have: \n")
            s_fafsa = input("Enter the total amount of FAFSA money you will be receiving. \n")
            s_sch = input("Enter the total amount of scholarship money you will be receiving for the given school. \n")
            savings_total = s_529 + s_sav + s_fafsa + s_sch
            return savings_total
        elif prompt == 'no':
            continue
        else:
            print("Invalid Statement. ")
            savings()
            
    savings()
    tuition_owed = 0
    def semester():
        # input savings amounts
        semester_tuition = float(input("Enter your semester's tuition: "))
        semester_numbers = int(input("How many semester of college have you had?: "))
        total_tuition = semester_tuition * semester_numbers
        tuition_owed = total_tuition - savings_total
        print('Your total tuition is: ', total_tuition)
        print('Your total tuition, subtracting savings/fafsa/scholarships, is: ', tuition_owed)
        return tuition_owed
    semester()
    def loan():
        loan_status = input("\n Have you yet taken out a student loan for tuition? (reply either 'yes', 'no', or 'future' for a possible loan in the future. \n")
        if loan_status == 'yes':
            print("\n Below, do not enter any special characters. Information below must be provided. \n")
            loan_amt = input("\n Enter the amount of money you were loaned: \n")
            if loan_amt > tuition_owed:
                print("WARNING: your loan amount is greater than the amount you will owe in tuition. You've gone into more debt than needed. ")
            loan_intr = input("\n Enter the interest rate on the loan you took out (as a whole number, without the percent, such as '5' for 5%)")
            loan_intr /= 100
            loan_pd = input("\n Enter the amount of monthly payments to be made. If it is indefinite, reply '0'. \n")
            print("\n Here is a 10 year projection on the amount you will owe per year: \n")
            for year in range(10):
                loan = (loan_amt * loan_intr) + loan_amt
                print((year+1) +": $"+ round(loan,2))
        elif loan_status == 'future':
            loan_amt = tuition_owed
            print("If you must take out a loan (but only do so if you absolutely need to), take out the exact amount as the amount of tuition you will owe, which for you is: $", loan_amt)
            print("Also, it is best practice to take out the LOWEST interest rate possible. It would be best to be within the 1-7% range. \n")
        else:
            print("Excellent! You should be debt free then. Don't take out a loan unless you ABSOLUTELY need to. ")
        
        
            
            
    loan()
    def living():
        # input living expenses
    living()
    
main()
