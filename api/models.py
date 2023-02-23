from django.db import models
import qrcode
from io import BytesIO
from PIL import Image
from django.core.files import File
from django.contrib.auth.models import User

# Create your models here.


class Qr(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,related_name='user')
    text=models.CharField(max_length=100)
    qr_code = models.ImageField(upload_to='media', blank=True)


    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(self.user) 
        canvas = Image.new('RGB', (290, 290), 'white')
        canvas.paste(qrcode_img)
        fname = f'qr_code-{self.text}.png'
        buffer = BytesIO()
        canvas.save(buffer,'PNG')
        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.text
