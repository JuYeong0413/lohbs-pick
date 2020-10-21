from allauth.account.forms import SignupForm
from allauth.socialaccount.forms import SignupForm
from django import forms

    
class MyCustomSignupForm(SignupForm):
    nickname = forms.CharField(label='닉네임')

    def save(self, request):
        user = super(MyCustomSignupForm, self).save(request)
        user.profile.nickname = self.cleaned_data['nickname']
        user.save()
        return user
    

class MyCustomSocialSignupForm(SignupForm):
    nickname = forms.CharField(label='닉네임')
    
    def save(self, request):
        user = super(MyCustomSocialSignupForm, self).save(request)
        user.profile.nickname.add(self.cleaned_data['nickname'])
        user.save()
        return user
    