from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=25)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=25)

    def __str__(self):
        return self.email


class Passport(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='passports')
    scan_file = models.FileField(upload_to='D:\\Desktop\\django\\TrawellTask\\filefolder')
    doc_num = models.CharField(max_length=100)
    first_name = models.CharField(max_length=200)
    nationality = models.CharField(max_length=200)
    patronymic = models.CharField(max_length=100)
    birth_date = models.DateField(max_length=100)
    personal_number = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    issue_date = models.DateField(max_length=200)
    expire_date = models.DateField(max_length=200)
    issuing_authority = models.CharField(max_length=200)

    def __str__(self):
        return self.doc_num


