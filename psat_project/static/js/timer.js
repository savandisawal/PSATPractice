/**
 * Countdown timer for PSAT tests.
 * Usage: new CountdownTimer(remainingSeconds, onExpire)
 */
class CountdownTimer {
  constructor(seconds, onExpire) {
    this.remaining = seconds;
    this.onExpire = onExpire;
    this.interval = null;
    this.display = document.getElementById('timer-display');
    this._render();
  }

  start() {
    if (this.interval) return;
    this.interval = setInterval(() => {
      this.remaining--;
      this._render();
      if (this.remaining <= 0) {
        clearInterval(this.interval);
        this.interval = null;
        this.onExpire();
      }
    }, 1000);
  }

  pause() {
    clearInterval(this.interval);
    this.interval = null;
  }

  elapsed() {
    return window._testDuration - this.remaining;
  }

  _render() {
    const m = Math.floor(this.remaining / 60);
    const s = this.remaining % 60;
    const text = `${String(m).padStart(2, '0')}:${String(s).padStart(2, '0')}`;
    if (this.display) {
      this.display.textContent = text;
      // Color coding
      if (this.remaining <= 60) {
        this.display.className = 'timer-danger';
      } else if (this.remaining <= 300) {
        this.display.className = 'timer-warning';
      } else {
        this.display.className = 'timer-normal';
      }
    }
  }
}
