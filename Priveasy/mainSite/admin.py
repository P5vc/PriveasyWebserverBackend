from django.contrib import admin
from django.contrib.auth.models import User , Group



class CustomAdminSite(admin.AdminSite):
	site_header = 'Priveasy Database Management'
	site_title = 'Priveasy DB'
	index_title = 'Database Contents'



# Use custom, admin site:
customAdminSite = CustomAdminSite(name = 'customAdminSite')
from django.contrib.auth.admin import UserAdmin , GroupAdmin


# Add user administration:
@admin.register(User , site = customAdminSite)
class CustomUserAdmin(UserAdmin):
    pass



# Add group administration:
@admin.register(Group , site = customAdminSite)
class CustomGroupAdmin(GroupAdmin):
    pass
