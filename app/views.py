{}
from flask import render_template
from flask_wtf import Form
from wtforms import fields
from wtforms.validators import Required

from . import app, estimator, target_names, pipe, pd

class PredictForm(Form):
    """Fields for Predict"""
    myChoices = ["one", "two", "three"]
    input_text = fields.TextAreaField('Paste Transcript Here:')

    submit = fields.SubmitField('Submit')


@app.route('/', methods=('GET', 'POST'))
def index():
    """Index page"""
    form = PredictForm()
    prediction = None

    if form.validate_on_submit():
        # store the submitted values
        submitted_data = form.data
        text = submitted_data['input_text']

        # Create array from values
        my_prediction = estimator.predict(flower_instance)
        pred_vals = pipe.predict_proba(pd.Series([str(text)]))

        if pred_vals[0][1] > 0.5:
            prediction = 'borrrrrringgg..'
        else:
            prediction = 'like a TED talk! Oohh la laaa!'

    return render_template('index.html', form=form, prediction=prediction)
