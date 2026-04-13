from django.core.management.base import BaseCommand
import datetime
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, workouts, and leaderboard.'

    def handle(self, *args, **options):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()

        # Create test users
        user1 = User.objects.create(username='alice', email='alice@example.com')
        user2 = User.objects.create(username='bob', email='bob@example.com')

        # Create test teams
        team1 = Team.objects.create(name='Team Alpha')
        team1.members.add(user1, user2)

        # Create test activities
        Activity.objects.create(user=user1, type='run', duration=30, date=datetime.date(2024, 1, 1))
        Activity.objects.create(user=user2, type='cycle', duration=45, date=datetime.date(2024, 1, 2))

        # Create test workouts
        workout1 = Workout.objects.create(name='Pushups', description='Do 20 pushups')
        workout1.suggested_for.add(user1)

        # Create test leaderboard
        Leaderboard.objects.create(team=team1, score=100)

        self.stdout.write(self.style.SUCCESS('Test data created successfully.'))
