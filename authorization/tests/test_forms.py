from django.test import TestCase
from authorization.forms import LoginForm, RegisterForm


class RegisterFormValidTest(TestCase):
    def test_valid_from(self):
        form_data = {'username': 'valid', 'email': 'valid@valid.val',
                     'password': 'valpass111', 'confirm': 'valpass111'}
        form = RegisterForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_username(self):
        form_data = {'username': 'invalid%$@&', 'email': 'valid@valid.val',
                     'password': 'valpass111', 'confirm': 'valpass111'}
        form = RegisterForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_invalid_email(self):
        form_data = {'username': 'valid', 'email': 'invalidvalid.val',
                     'password': 'valpass111', 'confirm': 'valpass111'}
        form = RegisterForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_invalid_password(self):
        form_data = {'username': 'valid', 'email': 'valid@valid.val',
                     'password': 'valp%@%ass111', 'confirm': 'valpass111'}
        form = RegisterForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_pass_not_mutch(self):
        form_data = {'username': 'valid', 'email': 'valid@valid.val',
                     'password': 'valpass222', 'confirm': 'valpass111'}
        form = RegisterForm(data=form_data)
        self.assertFalse(form.is_valid())


class RegisterFormLabelTest(TestCase):
    def test_username_label(self):
        form = RegisterForm()
        self.assertTrue(form.fields['username'].label is None or
                        form.fields['username'].label == 'username')

    def test_email_label(self):
        form = RegisterForm()
        self.assertTrue(form.fields['email'].label is None or
                        form.fields['email'].label == 'email')

    def test_password_label(self):
        form = RegisterForm()
        self.assertTrue(form.fields['password'].label is None or
                        form.fields['password'].label == 'password')

    def test_confirm_label(self):
        form = RegisterForm()
        self.assertTrue(form.fields['confirm'].label is None or
                        form.fields['confirm'].label == 'confirm')


class LoginFormLabelTest(TestCase):
    def test_username_label(self):
        form = LoginForm()
        self.assertTrue(form.fields['username'].label is None or
                        form.fields['username'].label == 'username')

    def test_login_label(self):
        form = LoginForm()
        self.assertTrue(form.fields['password'].label is None or
                        form.fields['password'].label == 'password')
