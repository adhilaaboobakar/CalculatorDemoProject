from django.shortcuts import render
from django.views.generic import View
from django import forms
# Create your views here.

class AdditionView(View):
    
    def get(self,request,*args,**kwargs):
        return render(request,"addition.html")
    
    def post(self,request,*args,**kwargs):
        print(request.POST)
        n1=request.POST.get("num1")
        n2=request.POST.get("num2")
        result=int(n1)+int(n2)
        print("result =", result)
        # print(request.POST)
        return render(request,"addition.html",{"data":result})
    
class SubtractionView(View):

    def get(self,request,*args,**kwargs):
        return render(request,"subtraction.html")
    
    def post(self,request,*args,**kwargs):
        n1=request.POST.get("num1")
        n2=request.POST.get("num2")
        result=int(n1)-int(n2)
        print("result =", result)
        return render(request,'subtraction.html',{"data":result})  
    
class MultipilcationView(View):

    def get(self,request,*args,**kwargs):
        return render(request,"multiplication.html")
    
    def post(self,request,*args,**kwargs):
        n1=request.POST.get("num1")
        n2=request.POST.get("num2")
        result=int(n1)*int(n2)
        print("result =", result)
        return render(request,'multiplication.html',{"data":result})
    

class DivisionView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"division.html")
    
    def post(self,request,*args,**kwargs):
        n1=request.POST.get("num1")
        n2=request.POST.get("num2")
        result=int(n1)/int(n2)
        print("result =", result)
        return render(request,"division.html",{"data":result})
    
class LeapYearView(View):

    def get(self,request,*args,**kwargs):
        return render (request,"year.html")
    
    def post(self,request,*args,**kwargs):
        year=int(request.POST.get("year"))
        result=""
        if year%100==0 and year%400==0 or year%100!=0 and year%4==0:
            result=f"{year} is a leap year"
        else:
            result=f"{year} is not a leap year"
        return render(request,"year.html",{"data":result})

class EmiCalculatorView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"emicalculator.html")
    
    def post(self,request,*args,**kwargs):
        loan_amount=int(request.POST.get("amount"))
        intrest_rate=float(request.POST.get("interest"))
        tenure=int(request.POST.get("tenure"))


        p=loan_amount

        r=intrest_rate/12

        i=r/100
        n=tenure*12
        one_plus_power=(1+i)**n

        EMI=round((p*i*one_plus_power)/(one_plus_power-1))

        print(f"emi amount={EMI}")

        total_interest_payable=(EMI*n)-p
        total_payment=total_interest_payable+p
        context={
            "emi":EMI,
            "tip":total_interest_payable,
            "tp":total_payment
        }
        return render(request,"emicalculator.html",context)
    
class IndexView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"index.html")
    
    
class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()


class SigninView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,"login.html",{"form":form}) 


# registration first name,lname,email,username,pw
    
class RegistrationForm(forms.Form):
    firstname=forms.CharField(label="First Name")
    lastname=forms.CharField(label="Last Name")
    email=forms.EmailField(label="Email")
    username=forms.CharField(label="Username")
    password=forms.CharField(label="Password")

class RegistrationView(View):
    def get(self,request,*args,**kwargs):
        form=RegistrationForm()
        return render(request,"registration.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        print(request.POST.get("firstname"))
        print(request.POST.get("lastname"))
        print(request.POST.get("email"))
        print(request.POST.get("username"))
        print(request.POST.get("password"))
        form=RegistrationForm()
        return render(request,"registration.html",{"form":form})
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
        