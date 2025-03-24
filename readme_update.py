import feedparser
import ssl
import os

# 로컬 테스트 시 ssl 인증서 문제 해결용
ssl._create_default_https_context = ssl._create_unverified_context

# rss 추출
feed = feedparser.parse("https://striver.tistory.com/rss")

# README 양식
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
    # print(i['link'], i['title'])

# 기존 README.md 파일 내용과 비교
current_content = ""
if os.path.exists("README.md"):
    with open("README.md", "r", encoding="utf-8") as f:
        current_content = f.read()

# 내용이 변경된 경우에만 파일 업데이트
if current_content != markdown_text:
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(markdown_text)
    print("README.md 파일이 업데이트되었습니다.")
else:
    print("블로그 포스트에 변경사항이 없습니다.")
