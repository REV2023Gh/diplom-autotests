#Елена Ржеутская, 12-когорта, Дипломный проект
import sender_stand_request
import requests
import data
import configuration


#Автотест получение заказа по номеру.
def test_get_order_by_track():
    track_number = sender_stand_request.get_track_number()
    new_params = f'{track_number}'
    requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK, params=new_params)

    order_response = test_get_order_by_track()
    assert order_response.status_code == 200, f"Ошибка {order_response.status.code}"
    order = order_response.json()
    print(order)




