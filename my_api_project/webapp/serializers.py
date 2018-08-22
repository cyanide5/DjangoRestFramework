from rest_framework import serializers
from .models import Person


class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = ("firstName", "lastName")


    # Change fields to the below to send all fields
        # fields = "__all__"


