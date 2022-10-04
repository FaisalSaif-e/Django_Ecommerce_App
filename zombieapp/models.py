from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator

STATE_CHOICES=(
('Arunachal Pradesh','Arunachal Pradesh'),	
('Andhra Pradesh','Andhra Pradesh'),	
('Assam','Assam'),	
('Bihar','Bihar'),	
('Chhattisgarh','Chhattisgarh'),		
('Goa','Goa'),	
('Gujarat','Gujarat'),	
('Haryana','Haryana'),	
('Himachal Pradesh','Himachal Pradesh'),	
('Jharkhand','Jharkhand'),	
('Karnataka','Karnataka'),	
('Kerala','Kerala'),	
('Madhya Pradesh','Madhya Pradesh'),	
('Maharashtra','Maharashtra'),
('Manipur','Manipur'),	
('Meghalaya','Meghalaya'),	
('Mizoram','Mizoram'),	
('Nagaland','Nagaland'),	
('Odisha','Odisha'),	
('Punjab','Punjab'),	
('Rajasthan','Rajasthan'),	
('Sikkim','Sikkim'),
('Tamil Nadu','Tamil Nadu'),	
('Telangana','Telangana'),	
('Uttar Pradesh','Uttar Pradesh'),	
('Uttarakhand','Uttarakhand'),	
('West Bengal','West Bengal'),	
('Andaman and Nicobar Islands','Andaman and Nicobar Islands'),	
('Daman & Diu','Daman & Diu'),	
('New Delhi','New Delhi'),
('Jammu and Kashmir','Jammu and Kashmir'),	
('Lakshadweep','Lakshadweep'),	
('Puducherry','Puducherry'),	
('Ladakh','Ladakh'), 

)

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    locality = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zipcode =models.IntegerField()
    state =models.CharField(choices=STATE_CHOICES,max_length=50)

    def __str__(self):
        return str(self.id)


CATEGORY_CHOICES=(
    ('M','MOBILE'),
    ('L','LAPTOP'),
    ('TW','TOP_WEAR'),
    ('BW','BOTTOM_WEAR'),
)

class Product(models.Model):
    title = models.CharField(max_length=200)
    selling_price = models.FloatField()
    discount_price = models.FloatField()
    discription = models.TextField()
    brand = models.CharField(max_length=200)
    category = models.CharField(choices=CATEGORY_CHOICES,max_length=10)
    product_image=models.ImageField(upload_to='productimage')

    def __str__(self):
        return str(self.id)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

STATUS_CHOICES=(
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On The Way','On The Way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel'),
)

class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')