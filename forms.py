from flask.ext.wtf import Form, TextField, TextAreaField, SubmitField
# import classes above

#fill in variables
class ContactForm(Form):
    name = TextField("name")
    email = TextField("email")
    message = TextAreaField("message")
    submit = SubmitField("submit")


