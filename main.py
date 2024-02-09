import os
try:
	import requests
	import telebot
	import json
	import time
	from telebot import types
	import flask
	from user_agent import generate_user_agent
except:
	os.system("pip install requests")
	os.system("pip install telebot")
	os.system("pip install flask")
	os.system("pip install user_agent")
	os.system("clear")

tk = "6235253931:AAE5X9jrx4UOOFd9X_vkz_ip7zYWbPJA-So"
bot = telebot.TeleBot(tk)

ch = types.InlineKeyboardButton(text='''🗽 𝕮𝖍𝖆𝖓𝖓𝖊𝖑''', url="https://t.me/+Q5RcaQe268lmYmI9")
pr = types.InlineKeyboardButton(text='''👨🏻‍💻 𝕻𝖗𝖔𝖌𝖗𝖆𝖒𝖒𝖊𝖗''', url="t.me/X668F")
cookies = {
    '_ga': 'GA1.1.868853150.1686571031',
    'uid': '0ab9d21b837ac3f8',
    'clickAds': '53',
    'pushNotification': '92',
    'pushPage': '19',
    'XSRF-TOKEN': 'eyJpdiI6Ikoydk1rOUVmMExPOGF1WUMxWTNpTnc9PSIsInZhbHVlIjoiSE5VU0lSOTZnQnRhTGdDeE1cL3dIcDJmcmhWbm5IdU9wN3VNbytJck9DSjlVU2xqVkhPRUJuR21pS1JIUjRWSWRnYzZLXC8xXC9lNVJubWtOVlRHcjd1TFwvYU5sZFBCMkN6Y0pjZHNRWXJzMkYwcVE1aDMyR0xrb2x3SHlBU3ptbHZLIiwibWFjIjoiYzNjYjNhNWE4NGFlNzhmMTNlMTJiNGIxNDNmMDVjYThjZGUzZGU4ZjExMTEwN2QzNjgwNWE0OTNlNzE1ZDc1YyJ9',
    'aig_session': 'eyJpdiI6IlFPaGc0UnY2bjNIWmxKeTBIbDVjXC9BPT0iLCJ2YWx1ZSI6IktVck9mTWF5UDdxY3RFXC9WeW5kR0ZTOTM5U3RjalBaSnlSd05mUlhkanN2NStldDhaSWtFXC9IeXFlbFFFNHNrS09VS3J4V2NDVWVpd0lncFljWEhJMGlERWpHSGZ4bWZGQTN5RVF0Mm9jT0NhR0xnRGFEaEs5eTRLSFlCd01OckkiLCJtYWMiOiIwNDEzNDBkNTc2NTRkMTkxODc2ZmUxZTIzOGQ0ODU1MWZmYWQyM2NmNGQ3MGQwZGU0OWUyMjEzMmRhOGU2ODAyIn0%3D',
    '_ga_2S9JP0SPEL': 'GS1.1.1686741984.2.1.1686742384.0.0.0',
}

headers = {
    'authority': 'storiesig.info',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'if-none-match': 'W/"376-nN5i4Qu/s4Ex/bnNvBcI5Wa+U3U"',
    'referer': 'https://storiesig.info/en/',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 12; M2004J19C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    'x-token': 'null',
    'x-xsrf-token': 'eyJpdiI6Ikoydk1rOUVmMExPOGF1WUMxWTNpTnc9PSIsInZhbHVlIjoiSE5VU0lSOTZnQnRhTGdDeE1cL3dIcDJmcmhWbm5IdU9wN3VNbytJck9DSjlVU2xqVkhPRUJuR21pS1JIUjRWSWRnYzZLXC8xXC9lNVJubWtOVlRHcjd1TFwvYU5sZFBCMkN6Y0pjZHNRWXJzMkYwcVE1aDMyR0xrb2x3SHlBU3ptbHZLIiwibWFjIjoiYzNjYjNhNWE4NGFlNzhmMTNlMTJiNGIxNDNmMDVjYThjZGUzZGU4ZjExMTEwN2QzNjgwNWE0OTNlNzE1ZDc1YyJ9',
}
h={
'Host': 'api.sssgram.com',
'accept': 'application/json, text/plain, */*',
'origin': 'https://www.sssgram.com',
 'x-requested-with': 'mark.via.gp',
'sec-fetch-site': 'same-site',
'sec-fetch-mode': 'cors',
'sec-fetch-dest': 'empty',
'referer': 'https://www.sssgram.com/',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9,id-ID;q=0.8,id;q=0.7,hi-IN;q=0.6,hi;q=0.5',
'user-agent': str(generate_user_agent())}
bu = "https://api.sssgram.com/st-tik/ins/dlprofile"

