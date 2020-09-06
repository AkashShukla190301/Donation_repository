from required import views
from django.conf.urls import url

app_name = 'required'
urlpatterns = [
    url(r'^requirement/', views.RequirementView.as_view(), name='require'),
    url(r'^confirm/', views.ConfirmView.as_view(), name='confirm')
]
