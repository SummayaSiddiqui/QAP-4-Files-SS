# Description: A program for One Insurance Company
# Author: Summaya Siddiqui
# Date(s): 21st Mar, 2024 - 22nd Mar, 2024


# Define required libraries.
import datetime
import FormatValues as FV
import time
import sys

# Open the defaults file and read the values into variables
f = open('Def.dat', 'r')

POLICY_NUM = int(f.readline())
BASIC_PREMIUM = float(f.readline())
ADDITIONAL_CAR_DISCOUNT = float(f.readline())
EXTRA_LIABILITY_COVERAGE = float(f.readline())
GLASS_COVERAGE_COST = float(f.readline())
LOANER_CAR_COVERAGE = float(f.readline())
HST_RATE = float(f.readline())
PROCESSING_FEE = float(f.readline())

f.close()

# Define program constants.
TODAY = datetime.datetime.now()

# Define program functions.
def CalcInsurancePremium(NumInsuredCars):
    if NumInsuredCars >= 1:
        InsurancePremium = BASIC_PREMIUM + ADDITIONAL_CAR_DISCOUNT * (NumInsuredCars -1) * BASIC_PREMIUM
    else:
        InsurancePremium = BASIC_PREMIUM
    
    return InsurancePremium

def CalcExtraCosts(Cost1, Cost2, Cost3):
    if ExtraLiabilityCoverage == "Y":
        Cost1 = EXTRA_LIABILITY_COVERAGE * NumInsuredCars
    else:
        Cost1 = 0

    if OptionalGlassCoverage == "Y":
        Cost2 = GLASS_COVERAGE_COST * NumInsuredCars
    else:
        Cost2 = 0
    
    if OptionalLoanercar == "Y":
        Cost3 = LOANER_CAR_COVERAGE * NumInsuredCars
    else:
        Cost3 = 0

    ExtraCost = Cost1 + Cost2 + Cost3
    return Cost1, Cost2, Cost3, ExtraCost
    
def CalcMonthlyPay():
    if PaymentMethod == "Full":
        MonthlyPayment = 0
    elif PaymentMethod == "Monthly":
        MonthlyPayment = (PROCESSING_FEE + TotalCost) / 8
    else:
        MonthlyPayment = (PROCESSING_FEE + TotalCost - DownPaymentAmount) / 8

    return MonthlyPayment

def CalcFirstPaymentDate():
    InvYear = TODAY.year 
    InvMonth = TODAY.month
    InvDay = TODAY.day

    PayYear = InvYear
    PayMonth = InvMonth + 1
    PayDay = 1

    if PayMonth > 12:
        PayMonth -= 12
        PayYear += 1

    PayDate = datetime.datetime(PayYear, PayMonth, PayDay)

    return PayDate

def ClaimDateValidation(ClaimDate):
    try:
        datetime.datetime.strptime(ClaimDate, "%Y-%m-%d")
        return True
    except ValueError:
        return False


