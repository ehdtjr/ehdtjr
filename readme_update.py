import feedparser
import ssl
import os

# SSL 인증서 문제 해결용
ssl._create_default_https_context = ssl._create_unverified_context

# RSS 피드 파싱
feed = feedparser.parse("https://striver.tistory.com/rss")

# README 헤더 템플릿
markdown_text = """# 안녕하세요, LLM과 RAG 기술에 집중하는 개발자입니다 👋

**LLM, RAG** 기술에 깊은 관심을 가지고 있는 엔지니어 지망생입니다. **변화에 유연하게 대응**하며 능동적으로 실행하는 것을 중요하게 생각하며, 현재 이 기술들을 심도 있게 탐구하며 전문성을 키워가고 있습니다. 이를 바탕으로 **혁신적이고 실질적인 문제 해결**에 기여하는 것을 목표로 하고 있습니다.

RAG 시스템 구축, Agent Workflow에 집중하며, Python 기반의 백엔드 개발과 LLM 어플리케이션 통합에 역량을 쌓고 있습니다.

## 🛠️ Tech Stack

| 분야 | 기술 |
|------|------|
| **Language** | ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) |
| **LLM** | ![LangChain](https://img.shields.io/badge/LangChain-%23000000.svg?style=for-the-badge) ![LangGraph](https://img.shields.io/badge/LangGraph-%23000000.svg?style=for-the-badge) ![Transformers](https://img.shields.io/badge/Transformers-%23FF6F00.svg?style=for-the-badge) ![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white) |
| **WEB** | ![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi) ![Streamlit](https://img.shields.io/badge/streamlit-%23FF4B4B.svg?style=for-the-badge&logo=streamlit&logoColor=white) ![Flutter](https://img.shields.io/badge/Flutter-%2302569B.svg?style=for-the-badge&logo=Flutter&logoColor=white) |
| **DB** | ![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white) ![MariaDB](https://img.shields.io/badge/MariaDB-003545?style=for-the-badge&logo=mariadb&logoColor=white) |
| **LLMOps** | ![LangSmith](https://img.shields.io/badge/LangSmith-%23000000.svg?style=for-the-badge) ![Opik](https://img.shields.io/badge/Opik-%234285F4.svg?style=for-the-badge) ![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white) ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white) |
| **협업 도구** | ![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white) ![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white) ![Notion](https://img.shields.io/badge/Notion-%23000000.svg?style=for-the-badge&logo=notion&logoColor=white) |

<br>

### 📕 Latest Blog Posts   
"""

# 최근 블로그 추가
for i in feed["entries"][:10]:
    markdown_text += f"<a href =\"{i['link']}\"> {i['title']} </a> <br>\n"

# 푸터 추가
markdown_text += """
## 📫 Connect With Me

[![Blog](https://img.shields.io/badge/Blog-striver.tistory.com-FF5722?style=flat-square&logo=blogger&logoColor=white)](https://striver.tistory.com)
[![GitHub](https://img.shields.io/badge/GitHub-ehdtjr-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/ehdtjr)
"""

# 항상 새 내용 작성
with open("README.md", "w", encoding="utf-8") as f:
    f.write(markdown_text)
    
print("README.md가 최신 블로그 포스트로 업데이트되었습니다.")