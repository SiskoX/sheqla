# from .account_type import ACCOUNT_TYPE
# from rest_framework.permissions import BasePermission
# from .models import Account

# # ACCOUNT_TYPE = (
# #     (1,'ADMIN'),
# #     (2,'STUFF'),
# #     (3,'SELLER'),
# #     (4,'USER')


# # )

# class IsAuth(BasePermission):
#    pass


# class IsSeller(BasePermission):
#     def has_perm(self,request,view):
#         return bool (request.user and request.user.profile.account_type == 1)

# class IsAdmin(BasePermission):
#     def has_perm(self,request,view):
#         return bool (request.user and request.user.profile.account_type == 3)
    
    