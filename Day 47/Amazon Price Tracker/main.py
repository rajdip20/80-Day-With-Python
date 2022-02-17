import requests
from bs4 import BeautifulSoup
import smtplib

BUY_PRICE = 70000.0
url = "https://www.amazon.in/dp/B09G93H3BR/ref=twister_B09GG3LLD6"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.43",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
title = soup.find(id="productTitle").get_text().strip()
print(title)

price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("₹")[1]
price_without_currency = price_without_currency.split(",")[0] + price_without_currency.split(",")[1]
price_as_float = float(price_without_currency)
print(price_as_float)

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login("YOUR_EMAIL", "YOUR_PASSWORD")
        connection.sendmail(
            from_addr="YOUR_EMAIL",
            to_addrs="YOUR_EMAIL",
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
        )
