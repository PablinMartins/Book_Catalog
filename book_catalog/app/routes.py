from flask import render_template, redirect, url_for, flash, request, abort
from app import app, db
from app.models import Book, User
from app.forms import BookForm, LoginForm, RegistrationForm
from app.forms import BookForm, LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user, login_required, LoginManager



try:
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'
except Exception as e:
    abort(500) 

@login_manager.user_loader
def load_user(user_id):
    try:
        return User.query.get(int(user_id))
    except Exception as e:
        abort(500)

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def login():
    try:
        if current_user.is_authenticated:
            return redirect(url_for('catalog'))
        
        form = LoginForm()
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data
            
            user = User.query.filter_by(username=username).first()
            if user is None or not user.check_password(password):
                flash('Nome de usuário ou senha inválidos.', 'error')
                return redirect(url_for('login'))
            
            login_user(user)
            flash('Login bem-sucedido!', 'success')
            return redirect(request.args.get('next') or url_for('catalog'))
        
        return render_template('index.html', title='Login', form=form)
    except Exception as e:
        abort(500)


@app.route('/catalog', methods=['GET'])
@login_required
def catalog():
    try:
        books = Book.query.filter_by(user_id=current_user.id).all()
        return render_template('catalog.html', books=books)
    except Exception as e:
        abort(500)

@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    try:
        logout_user()
        flash('Você saiu da sua conta.', 'info')
        return redirect(url_for('login'))
    except Exception as e:
        abort(500)

@app.route('/add_book', methods=['GET', 'POST'])
@login_required
def add_book():
    try:
        form = BookForm()
        if form.validate_on_submit():
            book = Book(title=form.title.data, author=form.author.data, comment=form.comment.data, review = form.review.data, user_id=current_user.id)
            db.session.add(book)
            db.session.commit()
            flash('Livro adicionado com sucesso!', 'success')
            return redirect(url_for('catalog'))
        return render_template('add_book.html', title='Add Book', form=form)
    except Exception as e:
        abort(500)


@app.route('/edit_book/<int:book_id>', methods=['GET', 'POST'])
@login_required
def edit_book(book_id):
    try:
        book = Book.query.get_or_404(book_id)
        form = BookForm()
        if form.validate_on_submit():
            book.title = form.title.data
            book.author = form.author.data
            book.comment = form.comment.data
            book.review = form.review.data
            db.session.commit()
            flash('Livro editado com sucesso!', 'success')
            return redirect(url_for('catalog'))
        form.title.data = book.title
        form.author.data = book.author
        form.comment.data = book.comment
        return render_template('edit_book.html', title='Editar Livro', form=form, book_id=book_id)
    except Exception as e:
        abort(500)

@app.route('/delete/<int:book_id>', methods=['POST'])
@login_required
def delete_book(book_id):
    try:

        book = Book.query.get_or_404(book_id)
        db.session.delete(book)
        db.session.commit()
        flash('Livro removido com sucesso!', 'success')
        return redirect(url_for('catalog'))
    except Exception as e:
        abort(500)

@app.route('/register', methods=['GET', 'POST'])
def register():
    try:
        form = RegistrationForm()
        if form.validate_on_submit():
            user = User(username=form.username.data)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            flash('Registro bem-sucedido! Agora você pode fazer login.', 'success')
            return redirect(url_for('login'))
        return render_template('register.html', title='Registrar', form=form)
    except Exception as e:
        abort(500)

@app.route('/book/<int:book_id>', methods=['GET'])
@login_required
def book_detail(book_id):
    try:
        book = Book.query.get_or_404(book_id)
        if book.user_id != current_user.id:
            abort(403)
        return render_template('book_detail.html', title=book.title, book=book)
    except Exception as e:
        abort(500)
