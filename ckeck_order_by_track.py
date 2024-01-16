#Елена Ржеутская, 12-когорта, Дипломный проект
import sender_stand_request
import requests
import data
import configuration


#Автотест получение заказа по номеру.
def test_get_order_by_track():
    track_number = sender_stand_request.get_track_number().get('track')
    print('Номер заказа:', track_number)

    order_response = sender_stand_request.get_order_by_track(track_number)

    assert order_response.status_code == 200, f'Ошибка {order_response.status.code}'
    order = order_response.json()
    print('Ваш заказ', order)



