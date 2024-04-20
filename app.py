from flask import Flask,render_template ,request
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)


class MyText(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text=db.Column(db.String(200))


@app.route('/')
def first():
   return render_template('text.html')


@app.route('/text_send',methods=['POST'])
def text_send():
    if request.method=='POST':
        text=request.form.get('text')
        if text is not None:
            res=MyText(text=text)
            db.session.add(res)
            db.session.commit()
            return 'text saved',text
        else:
            return " text no receive"
        
    else:
        return "invalid text"
    

@app.route('/get_text/<int:id>',methods=['GET'])
def get_text(id):
    texts = MyText.query.get(id)
    return render_template('display.html', texts=texts)





if __name__=='__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True)


