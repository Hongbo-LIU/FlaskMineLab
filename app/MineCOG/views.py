from flask import render_template, redirect, request, url_for, flash
from . import MineCOG
from .forms import MineInfoForm


@MineCOG.route('/mineinfo', methods=['GET', 'POST'])
def mineinfo():
    form = MineInfoForm()
    if form.validate_on_submit():
        mine_name = form.mine_name
        mineral = form.mine_mineral
        flash('Mine site is {}, the main mineral is {}'.format(mine_name, mineral))
        return redirect(url_for('MineCOG.mineinfo'))
    return render_template('minecog/welcome.html', form=form)
