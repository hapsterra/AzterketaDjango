from django.urls import path
from . import views

urlpatterns = [
    path('pertsonak/', views.pertsonakIkusi, name='pertsonakIkusi'),
    path('', views.alokairuakIkusi, name='alokairuakIkusi'),
    path('deleteAlokairu/<int:id>', views.deleteAlokairu, name='deleteAlokairu'),
    path('kotxeak/', views.kotxeakIkusi, name='kotxeakIkusi'),
    path('alokairuaSartu/', views.addAlokairua, name='alokairuaSartu'),
    path('pertsonak/delete/<int:id>', views.deletePertsona, name='delete'),
    path('kotxeak/deleteK/<int:id>', views.deleteKotxea, name='deleteKotxea'),
    path('pertsonak/pertsonaSartu/', views.addPertsona, name='pertsonaSartu'),
    path('kotxeak/kotxeakSartu/', views.addKotxea, name='kotxeaSartu'),
    path('pertsonak/pertsonaSartu/addrecordPertsona/', views.addrecordPertsona, name='addrecordPertsona'),
    path('kotxeak/kotxeakSartu/addrecordKotxea/', views.addrecordKotxea, name='addrecordKotxea'),
    path('alokairuaSartu/addrecordAlokairua/', views.addrecordAlokairua, name='addrecordAlokairua'),
]
