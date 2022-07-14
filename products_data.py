import time
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from concurrent.futures import ThreadPoolExecutor

from selenium.webdriver import Firefox, FirefoxOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# session = requests.session()
options = FirefoxOptions()
options.add_argument("--headless")
# options.add_argument("--no-sandbox")
# options.add_experimental_option('debuggerAddress', 'localhost:9222')
# options.headless()

driver = Firefox(options=options, keep_alive=True)

address = "700 N MILWAUKEE AVE #134, VERNON HILLS, IL 60061, USA"

root_url = "https://www2.reservebar.com"
payload={}

cookies = [{'name': 'sid', 'value': 'k0rU17pUjgafu3LrtaAdMVTY67uG2lKp19Q', 'path': '/', 'domain': 'www2.reservebar.com', 'secure': True, 'httpOnly': False, 'sameSite': 'None'}, {'name': 'dwanonymous_a40f731d0711af5eb64499a73962349d', 'value': 'adMwa37b73jmgODuR36qrh0F7f', 'path': '/', 'domain': 'www2.reservebar.com', 'secure': True, 'httpOnly': False, 'expiry': 1673274032, 'sameSite': 'None'}, {'name': '__cq_dnt', 'value': '1', 'path': '/', 'domain': 'www2.reservebar.com', 'secure': True, 'httpOnly': False, 'sameSite': 'None'}, {'name': 'dw_dnt', 'value': '1', 'path': '/', 'domain': 'www2.reservebar.com', 'secure': True, 'httpOnly': False, 'sameSite': 'None'}, {'name': 'dwsid', 'value': '49pdgvcZZvGIR2YGa8jgBSRIYu7Ll7pewCjSHS5ebcNqpQ9yvuyFruf4uwnbg4xaPiPm0ya_tTXFgfGJRoa2Xg==', 'path': '/', 'domain': 'www2.reservebar.com', 'secure': True, 'httpOnly': True, 'sameSite': 'None'}, {'name': '_gcl_au', 'value': '1.1.43424040.1657722066', 'path': '/', 'domain': '.reservebar.com', 'secure': False, 'httpOnly': False, 'expiry': 1665498066, 'sameSite': 'None'}, {'name': '_com.auth0.auth.cVR9pfpGxQqF6tzLILPdSDZ7aZvBHkod_compat', 'value': '{%22nonce%22:%22~kd6J36zVps0xSg3lE_A9PUVTXni~oFJ%22%2C%22state%22:%22cVR9pfpGxQqF6tzLILPdSDZ7aZvBHkod%22}', 'path': '/', 'domain': 'www2.reservebar.com', 'secure': True, 'httpOnly': False, 'expiry': 1657723931, 'sameSite': 'None'}, {'name': 'com.auth0.auth.cVR9pfpGxQqF6tzLILPdSDZ7aZvBHkod', 'value': '{%22nonce%22:%22~kd6J36zVps0xSg3lE_A9PUVTXni~oFJ%22%2C%22state%22:%22cVR9pfpGxQqF6tzLILPdSDZ7aZvBHkod%22}', 'path': '/', 'domain': 'www2.reservebar.com', 'secure': True, 'httpOnly': False, 'expiry': 1657723931, 'sameSite': 'None'}, {'name': '_ga', 'value': 'GA1.3.1363514894.1657722098', 'path': '/', 'domain': '.www2.reservebar.com', 'secure': False, 'httpOnly': False, 'expiry': 1720794175, 'sameSite': 'None'}, {'name': '_gid', 'value': 'GA1.3.498484475.1657722098', 'path': '/', 'domain': '.www2.reservebar.com', 'secure': False, 'httpOnly': False, 'expiry': 1657808575, 'sameSite': 'None'}, {'name': '_gat_UA-34670124-1', 'value': '1', 'path': '/', 'domain': '.www2.reservebar.com', 'secure': False, 'httpOnly': False, 'expiry': 1657722235, 'sameSite': 'None'}, {'name': '_rdt_uuid', 'value': '1657722319191.68930c89-c0a9-45dd-abd7-6befee4931a8', 'path': '/', 'domain': '.reservebar.com', 'secure': True, 'httpOnly': False, 'expiry': 1665498319, 'sameSite': 'Strict'}, {'name': '__pdst', 'value': 'b44dc7dc70e54222b2576525f366cced', 'path': '/', 'domain': 'www2.reservebar.com', 'secure': False, 'httpOnly': False, 'expiry': 1689258319, 'sameSite': 'Strict'}, {'name': '_mibhv', 'value': 'anon-1657722319900-4326298013_9048', 'path': '/', 'domain': 'www2.reservebar.com', 'secure': True, 'httpOnly': False, 'expiry': 1689258319, 'sameSite': 'None'}, {'name': '_pin_unauth', 'value': 'dWlkPU5HRTVNR1l5Wm1ZdE9EVTFZaTAwWmpkbExUazRORGt0TVRZMVkyRTFPVEF5WVRGbQ', 'path': '/', 'domain': '.www2.reservebar.com', 'secure': False, 'httpOnly': False, 'expiry': 1689258321, 'sameSite': 'None'}, {'name': '_com.auth0.auth.KnU9Sz8J3ML7hB3PahGUuhkMuOxbsDNj_compat', 'value': '{%22nonce%22:%22kxLBcfC160kdYYhMo0Qv8jiQ1~ZK_HSr%22%2C%22state%22:%22KnU9Sz8J3ML7hB3PahGUuhkMuOxbsDNj%22}', 'path': '/', 'domain': 'www2.reservebar.com', 'secure': True, 'httpOnly': False, 'expiry': 1657724137, 'sameSite': 'None'}, {'name': 'com.auth0.auth.KnU9Sz8J3ML7hB3PahGUuhkMuOxbsDNj', 'value': '{%22nonce%22:%22kxLBcfC160kdYYhMo0Qv8jiQ1~ZK_HSr%22%2C%22state%22:%22KnU9Sz8J3ML7hB3PahGUuhkMuOxbsDNj%22}', 'path': '/', 'domain': 'www2.reservebar.com', 'secure': True, 'httpOnly': False, 'expiry': 1657724137, 'sameSite': 'None'}, {'name': '_svsid', 'value': 'a2777d558176c0af393921dcedef3642', 'path': '/', 'domain': '.reservebar.com', 'secure': False, 'httpOnly': False, 'expiry': 1689258339, 'sameSite': 'Lax'}, {'name': '_fbp', 'value': 'fb.1.1657722070797.192054849', 'path': '/', 'domain': '.reservebar.com', 'secure': False, 'httpOnly': False, 'expiry': 1665498340, 'sameSite': 'None'}, {'name': 'ajs_anonymous_id', 'value': '2569df03-304d-468a-9019-6a1b4d8a5cf2', 'path': '/', 'domain': '.reservebar.com', 'secure': False, 'httpOnly': False, 'expiry': 1689258340, 'sameSite': 'Lax'}, {'name': '__pr.av2re9', 'value': 'MxtQRhFY5b', 'path': '/', 'domain': '.www2.reservebar.com', 'secure': True, 'httpOnly': False, 'expiry': 1660314340, 'sameSite': 'Strict'}, {'name': '__zlcmid', 'value': '1Awl4VnIVQfLFJc', 'path': '/', 'domain': '.reservebar.com', 'secure': False, 'httpOnly': False, 'expiry': 1689258343, 'sameSite': 'Lax'}]

