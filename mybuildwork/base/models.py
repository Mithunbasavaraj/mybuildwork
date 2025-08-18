import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.contrib.auth.models import User

from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile


designation_choice = (
   ("Engineer", "Engineer"),
   ("Department Engineer", "Department Engineer"),
   ("Supervisor", "Supervisor"),
   ("Site Supervisor", "Site Supervisor"),
   ("Site Worker Writer", "Site Worker Writer"),
   ("Mestri", "Mestri"),
   ("Worker", "Worker"),
   ("Supplier", "Supplier"),
   ("Founder", "Founder"),
   ("Owner", "Owner"),
   ("Chairman", "Chairman"),
   ("CEO", "CEO"),
   ("Partner", "Partner"),
   ("Investor", "Investor"),
   ("Shop Owner", "Shop Owner"),
  
)



worker_choice = (
("Gare Workers","Gare Workers"),
("Male Helper","Male Helper"),
("Female Helper","Female Helper"),
("Paint Workers","Paint Workers"),
("Electrical Workers","Electrical Workers"),
("Plumbing Workers","Plumbing Workers"),
("Granite Workers","Granite Workers"),
("Tile Workers","Tile Workers"),
("Welding Workers","Welding Workers"),
("Aluminum Window Workers","Aluminum Window Workers"),
("ACC Workers","ACC Workers"),
("Stone Cladding Workers","Stone Cladding Workers"),
("Batch Workers","Batch Workers"),
("Structural Workers","Structural Workers"),
("Borewell Workers","Borewell Workers"),
("Street Light Workers","Street Light Workers"),
("UPS Workers","UPS Workers"),
("CC Camera Workers","CC Camera Workers"),
("LED Name Board Workers","LED Name Board Workers"),
("Retail Shop", "Retail Shop"),
("wholesale Shop", "wholesale Shop"),
("Distributor", "Distributor"),
("Factory", "Factory"),
("Temporary worker", "Temporary worker"),

)

