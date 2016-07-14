from django.contrib.auth.decorators import user_passes_test, login_required

active_required = user_passes_test(lambda u: u.is_active)

def active_login_required(view_func):
	decorated = login_required(active_required(view_func))
	return decorated
