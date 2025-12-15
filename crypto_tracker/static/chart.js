const ctx = document.getElementById('cryptoChart').getContext('2d');
let chart;
const refreshInterval = 10; // seconds
let countdown = refreshInterval;

// Fetch coin data from CoinGecko
async function fetchData(coin = 'bitcoin', days = '1') {
  try {
    const res = await fetch(`https://api.coingecko.com/api/v3/coins/${coin}/market_chart?vs_currency=usd&days=${days}`);
    const json = await res.json();
    const labels = json.prices.map(p => new Date(p[0]).toLocaleTimeString());
    const prices = json.prices.map(p => p[1]);
    return {
      labels,
      prices,
      current_price: prices[prices.length - 1],
      high_24h: Math.max(...prices),
      low_24h: Math.min(...prices),
      last_fetched: new Date().toLocaleTimeString()
    };
  } catch(e){
    console.error("Fetch error:", e);
    return null;
  }
}

// Update dashboard & chart
async function updateDashboard() {
  const coin = document.getElementById('coinSelect').value;
  const data = await fetchData(coin);
  if (!data) return;

  document.getElementById('lastUpdated').innerText = "Last updated: " + data.last_fetched;
  document.getElementById('currentPrice').innerText = "Current: $" + data.current_price.toLocaleString();
  document.getElementById('highPrice').innerText = "High 24h: $" + data.high_24h.toLocaleString();
  document.getElementById('lowPrice').innerText = "Low 24h: $" + data.low_24h.toLocaleString();

  countdown = refreshInterval;

  if (!chart) {
    chart = new Chart(ctx, {
      type: 'line',
      data: { labels: data.labels, datasets: [{
        label: coin.toUpperCase() + " Price (USD)",
        data: data.prices,
        borderColor: '#f39c12',
        backgroundColor: 'rgba(243,156,18,0.2)',
        tension: 0.3,
        pointRadius: 0
      }] },
      options: {
        responsive: true,
        animation: { duration: 800 },
        interaction: { mode: 'index', intersect: false },
        scales: {
          x: { ticks: { color: '#8b949e' }, grid: { color: '#30363d' } },
          y: { ticks: { color: '#8b949e' }, grid: { color: '#30363d' } }
        },
        plugins: { legend: { labels: { color: '#c9d1d9' } } }
      }
    });
  } else {
    chart.data.labels = data.labels;
    chart.data.datasets[0].data = data.prices;
    chart.data.datasets[0].label = coin.toUpperCase() + " Price (USD)";
    chart.update();
  }
}

// Countdown timer
function startCountdown() {
  setInterval(() => {
    countdown--;
    if (countdown < 0) countdown = 0;
    document.getElementById('nextUpdate').innerText = "Next refresh in: " + countdown + "s";
  }, 1000);
}

// Init
updateDashboard();
startCountdown();
setInterval(updateDashboard, refreshInterval * 1000);

// Update when coin changes
document.getElementById('coinSelect').addEventListener('change', updateDashboard);