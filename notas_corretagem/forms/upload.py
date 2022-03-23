from flask_wtf import FlaskForm
from wtforms import MultipleFileField


class Pdf(FlaskForm):
    pdfs = MultipleFileField()
