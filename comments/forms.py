from django.forms import ModelForm
from .models import Comment


class FormComment(ModelForm):
    def clean(self):
        data = self.cleaned_data
        name = data.get('name_comment')
        email = data.get('email_comment')
        comment = data.get('comment')

        if len(name) < 2:
            self.add_error(
                'name_comment',
                'your need more than 2 words in name'
            )

    class Meta:
        model = Comment
        fields = ('name_comment', 'email_comment', 'comment',)
