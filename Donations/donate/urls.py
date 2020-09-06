from django.conf.urls import url
from donate import views

app_name = 'donate'
urlpatterns = [
    url(r'^thankyou/', views.ThankYouView.as_view(), name="thankyou"),
    url(r'^books/', views.BookDetailView.as_view(), name='book_info'),
    url(r'^details/', views.AddressDetailView.as_view(), name='address_detail'),
    url(r'^about/', views.aboutUsView.as_view(), name='about')
]
