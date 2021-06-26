from django.http import HttpResponse, Http404
from django.contrib.auth.models import User
import pledges.models as pledges_models
from django.template import loader


def detail(request, user_id: int = None):
    user = request.user

    if user_id is not None:
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            raise Http404(f"User {user_id} not found!")

    if user.is_anonymous:
        raise Http404("No user specified!")

    user_pledges = []
    for subclass in pledges_models.Pledge.__subclasses__():
        user_pledges += subclass.objects.filter(user=user).all()

    template = loader.get_template("users/detail.html")
    context = {
        "user": user,
        "pledges": user_pledges,
    }
    return HttpResponse(template.render(context, request))
