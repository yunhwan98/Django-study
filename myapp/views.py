from django.shortcuts import render, HttpResponse, redirect #redirect 추가
from django.views.decorators.csrf import csrf_exempt    #csrf 에러 스킵
nextId = 4
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

@csrf_exempt    #csrf 에러 스킵
def create(request):
    global nextId
    if request.method == 'GET': #GET방식으로 받을 때
        article = '''
               <form action="/create/" method="post">
                   <p><input type="text" name="title" placeholder="title"></p>
                   <p><textarea name="body" placeholder="body"></textarea></p>
                   <p><input type="submit"></p>
               </form>
           '''
        return HttpResponse(HTMLTemplate(article))
    elif request.method == 'POST':  #POST방식으로 받을 때
        title = request.POST['title']
        body = request.POST['body']
        newTopic = {"id": nextId, "title": title, "body": body} #newTopic 생성
        topics.append(newTopic) #기존 topics에 추가
        url = '/read/' + str(nextId)
        nextId = nextId + 1 #다음을 위해 +1
        return redirect(url)    #create시 생성된 페이지로 이동