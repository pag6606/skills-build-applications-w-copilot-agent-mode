from django.core.management.base import BaseCommand
from django.conf import settings
from djongo import models


from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Limpiar colecciones usando pymongo
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']
        db['octofit_tracker_user'].delete_many({})
        db['octofit_tracker_team'].delete_many({})
        db['octofit_tracker_activity'].delete_many({})
        db['octofit_tracker_leaderboard'].delete_many({})
        db['octofit_tracker_workout'].delete_many({})

        # Crear equipos
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Crear usuarios
        ironman = User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel)
        captain = User.objects.create(name='Captain America', email='cap@marvel.com', team=marvel)
        batman = User.objects.create(name='Batman', email='batman@dc.com', team=dc)
        superman = User.objects.create(name='Superman', email='superman@dc.com', team=dc)

        # Crear actividades
        Activity.objects.create(user=ironman, type='Running', duration=30)
        Activity.objects.create(user=batman, type='Cycling', duration=45)

        # Crear leaderboard
        Leaderboard.objects.create(user=ironman, points=100)
        Leaderboard.objects.create(user=batman, points=120)

        # Crear workouts
        Workout.objects.create(name='Full Body', description='Marvel style workout')
        Workout.objects.create(name='Strength', description='DC style workout')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
