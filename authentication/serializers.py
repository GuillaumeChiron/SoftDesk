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
            "date_joined",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def validate_age(self, age):
        if age <= 15:
            raise ValidationError("Vous devez avoir plus de 15 ans pour vous inscrire")
        return age

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if password:
            instance.set_password(password)

        instance.save()
        return instance
