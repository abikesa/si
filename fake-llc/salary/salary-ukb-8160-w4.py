from datetime import datetime, timedelta
import csv

# === CONFIGURATION ===
HOURLY_RATE = 25.00
WEEKLY_HOURS = 23
BACKPAY_START = datetime(2025, 3, 31)  # First full workweek
BACKPAY_END = datetime(2025, 6, 14)    # Last full week before next Friday payday
PAYDAY = datetime(2025, 6, 21)         # Lump sum payday
EMPLOYEE_NAME = "UKB-8160"
STATE = "MD"

# Tax withholding rates - Updated for married filing jointly
# Federal withholding estimate (married filing jointly, standard deduction)
FEDERAL_TAX_RATE = 0.10  # Lower rate for married filing jointly
SOCIAL_SECURITY_RATE = 0.062
MEDICARE_RATE = 0.0145

# Maryland state income tax estimate (married filing jointly has lower rates)
MD_STATE_TAX_RATE = 0.045  # Slightly lower for married filing jointly

# Additional withholding if he's claimed as dependent on spouse's plan
# (This is conservative - actual may be lower depending on spouse's income)
ADDITIONAL_WITHHOLDING = 0.00  # Set to 0.02 if you want extra 2% withheld for safety

# === CALCULATION FUNCTIONS ===

def daterange(start_date, end_date, step_days=7):
    while start_date <= end_date:
        yield start_date
        start_date += timedelta(days=step_days)

def calculate_gross_pay(weeks):
    return round(weeks * WEEKLY_HOURS * HOURLY_RATE, 2)

def calculate_withholding(gross):
    fed = round(gross * (FEDERAL_TAX_RATE + ADDITIONAL_WITHHOLDING), 2)
    ss = round(gross * SOCIAL_SECURITY_RATE, 2)
    medicare = round(gross * MEDICARE_RATE, 2)
    state = round(gross * MD_STATE_TAX_RATE, 2)
    net = round(gross - fed - ss - medicare - state, 2)
    return {
        "federal": fed,
        "social_security": ss,
        "medicare": medicare,
        "state_tax": state,
        "net": net
    }

def generate_paystub(gross, withholdings, filename="paystub.csv"):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Employee", "Pay Date", "Gross Pay", "Federal Tax", "SS Tax", "Medicare", "State Tax", "Net Pay"])
        writer.writerow([
            EMPLOYEE_NAME,
            PAYDAY.strftime("%Y-%m-%d"),
            f"${gross:.2f}",
            f"${withholdings['federal']:.2f}",
            f"${withholdings['social_security']:.2f}",
            f"${withholdings['medicare']:.2f}",
            f"${withholdings['state_tax']:.2f}",
            f"${withholdings['net']:.2f}"
        ])
    return filename

def print_summary(gross, withholdings, weeks):
    print(f"=== PAYROLL SUMMARY ===")
    print(f"Employee: {EMPLOYEE_NAME}")
    print(f"Pay Period: {BACKPAY_START.strftime('%Y-%m-%d')} to {BACKPAY_END.strftime('%Y-%m-%d')}")
    print(f"Weeks worked: {weeks}")
    print(f"Hours per week: {WEEKLY_HOURS}")
    print(f"Hourly rate: ${HOURLY_RATE:.2f}")
    print(f"")
    print(f"Gross Pay: ${gross:.2f}")
    print(f"Federal Tax: ${withholdings['federal']:.2f}")
    print(f"Social Security: ${withholdings['social_security']:.2f}")
    print(f"Medicare: ${withholdings['medicare']:.2f}")
    print(f"MD State Tax: ${withholdings['state_tax']:.2f}")
    print(f"Net Pay: ${withholdings['net']:.2f}")
    print(f"")
    print(f"NOTE: Rates assume married filing jointly, no dependents")
    print(f"Employee should complete W-4 to confirm withholding preferences")

# === EXECUTION ===

backpay_weeks = len(list(daterange(BACKPAY_START, BACKPAY_END)))
gross = calculate_gross_pay(backpay_weeks)
withhold = calculate_withholding(gross)
paystub_file = generate_paystub(gross, withhold)

# Print summary and return results
print_summary(gross, withhold, backpay_weeks)
print(f"Paystub saved to: {paystub_file}")

(gross, withhold, paystub_file)