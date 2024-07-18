from django.contrib import admin
from .models import  Group
from .models import  ObjectInformatization
from .models import  Organization
from .models import  InformationSystem
from .models import  Place
from .models import  CheckList
from .models import  Project
from .models import  UserGroup

admin.site.register(Group)
admin.site.register(ObjectInformatization)
admin.site.register(Organization)
admin.site.register(InformationSystem)
admin.site.register(Place)
admin.site.register(CheckList)
admin.site.register(UserGroup)
admin.site.register(Project)
