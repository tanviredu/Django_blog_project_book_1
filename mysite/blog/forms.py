## making form for comment
## using django form
from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    ## it will directly create from from the model

    class Meta:
        model = Comment

        ## we need these three field for the comment
        fields = ('name','email','body')
