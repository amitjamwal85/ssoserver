from django.db import models


def directory_path(self, filename):
    return "files/{}".format(
       filename.replace(" ", "_")
    )


class Blogs(models.Model):
    title = models.CharField(max_length=50, null=False)
    desc = models.EmailField(max_length=200, null=False)


class Photo(models.Model):
    blogs = models.ForeignKey(Blogs, related_name='blogs_img', on_delete=models.DO_NOTHING)
    image = models.ImageField(upload_to=directory_path)
