from rest_framework import serializers

from zebrands.logs.models import Log


class PostLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = "__all__"


class GetLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = "__all__"
        depth = 1
