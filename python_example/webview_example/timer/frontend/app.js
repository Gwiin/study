const timeEl = document.getElementById('time');
const dateEl = document.getElementById('date');

async function refreshClock() {
    try {
        const response = await fetch('/api/clock', { cache: 'no-store' });
        if (!response.ok) {
            return;
        }

        const payload = await response.json();
        timeEl.textContent = payload.time;
        dateEl.textContent = payload.date;
    } catch (error) {
        // Network hiccups should not crash the demo UI.
    }
}

refreshClock();
setInterval(refreshClock, 1000);