# Tech Utils - Weather & News Application

A modern, responsive web application that provides real-time weather information and top news headlines in one convenient place. Built with Flask backend and vanilla JavaScript frontend.
## 🌟 Features

### Weather Information
- **Real-time Weather Data**: Get current weather conditions for any city worldwide
- **Detailed Metrics**:
  - Current temperature and "feels like" temperature
  - Weather condition description
  - Humidity percentage
  - Wind speed
  - Atmospheric pressure
- **Easy Search**: Simple city name input with instant results

### News Headlines
- **Multi-category News**: Browse news across different categories
- **Categories Supported**:
  - General
  - Technology
  - Business
  - Health
  - Science
- **Multiple Sources**: Aggregates news from NewsData.io and NewsAPI.org
- **Rich Display**: Shows title, source, and clickable links to full articles

## 🏗️ Project Structure

```
tech_utils/
├── app.py                      # Flask main application & API routes
├── weather_app.py             # Weather API integration
├── news_fetcher.py            # News API integration
│
├── templates/
│   └── index.html             # HTML template with UI
│
├── static/
│   ├── css/
│   │   └── style.css          # Modern responsive styling
│   ├── js/
│   │   └── app.js             # Frontend JavaScript logic
│   └── images/                # Images & icons directory
│
└── README.md                  # Project documentation
```

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)
- Modern web browser

### Installation

1. **Clone the repository**:
```bash
git clone https://github.com/shristijais2710-eng/tech_utils.git
cd tech_utils
```

2. **Create a virtual environment**:
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**:
```bash
pip install flask requests python-dotenv
```

4. **Set up API Keys** (Optional - uses free tier by default):
Create a `.env` file in the project root:
```
WEATHER_API_KEY=your_weather_api_key_here
NEWS_API_KEY=your_news_api_key_here
```

### Running the Application

1. **Start the Flask server**:
```bash
python app.py
```

2. **Open in browser**:
```
http://localhost:5000
```

The application will be available at:
- Local: http://127.0.0.1:5000
- Network: http://0.0.0.0:5000

## 📚 API Documentation

### Weather Endpoint

**Request:**
```
GET /api/weather?city=<city_name>
```

**Example:**
```bash
curl "http://localhost:5000/api/weather?city=London"
```

**Response:**
```json
{
  "city": "London",
  "country": "UK",
  "temperature": "15",
  "feels_like": "14",
  "condition": "Partly Cloudy",
  "humidity": "65",
  "wind_speed": "12",
  "pressure": "1013"
}
```

### News Endpoint

**Request:**
```
GET /api/news?category=<category>
```

**Categories:** `general`, `technology`, `business`, `health`, `science`

**Example:**
```bash
curl "http://localhost:5000/api/news?category=technology"
```

**Response:**
```json
{
  "articles": [
    {
      "title": "New AI Technology Released",
      "source": "NewsAPI.org",
      "description": "Article description...",
      "url": "https://example.com/article",
      "published_at": "2025-12-05"
    }
  ]
}
```

## 📁 File Descriptions

### `app.py`
Main Flask application file containing:
- Flask app initialization
- Route definitions (`/`, `/api/weather`, `/api/news`)
- Request validation and data formatting
- Error handling

### `weather_app.py`
Weather API integration module:
- Connects to WeatherAPI.com
- Retrieves current weather data
- Handles API errors gracefully
- Returns formatted weather dictionary

### `news_fetcher.py`
News API integration module:
- NewsData.io integration
- NewsAPI.org integration
- Historical news fetching
- Data parsing and formatting

### `templates/index.html`
HTML template featuring:
- Responsive layout
- Weather input section
- News category selector
- Results display areas
- Flask Jinja2 template syntax for static files

### `static/css/style.css`
Modern stylesheet with:
- Responsive grid layout
- Gradient backgrounds
- Smooth animations
- Mobile-first design
- Color variables for easy customization
- Media queries for all screen sizes

### `static/js/app.js`
Client-side JavaScript handling:
- Event listeners for user interactions
- Fetch API calls to backend endpoints
- JSON response parsing
- Dynamic HTML rendering
- Error handling and validation
- Loading states

## 🎨 Design Features

- **Responsive Design**: Works perfectly on desktop, tablet, and mobile
- **Modern UI**: Clean, intuitive interface with smooth interactions
- **Gradient Background**: Visually appealing purple gradient
- **Loading States**: Visual feedback while fetching data
- **Error Handling**: User-friendly error messages
- **Accessibility**: Semantic HTML and keyboard support

## 🔧 Technologies Used

### Backend
- **Python 3.7+**: Programming language
- **Flask**: Lightweight web framework
- **Requests**: HTTP library for API calls
- **python-dotenv**: Environment variable management

### Frontend
- **HTML5**: Page structure
- **CSS3**: Styling with modern features (Grid, Flexbox, Gradients)
- **Vanilla JavaScript**: No frameworks, lightweight and fast

### APIs
- **WeatherAPI.com**: Weather data
- **NewsData.io**: News articles
- **NewsAPI.org**: Alternative news source

## 📊 How It Works

### Weather Flow
1. User enters city name in the input field
2. JavaScript fetches from `/api/weather?city=...`
3. Backend calls WeatherAPI.com
4. Response is formatted and returned to frontend
5. Data is displayed in a formatted card

### News Flow
1. User selects a category from dropdown
2. JavaScript fetches from `/api/news?category=...`
3. Backend calls both NewsData.io and NewsAPI.org
4. Results are combined and formatted
5. Articles are displayed with title, source, and link

## 🐛 Troubleshooting

### "City not found" error
- Check spelling of the city name
- Try using a different city
- Use city,country format (e.g., "London,UK")

### "No news articles found"
- Ensure API keys are valid
- Try a different category
- Check internet connection

### Port 5000 already in use
```bash
# Use a different port
python app.py --port=5001
```

Or modify in `app.py`:
```python
app.run(debug=True, host='0.0.0.0', port=5001)
```

### CORS Issues
If accessing from a different domain, CORS headers may be needed. Install Flask-CORS:
```bash
pip install flask-cors
```

## 🔐 Security Notes

- API keys are stored in `.env` (not committed to git)
- `.gitignore` should include `.env` and `__pycache__`
- Never commit sensitive information
- Use environment variables for production

## 📈 Future Enhancements

- [ ] User authentication system
- [ ] Save favorite cities
- [ ] Weather forecast (5-day, 10-day)
- [ ] Search history
- [ ] Dark mode toggle
- [ ] Multi-language support
- [ ] Caching for faster load times
- [ ] Mobile app version
- [ ] Social sharing features
- [ ] Email notifications

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

Created by **Rajat** for Tech Utils Project

## 📞 Support

For issues and questions:
- Open an issue on GitHub
- Check existing documentation
- Review API documentation

---

**Last Updated**: December 5, 2025

**Version**: 1.0.0

**Status**: ✅ Production Ready
