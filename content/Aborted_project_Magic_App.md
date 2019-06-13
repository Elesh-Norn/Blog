Title: Abandoned project: Data visualisation App with Magic the Gathering
Date: 2019-06-11
Category: Project
Tags: Python, MtG, Magic, Dataviz, Tkinter

### Hello there!

It's been a while but I didn't abandon this blog. However, I will talk today of an abandoned project of mine and why it still has value for me.

A great way to learn anything is having little projects. It helps confronts your theoretical knowledge to reality and make you resolve problems. 
As a self-taught hobbyist programmer it's especially important to me, because it's the only form of evaluation I can get. You could conclude that 
only results matters then, but it's not entirely true.

I started this project last year with some objective in mind: 

* Would contain data visualisation

* Fun

* Learn new things

* Really challenge myself with something outside my comfort zone

## Chosing a project

I was working at the time on my thesis and I was fed of blood levels. I still wanted to cash in my newly acquired **pandas** and **matplotlib** skills and I stumbled 
upon this [series of tutorials](https://pythonprogramming.net/tkinter-depth-tutorial-making-actual-program/) on PythonProgramming.net, to make a Bitcoin 
trading app with Python and **Tkinter**. Fun, but not fun enough. At this time, i started 
playing Magic the Gathering, a successfull collectible card game. Due to the popularity of the game and their business model, people trade cards and their price varies
depending on their popularity and the stocks. I would make a data viz app, about Magic the Gathering prices!

## Gathering Data (requests to scryfall)

First, I needed data. Where to get the list of cards, their name, prices and different attributes such as rarity? Fortunately for me, there is a 
good number of websites that provides this. I chose https://scryfall.com. Here was the first difficulty for me. As a biologist, you never learn what is an API. 
Quickly enough I was able to build the request I wanted to get a nice JSON (scryfall have a [Rest-like API](https://scryfall.com/docs/api)) 
that I can convert to a Pandas Dataframe. From there it's easy to build some visualization and following the Tkinter tutorial. However, I had huge troubles 
adapting/understanding how Tkinter animates as I wanted buttons to modify the type of 
visualization/subset of data without surimposed them. With some horrible fidgeting, I would destroy and recreate a canvas and have something sorta functional. 


![output]({filename}/image/magic_exemple_app.png)

## Storing the data (Redis)
Another problem was to get daily prices. I needed to actualize the price every day, and keep them for history. I didn't want to learn a whole 
database system, so I needed something light and easy. Redis was the best choice in my opinion. It's a system that can be used as a database that 
store what you want as key/value. Luckily I could get a unique identifier for any magic card, I just had to pull the price everyday and I could store 
like ID : (date, price), with simple function to convert Dataframes to redis and vice versa. It can be done in a few lines: 

~~~~
import redis
import datetime
import pandas as pd

r = redis.Redis(host="redis_price", port=6379, decode_responses=True)

def get_all_redis_hash(df):
    """
    Set the price of today, in redis server, as card id : date : price
    :param df: pandas DataFrame with card id and price from scryfall
    """
    today_date = datetime.date.today()
    for _ in df['id']:
        price = float(df.loc[df['id'] == _]['usd'].values)
        r.hset(_, today_date, price)

def get_price_list_from_redis(card_id):
    df = pd.DataFrame.from_dict(r.hgetall(card_id),
                                orient="index", columns=['price'])
    df['price'] = df['price'].astype('float', copy=False)
    df.index.name = 'date'
    return df
~~~~

What's fun looking back at old project is looking at your old mistakes. I recently read [Clean Code](https://www.amazon.co.uk/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882) 
which is a book teaching some principles of good software programming. I can now notice how my comments are unnecessary and the naming is horrid. 
Looking back at your old projects is also a lot of cringes. But it helps you see how you progressed? 

## Get the data each day (schedule and Docker)

Next step was to pull them every day. It's easy enough with **schedule**.

~~~~
from app.redis_price_server import get_all_redis_hash
import schedule
from app.card_fetcher import get_all_standard

print("Scheduler launched!")

schedule.every().day.at("15:00").do(get_all_redis_hash(get_all_standard())
~~~~

But then i realize, that this is working only on my computer. I would need to let this script forever goes and never close my computer. 
So the next logical step would be to deploy all of this on a server. So i learn docker, i play with it a bit and manage to launch an image 
that pulls the price, the redis server and the automated script. 

## End of the line 

I then understand that i've made the wrong choices, that i can't launch my Tkinter app in this and that was a terrible idea. 
Combining with the problem i had to make Tkinter and Matplotlib more reactive, i realise that i should then orient 
myself towards a web application. 

Unfortunately, i would have to learn [bokeh](https://bokeh.pydata.org/en/latest/) (who looks amazing) or 
even something in Javascript to make it functional. (However, Mozilla is working on bringing python dataviz tools to the web. Check [Pyodide](https://hacks.mozilla.org/2019/04/pyodide-bringing-the-scientific-python-stack-to-the-browser/)
if you're curious.) Since i don't know anything about web development i decided to stop the project there. It was definitely becoming too big
for what i wanted initially. 

Were all those hours lost? No. Look up to my objectives. I manage to practice data manipulation, GUI, Redis, Docker, schedule and also Rest-like API.
I went far beyond my comfort zone and this made me definitly better. Looking at it now and i'm thinking of all the ways i could have make it better.
So even if i didn't deliver in the end, i'm proud of the result and i feel like it made me a better programmer.

Next blog post will be about a project that did succeed ;). 

Stay tuned and goodbye dear reader.
