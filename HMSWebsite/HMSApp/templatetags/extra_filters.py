from django import template
register = template.Library()

@register.filter(name='addcss')
def addcss(field, css):
	if 'readonly' in css:
		return field.as_widget(attrs={"class":css, 'readonly':'readonly'})
	return field.as_widget(attrs={"class":css,})