import requests
import bs4
from fake_useragent import UserAgent
from time import sleep
import sqlite3 as sq

user = UserAgent()
header = {'user-agent': user.random}


def diapers_url_get():
    """This function receives links to product cards from site pages that have products in stock"""
    try:

        page = 1
        while True:

            page_url = f'https://detmir.by/catalog/index/name/podguzniki/page/{page}/'

            response = requests.get(page_url, headers=header)
            response.encoding = 'UTF-8'

            soup = bs4.BeautifulSoup(response.text, 'lxml')
            data_product = soup.find_all('a', class_='PS Qj')

            print(f'Page number {page} is being processed...')

            '''Check for active links, if there are no active links, then end the cycle'''
            if len(data_product) != 0:
                for link in data_product:
                    card_url = link.get('href')
                    yield card_url
                page += 1
            else:
                break

    except Exception as err:
        print(err)
    else:
        print(f'Pages processed successfully')


def child_world_diapers_data_parsing():
    """In this function, we get the data we need from each product card"""
    try:

        for card_url_info in diapers_url_get():

            headers = {'user-agent': user.random}

            response_card = requests.get(card_url_info, headers=headers)
            sleep(3)
            soup_card = bs4.BeautifulSoup(response_card.text, 'lxml')

            data_card_info = soup_card.find('main', class_='c_0')

            '''We get the brand name, there are products without the specified brand, 
            we assign an unknown to such products'''
            brand_name = data_card_info.find('span', class_='v_8')
            if brand_name:
                brand_name = brand_name.text.strip()
            else:
                brand_name = 'Unknown'

            '''Getting the product name'''
            name = data_card_info.find('h1', class_='sP sQ').text

            '''We get the diaper size from the product information line, 
            if the brand is not indicated in the line, then the index is shifted, 
            and we translate it into a integer data type.'''
            size_all = data_card_info.find_all('li', class_='Pa')
            size_for_sql = None
            if len(size_all) == 6:
                size = size_all[-2].text
                size_for_sql = int(size[0])
            elif len(size_all) == 5:
                size = size_all[-1].text
                size_for_sql = int(size[0])

            '''We get the current price and convert it to a fractional number 
            for further work with it in the database'''
            actual_price = float(data_card_info.find('div', class_='Rl').text.replace(',', '.').replace('руб.', ''))

            '''We get the old price of the product and convert it to a fractional number 
            for further work with it in the database. For products that do not have an old price, assign actual price'''
            old_price = data_card_info.find('span', class_='Rn')
            if old_price:
                old_price = float(old_price.text.replace(',', '.').replace('руб.', ''))
            else:
                old_price = actual_price

            '''Shop name for the filter in the general database'''
            store_name = 'CHILD WORLD'

            with sq.connect('child_world_diapers.db') as con:
                cur = con.cursor()

                cur.execute("""CREATE TABLE IF NOT EXISTS diapers_child_world(
                    name_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    brand_name TEXT,
                    name TEXT,
                    size INTEGER,
                    actual_price REAL,
                    old_price REAL,
                    store_name TEXT
                    )""")
                cur.execute(
                    f"""INSERT INTO diapers_child_world (brand_name, name, size, actual_price, old_price, store_name) 
                    VALUES(?, ?, ?, ?, ?, ?)""",
                    (brand_name, name, size_for_sql, actual_price, old_price, store_name))
                cur.execute("SELECT * FROM diapers_child_world")
                result = cur.fetchall()
        for i in result:
            print(
                f'{i[0]}: {i[2]}\nBrand: {i[1]}, Size: {i[3]}\nActual price: {i[4]} BYN | Old price: {i[5]} BYN\n')

    except Exception as err:
        print(err)
    else:
        print(f'The program worked successfully')
    finally:
        print('End of program')


child_world_diapers_data_parsing()
