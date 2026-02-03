from django.db import models

class ChatMessage(models.Model):
    user_message = models.TextField()
    ai_message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_message[:50]
