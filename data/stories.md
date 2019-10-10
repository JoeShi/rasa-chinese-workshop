## weather + date + city
* weather_search{"date": "今天", "city": "北京"}
  - action_weather_search
  
## weather + date 1
* weather_search{"date": "今天"}
  - action_weather_search

## weather + date 2
* weather_search{"date": "周五"}
  - action_weather_search
  
## weather + city
* weather_search{"city": "青岛"}
  - action_weather_search

## greet + weather(city, date)
* greet
  - utter_greet_weather
* weather_search{"date": "今天", "city": "北京"}
  - action_weather_search
   
## greet + weather(date)
* greet
  - utter_greet_weather
* weather_search{"date": "下周四"}
  - action_weather_search
  