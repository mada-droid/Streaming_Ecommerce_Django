from django import forms
from django.contrib.auth.forms import UserCreationForm

from blog.models import BlogPost
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


# def form_validation_error(form):
#     msg = ""
#     for field in form:
#         for error in field.errors:
#             msg += "%s: %s \\n " % (field.label if hasattr(field, 'label') else 'Error', error)
#     return msg


class BlogPostForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_id = 'blog_post_form'
    helper.form_method = 'POST'
    helper.add_input(Submit('submit', 'Submit', css_class="btn btn-success"))
    helper.inputs[0].field_classes = 'btn btn-primary'

    class Meta:
        model = BlogPost
        fields = ['author', 'title', 'content']


# class AuthorProfileForm(forms.ModelForm):
#     helper = FormHelper()
#     helper.form_id = 'blog_post_crispy_form'
#     helper.form_method = 'POST'
#     helper.add_input(Submit('save', 'Save'))
#     helper.inputs[0].field_classes = 'btn btn-success'
#
#     class Meta:
#         model = AuthorProfile
#         fields = ['first_name', 'last_name', 'email', 'short_bio']
