from django.contrib import admin
from .models import (
    Address,
    TopLevel,
    MiddleLevel,
    BottomLevel,
    Crop,
    Farm,
    Prediction,
    Node,
)

admin.site.register(TopLevel)
admin.site.register(MiddleLevel)
admin.site.register(BottomLevel)
admin.site.register(Crop)
admin.site.register(Farm)
admin.site.register(Prediction)
admin.site.register(Node)
