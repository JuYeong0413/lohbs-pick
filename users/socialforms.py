from allauth.socialaccount.forms import SignupForm
from django import forms

class MyCustomSocialSignupForm(SignupForm):
    nickname = forms.CharField(label='닉네임')

    def save(self, request):
        user = super(MyCustomSocialSignupForm, self).save(request)
        user.profile.nickname = self.cleaned_data['nickname']
        user.save()
        return user