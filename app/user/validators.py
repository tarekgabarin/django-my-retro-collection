import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


class DigitValidator(object):
    def validate(self, password, user=None):
        if not bool(re.search(r"\d", password)):
            raise ValidationError(
                _("Password must contain at least 1 digit, 0-9"),
                code="password_no_number",
            )

    def get_help_text(self):
        return _("Your password must contain at least 1 digit, 0-9")


class UpperCaseValidator(object):
    def validate(self, password, user=None):
        if not re.findall("[A-Z]", password):
            raise ValidationError(
                _("The password must contain at least 1 uppercase letter, A-Z."),
                code="password_no_upper",
            )

    def get_help_text(self):
        return _("Your password must contain at least 1 uppercase letter, A-Z.")


class LowerCaseValidator(object):
    def validate(self, password, user=None):
        if not re.findall("[a-z]", password):
            raise ValidationError(
                _("The password must contain at least 1 uppercase letter, a-z."),
                code="password_no_upper",
            )

    def get_help_text(self):
        return _("Your password must contain at least 1 uppercase letter, a-z.")


class SpecialCharacterValidator(object):
    def validate(self, password, user=None):
        if not re.findall("[()[\]{}|\\`~!@#$%^&*_\-+=;:'\",<>./?]", password):
            raise ValidationError(
                _(
                    "The password must contain at least 1 symbol: "
                    + "()[]{}|\`~!@#$%^&*_-+=;:'\",<>./?"
                ),
                code="password_no_symnol",
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least 1 symbol: "
            + "()[]{}|\`~!@#$%^&*_-+=;:'\",<>./?"
        )
