
from django.urls import path
from account.views import loginView, RegView

urlpatterns = [

    path('log', loginView, name='login'),
    path('reg', RegView.as_view(), name='reg')


]