# Main program starts here.
while True:

    # Gather user inputs.
    # Customer Name.
    while True:
        FirstName = input ("Enter customer's first name: ").title()
        if FirstName == "":
            print("Error - Customer first name cannot be blank.")
        else:
            break
    while True:
        LastName = input ("Enter customer's last name: ").title()
        if LastName == "":
            print("Error - Customer's last name cannot be blank.")
        else:
            break
    
    CustomerName = FirstName + " " + LastName

    # Customer Street Address and City.
    StreetAddress = input("Enter customer's address: ").title()
    City = input("Enter customer's city: "). title()

    # Customer Province.
    ProvLst = ["NL", "NS", "NB", "PQ", "ON", "MB", "AB", "BC", "NT", "YT", "NV"]

    while True:
        Prov = input("Enter the customer's province (XX): ").upper()
        if Prov == "":
            print("Error - Customer's province cannot be blank.")
        elif len(Prov) != 2:
            print("Error - Customer's province must be 2 characters only.")
        elif Prov not in ProvLst:
            print("Error - Customer's province must be the valid entry.")
        else:
            break

    # Cystomer Postal code.
    allowed_char = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    allowed_num = set("0123456789")
    while True:
        PostalCode = input("Enter customer's postal code (X0X0X0): ").upper()
        if PostalCode == "":
            print("Error - Postal code cannot be blank.")
        elif len(PostalCode) != 6:
            print("Error - Postal code can be of 6 characrters only.")
        elif set(PostalCode[0]).issubset(allowed_char) == False and set(PostalCode[2]).issubset(allowed_char) == False and set(PostalCode[4]).issubset(allowed_char) == False:
            print("Error - The 1st, 3rd and 5th character in a postal code can be an alphabet only.")
        elif set(PostalCode[1]).issubset(allowed_num) == False and set(PostalCode[3]).issubset(allowed_num) == False and set(PostalCode[5]).issubset(allowed_num) == False:
            print("Error - The 1st, 3rd and 5th character in a postal code can be an alphabet only.")
        else:
            break
    PostalCode1 = PostalCode[0] + PostalCode[1] + PostalCode[2] + PostalCode[3] + PostalCode[4] + PostalCode[5]

    CustomerAdd = StreetAddress + " " + City + " " + Prov + "," + PostalCode1

    # Customer Phone number.
    while True:
        PhoneNum = input("Enter customer's phone number (9999999999): ")
        if PhoneNum == "":
            print("Data Entry Error - Phone number cannot be blank.")
        elif PhoneNum.isdigit() == False:
            print("Data Entry Error - Phone number contains digits only.")
        elif len(PhoneNum) != 10:
            print("Data Entry Error - Phone number contains 10 digits only.")
        else:
            break

    PhoneNum1 = "(" + PhoneNum[0:3] + ")" + " " + PhoneNum[3:6] + "-" + PhoneNum[6:11]
    
    NumInsuredCars = input("Enter the number of cars insured: ")
    NumInsuredCars = int(NumInsuredCars)

    ExtraLst = ["Y", "N"]
    while True:
        ExtraLiabilityCoverage = input("Extra liability coverage (Y/N): ").upper()
        if ExtraLiabilityCoverage == "":
            print("Error - Field cannot be blank.")
        elif ExtraLiabilityCoverage not in ExtraLst:
            print("Eror - Invalid entry.")
        else:
            break
    
    while True:   
        if ExtraLiabilityCoverage == "Y":
            LiabilityCoverage1 = "Yes"
        elif ExtraLiabilityCoverage == "N":
            LiabilityCoverage1 = "No"
        break
    
    ExtraLst = ["Y", "N"]
    while True:
        OptionalGlassCoverage = input("Optional glass coverage (Y/N): ").upper()
        if OptionalGlassCoverage == "":
            print("Error - Field cannot be blank.")
        elif OptionalGlassCoverage not in ExtraLst:
            print("Eror - Invalid entry.")
        else:
            break
        
    while True:
        if OptionalGlassCoverage == "Y":
            GlassCoverage1 = "Yes"
        elif OptionalGlassCoverage == "N":
            GlassCoverage1 = "No"
        break
        
    ExtraLst = ["Y", "N"]
    while True:
        OptionalLoanercar = input("Optional loaner car (Y/N): ").upper()
        if OptionalLoanercar == "":
            print("Error - Field cannot be blank.")
        elif OptionalLoanercar not in ExtraLst:
            print("Eror - Invalid entry.")
        else:
            break
        
    while True:
        if OptionalLoanercar == "Y":
            LoanerCar1 = "Yes"
        elif OptionalLoanercar == "N":
            LoanerCar1 = "No"
        break
    
    PaymentMethodLst = ["Full", "Monthly", "Down Pay"]
    while True:
        PaymentMethod = input("Enter payment method Full, Monthly, Down Pay: ").title()
        if PaymentMethod == "":
            print("Error - Payment method cannot be blank.")
        elif PaymentMethod not in PaymentMethodLst:
            print("Error - Payment method can only be Full, Monthly or Down Pay.")
        else:
            break
    
    while True:
        if PaymentMethod == "Down Pay":
            DownPaymentAmount = input("Enter the amount of the down payment: ")
            DownPaymentAmount = int(DownPaymentAmount)
        else:
            DownPaymentAmount = 0
        break
    
    ClaimNumLst = []
    ClaimDateLst = []
    ClaimAmountLst = []

    while True:
        ClaimNum = input("Enter claim number (-1 to end): ")
        if ClaimNum == "-1":
            break

        ClaimDate = input("Enter claim date (YYYY-MM-DD): ")
        while not ClaimDateValidation(ClaimDate):
            print("Invalid date format! Please enter date in YYYY-MM-DD format.")
            ClaimDate = input("Enter claim date (YYYY-MM-DD): ")
        ClaimDate = datetime.datetime.strptime(ClaimDate, "%Y-%m-%d")


        ClaimAmount = input("Enter claim amount: ")
        ClaimAmount = float(ClaimAmount)

        ClaimNumLst.append(ClaimNum)
        ClaimDateLst.append(ClaimDate)
        ClaimAmountLst.append(ClaimAmount)


    # Perform required calculations.
    FirstPaymentDate = CalcFirstPaymentDate()
    
    InsurancePremium = CalcInsurancePremium(NumInsuredCars)
    Discount = ADDITIONAL_CAR_DISCOUNT * (NumInsuredCars - 1)

    Result = CalcExtraCosts(ExtraLiabilityCoverage, OptionalGlassCoverage, OptionalLoanercar)
    TotalExtraCosts = Result[3]
    LiabilityCoverage = Result[0]
    GlassCoverage = Result[1]
    LoanerCar = Result[2]
    

    TotalInsurancePremium = InsurancePremium + TotalExtraCosts
    HST = TotalInsurancePremium * HST_RATE
    TotalCost = TotalInsurancePremium + HST

    if PaymentMethod == "Full":
        MonthlyPayment = 0
    elif PaymentMethod == "Monthly":
        MonthlyPayment = PROCESSING_FEE + (TotalCost / 8)
    else:
        MonthlyPayment = PROCESSING_FEE + ((TotalCost - DownPaymentAmount)/8)


    # Display results.
    
    print()
    print("-----------------------------------------------------------------------------------------")
    print("                              ONE STOP INSURANCE COMPANY")
    print("                                     POLICY REPORT")
    print("-----------------------------------------------------------------------------------------")
    print()
    print("   Customer Information:")
    print()
    print(f"        Customer Name: {(CustomerName):<20s}            Invoice Date:       {FV.FDateAbb(TODAY):<11s}")
    print(f"        Address:       {StreetAddress:<20s}")
    print(f"                       {(City + "," + Prov + " " + PostalCode1):<20s}")
    print(f"        Phone:         {(PhoneNum1):<14s}")
    print()
    print("-----------------------------------------------------------------------------------------")
    print()
    print("   Policy Details:")
    print()
    print(f"        Number of Insured Cars:   {NumInsuredCars:>2d}        Insurance Premium:                {FV.FDollar2(InsurancePremium):>9s}")
    print(f"        Extra Liabality Coverage: {LiabilityCoverage1:<3s}       Cost of Extra Liability Coverage: {FV.FDollar2(LiabilityCoverage):>9s}")
    print(f"        Glass Coverage:           {GlassCoverage1:<3s}       Cost of Glass Coverage:           {FV.FDollar2(GlassCoverage):>9s}")
    print(f"        Loaner Car Coverage:      {LoanerCar1:<3s}       Cost for Loaner Car:              {FV.FDollar2(LoanerCar):>9s}")
    print(f"                                                                            ============")
    print(f"                                            Total Extra Costs:                {FV.FDollar2(TotalExtraCosts):>9s}")
    print(f"                                            Total Insurance Premium:          {FV.FDollar2(TotalInsurancePremium):>9s}")
    print(f"                                            HST:                              {FV.FDollar2(HST):>9s}")
    print(f"                                                                            ============")
    print(f"        Payment Method: {PaymentMethod:>8s}            Total Cost:                       {FV.FDollar2(TotalCost):>9s}")
    print(f"                                                                            ============")
    if PaymentMethod == "Monthly" or PaymentMethod == "Down Pay":
        print(f"                                            Processing Fee:                   {FV.FDollar2(PROCESSING_FEE):>9s}")
        print(f"                                            Down Fee:                         {FV.FDollar2(DownPaymentAmount):>9s}")
        print("-----------------------------------------------------------------------------------------")
        print()
        print(f"       First Payment Date: {FV.FDateAbb(FirstPaymentDate):<11s}     Monthly Payment:                  {FV.FDollar2(MonthlyPayment):>9s}")
    

    print()
    print()

    print(f"        Claim #            Claim Date              Amount")
    print("-------------------------------------------------------------------")

    Index = 0
    for i in range(len(ClaimNumLst)):
        print(f"        {ClaimNumLst[Index]:>5s}              {FV.FDateS(ClaimDateLst[Index]):>10s}           {FV.FDollar2(ClaimAmountLst[Index]):>10s}")
        Index += 1
            
    print("-------------------------------------------------------------------")


    # Store the claim data into a file called Claims.dat

    for _ in range(5):
        print("Saving policy data ...", end='\r')
        time.sleep(.3) 
        sys.stdout.write('\033[2K\r') 
        time.sleep(.3)

    f = open("Claim.dat", "a")

    f.write("{}, ".format(str(POLICY_NUM)))
    f.write("{}, ".format(str(CustomerName)))
    f.write("{}, ".format(str(CustomerAdd)))
    f.write("{}, ".format(str(PhoneNum1)))
    f.write("{}, ".format(str(NumInsuredCars)))
    f.write("{}, ".format(str(LiabilityCoverage)))
    f.write("{}, ".format(str(GlassCoverage)))
    f.write("{}, ".format(str(LoanerCar)))
    f.write("{}\n".format(str(TotalInsurancePremium)))

    f.close()

    # Open default file to add 1 to the policy number.
    f = open("Def.dat", "a")

    f.write("{}, ".format(str(POLICY_NUM)))

    f.close()

    print()
    print("Policy data successfully saved ...", end='\r')
    time.sleep(1) 
    sys.stdout.write('\033[2K\r')
    print()
    print()

    POLICY_NUM += 1

    Continue = input("Do you want to proceed with another policy (Y/N): ").title()
    if Continue == "Y":
        print("You are all set to proceed.")
        print()
    else:
        break
    

# Any housekeeping duties at the end.
f = open('Def.dat', 'w')

f.write("{}\n".format(str(POLICY_NUM)))
f.write("{}\n".format(str(BASIC_PREMIUM)))
f.write("{}\n".format(str(ADDITIONAL_CAR_DISCOUNT)))
f.write("{}\n".format(str(EXTRA_LIABILITY_COVERAGE)))
f.write("{}\n".format(str(GLASS_COVERAGE_COST)))
f.write("{}\n".format(str(LOANER_CAR_COVERAGE)))
f.write("{}\n".format(str(HST_RATE)))
f.write("{}\n".format(str(PROCESSING_FEE)))

f.close()

print()
print("Thank you for using the program!")
print()
    
