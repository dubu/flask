__author__ = 'dubu'
#!/usr/bin/python
#-*- coding: utf-8 -*-
import requests
import json
import time

#from __future__ import absolute_import, print_function
import tweepy

headers = {'Referer': 'http://ticket.interpark.com/Ticket/Goods/GoodsInfo.asp?GoodsCode=15001801'}

while(True):
	#for i in ['003','004','005','006','007','008','009','010','011','014','015','016']:
	for i in ['009','010','011','014','015','016']:
	#for i in ['003']:
		r = requests.get('http://ticket.interpark.com/Ticket/Goods/GoodsInfoJSON.asp?Flag=RemainSeat&GoodsCode=15001801&PlaceCode=14000312&PlaySeq='+i+'&Callback=fnPlaySeqChangeCallBack', headers=headers)
		#r.encoding = 'euc-kr'
		#print(r.json()['RemainCnt'])
		cont = r.text.replace('fnPlaySeqChangeCallBack({"JSON":[','')
		cont = cont.replace(']});','').encode('ascii', 'ignore').decode('ascii')
		cont = cont.replace("'", "\"")
		j = json.loads(cont)
		#print(type(j))
		#print(j['RemainCnt'])
		remainSeat = j['RemainCnt']
		if(remainSeat != '0'):
			#print i
			print time.strftime("%Y/%m/%d %H:%M:%S", time.localtime())
			print 'gogogo!! seat'
			print(j['RemainCnt'])


			# twitter
			consumer_key="gU6YOM9ifBiMAVdQGbUgQUmxh"
			consumer_secret="rWqUW21UT93sT947ya8vt5CxufBOX3zvMTdcXc8NaKvhwd2oPL"

			access_token="2941456268-Chqj5qc597O8gS9MeWRdZMHktxbo5pvS1BNG8N3"
			access_token_secret="3DOr7pMUEGUycANx0QXQ3AyAPGppzBul2hDvueDTB2VWA"

			auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
			auth.secure = True
			auth.set_access_token(access_token, access_token_secret)

			api = tweepy.API(auth)
			msg = time.strftime("%Y/%m/%d %H:%M:%S @kozazz @gony7650 @blue_supia ", time.localtime()) + i+ 'day gogogo!!  ' +j['RemainCnt']

			api.update_status(status=msg)
		else:
			#print time.strftime("%Y/%m/%d %H:%M:%S", time.localtime())
			#print 'no seat;;'
			print( '.')

	time.sleep(60)
