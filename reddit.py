import json, requests


# Currently only gets mentions from daily discussion thread (the first thread on the cryptocurrency subreddit page).

subreddit = 'cryptocurrency'

def get_top_level_json():
    r = requests.get(
        'http://www.reddit.com/r/{}.json'.format(subreddit),
        headers={'user-agent': 'Mozilla/5.0'}
    )
    return r.json()

# Returns a dict of <symbol> : <name>
# Gets coin names and symbols from 
# https://min-api.cryptocompare.com/data/all/coinlist
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
        # To get counts for coin names, use the following instead:
        # count_dict[name] = comment_block.count(" " + name.lower() + " ")
    return count_dict
