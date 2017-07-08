import random
import string

from django.conf import settings

SIZE_CODE = getattr(settings, "SIZE_CODE", 6)
def link_generator(size=SIZE_CODE, chars=string.ascii_lowercase + string.digits):
	return "".join(random.choice(chars) for _ in range(size))

def create_shortlink(instance, size=SIZE_CODE):
	new_link = link_generator(size=size)
	Klass = instance.__class__
	qs_exists = Klass.objects.filter(shortlink=new_link).exists()
	if qs_exists:
		return create_shortlink(instance, size=size)
	return new_link