import json,html,re
from urllib.parse import urlparse
S=[
("ai","🤖","AI 老師推薦的工具",[
("CMO｜AI 行銷工作台","https://cmo.oyag.com/","受眾分析、行銷時機、網站規劃、AI 焦點團體","AI老師"),
("TAVA AI｜Skills as a Service","https://www.tava-ai.com/chat","影片、網站、設計、研究的技能平台","AI老師"),
("Muse｜個人 AI 代理","https://muse.ai/","給它一個目標，幫你把事做完","AI老師"),
("Duck.ai｜私密 AI 聊天","https://duck.ai/","DuckDuckGo 出的免費匿名 AI 對話","AI老師"),
("SubEasy｜AI 轉寫字幕翻譯","https://www.subeasy.ai/zh-TW/users/myplan","音訊轉文字、影片字幕、翻譯（我的方案頁）","AI老師"),
("秒站 Site Now｜AI 架站","https://site-now.app/","零代碼填空建形象、購物車、課程網站","AI老師"),
("奎嵐 KueiLan｜AI 教學與社群代操","https://kueilan.com/","用 AI 幫你提早下班","AI老師"),
("Freebeat｜AI 音樂影片","https://freebeat.ai/tw","AI 音樂與影片創作（繁中版）","AI老師"),
("個人行銷／品牌網頁｜開工指令與製作經驗","https://coach1973.github.io/tava-brand-web-playbook/","TAVA 品牌網頁做法 v2（我的 GitHub 備份，一模一樣；2026-10-15 更新，新增公益足跡）","經驗手冊"),
("JFETEK｜聯絡洽詢","https://www.jfetek.com/contact","1–2 工作天回覆方案與時程，預設保密","AI老師"),
]),
("know","📚","學會・媒體・知識",[
("台灣人工智慧暨區塊鏈應用學會","https://www.ais.org.tw/index.html","AI 學會官網","學會"),
("餐飲人筆記","https://foodnote.tw/","餐飲老闆文章、知識分享","知識"),
("SoundOn Podcast 播放器","https://player.soundon.fm/p/01bac58b-741f-4cbc-8fa6-58dd45f24923","Podcast 節目頁","Podcast"),
]),
("home","🏠","大樹官方入口",[
("大樹教育顧問（官方網站）","https://www.bymyway.com/","大樹教練官方網站","官方"),
("BNI 大台南南區・分會列表","https://chapters.bymyway.com/","各分會入口","BNI"),
("大樹小講；無話不談","https://event.bymyway.com/bigtree/","2013 年起的公益巡講場次","官方"),
("AI 改變世界．百人導師同行","https://mentor100.bymyway.com/","mentor100 導師計畫","官方"),
("AI 特助心法・一鍵注入","https://coach1973.github.io/ai-go/","貼給任何 AI，30 秒進入特助狀態","常用"),
]),
("daily","🗓️","我的日常查詢",[
("2026 全年度行事曆","https://tainan-calender.netlify.app/","全年度行事曆","查詢"),
("大樹教練｜可約時間","https://event.bymyway.com/schedule/t1qZLUh7D4RoewGA/","別人預約我的時間表","查詢"),
("大樹教練待辦事項","https://event.bymyway.com/todo","特助主動提醒版","查詢"),
("2026 企業 AI 導入與政府補助需求調查","https://docs.google.com/forms/d/e/1FAIpQLSdCIH8ffceaxzxoTEZhd4ZaJlPVLMw9unkoHtUm_HOyD6v43g/viewform","Google 表單","表單"),
("字級大小對照表","https://coach1973.github.io/coach888/font-scale.html","大樹AI工具箱的字級參考","工具"),
("大樹策展中心｜上傳網址","https://event.bymyway.com/curation/upload","店家／品牌網站上傳，一條龍上架策展中心","查詢"),
("榮樹下｜來賓卡","https://event.bymyway.com/rongtree/a/b99f99e2f2b0","榮樹下來賓資料與 AI 來賓卡（專屬連結）","查詢"),
("免費線上調音器・節拍器｜家緯家吉他坊","https://pickd.tw/guitar-tuner-metronome/","吉他免安裝校音，手機也能用","工具"),
]),
("works","🎨","大樹作品・策展頁",[
("大臺南商圈整合計劃・大台南策展中心","https://event.bymyway.com/tainan-shangquan/","免費為店家建站、開通頻道","策展"),
("全世界最優秀的團隊計畫","https://event.bymyway.com/curated/three-lacks/","客戶、人才、伯樂","策展"),
("為你轉身｜真 AI 線上團隊商業導師席","https://event.bymyway.com/curated/turnforyou/","八位商業顧問師","策展"),
("顧問師天團・人才軍火庫","https://event.bymyway.com/curated/skyteam/","上百位專家人才與頂尖顧問師","策展"),
("約瑟布｜生命農業與永續商業計畫","https://event.bymyway.com/curated/joseph-cloth/","榮樹下客戶網站","策展"),
("有薇力，新東區｜蔡筱薇競選總部成立大會","https://event.bymyway.com/curated/111-wei/","11/1（日）09:00","策展"),
("像瘋子的發明家｜黃國彰","https://event.bymyway.com/curated/inventor/","能源專利發明人","策展"),
("南應大校友互動記憶牆","https://event.bymyway.com/curated/tut-memory/","TUT Alumni Memory Wall","策展"),
("海餅乾俱樂部 20 週年","https://event.bymyway.com/seabiscuit20/#home","Sea Biscuit Club 2007–2027","策展"),
("教練與軍師：深夜的 32MB 封包攻防戰 第1話","https://www.tava-ai.com/chat/b72pvmh9x1/index.html","TAVA 做的漫畫","漫畫"),
("大樹的答案 ── 漫畫版","https://event.bymyway.com/curated/answer/","日系漫畫版思想漫畫","漫畫"),
("大樹教練｜企業成長條漫 EP01–EP05","https://event.bymyway.com/curated/answer2/","全五話條漫","漫畫"),
]),
]
n=sum(len(s[3]) for s in S)
json.dump([{"id":a,"icon":b,"title":c,"items":[dict(name=x[0],url=x[1],desc=x[2],tag=x[3]) for x in d]} for a,b,c,d in S],open('tools.json','w',encoding='utf8'),ensure_ascii=False,indent=1)
defaults=[{"id":a,"icon":b,"title":c,"items":[dict(name=x[0],url=x[1],desc=x[2],tag=x[3]) for x in d]} for a,b,c,d in S]
tpl=open('template.html',encoding='utf8').read()
open('index.html','w',encoding='utf8').write(tpl.replace('__DEFAULTS__',json.dumps(defaults,ensure_ascii=False)))
print(n)
