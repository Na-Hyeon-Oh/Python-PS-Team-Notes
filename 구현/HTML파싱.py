# HTML 파싱
# https://www.acmicpc.net/problem/22859
'''
다음을 보장하는 HTML 문서가 주어질 때, parsing 결과를 출력하라.
1. HTML의 시작은 <main>으로 시작하고 </main>으로 끝난다. 또한 여는 태그가 있다면 닫는 태그가 항상 쌍으로 존재한다.
2. <main>, </main> 사이에 여러 문단이 있을 수 있으며 문단들을 구분할 때 사용하는 div 태그만 사용된다. 문단의 제목은 항상 알파벳(a-z, A-Z)과 언더바(_), 공백( )으로만 구성되어 있다. 제목의 시작 부분과 끝부분은 공백이 없다.
3. <div>, </div> 사이에는 반드시 문장을 의미하는 p 태그만 존재하고 여는 태그 <div>의 속성으로는 반드시 title이 존재한다.
즉, <div title="(A)"> 와 같이 존재하며, (A) 부분은 문단의 제목이다.
4. <p>, </p> 사이에는 main, div, p 태그를 제외한 다른 태그들이 존재할 수 있으며, 예시에서 <br>와 같이 여는 태그만 존재할 수 있고, 여는 태그와 닫는 태그가 올바른 쌍으로 존재한다. 이때, 올바른 쌍은 아직 닫히지 않는 태그가 있을 때 다른 닫는 태그가 올 수 없다. 예를 들어, <b>a<i></b></i>는 올바른 쌍이 아니고, <b>a<i>b</i></b>은 올바른 쌍이다.
태그를 표현하는 '<', '>'를 제외하고는 항상 알파벳(a-z, A-Z)과 공백(' ')으로만 주어진다.
5. 태그를 표시하는 '<'와 '>' 사이에는 소문자 알파벳(a-z), 공백(' '), 슬래시('/')로 이루어져 있으며 '/' 같은 경우는 닫는 태그에만 존재한다.
6. HTML 문서는 한 줄로 주어진다. <p>, </p> 사이에 존재하는 태그를 제외하고는 태그 사이의 공백이 없다.
파싱은 다음과 같이 진행한다.
1. p 태그 안에 있는 문장에서 태그가 있다면 태그를 지운다.
2. p 태그 안에 있는 문장 시작과 끝에 공백이 있다면 지운다.
문장에서 공백(space)이 2개 이상 연속적으로 붙어있다면 이를 하나의 공백으로 바꾼다.
3. 마지막으로, 여는 태그 <p>와 닫는 태그 </p>를 지운다.
* HTML 문서의 길이 <= 1,000,000
* 제한 시간 1초
'''

# (i)
import sys
import re

def input():
  return sys.stdin.readline().rstrip()

html = input()
html = html.split("<main>")[1].split("</main>")[0]
html = html.split("</div>")[:-1]
for div in html:
  title = div.split(">")[0]
  paragraphs = div[len(title)+1:].split("</p>")[:-1]
  title = title.split("\"")[1]
  print(f'title : {title}')
  for p in paragraphs:
    parsed = re.sub(r'</?[\w ]*>', '', p)
    parsed = ' '.join(parsed.split())
    print(parsed)


# (ii)

import re  
  
html_doc = input()  
  
html_doc = html_doc[len('<main>'): -len('</main>')]  
html_doc = re.sub(r'<div +title="([\w ]*)">', r'title : \1\n', html_doc)  
html_doc = re.sub(r'</div>', '', html_doc) 
html_doc = re.sub(r'<p>', '', html_doc)  
html_doc = re.sub(r'</p>', '\n', html_doc)  
html_doc = re.sub(r'</?[\w ]*>', '', html_doc)  
html_doc = re.sub(r' ?\n ?', '\n', html_doc)  
html_doc = re.sub(r' {2,}', ' ', html_doc)  
  
print(html_doc)
