from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    weather = None
    news = None
    if request.method == 'POST':
        city = request.form['city']
        weather = get_weather(city)
        news = get_news()
        if not weather:
            print("Ошибка получения погоды")
        if not news:
            print("Ошибка получения новостей")
    return render_template('index.html', weather=weather, news=news)

def get_weather(city):
    api_key = 'fa5b1d308594ef4e2f4fd895403f0a68'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Ошибка запроса погоды: {response.status_code}")
        return None

def get_news():
    api_key = 'bd1bd521f8664e7585dbeb7b2ca8318c'
    url = f'https://newsapi.org/v2/everything?q=Apple&sortBy=popularity&apiKey={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('articles', [])
    else:
        print(f"Ошибка запроса новостей: {response.status_code}")
        return []

if __name__ == '__main__':
    app.run(debug=True)

