## making form for comment
## using django form
from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    ## it will directly create from from the model
    ## overriding the base function to add style to our comment
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs = {'class': 'form-control',}
        self.fields['email'].widget.attrs = {'class': 'form-control',}
        self.fields['body'].widget.attrs = {'class': 'form-control',}

    class Meta:
        model = Comment

        ## we need these three field for the comment
        fields = ('name','email','body')
