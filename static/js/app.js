document.getElementById("weather-btn").addEventListener("click", async () => {
    let city = document.getElementById("city-input").value.trim();

    if (!city) {
        alert("Please enter a city name");
        return;
    }

    // Clear old data instantly (important)
    document.getElementById("weather-result").innerHTML = "<p>Loading...</p>";

    let res = await fetch(`/api/weather?city=${encodeURIComponent(city)}`);
    let data = await res.json();

    // ❌ Show error (City not found)
    if (data.error) {
        document.getElementById("weather-result").innerHTML =
            `<p style="color: red; font-weight: bold;">${data.error}</p>`;
        return;
    }

    // ✅ Show correct weather
    document.getElementById("weather-result").innerHTML = `
        <div class="weather-result">
            <h3>Weather in '${data.city}'</h3>
            <p><strong>Temperature:</strong> ${data.temperature}°C</p>
            <p><strong>Feels Like:</strong> ${data.feels_like}°C</p>
            <p><strong>Condition:</strong> ${data.condition}</p>
            <p><strong>Humidity:</strong> ${data.humidity}%</p>
            <p><strong>Wind Speed:</strong> ${data.wind_speed} kph</p>
        </div>
    `;
});


// ---------------------------
// NEWS BTN
// ---------------------------
document.getElementById("news-btn").addEventListener("click", async () => {
    let category = document.getElementById("news-category").value;

    document.getElementById("news-result").innerHTML = "<p>Loading...</p>";

    let res = await fetch(`/api/news?category=${encodeURIComponent(category)}`);
    let data = await res.json();

    if (data.error) {
        document.getElementById("news-result").innerHTML =
            `<p style="color: red; font-weight: bold;">${data.error}</p>`;
        return;
    }

    let articles = data.articles || [];
    let box = document.getElementById("news-result");
    box.innerHTML = "";

    if (articles.length === 0) {
        box.innerHTML = "<p>No articles found.</p>";
        return;
    }

    articles.forEach(a => {
        box.innerHTML += `
            <div class="news-item">
                <h4>${a.title}</h4>
                <p><small>Source: ${a.source}</small></p>
                <p>${a.description}</p>
                <a href="${a.url}" target="_blank">Read More</a>
            </div>
        `;
    });
});
