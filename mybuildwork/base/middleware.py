from django.shortcuts import redirect
from django.utils.timezone import now
from django.contrib import messages

class SubscriptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = request.user
        unrestricted_paths = ['/accounts/', '/register/', '/packages/','/profile/','/home/','/pay/','/payment-return/','/admin/','/__debug__/']

        if user.is_authenticated and hasattr(user, 'company'):
            company = user.company
            if not company.is_subscribed or not company.subscribed_till or company.subscribed_till < now().date():    
                if not any(request.path.startswith(path) for path in unrestricted_paths):
                  if user.designation == "Owner":
                    messages.error(request, "Your subscription has expired or inactive. Please renew to continue.")
                    return redirect("base:packages")
                  else:
                    messages.error(request, "Contact Your Admin")
                    return redirect("base:profile")

        return self.get_response(request)
