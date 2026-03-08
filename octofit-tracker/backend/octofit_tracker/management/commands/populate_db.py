from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(id=1, name='marvel', members=['Iron Man', 'Captain America', 'Thor'])
        dc = Team.objects.create(id=2, name='dc', members=['Superman', 'Batman', 'Wonder Woman'])

        # Create users
        User.objects.create(id=1, email='ironman@marvel.com', name='Iron Man', team='marvel')
        User.objects.create(id=2, email='cap@marvel.com', name='Captain America', team='marvel')
        User.objects.create(id=3, email='thor@marvel.com', name='Thor', team='marvel')
        User.objects.create(id=4, email='superman@dc.com', name='Superman', team='dc')
        User.objects.create(id=5, email='batman@dc.com', name='Batman', team='dc')
        User.objects.create(id=6, email='wonderwoman@dc.com', name='Wonder Woman', team='dc')

        # Create activities
        Activity.objects.create(id=1, user='Iron Man', type='run', duration=30, date='2026-03-08')
        Activity.objects.create(id=2, user='Batman', type='cycle', duration=45, date='2026-03-08')

        # Create leaderboard
        Leaderboard.objects.create(id=1, team='marvel', points=150)
        Leaderboard.objects.create(id=2, team='dc', points=120)

        # Create workouts
        Workout.objects.create(id=1, name='Pushups', description='Do 20 pushups', suggested_for='marvel')
        Workout.objects.create(id=2, name='Situps', description='Do 30 situps', suggested_for='dc')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
