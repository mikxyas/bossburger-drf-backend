from allauth.account.adapter import DefaultAccountAdapter


class CustomAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=False):
        user = super().save_user(request, user, form, commit)
        data = form.cleaned_data
        # user.username = None
        user.name = data.get('name')
        user.username = data.get('username')
        user.phone_number = data.get('phone_number')
        user.save()
        return user