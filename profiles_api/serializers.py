from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Een serializer vertaalt complexe Python-objecten (zoals modellen) naar JSON (en andersom).
    Dit is belangrijk voor API’s, want browsers of frontend apps begrijpen alleen JSON of andere standaardformaten."""
    name = serializers.CharField(max_length=10)
    
