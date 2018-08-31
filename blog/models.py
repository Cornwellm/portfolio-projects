from django.db import models


class Blog(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=255)
    body = models.TextField()
    #pub_date = models.DateTimeField
    pub_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title

        def summary(self):
            return self.body[:100]


            def pub_date_pretty(self):
                return self.pub_date.strftime('%b %d %Y')
