from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'     # созздание и название базы данных
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'jldwflnieoi234nevnoixcseqodp234lclsdsdc09lknmv'
db = SQLAlchemy(app)


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.Text, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)
    model = db.Column(db.Text, nullable=False)
    full_post = db.Column(db.Text, nullable=False)
    photo1 = db.Column(db.Text, nullable=False)
    photo2 = db.Column(db.Text, nullable=False)
    photo3 = db.Column(db.Text, nullable=False)


def __repr__(self):
    return '<Item %r>' % self.id


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST' and request.form['password'] == '2':
        password = request.form['password']
        session['password'] = password
        return redirect('/admin')
    else:
        return render_template("login.html")


@app.route('/admin')
def admin():
    if session['password'] == '2':
        return render_template('admin.html')
    else:
        return redirect('/login')


@app.route('/create', methods=['POST', 'GET'])
def create():
    if request.method == 'POST' and session['password'] == '2':
        link = request.form['link']
        price = request.form['price']
        description = request.form['description']
        model = request.form['model']
        full_post = request.form['full_post']
        photo1 = request.form['photo1']
        photo2 = request.form['photo2']
        photo3 = request.form['photo3']

        item = Item(link=link, price=price, description=description, model=model, full_post=full_post, photo1=photo1, photo2=photo2, photo3=photo3)
        try:
            db.session.add(item)
            db.session.commit()
            return redirect('/')
        except:
            return 'Так-Так, что-то не так'
    elif session['password'] == '2':
        return render_template('create.html')
    else:
        return f'место где что то пошло не так 1'


@app.route('/update/', methods=['POST', 'GET'])
def update():
    if request.method == 'POST' and 'id' in request.form and 'link' not in request.form and session['password'] == '2':
        id = request.form['id']
        article = Item.query.get(id)
        return render_template('post_update.html', article=article)
    elif request.method == 'POST' and 'link' in request.form:
        num = request.form['num']
        article = Item.query.get(num)
        article.link = request.form['link']
        article.price = request.form['price']
        article.description = request.form['description']
        article.model = request.form['model']
        article.full_post = request.form['full_post']
        article.photo1 = request.form['photo1']
        article.photo2 = request.form['photo2']
        article.photo3 = request.form['photo3']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'Так-Так, что-то не так'
    elif session['password'] == '2':
        return render_template('update.html')


@app.route('/del', methods=['POST', 'GET'])
def post_del():
    if request.method == 'POST' and session['password'] == '2':
        id = request.form['id']
        article = Item.query.get(id)
        try:
            db.session.delete(article)
            db.session.commit()
            return redirect('/')
        except:
            return 'При удалении произошла ошибка'
    elif session['password'] == '2':
        return render_template('del.html')
    else:
        return redirect('/login')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/cufflink')
def cufflink():
    model_post = Item.query.order_by(Item.id).all()
    return render_template("cufflinks.html", model_post=model_post)


@app.route('/rings')
def rings():
    model_post = Item.query.order_by(Item.id).all()
    return render_template("rings.html", model_post=model_post)


@app.route('/earrings')
def earrings():
    model_post = Item.query.order_by(Item.id).all()
    return render_template("earrings.html", model_post=model_post)


@app.route('/brooch')
def brooch():
    model_post = Item.query.order_by(Item.id).all()
    return render_template("brooch.html", model_post=model_post)


@app.route('/necklace')
def necklace():
    model_post = Item.query.order_by(Item.id).all()
    return render_template("necklace.html", model_post=model_post)


@app.route('/clip')
def clip():
    model_post = Item.query.order_by(Item.id).all()
    return render_template("clip.html", model_post=model_post)


@app.route('/post/<int:id>')
def full_post(id):
    post = Item.query.get(id)
    return render_template('post.html', post=post)


@app.route('/about')
def about():
    return render_template('About_us.html')


@app.route('/product')
def product():
    return render_template('Product.html')


if __name__ == '__main__':
    app.run(debug=False)
