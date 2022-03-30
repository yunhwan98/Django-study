from django.shortcuts import render, HttpResponse, redirect #redirect 추가
from django.views.decorators.csrf import csrf_exempt    #csrf 에러 스킵
nextId = 4
topics = [
    {'id':1, 'title':'routing', 'body':'Routing is ..'},
    {'id':2, 'title':'view', 'body':'View is ..'},
    {'id':3, 'title':'Model', 'body':'Model is ..'},
]

def HTMLTemplate(articleTag, id=None):  #id값을 기본값으로 줘서 에러 방지
    global topics
    contextUI = ''
    if id != None:  #id가 있을 때만 delete 설정
        contextUI = f'''
            <li>
                <form action="/delete/" method="post">  <!-- post방식 사용-->
                    <input type="hidden" name="id" value={id}>  <!--hidden은 눈에 보이지 않지만 전송-->
                    <input type="submit" value="delete">
                </form>
            </li>
        '''
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
            {contextUI}
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
    return HttpResponse(HTMLTemplate(article, id))   #id값 인자 추가


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
        newTopic = {"id":nextId, "title":title, "body":body}    #newTopic 생성
        topics.append(newTopic) #기존 topics에 추가
        url = '/read/'+str(nextId)
        nextId = nextId + 1 #다음을 위해 +1
        return redirect(url)    #create시 생성된 페이지로 이동

@csrf_exempt
def delete(request):
    global topics
    if request.method == 'POST':
        id = request.POST['id']
        newTopics = []
        for topic in topics:    #id와 일치하지 않는 것들 추가
            if topic['id'] != int(id):
                newTopics.append(topic)
        topics = newTopics
        return redirect('/')