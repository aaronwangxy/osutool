from django.db import models

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=255)
    player_id = models.IntegerField()

    def __str__(self):
        return self.name

class Score(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    beatmap_link = models.CharField(max_length=255)
    pp = models.FloatField()
    accuracy = models.FloatField()
    mods = models.CharField(max_length=255)
    rank = models.CharField(max_length=255)
    star_rating = models.FloatField()
    length = models.FloatField()

    def __str__(self):
        return self.player.name + ": " + self.title

    class Meta:
        verbose_name_plural = 'Scores'

class Suggested(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    beatmap_link = models.CharField(max_length=255)
    pp = models.FloatField()
    accuracy = models.FloatField()
    mods = models.CharField(max_length=255)
    rank = models.CharField(max_length=255)
    star_rating = models.FloatField()
    length = models.FloatField()

    def __str__(self):
        return self.player.name + ": " + self.title
    
    class Meta:
        verbose_name_plural = 'Suggested'

class Insights(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    avg_accuracy = models.FloatField()
    avg_map_length = models.FloatField()
    fav_mod = models.CharField(max_length=255)
    farmable_pp = models.FloatField()

    def __str__(self):
        return self.player.name + ": " + "Insights"
    
    class Meta:
        verbose_name_plural = 'Insights'