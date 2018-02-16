import json, requests

# Get coin names and symbols from 
# https://min-api.cryptocompare.com/data/all/coinlist

# Mentions from daily discussion thread
# Mentions from threads created in the past day

subreddit = 'cryptocurrency'

def get_top_level_json():
    r = requests.get(
        'http://www.reddit.com/r/{}.json'.format(subreddit),
        headers={'user-agent': 'Mozilla/5.0'}
    )
    return r.json()

# Returns a dict of <symbol> : <name>
def get_coin_names():
    url =  'https://min-api.cryptocompare.com/data/all/coinlist'
    coin_dict = {}
    r = requests.get(url)
    coin_data = r.json()["Data"]
    for name in coin_data:
        entry = coin_data[name]
        coin_dict[entry["Symbol"]] = entry["CoinName"]
    return coin_dict

def get_daily_discussion():
    comments_url = r.json()['data']['children'][0]['data']['url']
    comment_req = requests.get(comments_url + '.json', headers={'user-agent': 'Mozilla/5.0'})
    return comment_req.json()

def get_comment_bodies():
    comments = []
    d = get_daily_discussion()
    for child_data in d[1]["data"]["children"]:
        data = child_data["data"]
        try:
          comments.append(data["body"])
        except KeyError as e:
            pass
    return comments

# Make sure to use space before and after.
def get_symbol_counts():
    count_dict = {}
    coin_dict = get_coin_names()
    comments = get_comment_bodies()
    comment_block = " ".join(comments).lower()
    for sym, name in coin_dict.iteritems():
        count_dict[sym] = comment_block.count(" " + sym.lower() + " ")
        #count_dict[name] = comment_block.count(" " + name.lower() + " ")
    return count_dict

# counts = get_symbol_counts()
# [(sym, count) for sym, count in counts.iteritems() if count > 0]

# view structure of an individual post
comments_url = r.json()['data']['children'][0]['data']['url']
comment_req = requests.get(comments_url + '.json', headers={'user-agent': 'Mozilla/5.0'})
print(json.dumps(r.json()['data']['children'][0]['data']))

'''
for post in r.json()['data']['children']:
    print(post['data']['title'])
'''
