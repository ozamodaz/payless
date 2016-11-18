from flask import Flask, render_template, redirect, url_for
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap
from flask.ext.wtf import Form
from wtforms import SubmitField
from payless import get_data

app = Flask(__name__)
app.config['SECRET_KEY'] = 'KEY'

manager = Manager(app)
bootstrap = Bootstrap(app)


class MyForm(Form):
    submit = SubmitField('Refresh')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyForm()
    if form.validate_on_submit():
        db = get_data(force_refresh=True)
        return redirect(url_for('index'))
    else:
        db = get_data()
    providers = db['order']
    domains = db['cmp_domains']
    prices = db['data']
    date = db['creation_date'].strftime('%d.%m.%Y %H:%M')
    # import ipdb; ipdb.set_trace()

    return render_template(
                           'index.html', form=form, prices=prices,
                           domains=domains, providers=providers, date=date
                           )


if __name__ == '__main__':
    manager.run()
