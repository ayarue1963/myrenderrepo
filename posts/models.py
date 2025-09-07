from django.db import models
from django.contrib.auth import get_user_model
import os
from django.core.exceptions import ValidationError

User = get_user_model()

class Post(models.Model):
    def validate_file_size(value):
        
        """
        Validate uploaded file size based on file type:
        - Images: max 5MB
        - PDFs: max 20MB
        """
        filesize = value.size
        ext = os.path.splitext(value.name)[1].lower()

        if ext in [".jpg", ".jpeg", ".png", ".gif"]:
           limit = 0.030 * 1024 * 1024  # 30 KB
           if filesize > limit:
              raise ValidationError(f"Image file too large. Max size is {limit / (1024*1024)} MB.")

        elif ext == ".pdf":
             limit = 0.40 * 1024 * 1024  # 400 KB
             if filesize > limit:
                raise ValidationError(f"PDF file too large. Max size is {limit / (1024*1024)} MB.")

        else:
            raise ValidationError("Unsupported file type. Only images and PDFs are allowed.")
    # Fields:    
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='post_images/', blank=True, null=True, validators=[validate_file_size])
    pdf = models.FileField(upload_to='post_pdfs/', blank=True, null=True, validators=[validate_file_size])
    is_published = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    score = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
