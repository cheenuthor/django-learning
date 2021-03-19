from book_outlet.models import Book
from django.contrib import admin

# Register your models here.


class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ("slug",)
    prepopulated_fields = {"slug": ("title",)}
    list_filter =("author","rating")
    list_display = ("title","author","rating")


admin.site.register(Book, BookAdmin)
