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
    def semester():
        # input savings amounts
        semester_tuition = float(input("Enter your semester's tuition: "))
        semester_numbers = int(input("How many semester of college have you had?: "))
        total_tuition = semester_tuition * semester_numbers
        total_tuition2 = total_tuition - savings_total
        print('Your total tuition is: ', total_tuition)
        print('Your total tuition is: ', total_tuition2)
    semester()
    def loan():
        loan_status = input("Have you yet taken out a student loan for tuition? (reply either 'yes' or 'no' \n")
        if loan_status == 'yes':
            print("Below, do not enter any special characters. Information below must be provided. \n")
            loan_amt = input("Enter the amount of money you were loaned: \n")
            loan_intr = input("Enter the interest rate on the loan you took out (as a whole number, without the percent, such as '5' for 5%):
    loan()
    def living():
        # input living expenses
    living()
    
main()
