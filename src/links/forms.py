from django import forms

from .validators import validate_url

class SubmitUrlForm(forms.Form):
	link_web = forms.CharField(
			label='',
			validators=[validate_url],
			widget=forms.TextInput(
					attrs = {
						"placeholder": "Long URL",
						"class": "form-control"
					}
				)
		)