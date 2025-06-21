from django.db.models import Q
from django.db import models
from rest_framework import generics
from rest_framework.throttling import UserRateThrottle
from .models import Candidate
from .serializers import CandidateSerializer
from django.shortcuts import render
from django.utils.html import escape

# List and create candidates
class CandidateListCreateView(generics.ListCreateAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

# Retrieve, update, or delete a candidate by id
class CandidateRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    import pdb; pdb.set_trace()
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    lookup_field = 'id'
    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        print(response.data)  # Print the response data to the console
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        print(response.data)  # Print the response data to the console
        return response

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        print(response.status_code)  # Print the response status code to the console
        return response

# Search candidates by name, ranking results by number of matched words
class CandidateSearchView(generics.ListAPIView):
    throttle_classes = [UserRateThrottle]
    serializer_class = CandidateSerializer

    def get_queryset(self):
        raw_query = self.request.GET.get('q', '')
        search_query = escape(raw_query).strip()  
        if not search_query:
            return []  # Return empty if no query
        
        search_words = search_query.split()  # Split query into words
        queryset = Candidate.objects.all()
        
        # Build a Q object to OR together all word matches
        q_objects = Q()
        for word in search_words:
            q_objects |= Q(name__icontains=word)
        
        queryset = queryset.filter(q_objects)  # Filter candidates matching any word
        
        # Annotate each candidate with a match count for each word
        for word in search_words:
            queryset = queryset.annotate(
                **{f'match_{word}': models.Case(
                    models.When(name__icontains=word, then=1),
                    default=0,
                    output_field=models.IntegerField()
                )}
            )
        
        # Sum up all match counts to get total matches
        match_fields = [f'match_{word}' for word in search_words]
        queryset = queryset.annotate(
            total_matches=models.ExpressionWrapper(
                sum(models.F(field) for field in match_fields),
                output_field=models.IntegerField()
            )
        )
        
        # Order by total matches descending, then by name
        return queryset.order_by('-total_matches', 'name')

# UI view for candidate search
def candidate_search_ui(request):
    query = request.GET.get('q', '').strip()
    candidates = []
    if query:
        # Reuse the same search logic as the API view
        search_view = CandidateSearchView()
        search_view.request = request
        candidates = search_view.get_queryset()
    return render(request, 'candidates/search.html', {'candidates': candidates, 'query': query})