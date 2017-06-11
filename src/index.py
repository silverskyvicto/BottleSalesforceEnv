from bottle import route, run, template, request
from simple_salesforce import Salesforce

@route('/')
def index(msg='This page is home page.'):
    return template('index.tpl', msg=msg)

@route('/', method=["POST"])
def login_salesforce():
    uname = request.POST.getunicode("username")
    upw   = request.POST.getunicode("password")
    token = request.POST.getunicode("security_token")
    try:
        sf = Salesforce(username=uname, password=upw, security_token=token)
        print(sf)
    except Exception as e:
        return template("login_error")
    finally:
        print("ログイン処理終了")

    return template("login_success")

run(host='localhost', port=8080, debug=True, reloader=True)
