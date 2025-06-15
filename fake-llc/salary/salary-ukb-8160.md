# Ukubona LLC Payroll Setup – README

This document outlines the payroll setup, schedule, and compliance obligations for Ukubona LLC's internal W-2 employee payroll operations, beginning with the initial disbursement on **June 21, 2025**.

---

## 📌 Key Facts

| Item               | Value                               |
| ------------------ | ----------------------------------- |
| **Employee**       | Founder (MD resident)               |
| **Company State**  | Virginia                            |
| **First Payroll**  | June 21, 2025 (backpay)             |
| **Pay Frequency**  | Weekly                              |
| **Work Schedule**  | Mon–Wed (23 hours/week)             |
| **Hourly Rate**    | \$25/hr                             |
| **Weekly Gross**   | \$575                               |
| **Backpay Period** | March 31 – June 14, 2025 (11 weeks) |
| **Backpay Gross**  | \$6,325                             |
| **Next Payday**    | June 21, 2025                       |

---

## 📎 Tax Withholding Summary (Backpay Lump Sum)

| Tax Type           | Rate  | Amount         |
| ------------------ | ----- | -------------- |
| Federal Income Tax | 12%   | \$759.00       |
| Social Security    | 6.2%  | \$392.15       |
| Medicare           | 1.45% | \$91.71        |
| MD State Tax       | \~5%  | \$316.25       |
| **Total Withheld** |       | **\$1,559.11** |
| **Net Pay**        |       | **\$4,765.89** |

---

## ⏰ Compliance Deadlines

### 🏛️ Federal (IRS)

| Form / Action     | Frequency | Due Date          | Notes                        |
| ----------------- | --------- | ----------------- | ---------------------------- |
| **Tax Deposit**   | Monthly   | **July 15, 2025** | For June 21 disbursement     |
| **Form 941 (Q2)** | Quarterly | **July 31, 2025** | IRS quarterly payroll return |
| **W-2 / W-3**     | Annual    | Jan 31, 2026      | Filed with SSA & employee    |

### 🏛️ State (Virginia Employer, MD Resident Employee)

| Form / Action            | Frequency | Due Date          | Notes                             |
| ------------------------ | --------- | ----------------- | --------------------------------- |
| **VA Withholding Setup** | One-time  | ASAP              | Register with VA Dept of Taxation |
| **VA-5**                 | Quarterly | July 31, 2025     | State withholding return          |
| **MD Withholding**       | Ongoing   | Monthly/Quarterly | Withheld from employee paycheck   |

> ⚠️ **VA/MD Reciprocity:** As a Maryland resident, the employee is subject to MD income tax. VA withholding can be avoided with the proper non-resident exemption filing. Double-check this with a state tax advisor.

---

## ✅ Next Steps Checklist

* [x] Register for [EFTPS.gov](https://www.eftps.gov) for Federal deposits
* [x] Register for Virginia Employer Withholding account
* [x] Set up MD state withholding account if necessary
* [ ] Create a reminder system for:

  * [ ] Monthly tax deposit (EFTPS) due by 15th of following month
  * [ ] Quarterly filings: IRS Form 941 + VA-5 due by end of month after quarter ends
* [ ] Run `payroll.py` weekly to generate paystubs and exports
* [ ] Track all net payments and tax withholdings in BoA business account

---

## 🔐 File Outputs

* `payroll.py` → Calculates gross, withholding, net pay
* `paystub.csv` → Single-pay disbursement stub
* Future: add `941-generator.py`, `W2-export.py`, and API endpoint

---

## 🧠 Notes

This system is designed to keep Ukubona LLC compliant and nimble while you grow. The backpay lump sum is compliant with federal and state law as long as:

* Taxes are calculated and remitted properly
* Filings reflect the **correct amount** in the **correct quarter**

---

For questions, contact your payroll admin (yourself), or consult a CPA before year-end to ensure filings (W-2, 941, VA-5) align with actual disbursements.

---

*Last updated: June 12, 2025*

