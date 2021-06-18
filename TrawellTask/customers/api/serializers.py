from rest_framework import serializers
from customers.models import Customer, Passport


class PassportSerializer(serializers.ModelSerializer):
    # customer = CustomerSerializer()

    class Meta:
        model = Passport
        fields = '__all__'
        # read_only_fields = ['id', 'customer']


class PassportAndCustomerSerializer(serializers.ModelSerializer):
    # customer = CustomerSerializer()

    class Meta:
        model = Passport
        fields = '__all__'
        read_only_fields = ['id', 'customer']


class CustomerSerializer(serializers.ModelSerializer):
    passports = PassportAndCustomerSerializer(many=True)
    # passports = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='passport_actions',
    # )

    class Meta:
        model = Customer
        fields = ['id', 'name', 'surname', 'email', 'phone', 'passports']

    def create(self, validated_data):
        specs = validated_data.pop('passports')
        instance = Customer.objects.create(**validated_data)

        for spec in specs:
            Passport.objects.create(customer=instance, **spec)

        return instance
