import configuration
import requests
import data

def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOCS)


#Создание нового заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_NEW_ORDER, json=body, headers=data.headers)


response = post_new_order(data.order_body)
print(response.json())


#Получение номера заказа
def get_track_number():
    #response = post_new_order(data.order_body)
    track_number = response.json().get('track')
    return track_number


print(get_track_number())
