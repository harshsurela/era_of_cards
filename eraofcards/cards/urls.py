from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Customer URLS Goes Here...
    path("",views.home,name="home"),
    path("dashboard",views.dashboard,name="dashboard"),
    path("register",views.register,name="register"),
    path("accountsettings",views.accountsettings,name="accountsettings"),
    path("socialsettings",views.socialsettings,name="socialsettings"),
    path("changepass",views.changepass,name="changepass"),
    path("layouts",views.layouts,name="layouts"),
    path("features",views.features,name="features"),
    path("product",views.product,name="product"),
    path("gallery",views.gallery,name="gallery"),
    path("videogal",views.vgallery,name="videogal"),
    path("services",views.services,name="services"),
    # path("feedback",views.feedback,name="feedback"),
    path("mypackage",views.mypackage,name="mypackage"),
    path("payments",views.payments,name="payments"),
    # path("appointments",views.appointments,name="appointments"),
    path("testimonial/",views.testimonial ,name="testimonial"),
    path("country_ajax-data/",views.country_ajax_data,name="country_ajax-data"),
    path("state_ajax-data/",views.state_ajax_data,name="state_ajax-data"),
    path("addproduct",views.addproduct,name="addproduct"),
    path("addservice",views.addservice,name="addservice"),
    path("addgallery",views.addgallery,name="addgallery"),
    path("addvgallery",views.addvgallery,name="addvgallery"),
    path("addtest",views.addtest,name="addtest"),
    path("editproduct/<str:id>",views.editproduct,name="editproduct"),
    path("editservice/<str:id>",views.editservice,name="editservice"),
    path("editgallery/<str:id>",views.editgallery,name="editgallery"),
    path("editvgallery/<str:id>",views.editvgallery,name="editvgallery"),
    path("sign-in/",views.signIn,name="sign-in"),
    path("logout_user/",views.logout_user,name="logout_user"),
    path("delprod/<str:id>",views.delprod,name="delprod"),
    path("delserv/<str:id>",views.delserv,name="delserv"),
    path("delgal/<str:id>",views.delgal,name="delgal"),
    path("delvgal/<str:id>",views.delvgal,name="delvgal"),
    path("deltest/<str:id>",views.deltest,name="deltest"),
    path("password-reset/", auth_views.PasswordResetView.as_view(template_name="auth/forgot-password.html"),name="password_reset"),
    path("password-change/", auth_views.PasswordResetView.as_view(template_name="auth/change-password.html"),name="password_change"),
    path("password-reset/done/", auth_views.PasswordResetDoneView.as_view(template_name="auth/password-sent.html"),name="password_reset_done"),
    path("password-reset-confirm/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name="auth/changepassword.html"),name="password_reset_confirm"),
    path("reset_password_complete/", auth_views.PasswordResetCompleteView.as_view(template_name="auth/password-reset-done.html"),name="password_reset_complete"),

    path("<str:username>",views.maincard,name="maincard"),


]