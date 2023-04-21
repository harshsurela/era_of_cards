from django.conf import settings
import os
from django.template import RequestContext
from django.shortcuts import render, redirect
from django.http.response import HttpResponse, JsonResponse
from .models import *
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
# import pywhatkit  

# Create your views here.
 

def home(request):
    return render(request, "home/index.html")


@login_required(login_url='sign-in')
def dashboard(request):
    try:
        user = UserBase.objects.get(user_id=request.user.id)
    except Exception as e:
        print(e)
        return redirect("sign-in")
    return render(request, "dashboard/home.html", {'user': user})


def register(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        upass = request.POST.get('pass')
        email = request.POST.get('email')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        org = request.POST.get('org')
        phone = request.POST.get('phone')
        try:
            user = User.objects.get(username=uname)
            messages.warning(
                request, "User Already Registered With This Username !!")
            return redirect("register")
        except Exception as e:
            print(e)
            try:
                user = User.objects.get(email=email)
                messages.warning(
                    request, "User Already Registered With This Email !!")
                return redirect("register")
            except Exception as e:
                print(e)
                user = User.objects.create_user(
                    username=uname, password=upass, email=email)
                user.save()
                UserBaseInstance = UserBase()
                UserBaseInstance.first_name = fname
                UserBaseInstance.last_name = lname
                UserBaseInstance.cus_phone = phone
                UserBaseInstance.organization = org
                UserBaseInstance.user_id = user
                UserBaseInstance.save()
                messages.success(request, "registration Succesfull")
                return redirect("sign-in")
    return render(request, "auth/register.html")


@login_required(login_url='sign-in')
def accountsettings(request):
    country = Country.objects.all()
    try:
        user = UserBase.objects.get(user_id=request.user.id)
        if request.method == "POST":
            fname = request.POST.get('fname')
            lname = request.POST.get('lname')
            desig = request.POST.get('desig')
            org = request.POST.get('org')
            website = request.POST.get('website')
            phone = request.POST.get('phone')
            wp = request.POST.get('wp')
            skype = request.POST.get('skype')
            aboutme = request.POST.get('about')
            bank = request.POST.get('bank')
            add1 = request.POST.get('add1')
            add2 = request.POST.get('add2')
            pincode = request.POST.get('pincode')
            try:
                profile = request.FILES['propic']
                user.profile = profile
            except Exception as e:
                print(e)
            try:
                city = request.POST.get('city')
                user.city_id = City(city)
            except Exception as e:
                print(e, "joo")
            user.first_name = fname
            user.last_name = lname
            user.designation = desig
            user.organization = org
            user.website = website
            user.wp = wp
            user.cus_phone = phone
            user.skype = skype
            user.aboutme = aboutme
            user.bank_details = bank
            user.cus_add1 = add1
            user.cus_add2 = add2
            user.pincode = pincode
            user.save()
            messages.success(request, "Account Updated Succesfully")
            return redirect("dashboard")
    except Exception as e:
        print(e)
        messages.warning(request, "Session Expired")
        return redirect("sign-in")
    return render(request, "dashboard/account.html", {"country": country, 'user': user})


@login_required(login_url='sign-in')
def socialsettings(request):
    try:
        user = UserBase.objects.get(user_id=request.user.id)
        if request.method == "POST":
            fb = request.POST.get('fb')
            tw = request.POST.get('tw')
            ld = request.POST.get('ld')
            ig = request.POST.get('ig')
            yt = request.POST.get('yt')
            gps = request.POST.get('gps')
            user.fb = fb
            user.twitter = tw
            user.linkedin = ld
            user.ig = ig
            user.yt = yt
            user.gps = gps
            user.save()
            messages.success(request, "Social Settings Updated")
            return redirect("dashboard")
    except Exception as e:
        print(e)
        messages.warning(request, "Session Expired")
        return redirect("sign-in")
    return render(request, "dashboard/social.html")


@login_required(login_url='sign-in')
def changepass(request):
    if request.method == "POST":
        oldpass = request.POST.get('opass')
        newpass = request.POST.get('pass')
        print(request.user.username)
        user = authenticate(request, username=request.user, password=oldpass)
        if user:
            user.set_password(newpass)
            user.save()
            messages.success(request, "Password Updated")
        else:
            messages.warning(request, "The Old Password Is Wrong")

        # except Exception as e:
        #     print(e)
        #     messages.warning(request,"The Old Password Is Wrong")
    return render(request, "auth/changepass.html")


@login_required(login_url='sign-in')
def layouts(request):
    return render(request, "dashboard/layouts.html")


@login_required(login_url='sign-in')
def features(request):
    return render(request, "dashboard/features.html")


@login_required(login_url='sign-in')
def product(request):
    prod = Product.objects.all()
    return render(request, "dashboard/product.html", {'prod': prod})


@login_required(login_url='sign-in')
def services(request):
    serv = Service.objects.all()
    return render(request, "dashboard/services.html", {'serv': serv})


@login_required(login_url='sign-in')
def testimonial(request):
    test = Testimonial.objects.all()
    return render(request, "dashboard/testimonial.html", {'test': test})


@login_required(login_url='sign-in')
def mypackage(request):
    return render(request, "dashboard/mypackage.html")


@login_required(login_url='sign-in')
def payments(request):
    return render(request, "dashboard/payments.html")


@login_required(login_url='sign-in')
def appointments(request):
    return render(request, "dashboard/appointments.html")




@login_required(login_url='sign-in')
def country_ajax_data(request):
    if request.method == "POST":
        c_id = request.POST.get("country_id")
        print(c_id)
        try:
            country = Country.objects.filter(id=c_id).first()
            print(country)
            state = State.objects.filter(country_id=country)
        except Exception:
            data = "Error"
            return JsonResponse(data)
        return JsonResponse(list(state.values('id', 'state_name')), safe=False)


@login_required(login_url='sign-in')
def state_ajax_data(request):
    if request.method == "POST":
        s_id = request.POST.get("state_id")
        print(s_id)
        try:
            state = State.objects.filter(id=s_id).first()
            print(state)
            city = City.objects.filter(state_id=state)
        except Exception:
            data = "Error"
            return JsonResponse(data)
        return JsonResponse(list(city.values('id', 'city_name')), safe=False)


@login_required(login_url='sign-in')
def addproduct(request):

    if request.method == "POST":
        pname = request.POST.get("pname")
        pdetails = request.POST.get("pdetails")
        status = request.POST.get("status")
        print(status)
        prod = Product()
        try:
            pimg = request.FILES.get("pimg")
            prod.product_img = pimg
        except Exception as e:
            print(e)
        prod.product_name = pname
        prod.desc = pdetails
        if status == "on":
            prod.status = "active"
        else:
            prod.status = "deactive"
        
        prod.user_id = UserBase(request.user.id)
        prod.save()
        messages.success(request, "Product Added")
        return redirect("product")
    return render(request, "dashboard/addproduct.html")


@login_required(login_url='sign-in')
def addgallery(request):
    if request.method == "POST":
        gname = request.POST.get("gname")
        status = request.POST.get("status")
        gal = Gallery()
        try:
            gimg = request.FILES.get("gimg")
            gal.gallery_img = gimg
        except Exception as e:
            print(e)
        gal.gallery_name = gname
        if status == "on":
            gal.status = "active"
        else:
            gal.status = "deactive"
        gal.user_id = UserBase(request.user.id)
        gal.save()
        messages.success(request, "Photo Added To Gallery ")
        return redirect("gallery")
    return render(request, "dashboard/addgallery.html")


@login_required(login_url='sign-in')
def addvgallery(request):
    if request.method == "POST":
        vgname = request.POST.get("vgname")
        vglink = request.POST.get("vglink")
        status = request.POST.get("status")
        vgal = Vgallery()
        vgal.vgallery_name = vgname
        vgal.vgallery_link = vglink
        if status == "on":
            vgal.status = "active"
        else:
            vgal.status = "deactive"
        vgal.user_id = UserBase(request.user.id)
        vgal.save()
        messages.success(request, "Video Added To Gallery ")
        return redirect("videogal")
    return render(request, "dashboard/addvgallery.html")


@login_required(login_url='sign-in')
def addservice(request):
    if request.method == "POST":
        sname = request.POST.get("sname")
        sdetails = request.POST.get("sdetails")
        status = request.POST.get("status")
        serv = Service()
        try:
            simg = request.FILES.get("simg")
            serv.service_img = simg
        except Exception as e:
            print(e)
        serv.service_name = sname
        serv.service_desc = sdetails
        if status == "on":
            serv.status = "active"
        else:
            serv.status = "deactive"
        serv.user_id = UserBase(request.user.id)
        serv.save()
        messages.success(request, "Service Added")
        return redirect("services")
    return render(request, "dashboard/addservice.html")

@login_required(login_url='sign-in')
def addtest(request):
    if request.method == "POST":
        cname = request.POST.get("clientName")
        testTitle = request.POST.get("testTitle")
        testDesc = request.POST.get("testDesc")
        status = request.POST.get("status")
        test=Testimonial()
        try:
            clientImg = request.FILES.get("clientImg")
            test.client_image=clientImg
        except Exception as e:
            print(e)
        test.client_name=cname
        test.test_title=testTitle
        test.test_desc=testDesc
        if status == "on":
            test.status = "active"
        else:
            test.status = "deactive"
        test.user_id = UserBase(request.user.id)
        test.save()
        messages.success(request, "Testimonial Added")
        return redirect("testimonial")
    return render(request, "dashboard/addtestimonial.html")


@login_required(login_url='sign-in')
def editproduct(request, id):
    prod = Product.objects.get(id=id)
    if request.method == "POST":
        pname = request.POST.get("pname")
        pdetails = request.POST.get("pdetails")
        status = request.POST.get("status")
        try:
            pimg = request.FILES.get("pimg")
            if pimg is not None:
                prod.product_img = pimg
        except Exception as e:
            print(e)
        prod.product_name = pname
        prod.desc = pdetails
        if status == "on":
            prod.status = "active"
        else:
            prod.status = "deactive"
        prod.user_id = UserBase(request.user.id)
        prod.save()
        messages.success(request, "Product Updated")
        return redirect("product")
    return render(request, "dashboard/editproduct.html", {'prod': prod})


@login_required(login_url='sign-in')
def edittest(request, id):
    test = Testimonial.objects.get(id=id)
    if request.method == "POST":
        cname = request.POST.get("clientName")
        testTitle = request.POST.get("testTitle")
        testDesc = request.POST.get("testDesc")
        status = request.POST.get("status")
        try:
            clientImg = request.FILES.get("clientImg")
            if clientImg is not None:
                test.client_image=clientImg
        except Exception as e:
            print(e)
        test.client_name=cname
        test.test_title=testTitle
        test.test_desc=testDesc
        if status == "on":
            test.status = "active"
        else:
            test.status = "deactive"
        
        test.user_id = UserBase(request.user.id)
        test.save()
        messages.success(request, "Testimonial Updated")
        return redirect("testimonial")
    return render(request, "dashboard/edittestimonial.html", {'test': test})


@login_required(login_url='sign-in')
def editgallery(request, id):
    gal = Gallery.objects.get(id=id)
    if request.method == "POST":
        gname = request.POST.get("gname")
        status = request.POST.get("status")
        try:
            gimg = request.FILES.get("gimg")
            if gimg is not None:
                gal.gallery_img = gimg
        except Exception as e:
            print(e)
        gal.gallery_name = gname
        if status == "on":
            gal.status = "active"
        else:
            gal.status = "deactive"
        gal.user_id = UserBase(request.user.id)
        gal.save()
        messages.success(request, "Gallery Updated")
        return redirect("gallery")
    return render(request, "dashboard/editgallery.html", {'gal': gal})


@login_required(login_url='sign-in')
def editvgallery(request, id):
    vgal = Vgallery.objects.get(id=id)
    if request.method == "POST":
        vgname = request.POST.get("vgname")
        vglink = request.POST.get("vglink")
        status = request.POST.get("status")
        vgal.vgallery_name = vgname
        vgal.vgallery_link = vglink
        if status == "on":
            vgal.status = "active"
        else:
            vgal.status = "deactive"
        vgal.user_id = UserBase(request.user.id)
        vgal.save()
        messages.success(request, "Video Gallery Updated")
        return redirect("videogal")
    return render(request, "dashboard/editvgallery.html", {'vgal': vgal})


@login_required(login_url='sign-in')
def editservice(request, id):
    serv = Service.objects.get(id=id)
    if request.method == "POST":
        sname = request.POST.get("sname")
        sdetails = request.POST.get("sdetails")
        status = request.POST.get("status")
        try:
            simg = request.FILES.get("simg")
            if simg is not None:
                serv.service_img = simg
        except Exception as e:
            print(e)
        serv.service_name = sname
        serv.service_desc = sdetails
        if status == "on":
            serv.status = "active"
        else:
            serv.status = "deactive"
        serv.user_id = UserBase(request.user.id)
        serv.save()
        messages.success(request, "Service Updated")
        return redirect("services")
    return render(request, "dashboard/editservice.html", {'serv': serv})


def signIn(request):
    if request.method == "POST":
        uname = request.POST['username']
        upass = request.POST['password']
        user = authenticate(username=uname, password=upass)
        if user is not None:
            if user.is_superuser != True:
                login(request, user)
                request.session.set_expiry(0)
                messages.success(request, "Login Successfull!")
                return redirect("dashboard")
            else:
                messages.warning(request, "Invalid Username And Password!!")
                return redirect("sign-in")
        else:
            messages.warning(request, "Invalid Username And Password!!")
            redirect("sign-in")
    else:
        if request.user.is_authenticated:
            return redirect("dashboard")
    return render(request, "auth/login.html")


@login_required(login_url='sign-in')
def logout_user(request):
    logout(request)
    messages.success(request, "Logout Successfull!!")
    return redirect("sign-in")


@login_required(login_url='sign-in')
def delprod(request, id):
    prod = Product.objects.get(id=id)
    prod.delete()
    messages.success(request, "Product Removed")
    return redirect("product")

@login_required(login_url='sign-in')
def deltest(request, id):
    test = Testimonial.objects.get(id=id)
    test.delete()
    messages.success(request, "Testimonial Removed")
    return redirect("testimonial")

@login_required(login_url='sign-in')
def delserv(request, id):
    serv = Service.objects.get(id=id)
    serv.delete()
    messages.success(request, "Service Removed")
    return redirect("services")


@login_required(login_url='sign-in')
def delgal(request, id):
    gal = Gallery.objects.get(id=id)
    gal.delete()
    messages.success(request, "Image Removed")
    return redirect("gallery")


@login_required(login_url='sign-in')
def delvgal(request, id):
    vgal = Vgallery.objects.get(id=id)
    vgal.delete()
    messages.success(request, "Video Removed")
    return redirect("videogal")

# @login_required(login_url='sign-in')
# def delfeed(request, id):
#     feed = Feedback.objects.get(id=id)
#     feed.delete()
#     messages.success(request, "Feedback Removed")
#     return redirect("feedback")




def page_not_found_view(request, exception):
    return render(request, 'dashboard/error-404.html', status=404)


def server_error(request, *args, **argv):
    return render(request, "dashboard/error-500.html", status=500)

@login_required(login_url='sign-in')
def gallery(request):
    gallery = Gallery.objects.all()
    return render(request, "dashboard/photogallery.html", {'gallery': gallery})

@login_required(login_url='sign-in')
def vgallery(request):
    vgallery = Vgallery.objects.all()
    return render(request, "dashboard/videogallery.html", {'vgallery': vgallery})
# def sendmsg(request):
#     # syntax: phone number with country code, message, hour and minutes
#     pywhatkit.sendwhatmsg('+918182572762', 'Message 1')


def maincard(request, username):
    # try:
        user = User.objects.get(username=username)
        userdata = UserBase.objects.get(user_id=user.id)
        prod = Product.objects.filter(user_id=user.id, status="Active")
        gal = Gallery.objects.filter(user_id=user.id, status="Active")
        vgal = Vgallery.objects.filter(user_id=user.id, status="Active")
        test = Testimonial.objects.filter(user_id=user.id)
        serv = Service.objects.filter(user_id=user.id, status="Active")
        for data in vars(userdata).items():
            print(data)
        print(prod)
        print(gal)
        print(vgal)
        print(test)
        print(serv)
        # return render(request, "dashboard/card.html", {'userdata': userdata, 'gal': gal, 'vgal': vgal, 'prod': prod, 'feed': feed, 'serv': serv})
        directory=os.path.join(settings.BASE_DIR,'cards/templates/Cards_Users/{}'.format(userdata.user_id.username))
        data=open("{}.html".format(directory),"w")
        data.write(str(render(request, "dashboard/card.html", {'userdata': userdata, 'gal': gal, 'vgal': vgal, 'prod': prod, 'test': test, 'serv': serv}).content.decode("utf-8")))
        data.close()
        return render(request,f"Cards_Users/{userdata.user_id.username}.html")
        
    # except Exception as e:
    #     print(e)
    #     return render(request, 'dashboard/error-404.html', status=404)
