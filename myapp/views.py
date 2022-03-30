from django.shortcuts import render, HttpResponse

topics = [#리스트 생성
    {'id': 1, 'title': 'routing', 'body': 'Routing is ..'},
    {'id': 2, 'title': 'view', 'body': 'View is ..'},
    {'id': 3, 'title': 'Model', 'body': 'Model is ..'},
]


def index(request):
    global topics #전역변수 지정
    ol = ''
    for topic in topics:
        ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>' #f 사용시 중괄호에서 변수 바로 사용가능
    return HttpResponse(f'''
    <html>
    <body>
        <h1>Django</h1>
        <ol>
            {ol}
        </ol>
        <h2>Welcome</h2>
        Hello, Django
    </body>
    </html>
    ''')


def create(request):
    return HttpResponse('Create')

def read(request, id):
    return HttpResponse('Read!'+id)