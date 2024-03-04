from django.urls import path
from .views import ledgerDetailView, ledgerListView #might need to change import of recipe1 etc

urlpatterns = [
	path('recipes/list/', ledgerListView.as_view(),name='recipeslist'),
	path('recipe/<int:pk>/detail', ledgerDetailView.as_view(), name='recipe'),
]

app_name = 'ledger'