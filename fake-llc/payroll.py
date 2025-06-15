from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from datetime import datetime, timedelta
import yaml
import os
import csv
import io

app = Flask(__name__)    
CORS(app)

DATA_FILE = 'fake-data.yml'

# Payroll configuration
PAYROLL_CONFIG = {
    "UKB-8160": {
        "name": "Thandi Mthembu",
        "hourly_rate": 25.00,
        "weekly_hours": 23,
        "filing_status": "married_jointly",
        "state": "MD",
        "hire_date": "2025-03-31"
    },
    "UKB-7240": {
        "name": "Kabelo Nkomo",
        "hourly_rate": 45.00,
        "weekly_hours": 40,
        "filing_status": "single",
        "state": "MD",
        "hire_date": "2024-01-15"
    },
    "UKB-9501": {
        "name": "Lebo Mashile",
        "hourly_rate": 75.00,
        "weekly_hours": 50,
        "filing_status": "married_jointly",
        "state": "MD",
        "hire_date": "2023-06-01"
    },
    "UKB-3847": {
        "name": "Priya Patel",
        "hourly_rate": 55.00,
        "weekly_hours": 40,
        "filing_status": "single",
        "state": "MD",
        "hire_date": "2024-09-12"
    }
}

# Tax rates by filing status
TAX_RATES = {
    "single": {
        "federal": 0.12,
        "state_md": 0.05
    },
    "married_jointly": {
        "federal": 0.10,
        "state_md": 0.045
    },
    "married_separately": {
        "federal": 0.115,
        "state_md": 0.048
    }
}

STANDARD_RATES = {
    "social_security": 0.062,
    "medicare": 0.0145
}

def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, 'r') as f:
        return yaml.safe_load(f) or {}

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        yaml.dump(data, f)

def calculate_payroll(employee_id, start_date, end_date):
    """Calculate payroll for an employee between two dates"""
    if employee_id not in PAYROLL_CONFIG:
        return None
    
    config = PAYROLL_CONFIG[employee_id]
    
    # Calculate weeks between dates
    start = datetime.strptime(start_date, '%Y-%m-%d')
    end = datetime.strptime(end_date, '%Y-%m-%d')
    weeks = ((end - start).days + 1) / 7
    
    # Calculate gross pay
    gross_pay = weeks * config["weekly_hours"] * config["hourly_rate"]
    
    # Get tax rates
    rates = TAX_RATES[config["filing_status"]]
    
    # Calculate deductions
    federal_tax = gross_pay * rates["federal"]
    state_tax = gross_pay * rates["state_md"]
    social_security = gross_pay * STANDARD_RATES["social_security"]
    medicare = gross_pay * STANDARD_RATES["medicare"]
    
    total_deductions = federal_tax + state_tax + social_security + medicare
    net_pay = gross_pay - total_deductions
    
    return {
        "employee_id": employee_id,
        "employee_name": config["name"],
        "period_start": start_date,
        "period_end": end_date,
        "weeks_worked": round(weeks, 2),
        "hourly_rate": config["hourly_rate"],
        "weekly_hours": config["weekly_hours"],
        "gross_pay": round(gross_pay, 2),
        "federal_tax": round(federal_tax, 2),
        "state_tax": round(state_tax, 2),
        "social_security": round(social_security, 2),
        "medicare": round(medicare, 2),
        "total_deductions": round(total_deductions, 2),
        "net_pay": round(net_pay, 2),
        "filing_status": config["filing_status"]
    }

@app.after_request
def add_header(response):
    response.cache_control.no_store = True
    return response

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(load_data())

@app.route('/update', methods=['POST'])
def update_data():
    new_data = request.get_json()
    save_data(new_data)
    return jsonify({"message": "Data updated successfully!"})

@app.route('/api/owners')
def get_owners():
    data = load_data()
    owners = set()
    for layer in data.get("layers", {}).values():
        for task in layer.get("tasks", []):
            owners.add(task.get("owner", "unknown"))
    return jsonify(sorted(owners))

@app.route('/api/tasks/<owner>')
def get_tasks_by_owner(owner):
    data = load_data()
    filtered_tasks = []
    for layer_key, layer in data.get("layers", {}).items():
        for task in layer.get("tasks", []):
            if task.get("owner") == owner:
                task_info = task.copy()
                task_info["layer"] = layer.get("name", layer_key)
                task_info["layerColor"] = layer.get("color", "#cccccc")
                filtered_tasks.append(task_info)
    return jsonify(filtered_tasks)

# Payroll API endpoints
@app.route('/api/employees')
def get_employees():
    """Get list of all employees"""
    employees = []
    for emp_id, config in PAYROLL_CONFIG.items():
        employees.append({
            "id": emp_id,
            "name": config["name"],
            "hourly_rate": config["hourly_rate"],
            "weekly_hours": config["weekly_hours"],
            "filing_status": config["filing_status"],
            "hire_date": config["hire_date"]
        })
    return jsonify(employees)

@app.route('/api/payroll/<employee_id>')
def get_payroll(employee_id):
    """Calculate payroll for specific employee"""
    start_date = request.args.get('start_date', '2025-03-31')
    end_date = request.args.get('end_date', '2025-06-14')
    
    payroll_data = calculate_payroll(employee_id, start_date, end_date)
    if not payroll_data:
        return jsonify({"error": "Employee not found"}), 404
    
    return jsonify(payroll_data)

@app.route('/api/payroll/<employee_id>/csv')
def export_payroll_csv(employee_id):
    """Export payroll as CSV"""
    start_date = request.args.get('start_date', '2025-03-31')
    end_date = request.args.get('end_date', '2025-06-14')
    
    payroll_data = calculate_payroll(employee_id, start_date, end_date)
    if not payroll_data:
        return jsonify({"error": "Employee not found"}), 404
    
    # Create CSV
    output = io.StringIO()
    writer = csv.writer(output)
    
    # Header
    writer.writerow([
        'Employee ID', 'Employee Name', 'Period Start', 'Period End',
        'Gross Pay', 'Federal Tax', 'State Tax', 'Social Security', 
        'Medicare', 'Net Pay'
    ])
    
    # Data
    writer.writerow([
        payroll_data['employee_id'],
        payroll_data['employee_name'],
        payroll_data['period_start'],
        payroll_data['period_end'],
        f"${payroll_data['gross_pay']:.2f}",
        f"${payroll_data['federal_tax']:.2f}",
        f"${payroll_data['state_tax']:.2f}",
        f"${payroll_data['social_security']:.2f}",
        f"${payroll_data['medicare']:.2f}",
        f"${payroll_data['net_pay']:.2f}"
    ])
    
    csv_content = output.getvalue()
    output.close()
    
    return csv_content, 200, {
        'Content-Type': 'text/csv',
        'Content-Disposition': f'attachment; filename=payroll_{employee_id}.csv'
    }

if __name__ == '__main__':
    app.run(debug=True)
