from django.test import TestCase
from authorization.forms import LoginForm, RegisterForm


class RegisterFormValidTest(TestCase):
    def test_valid_from(self):
        form_data = {'username': 'valid', 'email': 'valid@valid.val',
                     'password1': 'valpass111', 'password2': 'valpass111'}
        form = RegisterForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_username(self):
        form_data = {'username': 'invalid%$@&', 'email': 'valid@valid.val',
                     'password1': 'valpass111', 'password2': 'valpass111'}
        form = RegisterForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_invalid_email(self):
        form_data = {'username': 'valid', 'email': 'invalidvalid.val',
                     'password1': 'valpass111', 'password2': 'valpass111'}
        form = RegisterForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_invalid_password(self):
        form_data = {'username': 'valid', 'email': 'valid@valid.val',
                     'password1': 'valp%@%ass111', 'password2': 'valpass111'}
        form = RegisterForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_pass_not_mutch(self):
        form_data = {'username': 'valid', 'email': 'valid@valid.val',
                     'password1': 'valpass222', 'password2': 'valpass111'}
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

    def test_password1_label(self):
        form = RegisterForm()
        self.assertTrue(form.fields['password1'].label is None or
                        form.fields['password1'].label == 'password')

    def test_password2_label(self):
        form = RegisterForm()
        self.assertTrue(form.fields['password2'].label is None or
                        form.fields['password2'].label == 'Confirm password')


class LoginFormLabelTest(TestCase):
    def test_username_label(self):
        form = LoginForm()
        self.assertTrue(form.fields['username'].label is None or
                        form.fields['username'].label == 'username')

    def test_login_label(self):
        form = LoginForm()
        self.assertTrue(form.fields['password'].label is None or
                        form.fields['password'].label == 'password')
