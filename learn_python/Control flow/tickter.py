# HINT: modify the headlines list to verify your loop works with different inputs
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""
# write your loop here
for headline in headlines:
    if len(news_ticker) + len(headline) > 140:
        news_ticker += headline[:(140-len(news_ticker))]
        break
    else:
        news_ticker += headline  

print(news_ticker)
print(len(news_ticker))

news_ticker = ""
print('News ticker has been reset to {}.'.format(news_ticker))

news_ticker = "".join(headlines)[0:140] 
print(news_ticker)
print(len(news_ticker))