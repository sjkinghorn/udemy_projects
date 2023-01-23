import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_API_KEY = "U4UJ0G1APRF5I2S5"
STOCK_URL = "https://www.alphavantage.co/query"

NEWS_API_KEY = "565c44a5ebff411589c5b7f7f8735c11"
NEWS_URL = "https://newsapi.org/v2/everything"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

parameters = {
    'function': 'TIME_SERIES_DAILY_ADJUSTED',
    'symbol': STOCK,
    'apikey': STOCK_API_KEY,
}
response = requests.get(url=STOCK_URL, params=parameters)
response.raise_for_status()
data = response.json()
yesterday_close = list(data['Time Series (Daily)'].values())[0]['4. close']
before_yesterday_close = list(data['Time Series (Daily)'].values())[1]['4. close']
price_change = (float(yesterday_close) - float(before_yesterday_close)) / float(before_yesterday_close) * 100

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

parameters_news = {
    'q': COMPANY_NAME,
    'apiKey': NEWS_API_KEY,
}
response_news = requests.get(url=NEWS_URL, params=parameters_news)
response_news.raise_for_status()
news_data = response_news.json()
if abs(price_change) > 5 and price_change < 0:
    print(f"{STOCK}: 🔻{round(price_change)}"
          f"\n1.) Headline: {news_data['articles'][0]['title']} \n\turl: {news_data['articles'][0]['url']}"
          f"\n2.) Headline: {news_data['articles'][1]['title']} \n\turl: {news_data['articles'][1]['url']}"
          f"\n3.) Headline: {news_data['articles'][2]['title']} \n\turl: {news_data['articles'][2]['url']}")
elif abs(price_change) > 5 and price_change > 0:
    print(f"{STOCK}: 🔺{round(price_change)}"
          f"\n1.) Headline: {news_data['articles'][0]['title']} \n\turl: {news_data['articles'][0]['url']}"
          f"\n2.) Headline: {news_data['articles'][1]['title']} \n\turl: {news_data['articles'][1]['url']}"
          f"\n3.) Headline: {news_data['articles'][2]['title']} \n\turl: {news_data['articles'][2]['url']}")

# or

articles = news_data['articles']
three_articles = articles[:3]
formatted_articles = [f"Headline: {article['title']}. \n Brief: {article['description']}" for article in three_articles]

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 

account_sid = "AC72403677e61c505ac352419518089f11"
auth_token = "550f107a1347a960950ccc3db808288a"

if abs(price_change) > 5 and price_change < 0:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body=f"{STOCK}: 🔻{round(price_change)}%"
             f"\n1.) Headline: {news_data['articles'][0]['title']} \n\turl: {news_data['articles'][0]['url']}"
             f"\n2.) Headline: {news_data['articles'][1]['title']} \n\turl: {news_data['articles'][1]['url']}"
             f"\n3.) Headline: {news_data['articles'][2]['title']} \n\turl: {news_data['articles'][2]['url']}",
        from_='+17743325717',
        to='+15558675310')
    print(message.status)
elif abs(price_change) > 5 and price_change > 0:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body=f"{STOCK}: 🔺{round(price_change)}%"
             f"\n1.) Headline: {news_data['articles'][0]['title']} \n\turl: {news_data['articles'][0]['url']}"
             f"\n2.) Headline: {news_data['articles'][1]['title']} \n\turl: {news_data['articles'][1]['url']}"
             f"\n3.) Headline: {news_data['articles'][2]['title']} \n\turl: {news_data['articles'][2]['url']}",
        from_='+17743325717',
        to='+17657442195')
    print(message.status)

    # Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
