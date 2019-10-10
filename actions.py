# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# 天气查询 API https://www.tianqiapi.com

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests


class ActionWeatherSearch(Action):

    def name(self) -> Text:
        return "action_weather_search"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        payload = {"appid": "32999947", "appsecret": "ni7TskDn"}
        city = tracker.get_slot("city")
        print('action_weather_search: ' + city)

        if city is not None:
            payload["city"] = city

        r = requests.get("https://www.tianqiapi.com/api/", params=payload)

        weather = r.json()["data"][0]
        weather_info = "当前: " + weather["wea"] + ", 温度" + weather["tem"] + ", 白天" + weather["tem1"] + ", 晚上" + \
                       weather["tem2"] + ". 空气质量: " + weather["air_level"] + ". " + weather["air_tips"]

        dispatcher.utter_message(weather_info)

        return []
