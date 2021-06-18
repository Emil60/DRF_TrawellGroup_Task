from .serializers import PassportSerializer, CustomerSerializer
from customers.models import Customer, Passport
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404


class CustomerListCreateAPIView(APIView):
    def get(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PassportListCreateAPIView(APIView):
    def get(self, request):
        customers = Passport.objects.all()
        serializer = PassportSerializer(customers, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = PassportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PassportDetailAPIView(APIView):
    def get_object(self, pk):
        passport_instance = get_object_or_404(Passport, pk=pk)
        return passport_instance

    def get(self, request, pk):
        passport = self.get_object(pk=pk)
        serializer = PassportSerializer(passport, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        passport = self.get_object(pk=pk)
        serializer = PassportSerializer(passport, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        passport = self.get_object(pk=pk)
        passport.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CustomerDetailAPIView(APIView):
    def get_object(self, pk):
        customer_instance = get_object_or_404(Customer, pk=pk)
        return customer_instance

    def get(self, request, pk):
        customer = self.get_object(pk=pk)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    def put(self, request, pk):
        customer = self.get_object(pk=pk)
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        customer = self.get_object(pk=pk)
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

