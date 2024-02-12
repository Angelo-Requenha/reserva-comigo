from django.conf import settings
from django.shortcuts import redirect
from urllib.parse import urlencode
import requests
import json
import datetime
from django.http import JsonResponse



def FormErrors(*args):
	'''
	Handles form error that are passed back to AJAX calls
	'''
	message = ""
	for f in args:
		if f.errors:
			message = f.errors.as_text()
	return message




def RedirectParams(**kwargs):
	'''
	Used to append url parameters when redirecting users
	'''
	url = kwargs.get("url")
	params = kwargs.get("params")
	response = redirect(url)
	if params:
		query_string = urlencode(params)
		response['Location'] += '?' + query_string
	return response


class AjaxFormMixin(object):

	'''
	Mixin to ajaxify django form - can be over written in view by calling form_valid method
	'''

	def form_invalid(self, form):
		response = super(AjaxFormMixin, self).form_invalid(form)
		if self.request.is_ajax():
			message = FormErrors(form)
			return JsonResponse({'result':'Error', 'message': message})
		return response

	def form_valid(self, form):
		response = super(AjaxFormMixin, self).form_valid(form)
		if self.request.is_ajax():
			form.save()
			return JsonResponse({'result':'Success', 'message': ""})
		return response



