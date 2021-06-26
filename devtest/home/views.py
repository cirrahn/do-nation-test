from django.http import HttpResponse
import pledges.models as pledges_models
from django.template import loader


def index(request):
    cnt_pledges = 0
    total_metric_c20 = 0
    total_metric_water = 0
    total_metric_waste = 0

    for subclass in pledges_models.Pledge.__subclasses__():
        cnt_pledges += subclass.objects.count()
        for pledge in subclass.objects.all():
            total_metric_c20 += pledge.action.get_co2(pledge) or 0
            total_metric_water += pledge.action.get_water(pledge) or 0
            total_metric_waste += pledge.action.get_waste(pledge) or 0

    template = loader.get_template("home/index.html")
    context = {
        "cnt_pledges": cnt_pledges,
        "metric_c20": total_metric_c20,
        "metric_water": total_metric_water,
        "metric_waste": total_metric_waste,
    }
    return HttpResponse(template.render(context, request))
