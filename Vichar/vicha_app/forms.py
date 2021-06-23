from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

#to create signup form
class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ("username", "email", "password1", "password2")
        model = get_user_model()#allows us to use the model whoever is using it

    def __init__(self, *args, **kwargs):
        #this is just for customisation purpose
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Display name"
        self.fields["email"].label = "Email address"
