/**
 * Windows-style calculator logic.
 */
(function () {
  let currentVal = '0';
  let storedVal = null;
  let operator = null;
  let waitingForOperand = false;
  let expression = '';

  function updateDisplay() {
    const main = document.getElementById('calc-display');
    const expr = document.getElementById('calc-expression');
    if (main) main.textContent = currentVal;
    if (expr) expr.textContent = expression;
  }

  function press(val) {
    switch (val) {
      case 'C':
        currentVal = '0'; storedVal = null; operator = null;
        waitingForOperand = false; expression = '';
        break;

      case 'CE':
        currentVal = '0';
        break;

      case '⌫':
        if (waitingForOperand) break;
        currentVal = currentVal.length > 1 ? currentVal.slice(0, -1) : '0';
        break;

      case '+': case '−': case '×': case '÷':
        if (storedVal !== null && !waitingForOperand) {
          currentVal = String(calculate(storedVal, parseFloat(currentVal), operator));
        }
        storedVal = parseFloat(currentVal);
        operator = val;
        expression = currentVal + ' ' + val;
        waitingForOperand = true;
        break;

      case '=':
        if (storedVal !== null && operator) {
          expression = storedVal + ' ' + operator + ' ' + currentVal + ' =';
          currentVal = String(calculate(storedVal, parseFloat(currentVal), operator));
          storedVal = null; operator = null; waitingForOperand = true;
        }
        break;

      case '.':
        if (waitingForOperand) { currentVal = '0.'; waitingForOperand = false; break; }
        if (!currentVal.includes('.')) currentVal += '.';
        break;

      case '%':
        currentVal = String(parseFloat(currentVal) / 100);
        waitingForOperand = true;
        break;

      case '1/x':
        if (parseFloat(currentVal) === 0) { currentVal = 'Cannot divide by zero'; waitingForOperand = true; break; }
        currentVal = String(1 / parseFloat(currentVal));
        waitingForOperand = true;
        break;

      case 'x²':
        currentVal = String(Math.pow(parseFloat(currentVal), 2));
        waitingForOperand = true;
        break;

      case '√x':
        currentVal = parseFloat(currentVal) < 0 ? 'Invalid input' : String(Math.sqrt(parseFloat(currentVal)));
        waitingForOperand = true;
        break;

      case '+/−':
        currentVal = currentVal.startsWith('-') ? currentVal.slice(1) : '-' + currentVal;
        break;

      default:
        // Digit
        if (waitingForOperand) { currentVal = val; waitingForOperand = false; }
        else currentVal = currentVal === '0' ? val : currentVal + val;
    }
    updateDisplay();
  }

  function calculate(a, b, op) {
    switch (op) {
      case '+': return round(a + b);
      case '−': return round(a - b);
      case '×': return round(a * b);
      case '÷': return b === 0 ? 'Cannot divide by zero' : round(a / b);
      default: return b;
    }
  }

  function round(n) {
    return parseFloat(n.toFixed(10));
  }

  window.Calculator = { press };

  // --- Draggable panel ---
  window.openCalculator = function () {
    document.getElementById('calc-panel').style.display = 'block';
  };

  window.closeCalculator = function () {
    document.getElementById('calc-panel').style.display = 'none';
  };

  (function makeDraggable() {
    let dragging = false, startX, startY, origLeft, origTop;

    document.addEventListener('DOMContentLoaded', function () {
      const panel  = document.getElementById('calc-panel');
      const handle = document.getElementById('calc-drag-handle');
      if (!handle) return;

      handle.addEventListener('mousedown', function (e) {
        if (e.target.tagName === 'BUTTON') return;
        dragging = true;
        const rect = panel.getBoundingClientRect();
        panel.style.right  = 'auto';
        panel.style.bottom = 'auto';
        panel.style.left   = rect.left + 'px';
        panel.style.top    = rect.top  + 'px';
        origLeft = rect.left;
        origTop  = rect.top;
        startX   = e.clientX;
        startY   = e.clientY;
        handle.style.cursor = 'grabbing';
        e.preventDefault();
      });

      document.addEventListener('mousemove', function (e) {
        if (!dragging) return;
        panel.style.left = (origLeft + e.clientX - startX) + 'px';
        panel.style.top  = (origTop  + e.clientY - startY) + 'px';
      });

      document.addEventListener('mouseup', function () {
        if (dragging) { dragging = false; handle.style.cursor = 'grab'; }
      });
    });
  })();
})();
