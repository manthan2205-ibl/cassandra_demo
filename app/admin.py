from django.contrib import admin
from . models import *

# Register your models here.

admin.site.register(UserTokenModel)
admin.site.register(UserModel)
admin.site.register(MessageModel)
admin.site.register(BadgeModel)
admin.site.register(GroupModel)
admin.site.register(TeamModel)
admin.site.register(ExampleModel)