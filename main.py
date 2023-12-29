import requests
import time
from flask import Flask

prapti = Flask(__name__)

@prapti.route('/<num>/user=<username>&pass=<password>', methods=['GET'])
def sanchit(num, username, password):
    c = 'https://www.instagram.com/accounts/login/ajax/'
    head = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6',
        'content-length': '319',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'mid=YrX_FwABAAFVRYLepbLqUSO9nyBK; ig_did=B86D9D0C-8059-4D38-AB32-62F66F91EB8A; ig_nrcb=1; shbid="6887,479320179,1687630562:01f72f17d27d1bf82c5011a7e21c360468f4e96ffc8c8d9bc8f3389196b275ab0b6d598c"; shbts="1656094562,479320179,1687630562:01f75b9e3dad31375f7599a21ee1e6b0b33b430c850ee605a7591dd83682126848a683cd"; dpr=3; datr=av-1Yj1HLbt2sRgtjJ2hIyTk; rur="ASH,479320179,1687707865:01f7969a9a044b6e5a39c124177ea698ce171408d797be83e4e94e6efc69642ea3b90ed9"; csrftoken=QZnASSTl4lB3b1sG610j7UGrPk0TfrN0',
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/',
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.99 Safari/537.36',
        'viewport-width': '360',
        'x-asbd-id': '437806',
        'x-csrftoken': 'QZnASSTl4lB3b1sG610j7UGrPk0TfrN0',
        'x-ig-app-id': '1217981644879628',
        'x-ig-www-claim': 'hmac.AR2oFTCuitCzXvttHXW3DD1kZLwzL7oauskQL1Jp6ogO6FF6',
        'x-instagram-ajax': '57ac339ce6f4',
        'x-requested-with': 'XMLHttpRequest'}

    tim = str(time.time()).split('.')[1]
    data1 = {
        'username': username,
        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{tim}:{password}',
        'queryParams': '{}',
        'optIntoOneTap': 'false',
        'trustedDeviceRecords': '{}'
    }

    rq = requests.post(url=c, headers=head, data=data1)

    if '"userId"' in rq.text:
        sanchit = rq.cookies
        san = sanchit.get_dict()
        return f"<b>🟢 Login Successful!\nsessionid={san['sessionid']};csrftoken={san['csrftoken']} -Tele => @X668F ( SANCHIT )<br></br>Correct Password => {password}<b>"
    elif '"checkpoint_required"' in rq.text:
        return 'Account Is Secured'
    else:
        return 'No Login'

@prapti.route('/', methods=['GET'])
def san():
	return '<b>This Is Proxyless Instagram Login Api<br></br>Developer: @X668F ( SANCHIT)<br></br>[API => https://127.0.0.1:5000/1/user={username}&pass={password}]<br></br>[Method => (GET)]<b>'

if __name__ == '__main__':
    prapti.run(host='0.0.0.0', port='5000')
