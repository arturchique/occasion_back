import re

from rest_framework import serializers


class UserCreateSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150, required=False)
    password = serializers.CharField(max_length=128, required=True)
    first_name = serializers.CharField(max_length=150, required=False)
    last_name = serializers.CharField(max_length=150, required=False)
    tg_id = serializers.IntegerField(required=False)
    tg_username = serializers.CharField(max_length=32, required=False)

    def validate_password(self, password: str):
        if len(password) < 8:
            raise serializers.ValidationError('Too small password (try with more than 8 characters)')
        if not re.search('[a-z]', password):
            raise serializers.ValidationError('No lowercase characters in password')
        if not re.search('[A-Z]', password):
            raise serializers.ValidationError('At least one uppercase character should be in password')
        if not re.search('[0-9]', password):
            raise serializers.ValidationError('At least one number (0-9) should be in password')
        if not re.search('[_@$!]', password):
            raise serializers.ValidationError(
                'At least one special character ("!", "@", "$", "!") should be in password')
        if re.search('\s', password):
            raise serializers.ValidationError('There should be no spaces in password')

        return password

    def validate(self, data: dict):
        if not any((data.get('username'), data.get('tg_username'))):
            raise serializers.ValidationError(
                'You should provide data with at least on field:\n"username"\n"tg_username"'
            )
        if not data.get('username'):
            data['username'] = data['tg_username']

        return data
