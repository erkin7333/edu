from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Kategoriya'
        verbose_name_plural = "Kategoriyalar"


class Courses(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.FloatField()
    image = models.ImageField(upload_to='cours_image/')
    duration = models.FloatField(verbose_name="Kurs Davomiyligi")
    number_of_students = models.IntegerField(verbose_name='Talabalar soni')
    added_at = models.DateTimeField(auto_now_add=True, verbose_name="Dars qo'shilgan vaqti")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Dars yangilangan vaqti")
    subCategory = models.ForeignKey("SubCategory", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Kurs"
        verbose_name_plural = "Kurslar"


class SubCategory(models.Model):
    title = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Kurs mazmuni"
        verbose_name_plural = "Kurslar mazmuni"

class VideoCourses(models.Model):
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, blank=True, null=True)
    video = models.FileField(upload_to='cours_video/')

    def __str__(self):
        return str(self.video)


class RatingStar(models.Model):
    value = models.SmallIntegerField(default=0, max_length=5)
    comment = models.TextField()
    def __str__(self):
        return self.value

    class Meta:
        verbose_name = "Reyting yulduzi"
        verbose_name_plural = "Reytinglar yulduzi"

class Rating(models.Model):

    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE)
    courses = models.ForeignKey(Courses, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Reyting"
        verbose_name_plural = "Reytinglar"




class CategoryFooter(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey("self", on_delete=models.RESTRICT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Kategoriya Futiri'
        verbose_name_plural = 'Kategoriyalar Futiri'

class Footer(models.Model):
    categoryfooter = models.ForeignKey(CategoryFooter, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='footer_image/')
    description = models.TextField()

    def __str__(self):
        return self.title