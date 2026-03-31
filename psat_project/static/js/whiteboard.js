/**
 * Simple whiteboard using HTML Canvas — draggable & resizable panel.
 */
(function () {
  let canvas, ctx, drawing = false, lastX = 0, lastY = 0;
  let penColor = '#000000', penSize = 3;
  let initialized = false;

  // ---- Canvas setup (clears drawing) ----
  function setupCanvas() {
    if (!canvas) return;
    const panel  = document.getElementById('whiteboard-panel');
    const panelW = panel ? panel.offsetWidth : 480;

    let canvasH = 300;
    if (panel && panel.style.height) {
      const dragH    = document.getElementById('wb-drag-handle')  ? document.getElementById('wb-drag-handle').offsetHeight  : 44;
      const toolbarH = document.querySelector('.wb-toolbar')       ? document.querySelector('.wb-toolbar').offsetHeight       : 44;
      canvasH = Math.max(150, parseInt(panel.style.height) - dragH - toolbarH);
    }

    canvas.width  = panelW;
    canvas.height = canvasH;
    ctx.fillStyle = '#ffffff';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
  }

  // ---- Init (runs once) ----
  function init() {
    if (initialized) return;

    canvas = document.getElementById('whiteboard-canvas');
    if (!canvas) return;
    ctx = canvas.getContext('2d');

    canvas.addEventListener('mousedown', startDraw);
    canvas.addEventListener('mousemove', draw);
    canvas.addEventListener('mouseup',   stopDraw);
    canvas.addEventListener('mouseleave', stopDraw);

    canvas.addEventListener('touchstart', (e) => { e.preventDefault(); startDraw(e.touches[0]); }, { passive: false });
    canvas.addEventListener('touchmove',  (e) => { e.preventDefault(); draw(e.touches[0]); },      { passive: false });
    canvas.addEventListener('touchend', stopDraw);

    window.addEventListener('resize', setupCanvas);

    initialized = true;
    setupCanvas();
  }

  // ---- Drawing ----
  function getPos(e) {
    const rect = canvas.getBoundingClientRect();
    return {
      x: (e.clientX || e.pageX) - rect.left,
      y: (e.clientY || e.pageY) - rect.top,
    };
  }

  function startDraw(e) {
    drawing = true;
    const pos = getPos(e);
    lastX = pos.x; lastY = pos.y;
  }

  function draw(e) {
    if (!drawing) return;
    const pos = getPos(e);
    ctx.beginPath();
    ctx.moveTo(lastX, lastY);
    ctx.lineTo(pos.x, pos.y);
    ctx.strokeStyle = penColor;
    ctx.lineWidth   = penSize;
    ctx.lineCap     = 'round';
    ctx.lineJoin    = 'round';
    ctx.stroke();
    lastX = pos.x; lastY = pos.y;
  }

  function stopDraw() { drawing = false; }

  // ---- Public API ----
  window.Whiteboard = {
    init,
    clear()    { if (ctx) { ctx.fillStyle = '#ffffff'; ctx.fillRect(0, 0, canvas.width, canvas.height); } },
    setColor(c){ penColor = c; },
    setSize(s) { penSize  = parseInt(s); },
  };

  // ---- Open / Close ----
  window.openWhiteboard = function () {
    const panel = document.getElementById('whiteboard-panel');
    panel.style.display = 'block';
    init();          // no-op after first call
    // canvas retains its drawing when hidden via display:none — no reset needed
  };

  window.closeWhiteboard = function () {
    document.getElementById('whiteboard-panel').style.display = 'none';
  };

  // ---- Drag (header) ----
  (function makeDraggable() {
    let dragging = false, startX, startY, origLeft, origTop;

    document.addEventListener('DOMContentLoaded', function () {
      const panel  = document.getElementById('whiteboard-panel');
      const handle = document.getElementById('wb-drag-handle');
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
      const panel = document.getElementById('whiteboard-panel');
      const grip  = document.getElementById('wb-resize-handle');
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
        panel.style.width  = Math.max(380, startW + e.clientX - startX) + 'px';
        panel.style.height = Math.max(250, startH + e.clientY - startY) + 'px';
        setupCanvas();   // clears drawing — acceptable for a scratchpad
      });

      document.addEventListener('mouseup', function () { resizing = false; });
    });
  })();
})();
