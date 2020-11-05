from django.forms import ModelForm
from .models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('context',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['context'].widget.attrs.update({'class':'textarea-css','placeholder': 'Enter text'})



