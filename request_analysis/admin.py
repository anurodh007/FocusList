import json
from django.contrib import admin
from django.db.models import F
from django.core.serializers.json import DjangoJSONEncoder 
from .models import Newstats


@admin.register(Newstats)
class NewstatsAdmin(admin.ModelAdmin):
    def changelist_view(self, request, extra_context=None):
        chart_data = Newstats.objects.values(
            Windows=F('win'),
            Mac=F('mac'),
            iPhone=F('iphone'),
            Android=F('android'),
            Others=F('others')
        ).first()

        as_json = json.dumps(chart_data, cls=DjangoJSONEncoder)
        extra_context = extra_context or {'chart_data': as_json}
        return super().changelist_view(request, extra_context=extra_context)