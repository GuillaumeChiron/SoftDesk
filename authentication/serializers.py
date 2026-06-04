from rest_framework.serializers import ModelSerializer, ValidationError

from authentication.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "password",
            "age",
            "can_be_contacted",
            "can_data_be_shared",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def validate_age(self, age):
        if age <= 15:
            raise ValidationError("Vous devez avoir plus de 15 ans pour vous inscrire")
        return age

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
