import requests
import bs4
from fake_useragent import UserAgent
from time import sleep
import sqlite3 as sq

user = UserAgent()
header = {'user-agent': user.random}


def url_get():
    """This function receives links to product cards from site pages that have products in stock"""
    try:

        page_url = f'https://buslik.by/catalog/podguzniki/?PAGEN_1=1'

        response = requests.get(page_url, headers=header)
        response.encoding = 'UTF-8'

        '''We are looking for the last page number in the diapers section'''
        soup = bs4.BeautifulSoup(response.text, 'lxml')
        page_number = soup.find_all('a', class_='new-pagination__link')

        '''We assign the number of the last page on the site to the variable to put it in a loop'''
        last_page_number = int(page_number[-2].text) + 1

        '''In a loop, we collect all links to product cards'''
        for page in range(1, last_page_number):
            product_url = f'https://buslik.by/catalog/podguzniki/?PAGEN_1={page}'
            print(f'Page number {page} is being processed...')

            response_page = requests.get(product_url, headers=header)
            response_page.encoding = 'UTF-8'

            soup_page = bs4.BeautifulSoup(response_page.text, 'lxml')
            data_page = soup_page.find_all('a', class_='catalog-item__link')

            '''String concatenation to make the link active'''
            for element in data_page:
                card_url = 'https://buslik.by' + element.get('href')
                yield card_url

    except Exception as err:
        print(err)
    else:
        print(f'Pages processed successfully')


def stork_data_parsing():
    """In this function, we get the data we need from each product card"""
    try:

        for card_url_info in url_get():

            headers = {'user-agent': user.random}

            response_card = requests.get(card_url_info, headers=headers)
            sleep(3)
            soup_card = bs4.BeautifulSoup(response_card.text, 'lxml')

            data_card_info = soup_card.find('article', class_='product-item')

            '''Add a conditional statement to get only diapers'''
            if 'odguz' in card_url_info:

                '''Getting the product name'''
                name = data_card_info.find('h1', class_='product-item__title').text.strip()

                '''Since the size is not indicated in the product card, we get the size from the url of the line'''
                if '_s_' in card_url_info:
                    size = 2
                elif '_m_' in card_url_info:
                    size = 3
                elif '_l_' in card_url_info:
                    size = 4
                elif '_xl_' in card_url_info:
                    size = 5
                elif '_xxl_' in card_url_info:
                    size = 6
                elif '_small_' in card_url_info:
                    size = 2
                elif '_0_' in card_url_info:
                    size = 0
                elif '_1_' in card_url_info:
                    size = 1
                elif '_2_' in card_url_info:
                    size = 2
                elif '_3_' in card_url_info:
                    size = 3
                elif '_4_' in card_url_info:
                    size = 4
                elif '_5_' in card_url_info:
                    size = 5
                elif '_6_' in card_url_info:
                    size = 6
                else:
                    size = 0

                '''We get the brand name, there are products without the specified brand, 
                we assign an unknown to such products'''
                brand_name = data_card_info.find('div', class_='product-item__brand').text
                if brand_name == '':
                    brand_name = 'Unknown'

                '''We get the current price and convert it to a fractional number 
                for further work with it in the database'''
                actual_price = float(data_card_info.find('div', class_='product-action__price-current'
                                                         ).text.replace(',', '.').replace('руб.', '').strip())

                '''We get the old price of the product and convert it to a fractional number 
                for further work with it in the database. 
                For products that do not have an old price, assign actual price'''
                old_price = data_card_info.find('div', class_='product-action__price-old')
                if old_price:
                    old_price = float(old_price.text.replace(',', '.').replace('руб.', ''))
                else:
                    old_price = actual_price

                '''Shop name for the filter in the general database'''
                store_name = 'STORK'

                with sq.connect('stork_diapers.db') as con:
                    cur = con.cursor()

                    cur.execute("""CREATE TABLE IF NOT EXISTS diapers_stork(
                        name_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        brand_name TEXT,
                        name TEXT,
                        size INTEGER,
                        actual_price REAL,
                        old_price REAL,
                        store_name TEXT
                        )""")
                    cur.execute(
                        f"""INSERT INTO diapers_stork (brand_name, name, size, actual_price, old_price, store_name)
                        VALUES(?, ?, ?, ?, ?, ?)""",
                        (brand_name, name, size, actual_price, old_price, store_name))
                    cur.execute("SELECT * FROM diapers_stork")
                    result = cur.fetchall()
        for i in result:
            print(f'{i[0]}: {i[2]}\nBrand: {i[1]}, Size: {i[3]}\nActual price: {i[4]} BYN | Old price: {i[5]} BYN\n')

    except Exception as err:
        print(err)
    else:
        print(f'The program worked successfully')
    finally:
        print('End of program')


stork_data_parsing()
