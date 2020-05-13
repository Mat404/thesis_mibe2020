from django.http import HttpResponse
from django.shortcuts import redirect, render
from functools import wraps
# def allowed_user(allowed_roles=[]):
#     def decorator(view_func):
#         def wrapper_func(request, *args, **kwargs):
#
#             group = None
#             if request.user.groups.exists():
#                 group = request.user.groups.all()
#
#             if group in allowed_roles:
#                 return view_func(request, *args, **kwargs)
#
#             else:
#                 return HttpResponse(' You are not Authorized!')
#         return wrapper_func
#     return decorator



def allowed_user(allowed_roles=()):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper_func(request, *args, **kwargs):
            if request.user.groups.filter(name__in=allowed_roles).exists():
                return view_func(request, *args, **kwargs)
            else:

                 return render(request, 'core/render_staff.html' )

        return wrapper_func
    return decorator
