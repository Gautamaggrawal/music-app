from django.db import models

# Create your models here.
class Music(models.Model):
	name=models.CharField(max_length=100)
	rank=models.IntegerField()
	artists=models.CharField(max_length=100)
	danceability=models.FloatField()
	energy=models.FloatField()
	key=models.IntegerField()
	loudness=models.FloatField()
	mode=models.IntegerField()
	speechiness=models.FloatField()
	acousticness=models.FloatField()
	instrumentalness=models.FloatField()
	liveness=models.FloatField()
	valence=models.FloatField()
	tempo=models.FloatField()
	duration_ms=models.IntegerField()
	time_signature=models.IntegerField()

	def __str__(self):
		return self.name



# p=Music(name=row['name'],rank=row['rank'],artists=row['artists'],danceability=row['danceability'],energy=row['energy'],key=row['key'],loudness=row['loudness'],mode=row['mode'],speechiness=row['speechiness'],acousticness=row['acousticness'],instrumentalness=row['instrumentalness'],liveness=row['liveness'],valence=row['valence'],tempo=row['tempo'],duration_ms=row['duration_ms'],time_signature=row['time_signature'])
# Music(name="row['name']",rank=65,artists="row['artists']",danceability=55,energy=55,key=558,loudness=66,mode=99,speechiness=77,acousticness=11,instrumentalness=0156,liveness=77,valence=44,tempo=16,duration_ms=4,time_signature=77)






