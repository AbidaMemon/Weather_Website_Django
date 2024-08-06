document.addEventListener('DOMContentLoaded', function () {
   
    function updateClock() {
        const now = new Date();
        document.getElementById('time').textContent = now.toLocaleTimeString();
    }
    setInterval(updateClock, 1000);

    
   
});
