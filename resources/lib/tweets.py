# -*- coding: utf-8 -*-
'''
    script.matchcenter - Football information for Kodi
    A program addon that can be mapped to a key on your remote to display football information.
    Livescores, Event details, Line-ups, League tables, next and previous matches by team. Follow what
    others are saying about the match in twitter.
    Copyright (C) 2016 enen92

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import xbmcgui
import xbmc
import datetime
import json
import mainmenu
from resources.lib.utilities import tweet
from resources.lib.utilities import ssutils
from resources.lib.utilities.common_addon import *

class detailsDialog(xbmcgui.WindowXMLDialog):
		
	def __init__( self, *args, **kwargs ):
		self.isRunning = True
		self.hash = kwargs["hash"]
		self.teamObjs = {}

	def onInit(self):
		xbmc.log(msg="[Match Center] Twitter cycle started", level=xbmc.LOGDEBUG)
		self.getControl(32540).setImage(os.path.join(addon_path,"resources","img","goal.png"))
		xbmc.executebuiltin("SetProperty(loading,1,home)")
		self.getTweets()
		xbmc.executebuiltin("ClearProperty(loading,Home)")
		i=0
		while self.isRunning:
			if (float(i*200)/(twitter_update_time*60*1000)).is_integer() and ((i*200)/(3*60*1000)) != 0:
				self.getTweets()
			xbmc.sleep(200)
			i += 1
		xbmc.log(msg="[Match Center] Twitter cycle stopped", level=xbmc.LOGDEBUG)

	def getTweets(self):
		self.getControl(32500).setLabel("#"+self.hash)
		self.getControl(32503).setImage(os.path.join(addon_path,"resources","img","twitter_sm.png"))
		tweetitems = []
		#tweets = tweet.get_hashtag_tweets(self.hash)
		#TODO Parse tweets
		tweets = [{'date': datetime.datetime(2016, 7, 13, 14, 58, 27), 'text': u'que mejor manera de arrancar, que con Seremos de SLB, para activar el d\xeda!', 'profilepic': u'https://pbs.twimg.com/profile_images/734921378000961541/3dOyYqWq.jpg', 'author': u'Magic Johnson Jr'}, {'date': datetime.datetime(2016, 7, 13, 14, 58, 24), 'text': u'\u30ab\u30a6\u30f3\u30c8\u30c0\u30a6\u30f3\u2026\u308f\u304f\u308f\u304f( \xb4\u2200`)', 'profilepic': u'https://pbs.twimg.com/profile_images/741597778514563072/iF0xUE1F.jpg', 'author': u'ViVid'}, {'date': datetime.datetime(2016, 7, 13, 14, 57, 41), 'text': u'RT @aalmeidaoficial: Entrar em campo com este emblema glorioso. \xc9 j\xe1 amanh\xe3 \U0001f4aa\U0001f3fd  #Juntos https://t.co/TG2HhvYgG4', 'profilepic': u'https://pbs.twimg.com/profile_images/732533114073976832/inscdwIt.jpg', 'author': u'SLB Fan'}, {'date': datetime.datetime(2016, 7, 13, 14, 57, 40), 'text': u'Ojos locos \U0001f602', 'profilepic': u'https://pbs.twimg.com/profile_images/736611131289141248/a4UgHzOX.jpg', 'author': u'Inocente! \u270c'}, {'date': datetime.datetime(2016, 7, 13, 14, 57, 25), 'text': u'RT @beriseando: Que la tristeza se convierta en alegr\xeda, y aquellas l\xe1grimas en sonrisas.', 'profilepic': u'https://pbs.twimg.com/profile_images/752679938789179392/u9yOuIvr.jpg', 'author': u'\xa1Que salte la banca!'}, {'date': datetime.datetime(2016, 7, 13, 14, 57, 16), 'text': u'RT @SLBenfica: \U0001f4aa\U0001f4aa\U0001f4aa #JUNTOS https://t.co/GUTwIGXz9a', 'profilepic': u'https://pbs.twimg.com/profile_images/732533114073976832/inscdwIt.jpg', 'author': u'SLB Fan'}, {'date': datetime.datetime(2016, 7, 13, 14, 57, 4), 'text': u'RT @RanveeriansFC: SLB is working for 19 hrs every day on Padmavati,to hit the floors frm September starring @RanveerOfficial ?\n https://t.\u2026', 'profilepic': u'https://pbs.twimg.com/profile_images/752459292800876544/Lz1N7bb3.jpg', 'author': u'Sukhveer'}, {'date': datetime.datetime(2016, 7, 13, 14, 56, 37), 'text': u'\u3044\u3084\u3001\u77e5\u3089\u3093\u3051\u3069', 'profilepic': u'https://pbs.twimg.com/profile_images/3715575771/88f07a23bccbce827a2c40b6d8c7bb8d.png', 'author': u'sin\u03b8\u3055\u3093\u2606\u30cf\u30a4\uff01'}, {'date': datetime.datetime(2016, 7, 13, 14, 56, 26), 'text': u'Quiero el celular nuevo lpm', 'profilepic': u'https://pbs.twimg.com/profile_images/736611131289141248/a4UgHzOX.jpg', 'author': u'Inocente! \u270c'}, {'date': datetime.datetime(2016, 7, 13, 14, 56, 12), 'text': u'\u7d2b\u5f0f\u90e8\u3063\u3066900\u5e74\u4ee3\u3084\u306a\u304b\u3063\u305f\u3063\u3051\uff1f', 'profilepic': u'https://pbs.twimg.com/profile_images/3715575771/88f07a23bccbce827a2c40b6d8c7bb8d.png', 'author': u'sin\u03b8\u3055\u3093\u2606\u30cf\u30a4\uff01'}, {'date': datetime.datetime(2016, 7, 13, 14, 55, 2), 'text': u'RT @potato250yen: \u307e\u3049\u3067\u3082\u3082\u3046\u3059\u3067\u306b\u5e73\u6210\u521d\u671f\u751f\u307e\u308c\u3082\u30a2\u30e9\u30b5\u30fc\u3060\u304b\u3089\u2026\u6700\u8fd1\u306e\u82e5\u8005\u306f1000\u5e74\u4ee3\u751f\u307e\u308c\u30682000\u5e74\u4ee3\u751f\u307e\u308c\u3067\u8003\u3048\u3066\u308b\u3089\u3057\u3044\u304b\u3089\u20261000\u5e74\u4ee3\u3063\u3066\u306a\u3093\u3060\u3088\u2026\u6025\u306b\u7d2b\u5f0f\u90e8\u3068\u540c\u4e16\u4ee3\u6271\u3044\u3060\u3088\u2026\u3042\u306a\u3084\u301c\u3060\u3088', 'profilepic': u'https://pbs.twimg.com/profile_images/3715575771/88f07a23bccbce827a2c40b6d8c7bb8d.png', 'author': u'sin\u03b8\u3055\u3093\u2606\u30cf\u30a4\uff01'}, {'date': datetime.datetime(2016, 7, 13, 14, 54, 49), 'text': u'\u30aa\u30d5\u30a1\u30fc\u826f\u3044\u3067\u3059\u306d(\uff1b\xb4\u0434\u2282)\n\u7121\u9650\u30c0\u30f3\u30b8\u30e7\u30f3\u2026\u697d\u3057\u305d\u3046', 'profilepic': u'https://pbs.twimg.com/profile_images/741597778514563072/iF0xUE1F.jpg', 'author': u'ViVid'}, {'date': datetime.datetime(2016, 7, 13, 14, 53, 15), 'text': u'\u767d\u732b\u306e\u5354\u529b\u5f8c\u306b\u3001\u9069\u5f53\u306b\u30d5\u30a9\u30ed\u30fc\u3055\u308c\u3066\u3082\u5fd8\u308c\u307e\u3059\u3088\u306d\u3002\u30d5\u30a9\u30ed\u30ef\u30fc\u69d8\u3001\u30ab\u30f3\u30b9\u30c8\u3055\u308c\u3066\u308b\u65b9\u9806\u306b300\u4ee5\u4e0a\u30d5\u30a9\u30ed\u30fc\u3067\u304d\u308b\u306e\u306f\u5b09\u3057\u3044\u3002', 'profilepic': u'https://pbs.twimg.com/profile_images/741597778514563072/iF0xUE1F.jpg', 'author': u'ViVid'}, {'date': datetime.datetime(2016, 7, 13, 14, 52, 32), 'text': u'\u2605seool&amp;#039;s \u3010\u30b7\u30fc\u30eb\u30ba\u3011 SLB-625 \u30e1\u30c3\u30b7\u30e5\u30b8\u30e3\u30b1\u30c3\u30c8 \u30b5\u30a4\u30ba3L\n\u73fe\u5728\u306e\u4fa1\u683c5,980 \u5186\n\u73fe\u5728\u306e\u5165\u672d\u4eba\u65700\u4eba\n\u8a73\u3057\u304f\u306f\u30b3\u30c1\u30e9\u21d2https://t.co/behSjcfz3t https://t.co/7W4CRv5KQy', 'profilepic': u'https://pbs.twimg.com/profile_images/562936711773040640/aU47LeB1.jpeg', 'author': u'\u30a2\u30f3\u30c0\u30ea\u30a8\u30eb'}, {'date': datetime.datetime(2016, 7, 13, 14, 52, 29), 'text': u'RT @RanveeriansFC: SLB is working for 19 hrs every day on Padmavati,to hit the floors frm September starring @RanveerOfficial ?\n https://t.\u2026', 'profilepic': u'https://pbs.twimg.com/profile_images/752497612570361856/_WuGv1Pr.jpg', 'author': u'RanveersKiran\u2764\ufe0f'}, {'date': datetime.datetime(2016, 7, 13, 14, 49, 57), 'text': u'https://t.co/NaVJWSvbKO', 'profilepic': u'https://abs.twimg.com/sticky/default_profile_images/default_profile_0.png', 'author': u'Ricardo Gon\xe7alves'}, {'date': datetime.datetime(2016, 7, 13, 14, 49, 35), 'text': u'\u308b\u307f\u308b\u307f\u306e\u5199\u771f\u96c6\u898b\u3066\u305f\u3051\u3069\u3053\u306e\u5199\u771f\u96c6\u3075\u3068\u3082\u3082\u5206\u304c\u8db3\u308a\u306a\u3044\u306e\u3088\u306d\u3002\u3002', 'profilepic': u'https://pbs.twimg.com/profile_images/3715575771/88f07a23bccbce827a2c40b6d8c7bb8d.png', 'author': u'sin\u03b8\u3055\u3093\u2606\u30cf\u30a4\uff01'}, {'date': datetime.datetime(2016, 7, 13, 14, 49, 32), 'text': u'#ConRockNacTeDigoQue No debe existir boca como esa en el mundo entero #SLB', 'profilepic': u'https://pbs.twimg.com/profile_images/751742226817028096/XjhS_cTV.jpg', 'author': u'Luna.'}, {'date': datetime.datetime(2016, 7, 13, 14, 48, 56), 'text': u'SLB is working for 19 hrs every day on Padmavati,to hit the floors frm September starring @RanveerOfficial ?\n https://t.co/vNdxIbjJAq (HT)', 'profilepic': u'https://pbs.twimg.com/profile_images/752459136110059520/8-Lz2x83.jpg', 'author': u'RanveeriansWorldwide'}, {'date': datetime.datetime(2016, 7, 13, 14, 48, 53), 'text': u'SLB\u2764 https://t.co/9mzAYVMiGW', 'profilepic': u'https://pbs.twimg.com/profile_images/753075318613745664/Tb9JUAXd.jpg', 'author': u'Sofi Beligoy.'}]
		if tweets:
			for _tweet in tweets:
				item = xbmcgui.ListItem(_tweet["text"].replace("\n",""))
				item.setProperty("profilepic",_tweet["profilepic"])
				item.setProperty("author","[B]" +"@" + _tweet["author"] + "[/B]")
				tweetitems.append(item)
				#print datetime.datetime.now() - _tweet["date"]
		self.getControl(32501).reset()
		self.getControl(32501).addItems(tweetitems)
		if tweetitems:
			self.setFocusId(32501)
		return

	def savecurrenthash(self):
		media_file = xbmc.getInfoLabel('Player.Filenameandpath')
		media_dict = {"file" : media_file, "hash":self.hash}
		ssutils.write_file(tweet_file,json.dumps(media_dict))
		return

	def reset(self):
		if os.path.exists(tweet_file):
			os.remove(tweet_file)
			xbmcgui.Dialog().ok(translate(32000), translate(32045))
		return

	def stopRunning(self):
		self.isRunning = False
		self.close()
		mainmenu.start()

	def onAction(self,action):
		if action.getId() == 92 or action.getId() == 10:
			self.stopRunning()

	def onClick(self,controlId):
		if controlId == 32501:
			teamid = self.getControl(controlId).getSelectedItem().getProperty("teamid")
			matchhistory.start(teamid)
		elif controlId == 32514:
			self.reset()

def start(twitterhash=None):
	if twitterhash == None:
		if os.path.exists(tweet_file):
			twitter_data = json.loads(ssutils.read_file(tweet_file))
			twitterhash = twitter_data["hash"]
			twitter_mediafile = twitter_data["file"]
			if twitter_mediafile == xbmc.getInfoLabel('Player.Filenameandpath'):
				userInput = False
				main = detailsDialog('script-matchcenter-Twitter.xml', addon_path, getskinfolder(), '', hash=twitterhash)
				main.doModal()
				del main
			else:
				userInput = True
		else:
			userInput = True

		if userInput:
			dialog = xbmcgui.Dialog()
			twitterhash = dialog.input(translate(32046), type=xbmcgui.INPUT_ALPHANUM)
			if len(twitterhash) != 0:
				main = detailsDialog('script-matchcenter-Twitter.xml', addon_path, getskinfolder(), '', hash=twitterhash.replace("#",""))
				if xbmc.getCondVisibility("Player.HasMedia") and save_hashes_during_playback == 'true':
					main.savecurrenthash()
				main.doModal()
				del main
			else:
				xbmcgui.Dialog().ok(translate(32000), translate(32047))
				mainmenu.start()
	else:
		main = detailsDialog('script-matchcenter-Twitter.xml', addon_path, getskinfolder(), '', hash=twitterhash)
		main.doModal()
		del main	