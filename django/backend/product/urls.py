from .views import CategoryList,ProductView, CategoryDetail,ShoeView

from django.urls import path ,include

 
urlpatterns = [
    path('category/',CategoryList.as_view()),
    path('category/<str:slug>', CategoryDetail.as_view({'get': 'list'}),name='category_detail'),
    # path('product/<int:pk>',ProductView.as_view()),
    path('product/',ProductView.as_view()),
    path('shoe/',ShoeView.as_view())
]