import configuration
import requests
import data

def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOCS)


#Создание нового заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_NEW_ORDER, json=body, headers=data.headers)


#Получение номера заказа
def get_track_number():
    response = post_new_order(data.order_body)
    track_number = response.json()
    return track_number


#Получение заказа
def get_order_by_track(track_number):
    get_order = (configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK + f'{track_number}')
    return requests.get(get_order)
