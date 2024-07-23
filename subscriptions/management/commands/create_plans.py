# subs_billing/management/commands/create_plans.py
from django.core.management.base import BaseCommand
from subscriptions.models import Plan

class Command(BaseCommand):
    help = 'Create initial subscription plans'

    def handle(self, *args, **kwargs):
        plans = [
            {
                "name": "Basic",
                "daily_plan": 10.00,
                "daily_stripe_plan_id": "price_1234",
                "threeday_plan": 100.00,
                "threeday_stripe_plan_id": "price_5678"
            },
            {
                "name": "Premium",
                "daily_plan": 20.00,
                "daily_stripe_plan_id": "price_9101",
                "threeday_plan": 200.00,
                "threeday_stripe_plan_id": "price_1121"
            },
            {
                "name": "Enterprise",
                "daily_plan": 30.00,
                "daily_stripe_plan_id": "price_3141",
                "threeday_plan": 300.00,
                "threeday_stripe_plan_id": "price_5161"
            }
        ]

        for plan_data in plans:
            plan, created = Plan.objects.get_or_create(**plan_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created plan: {plan.name}'))
            else:
                self.stdout.write(f'Plan already exists: {plan.name}')
