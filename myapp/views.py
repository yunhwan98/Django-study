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
        <h1><a href="/">Django</a></h1> #Django 클릭시 홈으로 이동
        <ul>
            {ol}
        </ul>
        {articleTag}    #articleTag따라 내용 변경
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
        if topic['id'] == int(id):  #선택한 id가 된다면
            article = f'<h2>{topic["title"]}</h2>{topic["body"]}'   #article 지정
    return HttpResponse(HTMLTemplate(article))

def create(request):
    return HttpResponse('Create')