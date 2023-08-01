from django.forms import ModelForm, Textarea, IntegerField
from .models import Review


class ReviewForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        # set for each form field a class attribute to use a Bootstrap class.
        self.fields['text'].widget.attrs.update({'class': 'form-control'})
        # set for each form field a class attribute to use a Bootstrap class.
        self.fields['stars'].widget.attrs.update({'class': 'form-control'})
        self.fields['recommend'].widget.attrs.update(
            {'class': 'form-check-input'})

    class Meta:
        """
        A class inside a class! 
        Specify which model the form is for and the fields we want in the form.

        More in documentation: 
        https://docs.djangoproject.com/en/4.2/topics/forms/modelforms/
        """
        model = Review
        # the only fields that the user has to fill are these
        fields = ['text', 'stars', 'recommend']
        labels = {
            'recommend': ('Recommend'),
            'stars': ('Stars')
        }
        widgets = {
            'text': Textarea(attrs={'rows': 4}),
            # 'stars': IntegerField(attrs={'rows': 1}),

        }
