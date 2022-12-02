from django import template

register = template.Library()


@register.filter(name='plural_comments')
def plural_comments(comment_number):
    try:
        comment_number = int(comment_number)

        if comment_number == 0:
            return f'No comments'
        elif comment_number == 1:
            return f'{comment_number} comment'
        else:
            return f'{comment_number} comments'
    except:
        return f'{comment_number} comment(s)'
