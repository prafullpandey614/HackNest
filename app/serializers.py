from rest_framework.serializers import ModelSerializer

from app.models import Hackathons

class HackathonSerializer(ModelSerializer):
    class Meta:
        model = Hackathons
        fields = "__all__"