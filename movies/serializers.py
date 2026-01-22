from rest_framework import serializers
from movies.models import Movie
from django.db.models import Avg


class MovieModelSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)  # campo calculado apenas para leitura (não aparece no cadastro)

    class Meta:
        model = Movie
        fields = '__all__'

    def get_rate(self, obj):  # obj representa cada MOVIE cadastrado
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']

        if rate:
            return rate
        return None

    def validate_release_date(self, value):
        if value.year < 1900:
            raise serializers.ValidarionError("A data de lançamento não deve ser inferior a 1900.")
        return value

    def validate_resume(self, value):
        if len(value) > 500:
            raise serializers.ValidationError("O resumo não deve conter mais do que 100 caracteres.")
        return value
