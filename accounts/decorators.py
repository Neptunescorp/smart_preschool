from functools import wraps

from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied


def teacher_required(view_func):

    @wraps(view_func)
    @login_required(login_url="login")
    def wrapper(request, *args, **kwargs):

        if request.user.role not in ["ADMIN", "TEACHER"]:
            raise PermissionDenied

        return view_func(request, *args, **kwargs)

    return wrapper


def parent_required(view_func):

    @wraps(view_func)
    @login_required(login_url="login")
    def wrapper(request, *args, **kwargs):

        if request.user.role != "PARENT":
            raise PermissionDenied

        return view_func(request, *args, **kwargs)

    return wrapper


def admin_required(view_func):

    @wraps(view_func)
    @login_required(login_url="login")
    def wrapper(request, *args, **kwargs):

        if request.user.role != "ADMIN":
            raise PermissionDenied

        return view_func(request, *args, **kwargs)

    return wrapper