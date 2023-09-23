import configuration
import requests
import data

# Анна Фролова, 8-а когорта — Финальный проект. Инженер по тестированию плюс
# Создать новый заказ
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=body)

# Запомнить трэк
def get_new_order_track():
    order_body = data.order_body
    resp_order = post_new_order(order_body)
    # Запомнить номер трека заказа
    return str(resp_order.json()["track"])


#Получить заказ по треку
def get_order_by_track():
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER + get_new_order_track())



#Тест 1. Успешное получение заказа по его трэк-номеру
def test_get_order_by_track_get_success_response():
    assert get_order_by_track().status_code == 200

