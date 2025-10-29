from django.db import models

# Create your models here.


class Bot(models.Model):
    BOT_TYPES = [
        ('text', 'Text Generation'),
        ('chat', 'Chat Bot'),
        ('custom', 'Custom Scenario'),
    ]

    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('active', 'Active'),
        ('paused', 'Paused'),
        ('archived', 'Archived'),
    ]

    name = models.CharField(max_length=64)
    description = models.CharField(blank=True)
    bot_type = models.CharField(max_length=20, choices=BOT_TYPES, default='chat')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')


    def __str__(self):
        return self.name

class Scenario(models.Model):
    SCENARIO_TYPES = [
        ('linear', 'Linear Flow'),
        ('branching', 'Branching Flow'),
        ('mixed', 'Mixed Flow'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    scenario_type = models.CharField(max_length=20, choices=SCENARIO_TYPES, default='linear')
    bot = models.ForeignKey(Bot, on_delete=models.CASCADE, related_name='scenarios')

    def __str__(self):
        return self.name


class Step(models.Model):
    STEP_TYPES = [
        ('message', 'Send Message'),
        ('question', 'Ask Question'),
        ('input', 'Get User Input'),
        ('condition', 'Condition Check'),
        ('api_call', 'API Call'),
        ('gpt_call', 'GPT Call'),
    ]

    scenario = models.ForeignKey(Scenario, on_delete=models.CASCADE, related_name='steps')
    name = models.CharField(max_length=255)
    step_type = models.CharField(max_length=20, choices=STEP_TYPES)