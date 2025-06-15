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

# Federal withholding estimate (simplified, no dependents, single filer)
FEDERAL_TAX_RATE = 0.12
SOCIAL_SECURITY_RATE = 0.062
MEDICARE_RATE = 0.0145

# Maryland state income tax estimate (2025, single filer, blended local + state avg)
MD_STATE_TAX_RATE = 0.05

# === CALCULATION FUNCTIONS ===

def daterange(start_date, end_date, step_days=7):
    while start_date <= end_date:
        yield start_date
        start_date += timedelta(days=step_days)

def calculate_gross_pay(weeks):
    return round(weeks * WEEKLY_HOURS * HOURLY_RATE, 2)

def calculate_withholding(gross):
    fed = round(gross * FEDERAL_TAX_RATE, 2)
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

# === EXECUTION ===

backpay_weeks = len(list(daterange(BACKPAY_START, BACKPAY_END)))
gross = calculate_gross_pay(backpay_weeks)
withhold = calculate_withholding(gross)
paystub_file = generate_paystub(gross, withhold)

(gross, withhold, paystub_file)

