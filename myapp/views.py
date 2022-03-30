from django.shortcuts import render, HttpResponse
topics = [
    {'id':1, 'title':'routing', 'body':'Routing is ..'},
    {'id':2, 'title':'view', 'body':'View is ..'},
    {'id':3, 'title':'Model', 'body':'Model is ..'},
]

def HTMLTemplate(articleTag): #템플릿 생성 함수 만들기
    global topics
    ol = ''
    for topic in topics:
        ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'
    return f'''
    <html>
    <body>
        <h1><a href="/">Django</a></h1> <!-- 클릭시 django로 이동-->
        <ul>
            {ol}
        </ul>
        {articleTag}    <!-- articleTag따라 내용 변경 -->
      <ul>
            <li><a href="/create/">create</a></li>
        </ul>
    </body>
    </html>
    '''
def index(request):
    article = '''
    <h2>Welcome</h2> 
    Hello, Django
    '''
    return HttpResponse(HTMLTemplate(article))
def read(request, id):
    global topics
    article = ''
    for topic in topics:
        if topic['id'] == int(id):
            article = f'<h2>{topic["title"]}</h2>{topic["body"]}'
    return HttpResponse(HTMLTemplate(article))

def create(request):
    article = '''
        <form action="/create/">     <!--폼 생성 -->
            <p><input type="text" name="title" placeholder="title"></p> <!--제목 -->
            <p><textarea name="body" placeholder="body"></textarea></p> <!--내용 -->
            <p><input type="submit"></p>  <!--제출 -->
        </form>
    '''
    return HttpResponse(HTMLTemplate(article))