product_choice = (
("M Sand", "M Sand"),
("P Sand", "P Sand"),
("Cement", "Cement"),
("Stone - 20mm", "Stone - 20mm"),
("Stone - 40mm", "Stone - 40mm"),
("Stone - 60mm", "Stone - 60mm"),
("RMC", "RMC"),
("Steel", "Steel"),
("Granite", "Granite"),
("Aluminum Window", "Aluminum Window"),
("ACP", "ACP"),
("Sanitary Item", "Sanitary Item"),
("Electric Item", "Electric Item"),
("Bricks", "Bricks"),
("Concrete Solid Blocks 4", "Concrete Solid Blocks 4"),
("Concrete Solid Blocks 6", "Concrete Solid Blocks 6"),
("Concrete Solid Blocks 8", "Concrete Solid Blocks 8"),
("PVC Pipes", "PVC Pipes"),
("GI Pipes", "GI Pipes"),
("Borewell Pumpset Materials", "Borewell Pumpset Materials"),
("School desk and furniture", "School desk and furniture"),
("Green Board and Notice Board", "Green Board and Notice Board"),
("UPS and Batteries", "UPS and Batteries"),
("LED Street light", "LED Street light"),
("Street light High Mast Poles", "Street light High Mast Poles"),
("Stones", "Stones"),

)
vehicle_choice={
    ("JCB", "JCB"),
    ("Tractor", "Tractor"),
    ("Tipper", "Tipper"),
    ("Lorre", "Lorre"),
    ("Tata-ace", "Tata-ace"),
    ("Canter", "Canter"),   
    ("Auto", "Auto"),   
}
Material_name_choice={
    ("Debris", "Debris"), 
    ("M Sand", "M Sand"),
("P Sand", "P Sand"),
("Cement", "Cement"),
("Stone - 20mm", "Stone - 20mm"),
("Stone - 40mm", "Stone - 40mm"),
("Stone - 60mm", "Stone - 60mm"),
("RMC", "RMC"),
("Steel", "Steel"),
("Granite", "Granite"),
("Aluminum Window", "Aluminum Window"),
("ACP", "ACP"),
("Sanitary Item", "Sanitary Item"),
("Electric Item", "Electric Item"),
("Bricks", "Bricks"),
("Concrete Solid Blocks 4", "Concrete Solid Blocks 4"),
("Concrete Solid Blocks 6", "Concrete Solid Blocks 6"),
("Concrete Solid Blocks 8", "Concrete Solid Blocks 8"),
("PVC Pipes", "PVC Pipes"),
("GI Pipes", "GI Pipes"),
("Borewell Pumpset Materials", "Borewell Pumpset Materials"),
("School desk and furniture", "School desk and furniture"),
("Green Board and Notice Board", "Green Board and Notice Board"),
("UPS and Batteries", "UPS and Batteries"),
("LED Street light", "LED Street light"),
("Street light High Mast Poles", "Street light High Mast Poles"),
("Stones", "Stones"), 
    
    
}
state_choice={
     ("Karnataka","Karnataka"),
    ("Andhra Pradesh","Andhra Pradesh"),
    ("Arunachal Pradesh","Arunachal Pradesh"),
    ("Assam","Assam"),
    ("Bihar","Bihar"),
    ("Chhattisgarh","Chhattisgarh"),
    ("Delhi","Delhi"),
    ("Goa","Goa"),
    ("Gujarat","Gujarat"),
    ("Haryana","Haryana"),
    ("Himachal Pradesh","Himachal Pradesh"),
    ("Jharkhand","Jharkhand"),
    ("Kerala","Kerala"),
    ("Maharashtra","Maharashtra"),
    ("Madhya Pradesh","Madhya Pradesh"),
    ("Manipur","Manipur"),
    ("Meghalaya","Meghalaya"),
    ("Mizoram","Mizoram"),
    ("Nagaland","Nagaland"),
    ("Odisha","Odisha"),
    ("Punjab","Punjab"),
    ("Rajasthan","Rajasthan"),
    ("Sikkim","Sikkim"),
    ("TamilNadu","TamilNadu"),
    ("Tripura","Tripura"),
    ("Telangana","Telangana"),
    ("Uttar Pradesh","Uttar Pradesh"),
    ("Uttarakhand","Uttarakhand"),
    ("West Bengal","West Bengal"),
    ("Jammu & Kashmir","Jammu & Kashmir"),
    ("Ladakh","Ladakh"),
    ("Andaman & Nicobar","Andaman & Nicobar"),
    ("Chandigarh","Chandigarh"),
    ("Lakshadweep","Lakshadweep"),
    ("Puducherry","Puducherry"),
    ("Dadra & Nagar Haveli & Daman & Diu","Dadra & Nagar Haveli & Daman & Diu"),
    
}
gender_choice={
    ("Male","Male"),
    ("Female","Female"),
    ("Others","Others"),
}
marital_status_choice={
    ("Single","Single"),
    ("Married","Married"),
    
}
# User and Company Models
class SubscriptionPlan(models.Model):
    name = models.CharField(max_length=50)
    total_months=models.IntegerField(default=0)
    total_amount=models.IntegerField(default=0)
    month = models.IntegerField(null=True, blank=True)
    price_monthly = models.IntegerField(null=True, blank=True)
    years = models.IntegerField(null=True, blank=True)
    price_yearly = models.IntegerField(null=True, blank=True)
    user_limit = models.IntegerField()
    project_limit = models.IntegerField()
    description = models.TextField(blank=True)
 

    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=100,blank=True, null=True)
    email = models.CharField(blank=True, null=True)
    phone = models.CharField(max_length=20,blank=True, null=True)
    address = models.TextField(blank=True,default="")
    about = models.TextField(blank=True,default="")
    subscription_plan = models.ForeignKey(SubscriptionPlan, on_delete=models.CASCADE, null=True)
    
    logo = models.ImageField(upload_to='logo/', blank=True)
    is_subscribed = models.BooleanField(default=False)
    subscribed_date = models.DateField(blank=True, null=True) 
    subscribed_till = models.DateField(blank=True, null=True) 
    subscribed_prise = models.IntegerField(null=True, blank=True)
    user_limit = models.IntegerField(null=True, blank=True)
    uu_id = models.CharField(max_length=255, null=True, blank=True)
    t_id = models.CharField(max_length=255, null=True, blank=True)
    gst= models.CharField(max_length=255, null=True, blank=True)
    pan= models.CharField(max_length=255, null=True, blank=True)
    bank_account_number=models.CharField(max_length=55, default="", blank=True)
    bank_account_name=models.CharField(max_length=155, default="", blank=True)
    bank_account_bank_name=models.CharField(max_length=155, default="", blank=True)
    bank_account_branch_name=models.CharField(max_length=155, default="", blank=True)
    ifsc_code=models.CharField(max_length=55, default="", blank=True) 
    upi_id=models.CharField(max_length=155, default="", blank=True) 

    # def __str__(self):
    #     return self.name

