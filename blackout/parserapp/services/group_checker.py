import requests
from bs4 import BeautifulSoup

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0',
    'Accept': '*/*',
    'Accept-Language': 'uk-UA,uk;q=0.8,en-US;q=0.5,en;q=0.3',
}

POWEROFF_URL = 'https://poweroff.loe.lviv.ua/'
STEP_BY = [
    ['gav_city3', 'city'],
    ['gav_streets3', 'street'],
    ['gav_builds3', 'build'],
    ['gav_group3', None],
]


def get_csrftoken(page_text: str):
    soup = BeautifulSoup(page_text, 'html.parser')
    inp = soup.find('input', attrs={'name': 'csrfmiddlewaretoken'})
    return inp.get('value', None)


def step_to_group(address_data: list):
    session = requests.Session()
    session.headers.update(HEADERS)
    for id_step, step in enumerate(STEP_BY):
        if not step is STEP_BY[-1]:
            req = session.get(f'{POWEROFF_URL}{step[0]}')
            if not req.ok:
                return None
            csrftoken = get_csrftoken(req.text)
            r = session.post(
                f'{POWEROFF_URL}{step[0]}',
                data={
                    'csrfmiddlewaretoken': csrftoken,
                    step[1]: address_data[id_step],
                    'q': 'Далі',
                },
            )
            if not r.ok:
                return None
        else:
            req = session.get(f'{POWEROFF_URL}{step[0]}')
            if not req.ok:
                return None
            return req.text


def get_group_by_address(city: str, street: str, building: str) -> int:
    group_page = step_to_group([city, street, building])
    if group_page is None:
        print('Такої адреси не знайдено')
        return -1
    soup = BeautifulSoup(group_page, 'html.parser')
    try:
        group_str = soup.find('h5', class_='card-title')
        group = int(group_str.text[-1])
    except:
        return 0
    return group


if __name__ == '__main__':
    while True:
        city = input('Місто: ')
        street = input('Вулиця: ')
        building = input('Будинок: ')

        print(f'Виявлено групу: {get_group_by_address(city, street, building)}')
