from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from base.models import Profile,Project,Inventory_use,stocks_in_Inventory,Project_daily_work_details,Project_work_inspection_details,Material_shifting,project_pre_plan,project_plan_files,Company,Pwd_sr_rates,project_progress,Qc_reports,expenses,Machinery,salary
from django import forms


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username','first_name','last_name','password1','password2']

class passwordForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['password',]

class RegisterUserForm1(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username','first_name','last_name','password1','password2']

class Pwd_sr_ratesForm(forms.ModelForm):
	class Meta:
		model = Pwd_sr_rates
		fields =('__all__')

class expensesForm(forms.ModelForm):
	class Meta:
		model = expenses
		fields =('photo','details','cost')

class Qc_reportsForm(forms.ModelForm):
	class Meta:
		model = Qc_reports
		fields =('file','name',)

class project_progressForm(forms.ModelForm):
	class Meta:
		model = project_progress
		fields =('photo','details','status',)

class CompanyProfileForm(forms.ModelForm):
	class Meta:
		model = Company
		fields =('__all__')

class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields =('__all__')
		exclude = ('user','image','pan_image','aadhar_image','shop_image',)
            
class ProjectForm(forms.ModelForm):
	class Meta:
		model = Project
		fields =('__all__')
		exclude = ('date','company',)

class SalaryForm(forms.ModelForm):
	class Meta:
		model = salary
		fields =('__all__')
		exclude = ('profile',)

class MachineryForm(forms.ModelForm):
	class Meta:
		model = Machinery
		fields =('__all__')
		exclude = ('user','project','company',)

class Inventory_useForm(forms.ModelForm):
	class Meta:
		model = Inventory_use
		fields =('__all__')
		exclude = ('user','project','company',)

class stocks_in_InventoryForm(forms.ModelForm):
	class Meta:
		model = stocks_in_Inventory
		fields =('__all__')
		exclude = ('user','project','company',)

class Project_daily_work_detailsForm(forms.ModelForm):
	class Meta:
		model = Project_daily_work_details
		fields =('__all__')
		exclude = ('user','project','company',)

class Project_work_inspection_detailsForm(forms.ModelForm):
	class Meta:
		model = Project_work_inspection_details
		fields =('__all__')
		exclude = ('user','project','company',)

class project_plan_filesForm(forms.ModelForm):
	class Meta:
		model = project_plan_files
		fields =('__all__')
		exclude = ('user','project_pre_plan','company',)

class project_pre_planForm(forms.ModelForm):
	class Meta:
		model = project_pre_plan
		fields =('__all__')
		exclude = ('user','company',)

####pend#####
class Material_shiftingForm(forms.ModelForm):
	class Meta:
		model = Material_shifting
		fields =('vehicle','image','Material_name','lon','lat',)
#user
# to_project = models.ForeignKey(Project,  blank=True, null=True, on_delete=models.CASCADE, related_name="to_project")
# vehicle= models.CharField(max_length=255,default="", blank=True) #
# image=models.ImageField(upload_to='uploads/' ,blank=True,)
# Material_name=models.CharField(max_length=225, default="", blank=True,) #
# lon=models.CharField(max_length=255, default="", blank=True)
# lat=models.CharField(max_length=255, default="", blank=True)

#user_re
# image_re=models.ImageField(upload_to='uploads/' ,blank=True,)
# lon_re=models.CharField(max_length=255, default="", blank=True)
# lat_re=models.CharField(max_length=255, default="", blank=True)



class Material_shifting_editForm(forms.ModelForm):
	class Meta:
		model = Material_shifting
		fields =('image_re','lon_re','lat_re',)

# class Material_shifting_receivedForm(forms.ModelForm):
# 	class Meta:
# 		model = Material_shifting_received
# 		fields =('__all__')
# 		exclude = ('user','company',)
	



