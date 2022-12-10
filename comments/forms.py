from django.forms import ModelForm
from .models import Comment
import requests
import environ

env = environ.Env()
environ.Env.read_env()


class FormComment(ModelForm):
    def clean(self):
        raw_data = self.data

        recaptcha_response = raw_data.get('g-recaptcha-response')

        if not recaptcha_response:
            self.add_error(
                None,
                "Please check the box 'I'm not a robot'"
            )

        recaptcha_request = requests.post(
            'https://www.google.com/recaptcha/api/siteverify',
            data={
                'secret': env('GOOGLE_RECAPTCHA_SECRET_KEY'),
                'response': recaptcha_response,
            }
        )
        recaptcha_result = recaptcha_request.json()

        if not recaptcha_result.get('success') and recaptcha_response:
            self.add_error(
                None,
                "Sorry Mr. Robot, an error occurred'"
            )

        cleaned_data = self.cleaned_data
        name = cleaned_data.get('name_comment')
        email = cleaned_data.get('email_comment')
        comment = cleaned_data.get('comment')

        if len(name) < 2:
            self.add_error(
                'name_comment',
                'your need more than 2 words in name'
            )

    class Meta:
        model = Comment
        fields = ('name_comment', 'email_comment', 'comment',)
