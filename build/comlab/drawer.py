# 컴랩 공용 오른쪽 사이드 메뉴 (메인·문의·만든 사람·학교 페이지 공통)

BURGER = ('<button class="cl-burger" id="cl-burger" type="button" aria-label="메뉴 열기" '
          'aria-expanded="false" aria-controls="cl-drawer"><span></span><span></span><span></span></button>')

def drawer(page):
    return f'''<div class="cl-scrim" id="cl-scrim"></div>
<nav class="cl-drawer" id="cl-drawer" data-page="{page}" aria-label="사이트 메뉴" aria-hidden="true">
  <div class="cl-dh"><b>컴랩</b><button class="cl-x" id="cl-x" type="button" aria-label="메뉴 닫기"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg></button></div>
  <ul>
    <li><a href="/" data-p="home">홈</a></li>
  </ul>
  <p class="cl-g">학교</p>
  <ul>
    <li><a href="/ku/" data-p="ku">고려대학교</a></li>
    <li><a href="/kaist/" data-p="kaist">KAIST</a></li>
  </ul>
  <p class="cl-g">컴랩</p>
  <ul>
    <li><a href="/contact/" data-p="contact">문의하기</a></li>
    <li><a href="/about/" data-p="about">만든 사람</a></li>
  </ul>
</nav>'''

CSS = '''
.cl-burger{margin-left:auto;flex:none;width:42px;height:42px;border:0;background:none;border-radius:10px;cursor:pointer;display:grid;place-content:center;gap:5px;padding:0}
.cl-burger span{display:block;width:20px;height:2px;border-radius:2px;background:#16181D}
.cl-burger:hover{background:#F1F2F4}.cl-burger:focus-visible,.cl-x:focus-visible,.cl-drawer a:focus-visible{outline:2px solid #16181D;outline-offset:2px}
.cl-scrim{position:fixed;inset:0;background:rgba(16,18,24,.28);-webkit-backdrop-filter:blur(2.5px);backdrop-filter:blur(2.5px);opacity:0;visibility:hidden;transition:opacity .4s ease,visibility .4s;z-index:1000}
.cl-drawer{position:fixed;top:10px;right:10px;bottom:10px;width:min(280px,calc(100vw - 64px));background:#fff;z-index:1001;border-radius:20px;
  transform:translateX(calc(100% + 24px));opacity:.6;visibility:hidden;
  transition:transform .45s cubic-bezier(.22,1,.36,1),opacity .35s ease,visibility .45s;box-shadow:0 20px 50px -12px rgba(16,18,24,.28);padding:0 12px 20px;overflow-y:auto;
  font-family:"Pretendard Variable",Pretendard,-apple-system,"Apple SD Gothic Neo","Noto Sans KR",sans-serif;color:#16181D}
html.cl-open .cl-scrim{opacity:1;visibility:visible}
html.cl-open .cl-drawer{transform:none;opacity:1;visibility:visible}
html.cl-open,html.cl-open body{overflow:hidden}
.cl-dh{display:flex;align-items:center;justify-content:space-between;height:60px;padding:0 2px 0 10px}
.cl-dh b{font-size:16px;font-weight:800}
.cl-x{width:38px;height:38px;border:0;background:none;border-radius:10px;cursor:pointer;display:grid;place-content:center;color:#16181D}
.cl-x:hover{background:#F1F2F4}
.cl-drawer ul{list-style:none;margin:0;padding:0}
.cl-drawer a{display:flex;align-items:center;gap:10px;padding:11px 10px;border-radius:10px;font-size:15.5px;font-weight:600;color:#16181D;text-decoration:none;transition:background-color .15s}
.cl-drawer a:hover{background:#F4F5F7}
.cl-drawer a[aria-current]{background:#F1F2F4}
.cl-g{margin:16px 10px 4px;font-size:12px;font-weight:650;color:#8A909C}
@media (max-width:560px){
  .cl-drawer{top:8px;right:8px;bottom:auto;max-height:calc(100% - 16px);width:min(232px,calc(100vw - 72px));border-radius:18px;padding:0 8px 16px}
  .cl-dh{height:54px}.cl-drawer a{font-size:15px;padding:10px 10px}.cl-g{margin-top:12px}
}
@media (prefers-reduced-motion:reduce){.cl-drawer,.cl-scrim{transition:none}}
'''

JS = '''<script>
(function(){
  var b=document.getElementById('cl-burger'), d=document.getElementById('cl-drawer'), s=document.getElementById('cl-scrim'), x=document.getElementById('cl-x'), H=document.documentElement;
  if(!b||!d) return;
  d.querySelectorAll('a').forEach(function(a){ if(a.dataset.p===d.dataset.page) a.setAttribute('aria-current','page'); });
  function set(o){ H.classList.toggle('cl-open',o); b.setAttribute('aria-expanded',o); d.setAttribute('aria-hidden',!o);
    if(o){ setTimeout(function(){ x.focus(); },60); } else { b.focus(); } }
  b.addEventListener('click',function(){ set(true); });
  x.addEventListener('click',function(){ set(false); });
  s.addEventListener('click',function(){ set(false); });
  document.addEventListener('keydown',function(e){ if(e.key==='Escape' && H.classList.contains('cl-open')) set(false); });
})();
</script>'''

def apply(html, page):
    """BURGER 자리표시(<!--CL-BURGER-->)를 버튼으로 바꾸고, CSS·메뉴·스크립트를 넣어요."""
    assert '<!--CL-BURGER-->' in html and '</style>' in html and '</body>' in html
    html = html.replace('<!--CL-BURGER-->', BURGER, 1)
    i = html.index('</style>'); html = html[:i] + CSS + html[i:]
    i = html.rindex('</body>'); html = html[:i] + drawer(page) + '\n' + JS + '\n' + html[i:]
    return html
