from django.contrib import admin
from .models import Category, Courses, CategoryFooter, SubCategory, Footer, RatingStar, Rating, VideoCourses


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name'
    )
    class Meta:
        model = Category
admin.site.register(Category, CategoryAdmin)


class CoursesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'category',
        'name',
        'price',
        'image',
        'duration',
        'number_of_students',
        'added_at',
        'updated_at',
        'subCategory'
    )
    class Meta:
        model = Courses
admin.site.register(Courses, CoursesAdmin)



class SubCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
    )
    class Meta:
        model = SubCategory

admin.site.register(SubCategory, SubCategoryAdmin)


class RatingStarAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'value',
        'comment'
    )
    class Meta:
        model = RatingStar
admin.site.register(RatingStar, RatingStarAdmin)


class RatingAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'star',
        'courses'
    )
    class Meta:
        model = Rating

admin.site.register(Rating, RatingAdmin)



class CategoryFooterAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'parent'
    )
    class Meta:
        model = CategoryFooter

admin.site.register(CategoryFooter, CategoryFooterAdmin)


class FooterAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'categoryfooter',
        'title',
        'image',
        'description'
    )
    class Meta:
        model = Footer

admin.site.register(Footer, FooterAdmin)


class VideoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'subcategory',
        'video'
    )

admin.site.register(VideoCourses)