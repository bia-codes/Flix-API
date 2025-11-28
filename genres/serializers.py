from rest_framework import serializers
from genres.models import Genre

# basicamente, os SERIALIZERS pegam um obejto python (meus dados do models) e transformam em um formato JSON (facilmente lido na internet)
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'