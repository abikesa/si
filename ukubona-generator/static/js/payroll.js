document.addEventListener('DOMContentLoaded', () => {
  // Configuration
  const FEDERAL_TAX_RATE = 0.12;
  const SOCIAL_SECURITY_RATE = 0.062;
  const MEDICARE_RATE = 0.0145;
  const STATE_TAX_RATE = 0.05;
  
  // DOM Elements
  const calculateBtn = document.getElementById('calculate-btn');
  const exportBtn = document.getElementById('export-btn');
  const hourlyRateInput = document.getElementById('hourly-rate');
  const weeklyHoursInput = document.getElementById('weekly-hours');
  
  // Initialize with current pay period
  updatePayPeriodDisplay();
  
  // Event Listeners
  calculateBtn.addEventListener('click', calculatePaystub);
  exportBtn.addEventListener('click', exportPaystub);
  
  // Calculate on initial load
  calculatePaystub();
  
  function updatePayPeriodDisplay() {
    const now = new Date();
    const startDate = new Date(now.getFullYear(), now.getMonth(), 1);
    const endDate = new Date(now.getFullYear(), now.getMonth() + 1, 0);
    
    document.getElementById('pay-period').value = 
      `${formatDate(startDate)} to ${formatDate(endDate)}`;
  }
  
  function formatDate(date) {
    return date.toLocaleDateString('en-US', { 
      year: 'numeric', 
      month: 'short', 
      day: 'numeric' 
    });
  }
  
  function calculatePaystub() {
    const hourlyRate = parseFloat(hourlyRateInput.value);
    const weeklyHours = parseFloat(weeklyHoursInput.value);
    
    // Calculate weeks in current month
    const now = new Date();
    const startDate = new Date(now.getFullYear(), now.getMonth(), 1);
    const endDate = new Date(now.getFullYear(), now.getMonth() + 1, 0);
    const daysInMonth = endDate.getDate();
    const weeksInMonth = daysInMonth / 7;
    
    // Calculate gross pay
    const grossPay = hourlyRate * weeklyHours * weeksInMonth;
    
    // Calculate deductions
    const federalTax = grossPay * FEDERAL_TAX_RATE;
    const socialSecurity = grossPay * SOCIAL_SECURITY_RATE;
    const medicare = grossPay * MEDICARE_RATE;
    const stateTax = grossPay * STATE_TAX_RATE;
    const netPay = grossPay - federalTax - socialSecurity - medicare - stateTax;
    
    // Update UI
    document.getElementById('gross-pay').textContent = `$${grossPay.toFixed(2)}`;
    document.getElementById('federal-tax').textContent = `$${federalTax.toFixed(2)}`;
    document.getElementById('ss-tax').textContent = `$${socialSecurity.toFixed(2)}`;
    document.getElementById('medicare').textContent = `$${medicare.toFixed(2)}`;
    document.getElementById('state-tax').textContent = `$${stateTax.toFixed(2)}`;
    document.getElementById('net-pay').textContent = `$${netPay.toFixed(2)}`;
  }
  
  function exportPaystub() {
    const rows = [
      ['Description', 'Amount'],
      ['Gross Pay', document.getElementById('gross-pay').textContent],
      ['Federal Tax', document.getElementById('federal-tax').textContent],
      ['Social Security', document.getElementById('ss-tax').textContent],
      ['Medicare', document.getElementById('medicare').textContent],
      ['State Tax', document.getElementById('state-tax').textContent],
      ['Net Pay', document.getElementById('net-pay').textContent]
    ];
    
    const csvContent = rows.map(row => row.join(',')).join('\n');
    const blob = new Blob([csvContent], { type: 'text/csv' });
    const url = URL.createObjectURL(blob);
    
    const a = document.createElement('a');
    a.href = url;
    a.download = `ukubona_paystub_${new Date().toISOString().slice(0,10)}.csv`;
    a.click();
    
    URL.revokeObjectURL(url);
  }
});
