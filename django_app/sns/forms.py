from django import forms
from.models import Message,Group,Friend,Good,Talk
from accounts.models import User

#Messageのフォーム
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['owner','group','content']
#Groupのフォーム
class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['owner','title']
#Friendのフォーム
class FriendForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = ['owner','user','group']
#Goodのフォーム
class GoodForm(forms.ModelForm):
    class Meta:
        model = Good
        fields = ['owner','message']
"""
#Photoフォーム
class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['owner','group','image']
"""
#検索フォーム
class SearchForm(forms.Form):
    search = forms.CharField(max_length=100)

#Groupのチェックボッックスフォーム
class GroupCheckForm(forms.Form):
    def __init__(self, user, *args, **kwargs):
        super(GroupCheckForm,self).__init__(*args,**kwargs)
        public = User.objects.filter(username='public').first()
        self.fields['groups'] = forms.MultipleChoiceField(
                choices=[(item.title,item.title) for item in \
                        Group.objects.filter(owner__in=[user,public])],
                widget=forms.CheckboxSelectMultiple(),
                )
        
#Groupの選択メニューフォーム
class GroupSelectForm(forms.Form):
    def __init__(self, user, *args, **kwargs):
        super(GroupSelectForm,self).__init__(*args,**kwargs)
        self.fields['groups'] = forms.ChoiceField(
                choices=[('-','-')] + [(item.title,item.title) \
                         for item in Group.objects.filter(owner=user)],
                )
        
#Friendのチェックボックスフォーム
class FriendsForm(forms.Form):
    def __init__(self, user, friends=[], vals=[], *args, **kwargs):
        super(FriendsForm, self).__init__(*args,**kwargs)
        self.fields['friends'] = forms.MultipleChoiceField(
                choices=[(item.user,item.user) for item in friends],
                widget=forms.CheckboxSelectMultiple(),
                initial = vals
                )
        
#Group作成フォーム
class CreateGroupForm(forms.Form):
    group_name = forms.CharField(max_length=50)
    
#投稿フォーム
class PostForm(forms.Form):
    content = forms.CharField(max_length=500, \
            widget=forms.Textarea)
    image = forms.ImageField(required=False)
    file = forms.FileField(required=False)
    
    def __init__(self, user, *args, **kwargs):
        super(PostForm, self).__init__(*args,**kwargs)
        public = User.objects.filter(username='public').first()
        self.fields['groups'] = forms.ChoiceField(
                choices=[('-','-')] + [(item.title,item.title) \
                         for item in Group.objects. \
                         filter(owner__in=[user,public])],
                )
#トークルームのフォーム
class TalkForm():
    class Meta:
        model = Talk
        fields = ['owner','content']

'''        
#ファイル投稿フォーム
class FileForm(forms.ModelForm):
    file = forms.FileField(label='Select a file.')
 
    class Meta:
        model = File
        fields = ('status','task_name','t_file')
        '''
'''
#Photoフォーム
class PhotoForm(forms.Form):
    image = forms.ImageField()

    def __init__(self, user, *args, **kwargs):
        super(PhotoForm, self).__init__(*args,**kwargs)
        public = User.objects.filter(username='public').first()
        self.fields['groups'] = forms.ChoiceField(
                choices=[('-','-')] + [(item.title,item.title) \
                         for item in Group.objects. \
                         filter(owner__in=[user,public])],
                )    
'''