class User(AbstractUser):
   company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
   designation = models.CharField(max_length = 20, choices = designation_choice, null=True, blank=True)

   def __str__(self):
      return self.username 

class payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    SubscriptionPlan = models.ForeignKey(SubscriptionPlan, on_delete=models.CASCADE, null=True)
    is_subscribed = models.BooleanField(default=False)
    subscribed_date = models.DateField(blank=True, null=True) 
    subscribed_till = models.DateField(blank=True, null=True) 
    subscribed_prise = models.IntegerField(null=True, blank=True)
    uu_id = models.CharField(max_length=255, null=True, blank=True)
    t_id = models.CharField(max_length=255, null=True, blank=True)


   
class Profile(models.Model) :
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   address=models.TextField(default="", blank=True)
   image=models.ImageField(upload_to='profile/' ,blank=True,)
   occupation=models.CharField(max_length=155, default="", blank=True)
   gender=models.CharField(max_length=55, choices = gender_choice, default="", blank=True)
   marital_status=models.CharField(max_length=155, choices=marital_status_choice, default="", blank=True)
   age=models.IntegerField( default=0, blank=True)
   nationality=models.CharField(max_length=55, default="", blank=True)
   state=models.CharField(max_length=155,choices = state_choice, default="", blank=True)
   email=models.CharField(max_length=55, default="", blank=True)
   phone=models.CharField(max_length=55, default="", blank=True)
   aadhar=models.CharField(max_length=55, default="", blank=True)
   pan=models.CharField(max_length=55, default="", blank=True)
   pan_image=models.ImageField(upload_to='profile/' ,blank=True,)
   aadhar_image=models.ImageField(upload_to='profile/' ,blank=True,)
   shop_type=models.CharField(max_length=255, default="", blank=True)
   shop_image=models.ImageField(upload_to='profile/' ,blank=True,)
   bank_account=models.CharField(max_length=55, default="", blank=True)
   bank_account_name=models.CharField(max_length=155, default="", blank=True)
   bank_account_bank_name=models.CharField(max_length=155, default="", blank=True)
   bank_account_branch_name=models.CharField(max_length=155, default="", blank=True)
   ifsc_code=models.CharField(max_length=55, default="", blank=True)
   role = models.CharField(max_length = 135, null=True, blank=True) 
   others=models.CharField(max_length=255, default="", blank=True)
   upi_id=models.CharField(max_length=155, default="", blank=True) 
   #add
   def compress_image(self, image_field):
        if not image_field:
            return None

        img = Image.open(image_field)
        img = img.convert("RGB")  
        img.thumbnail((1000, 1000)) 

        buffer = BytesIO()
        quality = 75
        img.save(buffer, format='JPEG', quality=quality)
        file_name = f"mbw_{image_field.name}"
        return ContentFile(buffer.getvalue(), name=file_name)
   
   def save(self, *args, **kwargs):
        if self.image:
            self.image = self.compress_image(self.image)

        if self.pan_image:
            self.pan_image = self.compress_image(self.pan_image)

        if self.aadhar_image:
            self.aadhar_image = self.compress_image(self.aadhar_image)
        
        if self.shop_image:
            self.shop_image = self.compress_image(self.shop_image)        

        super().save(*args, **kwargs)   


   def __str__(self):
     return self.user.first_name
   
    
