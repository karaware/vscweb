from django.db import models

class ResultModel(models.Model):
    videoId = models.TextField(max_length=255)
    videoTitle = models.TextField(max_length=255)
    startTime = models.TextField(max_length=255)
    endTime = models.TextField(max_length=255)
    likeCount = models.IntegerField()
    maxViewers = models.IntegerField()
    videoUrl = models.TextField(max_length=255)
    s3ThumbnailUrl = models.TextField(max_length=255)
    s3GraphUrl = models.TextField(max_length=255)
    def __str__(self):
        return self.title

