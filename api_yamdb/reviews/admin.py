from django.contrib import admin

from reviews.models import Comment, Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    # list_display = ()
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    # list_display = ()
    pass
