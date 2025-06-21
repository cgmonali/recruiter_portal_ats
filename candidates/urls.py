from django.urls import path
from .views import CandidateListCreateView, CandidateRetrieveUpdateDestroyView, CandidateSearchView, candidate_search_ui

urlpatterns = [
    path('candidates/', CandidateListCreateView.as_view(), name='candidate-list-create'),
    path('candidates/<int:id>/', CandidateRetrieveUpdateDestroyView.as_view(), 
         name='candidate-retrieve-update-destroy'),
    path('candidates/search/', CandidateSearchView.as_view(), name='candidate-search-api'),
    path('search/', candidate_search_ui, name='candidate-search-ui'),
]