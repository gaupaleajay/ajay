from flask import Flask,render_template,request
from flask_mail import Mail
import json

with open('config.json', 'r') as c:
    params = json.load(c)["params"]
	
app = Flask(__name__)
app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = '465',
    MAIL_USE_SSL = True,
    MAIL_USERNAME = params['gmail-user'],
    MAIL_PASSWORD=  params['gmail-password']
)
mail = Mail(app)

@app.route('/',methods = ['GET', 'POST'])
def home():
	if(request.method=='POST'):
		name = request.form.get('name')
		email = request.form.get('email')
		message = request.form.get('message')
		mail.send_message('New message from ' + name,
                          sender=email,
                          recipients = [params['gmail-user']],
                          body = message + "\n\nKindly contact me on\nemail_id : "+ email +"\n\n" + "Thank you"
                        )
	return render_template('index.html',params=params)
    
app.run(debug=True)  