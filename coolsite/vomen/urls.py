from django.urls import path

from django.urls import path

from vomen.views import *

urlpatterns = [
    path('', index),
    path('cat/', categories),
    path('mario/', moon, ),
    path('cot/', moon1),
    path('cod/', moon2),

]
handler404 = pageNotFound
handler500 = InternalServerError
handler403 = Forbidden
handler400 = BadRequest
