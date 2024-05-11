from django.db import models

class song(models.Model):
  song_name = models.CharField(max_length = 30)
  music_dir = models.CharField(max_length = 30)
  star_ring = models.CharField(max_length = 40)

  def __str__(self):
    return self.song_name.upper() + ',\t' + self.music_dir + ',\t' + self.star_ring 
  