from rest_framework import viewsets

from api.models import Bot, Scenario, Step
from api.serializers import BotSerializer, ScenarioSerializer, StepSerializer


# Create your views here.

class BotModelViewSet(viewsets.ModelViewSet):
    queryset = Bot.objects.all()
    http_method_names = ['post', 'get']
    serializer_class = BotSerializer


class ScenarioViewSet(viewsets.ModelViewSet):
    queryset = Scenario.objects.all()
    http_method_names = ['post', 'get']
    serializer_class = ScenarioSerializer


class StepViewSet(viewsets.ModelViewSet):
    queryset = Step.objects.all()
    http_method_names = ['post', 'get']
    serializer_class = StepSerializer
