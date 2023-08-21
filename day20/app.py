from nltk.chat.util import Chat
qa_pair = [
            ['(.*)your name',['my name is Snobot']],
            ['(.*)my name',['Do you not know your own name ? ']],
            ['(.*)who(.*)you',['I am Snobot was invented by snoobe for testing']],
            ['(hi|hey|hello)',['hello','hi there','heyy','hello']],
            ['(.*)snoobe(.*)',['He is my developer.']],
            ['(.*)robot(.*)',['Yes, I am a Bot, You can call me the SnoBot.']],
            ['(.*)joke(.*)',["I am not created for entertainment, I am created for testing."]],
            ['(.*)love(.*)',['''I think you are single ,feeling bad to know.
                             But don't worry I will treat you as a Friend.''']],
            ['(.*)hindi(.*)',["I can't understand hindi, Snoobe tought me only one language ."]],

    ]

cb = Chat(qa_pair)
from flask import Flask,render_template,request
app = Flask(__name__)
@app.route('/',methods=['GET'])
def home():
    text = 'Hi '
    global cb
    if request.args.get('q') !=None:
        que = request.args.get('q')
        text = cb.respond(que)
        if text == None:
            text = 'Unkonwn'
    return render_template('index.html',resp=text) #template tag :>{{ }},{% %}
@app.route('/new')
def new():
    return "<html><h1>Awsome</h1></html>"

app.run(debug=True)