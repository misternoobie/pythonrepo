from django.contrib import admin

# Register your models here.
from .models import friend

class FriendModelAdmin(admin.ModelAdmin):
	list_display = ['slug','id', 'Image', 'Name', 'Birthday', 'Address']
	list_editable = ['Name', 'Birthday']
	search_fields = ['Name', 'Birthday']
	class Meta:
		model = friend

admin.site.register(friend, FriendModelAdmin)