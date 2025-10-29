from rest_framework import serializers
from api.models import Bot, Scenario, Step


class BotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bot
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at')

class ScenarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scenario
        fields = '__all__'
        read_only_fields = ('id',)

class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = '__all__'
        read_only_fields = ('id',)