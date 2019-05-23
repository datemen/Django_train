from django.db import models
from accounts.models import User

#Messageクラス
class Message(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, \
            related_name='message_owner')
    image = models.ImageField(upload_to='django_app')
    file = models.FileField(upload_to='django_app')
    group = models.ForeignKey('Group', on_delete=models.CASCADE)
    content = models.TextField(max_length=1000)
    share_id = models.IntegerField(default=-1)
    good_count = models.IntegerField(default=0)
    share_count = models.IntegerField(default=0)
    pub_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.content) + ' (' + str(self.owner) + ')'
        
    def get_share(self):
        return Message.objects.get(id=self.share_id)
    
    class Meta:
        ordering = ('-pub_date',)
        
#Groupクラス
class Group(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, \
            related_name = 'group_owner')
    title = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.title
    
#Friendクラス
class Friend(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, \
            related_name = 'friend_owner')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.user) + ' (group:"' + str(self.group) + '")'
    
#GOODクラス
class Good(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, \
            related_name='good_owner')
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    
    def __str__(self):
        return 'good for "' + str(self.message) + '" (by ' + \
                str(self.owner) + ')'
        
class Talk(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, \
            related_name='talk_owner')
    opponent = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=1000)
    pub_date = models.DateTimeField(auto_now_add=True)

'''
#FILEクラス
class File(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, \
            related_name='file_owner')
    file_name = models.CharField(max_length=50)
    file = models.FileField(upload_to='documents/%Y/%m/%d')
 
    def __str__(self):
 
        return str(self.file_name)
'''
'''
#Photoクラス
class Image(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, \
            related_name = 'photo_owner')
    image = models.ImageField(upload_to='django_app')
    group = models.ForeignKey('Group', on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.owner)
        
    class Meta:
        ordering = ('-pub_date',)
'''       