from django.core.exceptions import ValidationError
from django.core.validators import URLValidator

def validate_url(value):
	url_validator = URLValidator()
	reg_val = value
	if "http" in reg_val:
		new_value = reg_val
	else:
		new_value = "http://" + value

	try:
		url_validator(new_value)
	except:
		raise ValidationError("Invalid URL")
	return new_value
