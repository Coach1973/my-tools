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
]),
("works","🎨","大樹作品・策展頁",[
("大臺南商圈整合計劃・大台南策展中心","https://event.bymyway.com/tainan-shangquan/","免費為店家建站、開通頻道","策展"),
("全世界最優秀的團隊計畫","https://event.bymyway.com/curated/three-lacks/","客戶、人才、伯樂","策展"),
("為你轉身｜真 AI 線上團隊商業導師席","https://event.bymyway.com/curated/turnforyou/","八位商業顧問師","策展"),
("約瑟布｜生命農業與永續商業計畫","https://event.bymyway.com/curated/joseph-cloth/","榮樹下客戶網站","策展"),
("有薇力，新東區｜蔡筱薇競選總部成立大會","https://event.bymyway.com/curated/111-wei/","11/1（日）09:00","策展"),
("像瘋子的發明家｜黃國彰","https://event.bymyway.com/curated/inventor/","能源專利發明人","策展"),
("南應大校友互動記憶牆","https://event.bymyway.com/curated/tut-memory/","TUT Alumni Memory Wall","策展"),
("海餅乾俱樂部 20 週年","https://event.bymyway.com/seabiscuit20/#home","Sea Biscuit Club 2007–2027","策展"),
("教練與軍師：深夜的 32MB 封包攻防戰 第1話","https://www.tava-ai.com/chat/b72pvmh9x1/index.html","TAVA 做的漫畫","漫畫"),
("大樹的答案 ── 漫畫版","https://event.bymyway.com/curated/answer/","日系漫畫版思想漫畫","漫畫"),
("大樹教練｜企業成長條漫 EP01–EP05","https://event.bymyway.com/curated/answer2/","全五話條漫","漫畫"),
("榮樹下｜來賓卡","https://event.bymyway.com/rongtree/a/b99f99e2f2b0","榮樹下來賓資料與 AI 來賓卡（專屬連結）","榮樹下"),
]),
]
n=sum(len(s[3]) for s in S)
json.dump([{"id":a,"icon":b,"title":c,"items":[dict(name=x[0],url=x[1],desc=x[2],tag=x[3]) for x in d]} for a,b,c,d in S],open('tools.json','w',encoding='utf8'),ensure_ascii=False,indent=1)
def host(u):
    p=urlparse(u);return p.netloc+(p.path.rstrip('/') if p.path!='/' else '')
secs=''
for a,ic,t,items in S:
    rows=''.join(f'<a class="item" href="{html.escape(u)}" target="_blank" rel="noopener" data-s="{html.escape((nm+" "+u+" "+d+" "+tg).lower())}"><div class="num">{i}</div><div class="mid"><div class="name">{html.escape(nm)}</div><div class="url">{html.escape(host(u))}</div><div class="desc">{html.escape(d)}</div></div><div class="badge">{html.escape(tg)}</div></a>' for i,(nm,u,d,tg) in enumerate(items,1))
    secs+=f'<section class="sec" id="{a}"><div class="sec-title"><span class="arrow">▼</span>{ic} {t} <span class="count">{len(items)}項</span></div><div class="grid">{rows}</div></section>\n'
page=f'''<!DOCTYPE html>
<html lang="zh-Hant"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>大樹的常用查詢網站（個人專用）</title>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@500;700;900&display=swap" rel="stylesheet">
<style>
:root{{--gold:#c8a96e;--dark:#0a0a0a;--dark2:#141414;--line:rgba(200,169,110,.3)}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{font-family:'Noto Sans TC',sans-serif;background:var(--dark);color:#fff;padding:36px 20px 100px}}
.wrap{{max-width:1500px;margin:0 auto;column-count:2;column-gap:48px}}
.head{{max-width:1500px;margin:0 auto}}
h1{{font-size:30px;font-weight:900;margin-bottom:6px}}h1 span{{color:var(--gold)}}
.sub{{color:rgba(255,255,255,.5);font-size:16px;margin-bottom:18px}}
.search{{width:100%;max-width:520px;background:var(--dark2);border:1px solid var(--line);color:#fff;border-radius:10px;padding:12px 16px;font:inherit;font-size:16px;margin-bottom:28px}}
.search:focus{{outline:none;border-color:var(--gold)}}
.sec{{break-inside:avoid;display:inline-block;width:100%}}
.sec-title{{display:flex;align-items:center;gap:10px;margin:40px 0 16px;font-size:20px;font-weight:900;color:var(--gold);cursor:pointer;user-select:none}}
.sec-title::after{{content:'';flex:1;height:1px;background:var(--line)}}
.sec-title .count{{font-size:14px;color:rgba(255,255,255,.4);font-weight:700;order:2}}
.sec-title::after{{order:3}}
.arrow{{font-size:13px;color:rgba(255,255,255,.4);transition:transform .2s}}
.sec.collapsed .arrow{{transform:rotate(-90deg)}}.sec.collapsed .grid{{display:none}}
.grid{{display:flex;flex-direction:column;gap:8px}}
.item{{display:flex;align-items:center;gap:12px;color:#fff;text-decoration:none;background:var(--dark2);border:1px solid var(--line);border-radius:10px;padding:10px 14px 10px 10px;transition:.2s}}
.item:hover{{border-color:var(--gold);background:#1a1a1a}}
.num{{flex-shrink:0;width:34px;height:34px;border-radius:8px;background:#1c1c1c;display:flex;align-items:center;justify-content:center;font-weight:900;font-size:15px;color:var(--gold);border:1px solid var(--line)}}
.mid{{flex:1;min-width:0}}.name{{font-weight:700;font-size:17px}}
.url{{font-size:13px;color:rgba(255,255,255,.35);overflow:hidden;text-overflow:ellipsis;white-space:nowrap}}
.desc{{font-size:13px;color:rgba(255,255,255,.55);margin-top:2px}}
.badge{{font-size:12px;font-weight:900;padding:3px 9px;border-radius:999px;flex-shrink:0;background:rgba(200,169,110,.15);color:var(--gold)}}
.hide{{display:none!important}}
.foot{{max-width:1500px;margin:40px auto 0;color:rgba(255,255,255,.3);font-size:13px}}
@media(max-width:900px){{.wrap{{column-count:1}}}}
</style></head><body>
<div class="head"><h1>大樹的常用查詢網站<span>｜個人專用</span></h1>
<p class="sub">共 {n} 個網址，分 {len(S)} 類。點名稱直接開新分頁；點分類標題可收合；上方可搜尋名稱、網址、說明。</p>
<input class="search" id="q" type="search" placeholder="🔍 搜尋：名稱／網址／說明（例如 AI、行事曆、約瑟）"></div>
<div class="wrap" id="wrap">
{secs}</div>
<div class="foot">這份清單由 AI 維護，新網址丟給 AI 就會補進來。</div>
<script>
document.querySelectorAll('.sec-title').forEach(t=>t.onclick=()=>t.parentElement.classList.toggle('collapsed'));
document.getElementById('q').addEventListener('input',e=>{{const k=e.target.value.trim().toLowerCase();
document.querySelectorAll('.item').forEach(i=>i.classList.toggle('hide',!!k&&!i.dataset.s.includes(k)));
document.querySelectorAll('.sec').forEach(s=>{{const v=s.querySelectorAll('.item:not(.hide)').length;s.classList.toggle('hide',!!k&&!v);if(k&&v)s.classList.remove('collapsed')}})}});
</script></body></html>'''
open('index.html','w',encoding='utf8').write(page)
print(n)
