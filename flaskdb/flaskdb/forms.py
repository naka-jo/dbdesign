"""
A Sample Web-DB Application for DB-DESIGN lecture
Copyright (C) 2022 Yasuhiro Hayashi
"""
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, SubmitField
from wtforms.validators import DataRequired, length
from flaskdb.widgets import ButtonField

class LoginForm(FlaskForm):
    username = StringField(
        "User Name",
        validators = [
            DataRequired(message="User Name is required."),
            length(max=64, message="User Name should be input within 64 characters."),
        ],
    )
    password = PasswordField(
        "Password",
        validators = [
            DataRequired(message="Password is required."),
        ],
    )
    cancel = ButtonField("Cancel")
    submit = SubmitField("Login")

    def copy_from(self, user):
        self.username.data = user.username
        self.password.data = user.password

    def copy_to(self, user):
        user.username = self.username.data
        user.password = self.password.data

class AddItemForm(FlaskForm):
    category = StringField(
        "Category",
        validators = [
            DataRequired(message="Category Name is required."),
        ],
    )
    task = StringField(
        "Task",
        validators = [
            DataRequired(message="Task is required."),
        ],
    )
    role = StringField(
        "Role",
        validators = [
            DataRequired(message="Role is required."),
        ],
    )
    start_date = StringField(
        "Start_date",
        validators = [
            DataRequired(message="Start_date is required."),
        ],
    )
    final_date = StringField(
        "Final_date",
        validators = [
            DataRequired(message="Final_date is required."),
        ],
    )
    cancel = ButtonField("Cancel")
    submit = SubmitField("Submit")

    def copy_from(self, item):
        self.category.data = item.category
        self.task.data = item.task
        self.role.data = item.role
        self.start_date = item.start_date
        self.final_date = item.final_date

    def copy_to(self, item):
        item.category = self.category.data
        item.task = self.task.data
        item.role = self.role.data
        item.start_date = self.start_date.data
        item.final_date = self.final_date.data
        
class SearchItemForm(FlaskForm):
    category = StringField(
        "Task Name",
        validators = [
            DataRequired(message="Task Name is required."),
        ],
    )
    cancel = ButtonField("Cancel")
    submit = SubmitField("Submit")

    def copy_from(self, item):
        self.category.data = item.category

    def copy_to(self, item):
        item.category = self.category.data
