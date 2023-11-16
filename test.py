import requests
url = 'https://suppliers-api.wildberries.ru/content/v1/analytics/nm-report/detail'  # Замените на URL вашего API
headers = {'Content-Type': 'application/json', 'Authorization': 'YOUR_API_KEY'}  # Установите необходимые заголовки
# Создайте словарь с данными для запроса
data = {
  "brandNames": [
    "Some"
  ],
  "objectIDs": [
    358
  ],
  "tagIDs": [
    123
  ],
  "nmIDs": [
    1234567
  ],
  "timezone": "Europe/Moscow",
  "period": {
    "begin": "2023-06-01 20:05:32",
    "end": "2023-06-26 20:05:32"
  },
  "orderBy": {
    "field": "ordersSumRub",
    "mode": "asc"
  },
  "page": 1
}
# Отправьте POST-запрос на API
response = requests.post(url, json=data, headers=headers)
# Обработайте полученный ответ
if response.status_code == 200:
    result = response.json()
    print(result)
    # Дальнейшая обработка полученных данных
else:
    print('Произошла ошибка при выполнении запроса:', response.status_code)