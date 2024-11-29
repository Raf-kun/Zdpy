import requests
from bs4 import BeautifulSoup


def main():
    url = 'https://digital-razor.ru/game-computers/detail/?id=151937&utm_source=yadirect&utm_medium=cpc&utm_campaign=%D0%A2%D0%9A%20AMD%20Ryzen%209000%2F%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D1%8F&utm_term=---autotargeting&utm_content=c:115960453|g:5513156047|b:16659078653|k:53688760370|st:search|a:no|s:none|t:other|p:4|r:53688760370|dev:desktop&roistat=direct1_search_115960453_rsMasterGroup_rsMasterBanner_---autotargeting&yclid=11322476297649913855'
    response = requests.get(url)
    print(response.status_code)
    # print(response.text)

    soup = BeautifulSoup(response.text, 'html.parser')
    spoon = soup.find_all("div", class_="slider-container")
    print([i.text for i in spoon])
    
    with open('page.txt', 'a', encoding='UTF-8') as file:
        file.write(''.join([i.text for i in spoon]))


if __name__ == "__main__":
    main()

