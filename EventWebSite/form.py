from django import forms
from django.contrib.auth.forms import UserCreationForm
from UserManager.models import User

class ParticipantRegForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('fname', 'lname', 'clg', 'stream', 'email',  'contect_no')

    def save(self, commit=True):
        user = super(ParticipantRegForm, self).save(commit=False)
        user.is_participant = True
        if commit:
            user.save()
        return user
