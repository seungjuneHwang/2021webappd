from flask import Flask, render_template, request
from hello import money_pung
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/money')
def money():
    return render_template("money.html")

@app.route('/show', methods=['GET', 'POST'])
def show():
    if request.method == 'GET':
        return "Get 으로 들어온 페이지"
    else:
        # form 으로 전달된 데이터를 받아서 뻥튀기 해주야 함!!
        money = request.form['money']
        # money 의 값이 문자열이기 때문에 숫자로 변경
        print("전달된 값은? ", int(money)*2)
        im = money_pung(int(money))    # 뻥튀기 함수 사용
        return "당신의 능력을 보여줘~ 얍<br><b>{}</b>원 드립니다".format(im)
        # return "당신의 능력을 보여줘~ 얍<br><b>{}</b>원 드립니다".format(money_pung(int(money)))

@app.route('/showmoney')
def showmoney():
    return render_template("smoney.html")
    # return '''
    #     <iframe width="420" height="345" src="https://www.youtube.com/embed/tgbNymZ7vqY?autoplay=1&mute=1">
    #     </iframe>
    # '''

if __name__ == '__main__':
    app.run()