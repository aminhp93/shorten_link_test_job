from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.views import View

from .forms import SubmitUrlForm
from .models import Link

# Create your views here.
class HomeView(View):
	def get(self, request, *args, **kwargs):
		form = SubmitUrlForm()
		template = "links/home.html"
		context = {
			"title": "shortened link",
			"form": form
		}
		return render(request, template, context)

	def post(self, request, *args, **kwargs):
		form = SubmitUrlForm(request.POST)
		template = "links/home.html"
		context = {
			"form": form
		}
		if form.is_valid():
			new_link = form.cleaned_data.get("link_web")
			print("test", new_link)
			print(request.user)
			obj, created = Link.objects.get_or_create(link_web=new_link)
			if not request.user.is_anonymous:
				obj.user = request.user
				obj.save()
			context = {
				"object": obj
			}
			if created:
				template = "links/success.html"
			else:
				template = "links/already-exists.html"
		return render(request, template, context)

class LinkRedirectView(View):
	def get(self, request, shortlink=None, *args, **kwargs):
		qs = Link.objects.filter(shortlink__iexact=shortlink)
		if qs.count() != 1 and not qs.exists():
			raise Http404
		obj = qs.first()
		return HttpResponseRedirect(obj.link_web)