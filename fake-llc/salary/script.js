// Configuration
const HOURLY_RATE = 25.00;
const WEEKLY_HOURS = 23;
const BACKPAY_START = new Date('2025-03-31');
const BACKPAY_END = new Date('2025-06-14');
const PAYDAY = new Date('2025-06-21');
const EMPLOYEE_NAME = "UKB-8160";

// Tax rates
const FEDERAL_TAX_RATE = 0.12;
const SOCIAL_SECURITY_RATE = 0.062;
const MEDICARE_RATE = 0.0145;
const STATE_TAX_RATE = 0.05;

// Calculate backpay weeks
function getBackpayWeeks(start, end) {
  const msPerWeek = 7 * 24 * 60 * 60 * 1000;
  return Math.round((end - start) / msPerWeek) + 1;
}

// Calculate paystub values
function calculatePaystub(weeks) {
  const gross = weeks * WEEKLY_HOURS * HOURLY_RATE;
  const federal = gross * FEDERAL_TAX_RATE;
  const ss = gross * SOCIAL_SECURITY_RATE;
  const medicare = gross * MEDICARE_RATE;
  const state = gross * STATE_TAX_RATE;
  const net = gross - federal - ss - medicare - state;
  
  return {
    gross: gross.toFixed(2),
    federal: federal.toFixed(2),
    ss: ss.toFixed(2),
    medicare: medicare.toFixed(2),
    state: state.toFixed(2),
    net: net.toFixed(2)
  };
}

// Display paystub
function displayPaystub() {
  const weeks = getBackpayWeeks(BACKPAY_START, BACKPAY_END);
  const paystub = calculatePaystub(weeks);
  
  document.getElementById('employee-name').textContent = EMPLOYEE_NAME;
  document.getElementById('pay-date').textContent = PAYDAY.toISOString().split('T')[0];
  document.getElementById('gross-pay').textContent = `$${paystub.gross}`;
  document.getElementById('federal-tax').textContent = `$${paystub.federal}`;
  document.getElementById('ss-tax').textContent = `$${paystub.ss}`;
  document.getElementById('medicare').textContent = `$${paystub.medicare}`;
  document.getElementById('state-tax').textContent = `$${paystub.state}`;
  document.getElementById('net-pay').textContent = `$${paystub.net}`;
}

// Load tasks and paystub when page loads
document.addEventListener('DOMContentLoaded', () => {
  displayPaystub();
  
  fetch('data/tasks.csv')
    .then(response => response.text())
    .then(text => {
      const rows = text.trim().split('\n').slice(1);
      const tbody = document.querySelector('#task-table tbody');
      const now = new Date();

      rows.forEach(row => {
        const [task, created, due, done] = row.split(',');
        const dueDate = new Date(due);
        let deltaText = '';
        let deltaClass = '';   

        if (!isNaN(dueDate)) {
          const diffMs = dueDate - now;
          const days = Math.ceil(diffMs / (1000 * 60 * 60 * 24));
          deltaText = days > 0 ? `in ${days}d` : `${-days}d ago`;
          deltaClass = done === 'true' ? 'done' : (days < 0 ? 'overdue' : 'upcoming');
        } else {
          deltaText = 'TBD';
          deltaClass = 'upcoming';
        }

        const rowEl = document.createElement('tr');
        const status = done === 'true' ? '✔' : '';
        rowEl.innerHTML = `
          <td class="${done === 'true' ? 'done' : ''}">${status}</td>
          <td>${task}</td>
          <td>${created}</td>
          <td>${due}</td>
          <td class="${deltaClass}">${deltaText}</td>
        `;
        tbody.appendChild(rowEl);
      });
    });
});