@bot.message_handler(commands=["start"])
def start(message):
    b = types.InlineKeyboardMarkup(row_width=2)
    b.add(ch, pr)
    name = message.from_user.first_name
    bot.reply_to(message, f"🎉 _Welcome to Insta Info Bot_ 🎉\n\n" \
       f"👋 _Hi {message.from_user.first_name}!_ \n\n" \
       f"😊 _I am here to provide you with Instagram profile information._ \n\n" \
       f"🔍 _Just send me an Instagram username (with or without @), and I will fetch the details for you._ \n\n", parse_mode="Markdown", reply_markup=b)

@bot.message_handler(func=lambda m: True)
def url(message):
    profile = types.InlineKeyboardButton(text="• Go To Profile •", url=f"https://www.instagram.com/{message.text.lstrip('@')}")
    dev = types.InlineKeyboardButton(text="•👨🏻‍💻 𝐃𝐄𝐕𝐄𝐋𝐎𝐏𝐄𝐑 👨🏻‍💻•", url="X668F.t.me")
    sanchit = types.InlineKeyboardMarkup(row_width=1)
    sanchit.add(profile, dev)
    msgg = bot.send_message(message.chat.id, "<i>⏳ Wait a little bit please...</i>", parse_mode="HTML")    
    try:
        url = requests.get(f'https://storiesig.info/api/ig/profile/{message.text.lstrip("@")}', cookies=cookies, headers=headers)
        data = json.loads(url.content)
        p = {
        'url': f'https://www.instagram.com/{message.text.lstrip("@")}',
        'timestamp': '1702992016308'
        }
        img = requests.get(bu, params=p, headers=h).json()['result']['profileDowunLoadUrl']
        id = data['result']['id']
        url2 = f'https://o7aa.pythonanywhere.com/?id={id}'
        req = requests.get(url2).json()
        url3 = f'https://www.instagram.com/api/v1/users/web_profile_info/?username={message.text.lstrip("@")}'
        he = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'content-length': '336',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'mid=YPvYkQALAAH7ZlNgkXiBnW6y7AOy; ig_did=1C396C9B-7DC7-463E-A68B-FE991198F88A; ig_nrcb=1; shbid="944\0546317830362\0541658653745:01f7bf09c30c2bf6ae86e32af31b5991cd84a607e1547a0132f6b653c4b76ecc26abbc4e"; shbts="1627117745\0546317830362\0541658653745:01f716bcf5ca94c711aa8ee17e52cf927685a30c29c89e0310cfe9f86589901109fd5b1e"; rur="RVA\05448065200129\0541658659405:01f7d96b5f9c1cf2396b6d00cbc7281da4dc2bb4c75a035bf4917e188315d170aec60aa2"; csrftoken=mWehV8ELhUeOnA4aWc43a7PplDLL0jNL',
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/',
        'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
        'sec-ch-ua-mobile': '?0',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': str(generate_user_agent()),
        'x-asbd-id': '437806',
        'x-csrftoken': 'mWehV8ELhUeOnA4aWc43a7PplDLL0jNL',
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': 'hmac.AR2oFTCuitCzXvttHXW3DD1kZLwzL7oauskQL1Jp6ogO6FF6',
        'x-instagram-ajax': 'caee87137ae9',
        'x-requested-with': 'XMLHttpRequest'
        }
        da = {'username': f'{message.text.lstrip("@")}'}
        re = requests.get(url3, headers=he, json=da).json()
        #url4 = requests.get(f"https://22a15f7d-af7f-46c3-9408-3ae84ff49e9c-00-30fjjs3ronllj.janeway.replit.dev/sanchit={message.text.lstrip('@')}")
        fid = re['data']['user']['fbid']
        pn = re['data']['user']['business_phone_number']
        em = re['data']['user']['business_email']
        ba = re['data']['user']['is_business_account']
        v = re['data']['user']['is_verified']
        date = req['date']
        user = data['result']['username']
        bio = data['result']['biography']
        name = data['result']['full_name']
        mn = data['result']['edge_owner_to_timeline_media']['count']
        followed = data['result']['edge_followed_by']['count']
        follow = data['result']['edge_follow']['count']
        private = data['result']['is_private']
        text = f"𝐇𝐈 • 𝐓𝐇𝐈𝐒 𝐈𝐒 𝐀𝐂𝐂. 𝐈𝐍𝐅𝐎. 🌜💚\n•━━━━━━━━━━━━━━━•\n˹💁˼ 𝐔𝐒𝐄𝐑 ‣ @{user}\n─ ─ ─ ─ ─ ─\n˹🫰˼ 𝐍𝐀𝐌𝐄 ‣ {name}\n─ ─ ─ ─ ─ ─\n˹🆔˼ 𝐈𝐃 ‣ <code>{id}</code>\n─ ─ ─ ─ ─ ─\n˹👥˼ 𝐅𝐎𝐋𝐋𝐎𝐖𝐄𝐑𝐒 ‣ {followed}\n─ ─ ─ ─ ─ ─\n˹🗿˼ 𝐅𝐎𝐋𝐋𝐎𝐖𝐈𝐍𝐆 ‣ {follow}\n─ ─ ─ ─ ─ ─\n˹🗺˼ 𝐏𝐎𝐒𝐓𝐒 ‣ {mn}\n─ ─ ─ ─ ─ ─\n˹📅˼ 𝐃𝐀𝐓𝐄  ‣ {date}\n─ ─ ─ ─ ─ ─\n˹🔖˼ 𝐏𝐑𝐈𝐕𝐀𝐓𝐄  ‣ {private}\n─ ─ ─ ─ ─ ─\n˹🌟˼ 𝐕𝐄𝐑𝐈𝐅𝐈𝐄𝐃  ‣ {v}\n─ ─ ─ ─ ─ ─\n˹🤝˼ 𝐅𝐁𝐈𝐃  ‣ <code>{fid}</code>\n─ ─ ─ ─ ─ ─\n˹☎️˼ 𝐁𝐔𝐒𝐈𝐍𝐄𝐒𝐒 𝐏𝐇𝐎𝐍𝐄  ‣ {pn}\n─ ─ ─ ─ ─ ─\n˹📧️˼ 𝐁𝐔𝐒𝐈𝐍𝐄𝐒𝐒 𝐄𝐌𝐀𝐈𝐋  ‣ {em}\n─ ─ ─ ─ ─ ─\n˹💸˼ 𝐁𝐔𝐒𝐈𝐍𝐄𝐒𝐒  ‣ {ba}\n─ ─ ─ ─ ─ ─\n˹🌼˼ 𝐁𝐈𝐎 ‣ <code>{bio}</code>\n•━━━━━━━━━━━━━━━•"
        bot.delete_message(chat_id=message.chat.id, message_id=msgg.message_id)
        bot.send_photo(message.chat.id, img, caption=f"{text}", reply_markup=sanchit, parse_mode='HTML')
    except Exception as e:
        bot.reply_to(message, f'❌ _Invalid username. Please make sure the Instagram username is correct._', parse_mode="Markdown")
        print(f"{e}")

print("Bot Is Alive")
bot.infinity_polling()
