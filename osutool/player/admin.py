from django.contrib import admin
from .models import Score, Player, Suggested, Insights

# Register your models here.
admin.site.register(Player)
admin.site.register(Score)
admin.site.register(Suggested)
admin.site.register(Insights)