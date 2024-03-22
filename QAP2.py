# A program to prepare a reciept for St. John's Marina & Yatcht Club.
# Author: Summaya Siddiqui.
# Date (s): January 27 2024 to January 29 2024

# Setting program constants
EVENSITE_COST = 80.00
ODDSITE_COST = 120.00
ALTERNATE_MEMBER_COST = 5.00
WEEKLY_SITE_CLEANING = 50.00
VIDEO_SURV = 35.00
HST_RATE = 0.15
MONTHLYDUE_STANDARD = 75.00
MONTHLYDUE_EXECUTIVE = 150.00
PROCESSING_FEE = 59.99
CANCELLATION_FEE_RATE = 0.60

# Gather user inputs.
CurrentDate = input("Enter Date (YYYY-MM-DD): ")
SiteNumber = input("Enter the site number (1-100): ")
SiteNumber = int(SiteNumber)
MemberName = input("Enter the member name: ")
StreetAdd = input("Enter the street address: ")
City = input("Enter city: ")
Province = input("Enter province (AB): ").upper()
PostalCode = input("Enter postal code (L9L9L9): ")
PhoneNum = input("Enter the phone number (9999999999): ")
CellNum = input ("Enter the cell number (9999999999): ")

MembershipType = input("Enter the membership type (S or E): ").upper()
if MembershipType == "S":
    MembershipType1 = "Standard"

else:
    MembershipType1 = "Executive"

NumAlternateMember = int(input("Enter the number of alternate members: "))

WeeklySiteCleaning = input("Weekly site cleaning (Y or N): ").upper()
if WeeklySiteCleaning == "Y":
    WeeklySiteCleaning1 = "Yes"
else:
    WeeklySiteCleaning1 = "No"

VideoSurv = input("Video Surveillance (Y or N): ").upper()
if VideoSurv == "Y":
    VideoSurv1 = "Yes"
else:
    VideoSurv1 = "No"

# Caltulate user inputs.

# Calculating site charges.
if SiteNumber % 2 == 0:
    SiteCost = EVENSITE_COST
else:
    SiteCost = ODDSITE_COST

AlternateMemberCost = NumAlternateMember * ALTERNATE_MEMBER_COST

SiteCharges = SiteCost + AlternateMemberCost

# Calculating extra charges.
if WeeklySiteCleaning == "Y":
    WEEKLY_SITE_CLEANING = 50.00
else:
    WEEKLY_SITE_CLEANING = 0.00

if VideoSurv == "Y":
    VIDEO_SURV = 35.00
else:
    VIDEO_SURV = 0.00

ExtraCharges = WEEKLY_SITE_CLEANING + VIDEO_SURV

# Calculating Subtotal, HST, Total Monthly Charge.
SubTotal = SiteCharges + ExtraCharges
HST = SubTotal * 0.15
TotalMonthlyCharge = SubTotal + HST

# Calculating Total Monthly Fee.
if MembershipType == "S":
    MonthlyDues = MONTHLYDUE_STANDARD
else:
    MonthlyDues = MONTHLYDUE_EXECUTIVE

TotalMonthlyFee = TotalMonthlyCharge + MonthlyDues

# Calculating The Total Yearly Fee, Monthly Payment and Cancellation Fee.
TotalYearlyFee = TotalMonthlyFee * 12

MonthlyPayment = (TotalYearlyFee + PROCESSING_FEE) / 12

CancellationFee = SiteCharges * 12 * CANCELLATION_FEE_RATE


# Display user inputs.
print()
print()
print(f"   St. John's Marina & Yacht Club")
print(f"      Yearly Member Reciept")
print()   
print(f"____________________________________")
print()
print(f"Client Name and Address:")
print()
print(f"{MemberName:<36s}")
print(f"{StreetAdd:<36s}")
print(f"{City:<25s}, {Province:<2s} {PostalCode:<6s}")
print()
print(f"Phone: {PhoneNum:<10s} (H)")
print(f"       {CellNum:<10s} (C)")
print()
print(f"Site #: {SiteNumber:<3d}  Member type:  {MembershipType1:>9s}")

print()
print(f"Alternate members:                {NumAlternateMember:<2d}")

print(f"Weekly site cleaning:            {WeeklySiteCleaning1:<3s}")

print(f"Video surveillance:              {VideoSurv1:<3s}")

print()
SiteChargesDsp = "${:,.2f}".format(SiteCharges)
print(f"Site Charges:              {SiteChargesDsp:>9s}")
ExtraChargesDsp = "${:,.2f}".format(ExtraCharges)
print(f"Extra charges:               {ExtraChargesDsp:>7s}")
print(f"                            --------")
SubTotalDsp = "${:,.2f}".format(SubTotal)
print(f"Sub Total:                 {SubTotalDsp:>9s}")
HSTDsp = "${:,.2f}".format(HST)
print(f"Sales tax (HST):             {HSTDsp:>7s}")
print(f"                            --------")
TotalMonthlyChargeDsp = "${:,.2f}".format(TotalMonthlyCharge)
print(f"Total monthyly charges:    {TotalMonthlyChargeDsp:>9s}")
MonthlyDuesDsp = "${:,.2f}".format(MonthlyDues)
print(f"Monthly dues:                {MonthlyDuesDsp:>7s}")
print(f"                            --------")
TotalMonthlyFeeDsp = "${:,.2f}".format(TotalMonthlyFee)
print(f"Total monthly fees:        {TotalMonthlyFeeDsp:>9s}")
TotalYearlyFeeDsp = "${:,.2f}".format(TotalYearlyFee)
print(f"Total yearly fees:        {TotalYearlyFeeDsp:>10s}")
print()
MonthlyPaymentDsp = "${:,.2f}".format(MonthlyPayment)
print(f"Monthly payment:           {MonthlyPaymentDsp:>9s}")
print()
print(f"____________________________________")
print()
print(f"Issued: {CurrentDate}")
print(f"HST Reg No: 549-33-5849-4720-9885")
print()
CancellationFeeDsp = "${:,.2f}".format(CancellationFee)
print(f"Cancellation fee:          {CancellationFeeDsp:>9s}")
print()
print()

