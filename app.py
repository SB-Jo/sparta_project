from flask import Flask, render_template, request, redirect, send_file
from werkzeug.utils import secure_filename
from kakao_tokenize import get_wordcloud

app = Flask("kakao")

@app.route("/")
def render_file():
    return render_template('index.html')

@app.route('/fileupload', methods=['GET','POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        filename = 'kakao.txt'
        f.save(filename)
        return redirect('/')


@app.route('/wordcloud', methods=['GET', 'POST'])
def wordcloud():
    filename = 'kakao.txt'
    talk_dic, wc = get_wordcloud(filename)
    talker = [talker for talker in talk_dic.keys()]
    return render_template('index2.html', talkers=talker, wcs=wc)

@app.route('/export')
def export():
    try:
        word = request.args.get('word')
        if not word:
            raise Exception()
        return send_file(f"./static/wordcloud_{word}.png")
    except:
        return redirect('/')

        

# <> : PlaceHolder
# 주소 들어갈 때 https://****/sbjo로 들어가면 hello sbjo라고 출력된다.
@app.route("/<username>")
def funct(username):
    return f"hello {username} how are you doing "


app.run(host="0.0.0.0", port=5000, debug=True)