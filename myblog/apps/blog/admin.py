from django.contrib import admin
from wagtail.contrib.modeladmin.options import ModelAdminGroup, ModelAdmin, modeladmin_register

from blog.models import BlogCategory, BlogPost


@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "thumbnail", "created", "modified",)
    ordering = ("name",)


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "category", "is_published", "created", "modified",)
    list_filter = ("category", "created", "modified",)
    ordering = ("-modified",)


class CategoryAdmin(ModelAdmin):
    model = BlogCategory
    menu_label = "Category"
    menu_icon = "tag"
    menu_order = 290
    add_to_settings_menu = False
    exclude_from_explorer = False

    list_display = ("name", "slug", "thumbnail", "created", "modified",)
    ordering = ("name",)


class BlogAdmin(ModelAdmin):
    model = BlogPost
    menu_label = "List Blogs"
    menu_icon = "group"
    menu_order = 290
    add_to_settings_menu = False
    exclude_from_explorer = False

    list_display = ("title", "slug", "category", "image", "thumbnail", "content", "is_published",
                    "meta_keyword", "meta_description", "created", "modified",)
    list_filter = ("category", "created", "modified",)
    ordering = ("-modified",)


class BlogGroup(ModelAdminGroup):
    menu_label = "Blog"
    menu_icon = "list-ul"
    items = (CategoryAdmin, BlogAdmin)


modeladmin_register(BlogGroup)
