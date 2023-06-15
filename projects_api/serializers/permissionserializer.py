from rest_framework import serializers

from projects_api import choicesclass


class PermissionSerializer(serializers.ChoiceField):
    def __init__(self, **kwargs):
        choices = choicesclass.Permission.choices
        super().__init__(choices, **kwargs)

    def to_representation(self, value):
        if value in ("", None):
            return value
        return {
            "name": self.choices[value],
            "level": self.choice_strings_to_values.get(str(value), value),
        }
