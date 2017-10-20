from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

class ReuseableForm(Form):
    guess = TextField('Guess: ', validators=[validators.required()])

@app.route("/", methods=['GET', 'POST'])

def hello():
    form = ReuseableForm(request.form)

    print(form.errors)
    if request.method == 'POST':
        guess = request.form['guess']
        # Need to check input before passing it in
        print(guess)

        if form.validate():
            response = check(guess)
            form = ReuseableForm()
            flash(response)
        else:
            flash('Please enter a valid number')

    return render_template('hello.html', form=form)

def check(y):
    x = 4
    if int(y) == x:
        return 'Well done!'
    if int(y) > x:
        return 'Guess a little lower'
    if int(y) < x:
        return 'Guess a little higher'


if __name__ == '__main__':
    app.run()
