from django import forms
from blog.models import BlogPost
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class BlogPostFrom(forms.ModelForm):
    helper = FormHelper()
    helper.form_id = 'blog_post_form'
    helper.form_method = 'POST'
    helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = BlogPost
        fields = ['author', 'title', 'content']
