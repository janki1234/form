from django import template

register=template.Library()

@register.filter(name='cut')
def cut (value,arg):
	"""
	This cuts all values of arg from strings
	"""
	return value.replace(arg,'')

