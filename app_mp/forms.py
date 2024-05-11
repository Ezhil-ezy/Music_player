from django import forms
from .models import song


class MemberForm(forms.ModelForm):
  class Meta:
    model = song
    fields = ['song_name', 'music_dir']
