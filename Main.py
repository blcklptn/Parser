import requests
from bs4 import BeautifulSoup

#  Список ссылок на группы
LINKS = ['https://vk.com/linux0ids',
         'https://vk.com/jpmovement',
         'https://vk.com/torchfamily',
         'https://vk.com/zxcgen',
         'https://vk.com/absorballthepain'
        ]
    
#  Основной код. Получаем данные из ссылки, а потом парсим их
def parser(link: str="None") -> None:
    response = requests.get(link)
    soup = BeautifulSoup(response.text, 'lxml')
    elements = soup.find_all('a', href=True)
    print("https://vk.com/"+elements[0]['href'])


#  Проходимся по всем ссылкам
for link in LINKS:
    parser(link)
