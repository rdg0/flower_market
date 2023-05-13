from django.contrib import admin

from .models import (
    Deal,
    DealItem,
    Lot,
    ReviewLot,
    ReviewSeller,
    User,
)


admin.site.register(User)
admin.site.register(Lot)
admin.site.register(ReviewLot)
admin.site.register(ReviewSeller)
admin.site.register(Deal)
admin.site.register(DealItem)
