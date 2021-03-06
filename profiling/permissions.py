from rest_framework.permissions import BasePermission, SAFE_METHODS


class profileViewPermission(BasePermission):
    def has_object_permission(self,request,view,obj):
        if request.method in SAFE_METHODS:
            return True
        else:
            return obj.id==request.user.id

class itemPermission(BasePermission):
    def has_object_permission(self,request,view,obj):
        if request.method in SAFE_METHODS:
            return True
        else:
            return obj.user.id==request.user.id
