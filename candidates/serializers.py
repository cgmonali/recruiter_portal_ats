from rest_framework import serializers
from .models import Candidate

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        # model to serialize
        model = Candidate
        # fields to include in the serialized output
        fields = ['id', 'name', 'age', 'gender', 'email', 'phone_number']