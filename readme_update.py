import feedparser
import ssl
import os

# SSL 인증서 문제 해결용
ssl._create_default_https_context = ssl._create_unverified_context

# RSS 피드 파싱
feed = feedparser.parse("https://striver.tistory.com/rss")

# README 템플릿
markdown_text = """
###  🐱 github stats  

<div id="main" align="center">
    <img src="https://github-readme-stats.vercel.app/api?username=ehdtjr&count_private=true&show_icons=true&theme=radical"
        style="height: auto; margin-left: 20px; margin-right: 20px; padding: 10px;"/>
    <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=ehdtjr&layout=compact"   
        style="height: auto; margin-left: 20px; margin-right: 20px; padding: 10px;"/>
</div>

<br>

### 📕 Latest Blog Posts   

"""

# 최근 블로그 추가
for i in feed["entries"][:10]:
    markdown_text += f"<a href =\"{i['link']}\"> {i['title']} </a> <br>\n"

# 항상 새 내용 작성
with open("README.md", "w", encoding="utf-8") as f:
    f.write(markdown_text)
    
print("README.md가 최신 블로그 포스트로 업데이트되었습니다.")