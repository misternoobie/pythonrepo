from django import forms
from .models import friend

class PostForm(forms.ModelForm):
		class Meta:
			model = friend
			fields = ["slug","Name", "Address", "Birthday", "Image"]