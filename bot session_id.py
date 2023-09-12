import telebot
from telebot import types
import requests
import time
from user_agent import generate_user_agent

tok = '5641578460:AAGwb3bFdMM3pmkSFyvHzhYYsqomCSJCr_0'
bot = telebot.TeleBot(tok)
@bot.message_handler(commands=['start'])
def da(message):
	id= str(message.from_user.id)
	q1=types.InlineKeyboardButton(text='start-اضغط',callback_data='q1')
	ch=types.InlineKeyboardButton(text='قناة المطور',url='https://t.me/H_9_D')
	qq=types.InlineKeyboardMarkup(row_width=2);qq.add(q1,ch,inf)
	bot.send_message(message.chat.id,text=f'اهلا بك عزيزي العضو\nمرحباً بك في بوت استخراج السيشن انستا\nايدي حسابك على تليجرام => {id}',reply_markup=qq)
@bot.callback_query_handler(func=lambda call:True)
def bo(call):
	if call.data=='q1':
		q2=types.InlineKeyboardButton(text='Cookies-انستا',callback_data='q2')
		ch=types.InlineKeyboardButton(text='قناة المطور',url='https://t.me/H_9_D')
		ww=types.InlineKeyboardMarkup(row_width=1);ww.add(q2,ch)
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='عزيزي العضو \n اضغط الزر الذي تريدوه',reply_markup=ww)
	elif call.data=='q2':
		bv = types.InlineKeyboardButton(text='-رجوع-',callback_data='q1')
		ch=types.InlineKeyboardButton(text='قناة المطور',url='https://t.me/H_9_D')
		ssd=types.InlineKeyboardMarkup(row_width=1);ssd.add(bv,ch)
		uu = bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='ارسل الحساب الوهمي لسحب السيشن\n#ملاحضه ارسل الحساب بهذا النمط\n\n\r        USERNAME:PASSWORD',reply_markup=ssd)
		bot.register_next_step_handler(uu,Session)
def Session(message):
	us=str(message.text)
	try:
		username=us.split(':')[0]
		password=us.split(':')[1]
	except IndexError as Error:
		bot.send_message(message.chat.id,'لايمكن ارسال الحساب بهذا النمط')
	url = 'https://www.instagram.com/api/v1/web/accounts/login/ajax/'
	headers = {
		'Accept': '*/*',
		'Accept-Encoding': 'gzip, deflate, br',
		'Accept-Language': 'en-US,en;q=0.9',
		'Content-Length': '303',
		'Content-Type': 'application/x-www-form-urlencoded',
		'Cookie': 'mid=ZIwIGQALAAFJh0hs0zugnqEWswdV; ig_did=86209C21-70C2-4E14-B4F6-91D07CD08186; ig_nrcb=1; datr=EQiMZDSU8kuwtKAAlo7Zzc7X; csrftoken=hgsIi0RAc4SVEqqHPIXjO7PoWVcgKOpK',
		'Origin': 'https://www.instagram.com',
		'Referer': 'https://www.instagram.com/',
		'Sec-Ch-Prefers-Color-Scheme': 'light',
		'Sec-Ch-Ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
		'Sec-Ch-Ua-Full-Version-List': '"Not/A)Brand";v="99.0.0.0", "Google Chrome";v="115.0.5790.170", "Chromium";v="115.0.5790.170"',
		'Sec-Ch-Ua-Mobile': '?0',
		'Sec-Ch-Ua-Platform': '"Windows"',
		'Sec-Ch-Ua-Platform-Version': '"10.0.0"',
		'Sec-Fetch-Dest': 'empty',
		'Sec-Fetch-Mode': 'cors',
		'Sec-Fetch-Site': 'same-origin',
		'User-Agent': str(generate_user_agent()),
		'Viewport-Width': '685',
		'X-Asbd-Id': '129477',
		'X-Csrftoken': 'hgsIi0RAc4SVEqqHPIXjO7PoWVcgKOpK',
		'X-Ig-App-Id': '936619743392459',
		'X-Ig-Www-Claim': '0',
		'X-Instagram-Ajax': '1007975685',
		'X-Requested-With': 'XMLHttpReques',
	}
	tim = str(time.time()).split('.')[1]
	data = {
		'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{tim}:{password}',
		'optIntoOneTap': 'false',
		'queryParams': '{}',
		'trustedDeviceRecords': '{}',
		'username': username,
	}

	re = requests.post(url, headers=headers, data=data)
	if('"Sorry, your password was incorrect. Please double-check your password.",') in re.text:
		bot.send_message(message.chat.id,'كلمه السر خطاء')
	elif('"checkpoint_url"') in re.text:
		bot.send_message(message.chat.id,'الحساب سكيور')
	elif('"userId"') in re.text:
		cook=re.cookies
		ccok=cook.get_dict()
		sess = (ccok['sessionid'])
		bot.send_message(message.chat.id,f'True_Login\n\nتم تسجيل دخول الى الحساب\n\nتم جلب السيشن الخاص في الحساب \n\n SESSION : {sess}\n\n DEV BOT : @X_6_Z')
while True:
	bot.polling(none_stop=True)