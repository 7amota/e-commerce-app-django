from django.shortcuts import render ,redirect
from django.http import HttpResponse
from .forms import *
from django.views.generic import CreateView, FormView, View
from django.contrib.auth import authenticate, login


class LoginAndRegisterView(View):
    template_name = 'pages/login-register.html'
    form_class = UserLogin()
    form_class_two = UserRegister()
    def get(self,request):
        return render(request, self.template_name, context={'login':self.form_class, 'register':self.form_class_two})
    def post(self,request):
      if 'register' in request.POST:
          form = UserRegister(request.POST)
          if form.is_valid():
              form.save()
              return redirect('/')
          return render(request, self.template_name, {'register':form})


      if 'login' in request.POST:
            form = UserLogin()
            email = request.POST['email']
            password = request.POST['password']
            auth = authenticate(email=email, password=password)
            if auth:
                    login(request=request,user=auth)
                    return redirect('/')
            return render(request, self.template_name, {'login':form})

