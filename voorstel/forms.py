from django import forms

class AmendementForm(forms.Form):
    title = forms.CharField(max_length=256)
    email = forms.EmailField()



class AmendementCommentForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)




