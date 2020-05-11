import six
from django.contrib.auth.tokens import PasswordResetTokenGenerator


class UserTokenGenerator(PasswordResetTokenGenerator):

    def make_activate_token(self, user, timestamp):
        return six.text_type(user.pk) + six.text_type(timestamp) + six.text_type(user.is_active)


user_token_generator = UserTokenGenerator()
