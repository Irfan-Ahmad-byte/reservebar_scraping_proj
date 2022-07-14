import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from concurrent.futures import ThreadPoolExecutor

root_url = "https://www2.reservebar.com"
payload={}

headers = headers = {
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
  'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36',
  'Cookie': '__cq_dnt=1; dw_dnt=1; dwanonymous_a40f731d0711af5eb64499a73962349d=acufdphn0DuqzTqpqehaZp0DTc; dwsid=__EYAfXIo7BoEcYW1pQyOh0NcUmbp9wkncr3rR5ZPH6TknOGh6nHxPMEspRdXYKdgSkuZdsQqkrhWpEOf8P0NA==; sid=P67PVuk3mQcAmmYLM16Xkt1Sph6HWOaT9UE'
}


collections = ['spirits', 'wine', 'discover', 'gifts-accessories']

products_links = []

for cat in collections:
    cat_url = f"https://www2.reservebar.com/collections/{cat}"
    cat_res = requests.request("GET", cat_url, headers=headers, data=payload)
    soup = bs(cat_res.text, 'html.parser')
    more_results = soup.find('span', class_='results-span').get_text().strip().split(' ')[0].split(',')
    results = int(''.join(more_results))
    print(f"link: {cat_url}", " results: ",results)

    start = 1
    size = 100
    while True:
        if start>=results:
            break
        show_more_link = f"https://www2.reservebar.com/on/demandware.store/Sites-reservebarus-Site/default/Search-UpdateGrid?cgid={cat}&start={start}&sz={size}&selectedUrl=https%3A%2F%2Fwww2.reservebar.com%2Fon%2Fdemandware.store%2FSites-reservebarus-Site%2Fdefault%2FSearch-UpdateGrid%3Fcgid%3D{cat}%{size}start%3D{start}%{size}sz%3D{size}"

        response = requests.request("GET", show_more_link, headers=headers, data=payload)

        soup = bs(response.text, 'html.parser')
        all_products = soup.find_all('div', class_="product-tile")

        start += 100

        for prod in all_products:
            if "Not available in IL" in prod.get_text():
                ...
            else:
                a = prod.find('a')
                products_links.append(root_url+a['href'])
                # print(a['href'])

    print("number of products' links: ", len(products_links))

print("\n\nTotal number of products' links: ", len(products_links))

products_links_df = pd.DataFrame({'links': products_links})
products_links_df.to_csv('reservebank_products_links.csv')
# print(response.text)

# ====================================================================