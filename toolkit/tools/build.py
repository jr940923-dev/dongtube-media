import re,sys
src=open('templates/tip02.html').read()
HEAD=src[:src.index('<body>')+6].replace('</style>','.tt td{padding:16px 8px}.xs td{padding:10px 8px}.xs td:first-child span{width:64px;height:64px;line-height:64px;font-size:36px}.ttl{margin-bottom:34px}.cap{margin-top:34px}.sm{font-size:46px}\n</style>')
LOGO=' <img class="logo" src="../assets/dongtube_logo.png">\n'
def tbl(headers,rows,cls=''):
    h='<tr>'+''.join(f'<th>{x}</th>' for x in headers)+'</tr>'
    out=''
    for r in rows:
        cells=[]
        for j,c in enumerate(r):
            t,k=(c if isinstance(c,tuple) else (c,''))
            if j==0: cells.append(f'<td><span>{t}</span></td>')
            else: cells.append(f'<td{" class=%s"%chr(34)+k+chr(34) if k else ""}>{t}</td>')
        out+='   <tr>'+''.join(cells)+'</tr>\n'
    return f'  <table class="{cls}">\n   {h}\n{out}  </table>\n'
def vs(items):
    s='  <div class="vs">\n'
    for lb,n,k,s2 in items: s+=f'   <div><div class="lb">{lb}</div><div class="n {k}">{n}</div><div class="s2">{s2}</div></div>\n'
    return s+'  </div>\n'
def foot(t,top=None): return f'  <div class="foot"{" style=%smargin-top:%dpx%s"%(chr(34),top,chr(34)) if top is not None else ""}>{t}</div>\n'
def cap(*lines): return ' <div class="cap">'+'<br>'.join(f'<span class="hl{" r" if l.startswith("!") else ""}">{l.lstrip("!")}</span>' for l in lines)+'</div>\n'
def build(n,t):
    N=f'{n:02d}'; LB=t.get('label',f'홀덤 꿀팁 #{N}'); CAT=t.get('cat','토너먼트'); L=f'<div class="lesson">{LB}</div>'
    c=t['cover']; hs=f';font-size:{c["size"]}px' if c.get('size') else ''
    o=HEAD+f'''
<!-- 1 표지 -->
<div class="s"><div class="pg">1 / 6</div>
 <div class="note c"><div class="tab"><b>{LB}</b> · {CAT}</div>
  <div class="kick">{c["kick"]}</div>
  <div class="h1" style="margin-top:14px{hs}">{c["h1"]}</div>
  <div class="bar">{c["bar"]}</div>
  <div class="tags">{"".join(f'<div class="tag">{x}</div>' for x in c["tags"])}</div>
 </div>
{cap(c["cap"])}{LOGO}</div>
'''
    for i,(ttl,body,cp) in enumerate(t['pages'],start=2):
        o+=f'''
<div class="s">{L}<div class="pg">{i} / 6</div>
 <div class="ttl"><span class="hl">{ttl}</span></div>
 <div class="note">
{body} </div>
{cap(*cp)}{LOGO}</div>
'''
    pts=''.join(f'   <li><div>{a}<small>{b}</small></div></li>\n' for a,b in t['pts'])
    o+=f'''
<div class="s">{L}<div class="pg">5 / 6</div>
 <div class="ttl"><span class="hl">오늘의 핵심 📌</span></div>
 <div class="note">
  <ol class="pts">
{pts}  </ol>
 </div>
{cap(t["ptscap"])}{LOGO}</div>
'''
    q=t['quiz']
    opts=''.join((f'   <div style="padding:20px 0">{a}<span style="display:block;font-size:40px;margin-top:4px">{b}</span></div>\n' if b else f'   <div>{a}</div>\n') for a,b in q['opts'])
    o+=f'''
<div class="s">{L}<div class="pg">6 / 6</div>
 <div class="ttl" style="margin-bottom:30px"><span class="hl r">QUIZ</span> <span class="hl">{q["ttl"]}</span></div>
 <div class="note c">
  <div class="h2">{q["q"]}</div>
  <div class="ans">
{opts}  </div>
  <div class="foot" style="margin-top:28px">정답은 <b>내일 스토리</b>에서 공개!</div>
 </div>
 <div class="cta">
  <div class="t">{q["cta"]}<br><b>{q.get("cta2","플레이스토어 ‘ICM Now’")}</b></div>
 </div>
{LOGO}</div>
</body></html>
'''
    open(f'templates/tip{N}.html','w').write(o)
