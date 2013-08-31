from django.contrib import admin
from blog.models import Post

class PostAdmin(admin.ModelAdmin):
		list_display=['title','description','slug']
		list_filter=['published','created']
		search_fields=['title','description','content']
		date_hierarchy='created'
		prepopulated_fields={"slug":("title",)}







admin.site.register(Post,PostAdmin)
