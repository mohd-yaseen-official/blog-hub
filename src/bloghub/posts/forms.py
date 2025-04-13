from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    tags = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}), label='Tags (Comma seperated)')
    # creates a charField | label refers to the .label we use template
    class Meta:
        model = Post
        exclude = [
            'author',
            'categories',
            'published_date',
            'is_deleted',
        ]
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'input'
            }),
            'short_description': forms.Textarea(attrs={
                'class': 'input'
            }),
            'time_duration': forms.TextInput(attrs={
                'class': 'input',
            })
        }

        error_messages = {
            "title" : {
                "invalid": "Please enter a valid Title",
                "required": "Title field is required"
            },
            "short_description" : {
                "invalid": "Please enter a valid Short Descripton",
                "required": "Short Description field is required"
            },
            "description" : {
                "invalid": "Please enter a valid Description",
                "required": "Description field is required"
            },
            "featured_image" : {
                "invalid": "Please enter valid Tags",
                "required": "Tags field is required"
            },
            "time_duration" : {
                "invalid": "Please enter a valid Time Duration",
                "required": "Time Duration field is required"
            },
        }