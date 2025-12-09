// Weather
document.getElementById("weather-btn").addEventListener("click", async () => {
    const res = await fetch(`/api/weather`);
    const data = await res.json();

    const weatherBox = document.getElementById("weather-result");

    if (data.error) {
        weatherBox.innerHTML = `<p style="color: red;">Error: ${data.error}</p>`;
        return;
    }

    weatherBox.innerHTML = `
        <div class="result-box">
            <h3>Weather in ${data.city}, ${data.country}</h3>
            <p><strong>Temperature:</strong> ${data.temperature}°C</p>
            <p><strong>Feels Like:</strong> ${data.feels_like}°C</p>
            <p><strong>Condition:</strong> ${data.condition}</p>
            <p><strong>Humidity:</strong> ${data.humidity}%</p>
            <p><strong>Wind Speed:</strong> ${data.wind_speed} kph</p>
        </div>
    `;
});

// News
document.getElementById("news-btn").addEventListener("click", async () => {
    const category = document.getElementById("news-category").value;
    const res = await fetch(`/api/news?category=${encodeURIComponent(category)}`);
    const data = await res.json();

    const newsBox = document.getElementById("news-result");
    newsBox.innerHTML = "";

    if (data.error) {
        newsBox.innerHTML = `<p style="color: red;">Error: ${data.error}</p>`;
        return;
    }

    const articles = data.articles || [];
    if (articles.length === 0) {
        newsBox.innerHTML = "<p>No articles found.</p>";
        return;
    }

    articles.forEach(article => {
        newsBox.innerHTML += `
            <div class="news-item">
                <h4>${article.title}</h4>
                <p><small>Source: ${article.source}</small></p>
                <p>${article.description}</p>
                <a href="${article.url}" target="_blank">Read More</a>
            </div>
        `;
    });
});
