from .models import Post
from django import forms
class PostForm(forms.ModelForm):

	class Meta:
		model= Post
		fields = ('title','author','body','header_image')

		widgets={
		'title':forms.TextInput(attrs={'class':'form-control'}),
		'author':forms.TextInput(attrs={'class':'form-control','id':'elder','value':'','type':'hidden'}),
		'body':forms.Textarea(attrs={'class':'form-control'}),
		}