class Project(models.Model):
   company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
   project_name=models.CharField(max_length=255, default="", blank=True)
   address=models.TextField(default="", blank=True)
   date = models.DateTimeField(auto_now_add=True, blank=True)
   photo = models.ImageField(upload_to='project/' ,blank=True,)
   details=models.TextField(default="", blank=True)
   project_status=models.CharField(max_length=255, default="", blank=True)
   project_estimate=models.CharField(max_length=255, default="", blank=True)
   project_estimate_file=models.FileField(upload_to='files/', blank=True)
   project_plan_file=models.FileField(upload_to='files/', blank=True)
   project_deadline=models.CharField(max_length=255, default="", blank=True)


   def __str__(self):
      return self.project_name
   
class Pwd_sr_rates(models.Model):
    name=models.CharField(max_length=255, default="", blank=True)
    file=models.FileField(upload_to='files/', blank=True)
    date=models.DateField(null=True, blank=True)
    
    def __str__(self):
      return self.name    
    
########### edit

class project_progress(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
   project = models.ForeignKey(Project, blank=True, null=True, on_delete=models.CASCADE ) 
   photo = models.ImageField(upload_to='project/' ,blank=True,)
   details=models.TextField(default="", blank=True)
   status=models.CharField(max_length=255, default="", blank=True)
   date = models.DateTimeField(auto_now_add=True,blank=True, null=True, )

   def compress_image(self, image_field):
        if not image_field:
            return None

        img = Image.open(image_field)
        img = img.convert("RGB")  
        img.thumbnail((1000, 1000)) 

        buffer = BytesIO()
        quality = 75
        img.save(buffer, format='JPEG', quality=quality)
        file_name = f"mbw_{image_field.name}"
        return ContentFile(buffer.getvalue(), name=file_name)
   
   def save(self, *args, **kwargs):
        if self.photo:
            self.photo = self.compress_image(self.photo)

     
        super().save(*args, **kwargs) 

   def __str__(self):
      return self.user.first_name

class Qc_reports(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=255, default="", blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    project = models.ForeignKey(Project, blank=True, null=True, on_delete=models.CASCADE ) 
    file = models.FileField(upload_to='project/', blank=True)
    date = models.DateTimeField(auto_now_add=True,blank=True, null=True, )
    
    
    def __str__(self):
      return self.name 

class expenses(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
   project = models.ForeignKey(Project, blank=True, null=True, on_delete=models.CASCADE ) 
   photo = models.ImageField(upload_to='project/' ,blank=True,)
   details=models.TextField(default="", blank=True)
   cost=models.CharField(max_length=255, default="", blank=True)
   date = models.DateTimeField(auto_now_add=True,blank=True, null=True, )
   def compress_image(self, image_field):
        if not image_field:
            return None

        img = Image.open(image_field)
        img = img.convert("RGB")  
        img.thumbnail((1000, 1000)) 

        buffer = BytesIO()
        quality = 75
        img.save(buffer, format='JPEG', quality=quality)
        file_name = f"mbw_{image_field.name}"
        return ContentFile(buffer.getvalue(), name=file_name)
   
   def save(self, *args, **kwargs):
        if self.photo:
            self.photo = self.compress_image(self.photo)

        super().save(*args, **kwargs) 

   def __str__(self):
      return self.user.first_name



class Machinery(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    project = models.ForeignKey(Project, blank=True, null=True, on_delete=models.CASCADE ) 
    work_name=models.CharField(max_length=255, default="", blank=True)
    bill = models.ImageField(upload_to='project/' ,blank=True,)
    photo = models.ImageField(upload_to='project/' ,blank=True,)
    total_hours=models.CharField(max_length=55, default="", blank=True)
    total_cost=models.CharField(max_length=55, default="", blank=True)
    start_time=models.TimeField(blank=True)
    break_start_time=models.TimeField(blank=True)
    break_end_time=models.TimeField(blank=True)
    end_time=models.TimeField(blank=True)
    added_date = models.DateTimeField(auto_now_add=True,blank=True, null=True, )
    date=models.DateField(blank=True, null=True)
    

    def compress_image(self, image_field):
        if not image_field:
            return None

        img = Image.open(image_field)
        img = img.convert("RGB")  
        img.thumbnail((1000, 1000)) 

        buffer = BytesIO()
        quality = 75
        img.save(buffer, format='JPEG', quality=quality)
        file_name = f"mbw_{image_field.name}"
        return ContentFile(buffer.getvalue(), name=file_name)
   
    def save(self, *args, **kwargs):
        if self.photo:
            self.photo = self.compress_image(self.photo)
        if self.bill:
            self.bill = self.compress_image(self.bill)
        super().save(*args, **kwargs) 

    def __str__(self):
      return self.work_name

class Machinery_photo(models.Model):
    Machinery = models.ForeignKey(Machinery, on_delete=models.CASCADE)
    bill_images=models.ImageField(upload_to='project/',blank=True,)

    def __str__(self):
      return self.Machinery.work_name

class salary(models.Model): 
    profile = models.ForeignKey(Profile, blank=True, null=True, on_delete=models.CASCADE)
    from_date=models.DateField(blank=True, null=True)
    to_date=models.DateField(blank=True, null=True)
    no_days=models.CharField(max_length=25, default="", blank=True)
    per_day_salary=models.CharField(max_length=25, default="", blank=True)
    total_salary=models.CharField(max_length=55, default="", blank=True)
    photo =models.ImageField(upload_to='profile/' ,blank=True,)
    added_date = models.DateTimeField(auto_now_add=True,blank=True, null=True, )
    
    def compress_image(self, image_field):
            if not image_field:
                return None

            img = Image.open(image_field)
            img = img.convert("RGB")  
            img.thumbnail((1000, 1000)) 

            buffer = BytesIO()
            quality = 75
            img.save(buffer, format='JPEG', quality=quality)
            file_name = f"mbw_{image_field.name}"
            return ContentFile(buffer.getvalue(), name=file_name)
    
    def save(self, *args, **kwargs):
            if self.photo:
                self.photo = self.compress_image(self.photo)
            super().save(*args, **kwargs)  

#########
class Attendance(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
   project = models.ForeignKey(Project, blank=True, null=True, on_delete=models.CASCADE , related_name="project_attendance")
   project_lunch_start= models.ForeignKey(Project, blank=True, null=True, on_delete=models.CASCADE , related_name="lunch_start")
   project_lunch_end= models.ForeignKey(Project, blank=True, null=True, on_delete=models.CASCADE , related_name="lunch_end")
   project_punch_out= models.ForeignKey(Project, blank=True, null=True, on_delete=models.CASCADE , related_name="punch_out")
   date = models.DateField(default=timezone.now)
   punch_in = models.TimeField(null=True, blank=True)
   lunch_start = models.TimeField(null=True, blank=True)
   lunch_end = models.TimeField(null=True, blank=True)
   punch_out = models.TimeField(null=True, blank=True)
   #edit
   punch_in_photo = models.ImageField(upload_to='attendance/' ,blank=True,)
   punch_out_photo= models.ImageField(upload_to='attendance/' ,blank=True,)
   lunch_in_photo= models.ImageField(upload_to='attendance/' ,blank=True,)
   lunch_out_photo= models.ImageField(upload_to='attendance/' ,blank=True,)
   punch_in_lon=models.CharField(max_length=255, default="", blank=True)
   punch_in_lat=models.CharField(max_length=255, default="", blank=True)
   punch_out_lon=models.CharField(max_length=255, default="", blank=True)
   punch_out_lat=models.CharField(max_length=255, default="", blank=True)
   lunch_start_lon=models.CharField(max_length=255, default="", blank=True)
   lunch_start_lat=models.CharField(max_length=255, default="", blank=True)
   lunch_end_lon=models.CharField(max_length=255, default="", blank=True)
   lunch_end_lat=models.CharField(max_length=255, default="", blank=True)

   def get_work_duration(self):
        if self.punch_in and self.punch_out:
            punch_in_dt = datetime.datetime.combine(self.date, self.punch_in)
            punch_out_dt = datetime.datetime.combine(self.date, self.punch_out)
            work_duration = punch_out_dt - punch_in_dt

            lunch_duration = datetime.timedelta()
            if self.lunch_start and self.lunch_end:
                lunch_start_dt = datetime.datetime.combine(self.date, self.lunch_start)
                lunch_end_dt = datetime.datetime.combine(self.date, self.lunch_end)
                lunch_duration = lunch_end_dt - lunch_start_dt

            return work_duration - lunch_duration
        return None

   def formatted_work_duration(self):
        duration = self.get_work_duration()
        if duration:
            total_seconds = int(duration.total_seconds())
            hours, remainder = divmod(total_seconds, 3600)
            minutes = remainder // 60
            return f"{hours:02}:{minutes:02}"
        return False
   
   def compress_image(self, image_field):
        if not image_field:
            return None

        img = Image.open(image_field)
        img = img.convert("RGB")  
        img.thumbnail((1000, 1000)) 

        buffer = BytesIO()
        quality = 75
        img.save(buffer, format='JPEG', quality=quality)
        file_name = f"mbw_{image_field.name}"
        return ContentFile(buffer.getvalue(), name=file_name)
   
   def save(self, *args, **kwargs):
        if self.punch_in_photo:
            self.punch_in_photo = self.compress_image(self.punch_in_photo)

        if self.punch_out_photo:
            self.punch_out_photo = self.compress_image(self.punch_out_photo)

        if self.lunch_in_photo:
            self.lunch_in_photo = self.compress_image(self.lunch_in_photo)
        
        if self.punch_out:
            self.punch_out = self.compress_image(self.punch_out)        

        super().save(*args, **kwargs)    
   
   def __str__(self):
      return self.user.first_name
  

      


# class material_order(models.Model): 

  #edit
# class Inventory(models.Model):
#    user = models.ForeignKey(User, on_delete=models.CASCADE)
#    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
#    project = models.ForeignKey(Project, blank=True, null=True, on_delete=models.CASCADE)
#    name=models.CharField(max_length=255, default="", blank=True)
#    qty=models.CharField(max_length=25, default="", blank=True)
#    price=models.CharField(max_length=25, default="", blank=True)
#    image=models.ImageField(upload_to='inventory/' ,blank=True,)
#    image1=models.ImageField(upload_to='inventory/' ,blank=True,)
#    image2=models.ImageField(upload_to='inventory/' ,blank=True,)
#    image3=models.ImageField(upload_to='inventory/' ,blank=True,)
#    invoice_image=models.ImageField(upload_to='inventory/' ,blank=True,)
#    invoice_image1=models.ImageField(upload_to='inventory/' ,blank=True,)
#    invoice_image2=models.ImageField(upload_to='inventory/' ,blank=True,)
#    invoice_image3=models.ImageField(upload_to='inventory/' ,blank=True,)
#    date = models.DateTimeField(auto_now_add=True, blank=True)
#    lon=models.CharField(max_length=255, default="", blank=True)
#    lat=models.CharField(max_length=255, default="", blank=True)
#    material_taken_name=models.CharField(max_length=255, default="", blank=True)
#    material_taken_phone=models.CharField(max_length=55, default="", blank=True)
#    shop_name=models.CharField(max_length=255, default="", blank=True)
#    shop_image=models.ImageField(upload_to='inventory/' ,blank=True,)
   

#    def __str__(self):
#         return self.name

#edit
class stocks_in_Inventory(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
   project = models.ForeignKey(Project, blank=True, null=True, on_delete=models.CASCADE)
   name=models.CharField(max_length=255,default="", blank=True) #
   qty=models.CharField(max_length=25, default="", blank=True)
   price=models.CharField(max_length=25, default="", blank=True)
   image=models.ImageField(upload_to='inventory/' ,blank=True,)
   date = models.DateTimeField(auto_now_add=True, blank=True)
   lon=models.CharField(max_length=255, default="", blank=True)
   lat=models.CharField(max_length=255, default="", blank=True)
   def compress_image(self, image_field):
        if not image_field:
            return None

        img = Image.open(image_field)
        img = img.convert("RGB")  
        img.thumbnail((1000, 1000)) 

        buffer = BytesIO()
        quality = 75
        img.save(buffer, format='JPEG', quality=quality)
        file_name = f"mbw_{image_field.name}"
        return ContentFile(buffer.getvalue(), name=file_name)
   
   def save(self, *args, **kwargs):
        if self.image:
            self.image = self.compress_image(self.image)
        super().save(*args, **kwargs)  

   def __str__(self):
        return self.name

class Inventory_use(models.Model):
   company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   project = models.ForeignKey(Project, blank=True, null=True, on_delete=models.CASCADE)
   name=models.CharField(max_length=255, default="", blank=True) #
   qty=models.CharField(max_length=25, default="", blank=True)
   image=models.ImageField(upload_to='inventory/' ,blank=True,)
   date = models.DateTimeField(auto_now_add=True, blank=True)
   lon=models.CharField(max_length=255, default="", blank=True)
   lat=models.CharField(max_length=255, default="", blank=True)

   def compress_image(self, image_field):
        if not image_field:
            return None

        img = Image.open(image_field)
        img = img.convert("RGB")  
        img.thumbnail((1000, 1000)) 

        buffer = BytesIO()
        quality = 75
        img.save(buffer, format='JPEG', quality=quality)
        file_name = f"mbw_{image_field.name}"
        return ContentFile(buffer.getvalue(), name=file_name)
   
   def save(self, *args, **kwargs):
        if self.image:
            self.image = self.compress_image(self.image)

     
        super().save(*args, **kwargs) 

   def __str__(self):
        return self.name
   
   
class Project_daily_work_details(models.Model):
   company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
   date = models.DateTimeField(auto_now_add=True, blank=True)
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   project = models.ForeignKey(Project,  blank=True, null=True, on_delete=models.CASCADE)
   no_of_workers=models.CharField(max_length=25, default="", blank=True)
   image=models.ImageField(upload_to='uploads/' ,blank=True,)
   project_work_status=models.CharField(max_length=225, default="", blank=True,)
   lon=models.CharField(max_length=255, default="", blank=True)
   lat=models.CharField(max_length=255, default="", blank=True)

   def compress_image(self, image_field):
        if not image_field:
            return None

        img = Image.open(image_field)
        img = img.convert("RGB")  
        img.thumbnail((1000, 1000)) 

        buffer = BytesIO()
        quality = 75
        img.save(buffer, format='JPEG', quality=quality)
        file_name = f"mbw_{image_field.name}"
        return ContentFile(buffer.getvalue(), name=file_name)
   
   def save(self, *args, **kwargs):
        if self.image:
            self.image = self.compress_image(self.image)

     
        super().save(*args, **kwargs) 
   def __str__(self):
       return self.user.first_name

class Project_work_inspection_details(models.Model):
   company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
   date = models.DateTimeField(auto_now_add=True, blank=True)
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   project = models.ForeignKey(Project,  blank=True, null=True, on_delete=models.CASCADE)
   no_of_workers=models.CharField(max_length=25, default="", blank=True)
   image=models.ImageField(upload_to='uploads/' ,blank=True,)
   project_work_status=models.CharField(max_length=225, default="", blank=True,)
   lon=models.CharField(max_length=255, default="", blank=True)
   lat=models.CharField(max_length=255, default="", blank=True)

   def compress_image(self, image_field):
        if not image_field:
            return None

        img = Image.open(image_field)
        img = img.convert("RGB")  
        img.thumbnail((1000, 1000)) 

        buffer = BytesIO()
        quality = 75
        img.save(buffer, format='JPEG', quality=quality)
        file_name = f"mbw_{image_field.name}"
        return ContentFile(buffer.getvalue(), name=file_name)
   
   def save(self, *args, **kwargs):
        if self.image:
            self.image = self.compress_image(self.image)

     
        super().save(*args, **kwargs) 

   def __str__(self):
       return self.user.first_name
    
class Material_shifting(models.Model):
   company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
   date = models.DateTimeField(auto_now_add=True, blank=True)
   user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="from_user", null=True, blank=True )
   user_re = models.ForeignKey(User, on_delete=models.CASCADE ,  related_name="to_user", null=True, blank=True)
   project = models.ForeignKey(Project,  blank=True, null=True, on_delete=models.CASCADE, related_name="from_project")
   to_project = models.ForeignKey(Project,  blank=True, null=True, on_delete=models.CASCADE, related_name="to_project")
   vehicle= models.CharField(max_length=255,default="", blank=True) #
   image=models.ImageField(upload_to='uploads/' ,blank=True,)
   image_re=models.ImageField(upload_to='uploads/' ,blank=True,)
   Material_name=models.CharField(max_length=225, default="", blank=True,) #
   lon=models.CharField(max_length=255, default="", blank=True)
   lat=models.CharField(max_length=255, default="", blank=True)
   lon_re=models.CharField(max_length=255, default="", blank=True)
   lat_re=models.CharField(max_length=255, default="", blank=True)

   def compress_image(self, image_field):
        if not image_field:
            return None

        img = Image.open(image_field)
        img = img.convert("RGB")  
        img.thumbnail((1000, 1000)) 

        buffer = BytesIO()
        quality = 75
        img.save(buffer, format='JPEG', quality=quality)
        file_name = f"mbw_{image_field.name}"
        return ContentFile(buffer.getvalue(), name=file_name)
   
   def save(self, *args, **kwargs):
        if self.image:
            self.image = self.compress_image(self.image)

     
        super().save(*args, **kwargs) 

   def __str__(self):
       return self.user.first_name
   
#made
# class Material_shifting_received(models.Model):
#    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
#    date = models.DateTimeField(auto_now_add=True, blank=True)
#    user = models.ForeignKey(User, on_delete=models.CASCADE)
#    project = models.ForeignKey(Project,  blank=True, null=True, on_delete=models.CASCADE, )
#    image=models.ImageField(upload_to='uploads/' ,blank=True,)
   
#    Material_name=models.CharField(max_length=225, default="", blank=True,) #
#    lon=models.CharField(max_length=255, default="", blank=True)
#    lat=models.CharField(max_length=255, default="", blank=True)

#    def compress_image(self, image_field):
#         if not image_field:
#             return None

#         img = Image.open(image_field)
#         img = img.convert("RGB")  
#         img.thumbnail((1000, 1000)) 

#         buffer = BytesIO()
#         quality = 75
#         img.save(buffer, format='JPEG', quality=quality)
#         file_name = f"mbw_{image_field.name}"
#         return ContentFile(buffer.getvalue(), name=file_name)
   
#    def save(self, *args, **kwargs):
#         if self.image:
#             self.image = self.compress_image(self.image)

     
#         super().save(*args, **kwargs) 
        
#    def __str__(self):
#        return self.user.first_name
   
# add investor to project
class Project_investor(models.Model):
   company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   project = models.ForeignKey(Project,  blank=True, null=True, on_delete=models.CASCADE)
   def __str__(self):
       return self.user.first_name
   


class project_pre_plan(models.Model):
   company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
   date = models.DateTimeField(auto_now_add=True, blank=True)
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   project_name=models.CharField(max_length=255, default="", blank=True)
   address=models.TextField(default="", blank=True)

   def __str__(self):
       return self.project_name
   
   
class project_plan_files(models.Model):
   company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
   file = models.FileField(upload_to='uploads/')
   file_name=models.CharField(max_length=255, default="", blank=True)
   project_pre_plan = models.ForeignKey(project_pre_plan, on_delete=models.CASCADE)
   date = models.DateTimeField(auto_now_add=True, blank=True)
   user = models.ForeignKey(User, on_delete=models.CASCADE)

   def __str__(self):
       return self.file_name

# material shifting

#group of bill for who
#multiple files for upload
#bill generate
#bill items

# class Client(models.Model):
#     name = models.CharField(max_length=100)
#     phone = models.CharField(max_length=100)
#     # other client details
#     def __str__(self):
#        return self.name
    
# class bill_files(models.Model):
#    file = models.FileField(upload_to='uploads/')
#    file_name=models.CharField(max_length=255, default="", blank=True)
#    Client = models.ForeignKey(Client, on_delete=models.CASCADE)
#    date = models.DateTimeField(auto_now_add=True, blank=True)

#    def __str__(self):
#        return self.file_name
   
# class Invoice(models.Model):
#     client = models.ForeignKey(Client, on_delete=models.CASCADE)
#     invoice_number = models.CharField(max_length=50, unique=True)
#     date_issued = models.DateField(auto_now_add=True)
#     total_amount = models.DecimalField(max_digits=10, decimal_places=2)
#     # other invoice details
#     def __str__(self):
#        return self.date_issued

# class InvoiceItem(models.Model):
#     invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
#     description = models.CharField(max_length=200)
#     quantity = models.IntegerField()
#     unit_price = models.DecimalField(max_digits=8, decimal_places=2)
#     # other item details
#     def __str__(self):
#        return self.quantity