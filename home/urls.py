from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='home'),
    path('indexAdmin/', views.indexAdmin, name='homeAdmin'),
    path('indexHV/', views.indexHV, name='homeHV'),
    path('indexGV/', views.indexGV, name='homeGV'),
    path('loginAdmin/',auth_views.LoginView.as_view(template_name="home/admin/loginAdmin.html"), name="loginAdmin"),
    path('login/', views.login, name='login'),
    path('loginGV/', views.loginGV, name='loginGV'),
    path('logout/', views.logout, name='logout'),
    path('logoutGV/', views.logoutGV, name='logoutGV'),
    path('account/', views.account, name='account'),
    path('dsHocVien/', views.dsHocVien, name='dsHocVien'),
    path('dsHocVienAdmin/', views.dsHocVienAdmin, name='dsHocVienAdmin'),
    path('dsPhuHuynh/', views.dsPhuHuynh, name='dsPhuHuynh'),
    path('dsLopHoc/', views.dsLopHoc, name='dsLopHoc'),
    path('dsLopHocHV/', views.dsLopHocHV, name='dsLopHocHV'),
    path('dsHocVienLop/<str:lopHoc_id>/', views.dsHocVienLop, name='dsHocVienLop'),
    path('accountGV/', views.accountGV, name='accountGV'),
    path('dsKhoaHoc/', views.dsKhoaHoc, name='dsKhoaHoc'),
    path('hienThiThongTinGV/<str:maGV>/',views.hienThiThongTinGV, name='hienThiThongTinGV'),
    path('dangKyHoc',views.dangKyHoc, name='dangKyHoc'),
    path('send_email/',views.send_email, name='send_email'),
    path('hienThiThongTinPhuHuynh/<str:hocVien_id>/',views.hienThiThongTinPhuHuynh, name='hienThiThongTinPhuHuynh'),
    path('diemDanh/', views.diemDanh, name='diemDanh'),
    path('searchDD/', views.searchDD, name='searchDD'),
    path('export_excel/', views.export_excel, name='export_excel'),
    path('dsGiaoVien/', views.dsGiaoVien, name='dsGiaoVien'),
    path('dsLopHocAdmin/', views.dsLopHocAdmin, name='dsLopHocAdmin'),
    path('dsHocVienLopAdmin/<str:lopHoc_id>/', views.dsHocVienLopAdmin, name='dsHocVienLopAdmin'),
    path('addLopHoc/', views.addLopHoc, name='addLopHoc'),
    path('logout/',auth_views.LogoutView.as_view(next_page='/'),name='logoutAdmin'),
    path('addCaHoc/', views.addCaHoc, name='addCaHoc'),
    path('addHocVien/', views.addHocVien, name='addHocVien'),
    path('addPhuHuynh/', views.addPhuHuynh, name='addPhuHuynh'),
    path('addGiaoVien/', views.addGiaoVien, name='addGiaoVien'),
    path('editCaHoc/', views.editCaHoc, name='editCaHoc'),
    path('lichHoc/', views.lichHoc, name='lichHoc'),
    path('thongKe/', views.thongKe, name='thongKe'),
    path('import_excel/', views.import_excel, name='import_excel'),
    path('lichDay/', views.lichDay, name='lichDay'),
    path('lopHocPhuTrach/', views.lopHocPhuTrach, name='lopHocPhuTrach'),
    path('luongGV/', views.luongGV, name='luongGV'),
    path('dsKhoaHoc/', views.dsKhoaHoc, name='dsKhoaHoc')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
