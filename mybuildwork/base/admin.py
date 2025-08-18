from django.contrib import admin

# Register your models here.
from .models import User,Attendance,Profile,stocks_in_Inventory,Inventory_use,Project_daily_work_details,Project_work_inspection_details,Material_shifting,project_plan_files,Company,SubscriptionPlan,Project_investor,Project,payment,project_progress,expenses
admin.site.register(User)
admin.site.register(Attendance)
admin.site.register(Profile)
# admin.site.register(Inventory)
admin.site.register(stocks_in_Inventory)
admin.site.register(Inventory_use)
admin.site.register(Project_daily_work_details)
admin.site.register(Project_work_inspection_details)
admin.site.register(Material_shifting)
admin.site.register(project_plan_files)
# admin.site.register(Material_shifting_received)
admin.site.register(Company)
admin.site.register(SubscriptionPlan)
admin.site.register(Project_investor)
admin.site.register(Project)
admin.site.register(project_progress)
admin.site.register(payment)
admin.site.register(expenses)