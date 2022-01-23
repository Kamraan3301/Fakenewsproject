from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField
from wtforms.validators import Length


class OriginalTextForm(FlaskForm):
	original_text = TextAreaField('Original Text', validators=[Length(min=20, max=10000)], render_kw={'placeholder': 'Enter text here..'})
	global_times = SubmitField('Global Times ')
	predict = SubmitField('Predict')
	daily=SubmitField('Dailystar news')
	abc=SubmitField('ABC news')
