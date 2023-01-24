from django.contrib import admin
from .models import Order, OrderCourses



class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'total_price',
        'order_at',
    )

    class Meta:
        model = Order

admin.site.register(Order, OrderAdmin)

class OrderCoursesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'order',
        'courses',
        'price',
        'quantity'
    )
    class Meta:
        model = OrderCourses

admin.site.register(OrderCourses, OrderCoursesAdmin)