headers = {
  'authority': 'www2.reservebar.com',
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'accept-language': 'en-US,en;q=0.9',
  'cache-control': 'max-age=0',
  'sec-ch-ua': '"Chromium";v="103", ".Not/A)Brand";v="99"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Linux"',
  'sec-fetch-dest': 'document',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-site': 'none',
  'sec-fetch-user': '?1',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36'
#   'Cookie': cookies
}

products_links = pd.read_csv('reservebank_products_links.csv')['links']

# names = []
# prices = []
# fulfillments_by = []

# driver.get(products_links[0])
# print('cookies 2: ', driver.get_cookies())


def location_setup():
    driver.get('https://www2.reservebar.com/')
    driver.find_element(By.ID, 'header-address-select').click()
    add_cont = driver.find_element(By.CLASS_NAME, 'address-content')\
                    .find_element(By.ID, 'address')
    add_cont.click()
    add_cont.send_keys(address)
    time.sleep(1.5)
    add_cont.send_keys(Keys.ARROW_DOWN, Keys.ENTER)
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, 'address-content')\
                    .find_elements(By.CLASS_NAME, 'form-group')[-1].click()

location_setup()

i = 4964

for pl in products_links[4964:]:
    print("Now on link index: ", i)
    reservebank_prds_csv = pd.read_csv('reservebank_products.csv')
    reservebank_prds_excel = pd.read_excel('reservebank_products.xlsx')
    name = None
    price = None
    fulfil = None
    # response_post = session.post(this_url, headers=headers, data=payload)
    # response = requests.request("GET", pl, headers=headers, data=payload, cookies=cookies)
    driver.get(pl)
    # print('cookies 2: ', driver.get_cookies())
    # soup = bs(response.text, 'html.parser')
    try:
        eligibale_state = driver.find_element(By.CLASS_NAME, 'eligible-state-error').get_attribute('class')
    except:
        driver.close()
        driver = Firefox(options=options, keep_alive=True)
        location_setup()
        driver.get(pl)
        eligibale_state = driver.find_element(By.CLASS_NAME, 'eligible-state-error').get_attribute('class')
        
    # eligibale_state = soup.find(class_='eligible-state-error')['class']
    # print("=======>>: ", eligibale_state)
    if 'd-none' in eligibale_state:
        try:
            # name = soup.find('h1', class_="product-name").get_text().strip()
            name = driver.find_element(By.CLASS_NAME, 'product-name').text.strip()
        except:
            ...
        # names.append(name)

        try:
            # price = soup.find('div', class_="price").find('span', class_="value").get_text().strip()
            price = driver.find_element(By.CLASS_NAME, 'price')\
                            .find_element(By.CLASS_NAME, 'value').text.strip()
        except:
            ...
        # prices.append(price)

        try:
            # fulfil = soup.find('div', class_="shipping-area").find('p', class_="fulfillment-name").find('span').get_text().strip()
            fulfil = driver.find_element(By.CLASS_NAME, 'shipping-area')\
                            .find_element(By.CLASS_NAME, 'fulfillment-name')\
                                .find_element(By.TAG_NAME, 'span').text.strip()
        except:
            ...
        # fulfillments_by.append(fulfil)

        print("link: ", pl, "\n")
        print(f"'name':{name}, 'price':{price}, 'fulfilled_by':{fulfil}\n")

        # create a local dataframe to concatenate with storage data
        if price and fulfil:
            dd = pd.DataFrame({'name':[name], 'price':[price], 'fulfilled_by':[fulfil]})
            df_1 = pd.concat([reservebank_prds_csv,dd], axis=0, ignore_index=True)
            df_2 = pd.concat([reservebank_prds_excel,dd], axis=0, ignore_index=True)
            df_1.to_csv('reservebank_products.csv', index=False)
            df_2.to_excel('reservebank_products.xlsx', index=False)
    else:
        ...
    i+=1

driver.close()
print("\n\nI have collected products' data from reservebank.com succussfully")

# reservebank = pd.DataFrame({'name': names, 'price': prices, 'fulfilled_by': fulfillments_by})
# reservebank.to_csv('reservebank_products.csv', index=False)
# reservebank.to_excel('reservebank_products.xlsx', index=False)
