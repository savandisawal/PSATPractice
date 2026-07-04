/**
 * Desmos graphing calculator panel — draggable & resizable.
 * The Desmos API script is lazy-loaded the first time the panel opens,
 * so the test page itself stays fast.
 */
(function () {
  // Desmos' published demo API key — fine for local/classroom use.
  const DESMOS_SRC = 'https://www.desmos.com/api/v1.11/calculator.js?apiKey=dcb31709b452b1cf9dc26972add0fda6';

  let desmos = null;       // Desmos calculator instance
  let loading = false;

  function initDesmos() {
    const elt = document.getElementById('desmos-calc');
    if (!elt || desmos) return;
    desmos = Desmos.GraphingCalculator(elt, {
      expressions: true,
      keypad: true,
      settingsMenu: false,
      border: false,
      expressionsCollapsed: false,
    });
  }

  function loadDesmosScript() {
    if (window.Desmos) { initDesmos(); return; }
    if (loading) return;
    loading = true;

    const script = document.createElement('script');
    script.src = DESMOS_SRC;
    script.onload = () => { loading = false; initDesmos(); };
    script.onerror = () => {
      loading = false;
      const elt = document.getElementById('desmos-calc');
      if (elt) {
        elt.innerHTML = '<div class="desmos-fallback">⚠️ Could not load the Desmos calculator.<br>Check your internet connection and reopen this panel.</div>';
      }
    };
    document.head.appendChild(script);
  }

  // ---- Open / Close ----
  window.openCalculator = function () {
    const panel = document.getElementById('calc-panel');
    panel.style.display = 'flex';
    if (!desmos) {
      loadDesmosScript();
    } else {
      desmos.resize();
    }
  };

  window.closeCalculator = function () {
    document.getElementById('calc-panel').style.display = 'none';
  };

  // ---- Drag (header) ----
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

  // ---- Resize (bottom-right grip) ----
  (function makeResizable() {
    let resizing = false, startX, startY, startW, startH;

    document.addEventListener('DOMContentLoaded', function () {
      const panel = document.getElementById('calc-panel');
      const grip  = document.getElementById('calc-resize-handle');
      if (!grip) return;

      grip.addEventListener('mousedown', function (e) {
        resizing = true;
        const rect = panel.getBoundingClientRect();
        panel.style.right  = 'auto';
        panel.style.bottom = 'auto';
        panel.style.left   = rect.left + 'px';
        panel.style.top    = rect.top  + 'px';
        startX = e.clientX;
        startY = e.clientY;
        startW = rect.width;
        startH = rect.height;
        e.preventDefault();
        e.stopPropagation();
      });

      document.addEventListener('mousemove', function (e) {
        if (!resizing) return;
        panel.style.width  = Math.max(340, startW + e.clientX - startX) + 'px';
        panel.style.height = Math.max(300, startH + e.clientY - startY) + 'px';
        if (desmos) desmos.resize();
      });

      document.addEventListener('mouseup', function () { resizing = false; });
    });
  })();
})();
