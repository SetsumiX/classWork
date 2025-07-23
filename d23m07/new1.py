import requests
from bs4 import BeautifulSoup

response = requests.get("https://example.com")

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.find("title").get_text()
    h1_tag = soup.find("h1")
    if h1_tag:
        h1_text = h1_tag.get_text()
    else:
        h1_text = "Не найден"

    p = soup.find_all("p")
    p_text = ""

    for i in p:
        p_text += i.get_text() + " "

    print("Заголовок страницы:", title)
    print("Главный заголовок:", h1_text)
    print("Основной текст страницы")
    print(p_text[:500] + "...")
else:
    print(f"Ошибка чтения страницы {response.status_code}")