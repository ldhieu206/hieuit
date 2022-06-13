from sys import maxsize
from tkinter.tix import MAX
from django.db import models
from datetime import datetime
# Create your models here.
from django.db import models

# Create your models here.

class HocVien(models.Model):
    maHV = models.CharField(max_length=50,primary_key=True)
    name = models.CharField(max_length=50)
    ngaySinh = models.DateField(null=True,blank=True)
    gioiTinh = models.CharField(max_length=50, choices=[(
        'Nam', 'Nam'), ('Nữ', 'Nữ'), ('Khác', 'Khác')], default='Nam')
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    diaChi = models.CharField(max_length=255)
    password = models.CharField(max_length=50)
    ghiChu = models.TextField(blank=True, null=True)
    duPhong2 = models.CharField(max_length=50,null=True, blank=True)
    duPhong3 = models.CharField(max_length=50,null=True, blank=True)
    duPhong4 = models.CharField(max_length=50,null=True, blank=True)

    def __str__(self):
        return self.maHV


class GiaoVien(models.Model):
    maGV = models.CharField(max_length=50,primary_key=True)
    tenGV = models.CharField(max_length=50)
    gioiTinh = models.CharField(max_length=50,choices=[('Nam', 'Nam'), ('Nữ', 'Nữ'), ('Khác', 'Khác')], default='Nam')
    ngaySinh = models.DateField()
    sdt = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50,null=True)
    luongNgay = models.IntegerField()
    duPhong2 = models.CharField(max_length=50,null=True,blank=True)
    duPhong3 = models.CharField(max_length=50,null=True, blank=True)
    duPhong4 = models.CharField(max_length=50,null=True, blank=True)
    quyen = models.CharField(max_length=50,null=True, blank=True)

    def __str__(self):
        return self.maGV

class LopHoc(models.Model):
    maLop = models.CharField(max_length=50,primary_key=True)
    tenLop = models.CharField(max_length=50)
    # ngayHoc = models.ManyToManyField('NgayHoc',blank=True,null=True)
    # caHoc_id = models.ManyToManyField('CaHoc',blank=True,null=True)
    lichHoc = models.CharField(max_length=255, blank=True, null=True)
    hocPhi_ca = models.IntegerField()
    giaoVien_id = models.ForeignKey(GiaoVien, on_delete=models.SET_NULL, null=True)
    luongGV_ca = models.IntegerField()
    hocPhi_dot = models.IntegerField()
    luong_dot = models.IntegerField(default=0)

    ngayHoc = models.CharField(max_length=255, blank=True, null=True)
    ngayHoc = "t2,t3"

    traTheoKhoa = models.BooleanField(default=False)
    ngayBatDau = models.DateField(null=True,blank=True)
    ngayKetThuc = models.DateField(null=True,blank=True)
    soLuongHocVien = models.IntegerField(null=True,default=0)
    soLuongHocVienMax = models.IntegerField(null=True)
    duPhong1 = models.CharField(max_length=50,null=True,blank=True)
    duPhong2 = models.CharField(max_length=50,null=True, blank=True)

    def __str__(self):
        return str(self.maLop)

class CaHoc(models.Model):
    gioBatDau = models.TimeField()
    gioKetThuc = models.TimeField()
    ca = models.CharField(max_length=2)
    ghiChu = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.ca

class HOCVIEN_buoihoc(models.Model):
    hocVien_id = models.ForeignKey(HocVien, on_delete=models.SET_NULL, null=True)
    lopHoc_id = models.ForeignKey(LopHoc, on_delete=models.SET_NULL, null=True)
    diemDanhHV = models.BooleanField()
    ngay = models.DateField(blank=True,null=True)
    dongTien = models.BooleanField(default=False)
    ghiChu = models.TextField(blank=True)

    def __str__(self):
        return str(self.hocVien_id)

class HocVien_LopHoc(models.Model):
    lopHoc_id = models.ForeignKey(LopHoc, on_delete=models.SET_NULL, null=True)
    hocVien_id = models.ForeignKey(HocVien, on_delete=models.SET_NULL, null=True)
    hocPhiGiam = models.IntegerField(null=True,default=0,blank=True)
    ghiChu = models.TextField(null=True,blank=True)

    def __str__(self):
        return str(self.hocVien_id)

class GIAOVIEN_buoihoc(models.Model):
    caHoc_id = models.ForeignKey(CaHoc, on_delete=models.SET_NULL, null=True)
    giaoVien_id = models.ForeignKey(GiaoVien, on_delete=models.SET_NULL, null=True)
    lopHoc_id = models.ForeignKey(LopHoc, on_delete=models.SET_NULL, null=True)
    diemDanhGV = models.BooleanField()
    ngay = models.DateField()
    traLuong = models.CharField(max_length=50)
    ghiChu = models.TextField(blank=True)

    def __str__(self):
        return str(self.giaoVien_id)


class PhuHuynh(models.Model):
    maPH = models.CharField(max_length=50,primary_key=True)
    hocVien_id = models.ForeignKey(HocVien, on_delete=models.SET_NULL, null=True)
    tenPH = models.CharField(max_length=50)
    gioiTinh = models.CharField(max_length=50,choices=[('nam', 'Nam'), ('nu', 'Nữ'), ('khac', 'Khác')], default='khac')
    ngaySinh = models.DateField(null=True, blank=True)
    sdt1 = models.CharField(max_length=50)
    sdt2 = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    soZalo = models.CharField(max_length=50)
    duPhong2 = models.CharField(max_length=50,blank=True) 
    duPhong3 = models.CharField(max_length=50,blank=True)
    duPhong4 = models.CharField(max_length=50,blank=True)

    def __str__(self):
        return self.maPH


class HocPhi_HocVien(models.Model):
    phuHuynh_id = models.ForeignKey(PhuHuynh, on_delete=models.SET_NULL, null=True)
    hocVien_id = models.ForeignKey(HocVien, on_delete=models.SET_NULL, null=True)
    ngay = models.DateField()
    soTienDong = models.IntegerField(default=0)
    soChuaThanhToan = models.IntegerField(null=True)
    ghiChu = models.TextField(blank=True)

    def __str__(self):
        return str(self.phuHuynh_id)
    

class LuongGV(models.Model):
    giaoVien_id = models.ForeignKey(GiaoVien, on_delete=models.SET_NULL, null=True)
    ngay = models.DateField()
    soTienNhan = models.IntegerField()
    ghiChu = models.TextField(blank=True)

    def __str__(self):
        return str(self.giaoVien_id)
class KhoaHoc(models.Model):
    maKH = models.CharField(max_length=50,primary_key=True)
    tenKH = models.CharField(max_length=50)
    moTa = models.CharField(max_length=50)
    img = models.ImageField(upload_to='images/', null=True, blank=True)
    ghiChu = models.TextField(blank=True)

    def __str__(self):
        return self.maKH
class KhoanKhac(models.Model):
    maKK = models.CharField(max_length=50,primary_key=True)
    soTienChi = models.IntegerField()
    ngay = models.DateField()
    noiDungChi = models.CharField(max_length=255)
    soTienThu = models.IntegerField()
    noiDungThu = models.CharField(max_length=255)

    def __str__(self):
        return self.maKK

class Front_end(models.Model):
    slogan = models.CharField(max_length=255)
    slider = models.ImageField(upload_to='images/', null=True, blank=True)
    video = models.FileField(upload_to='videos/', null=True, blank=True)
    logo = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.slogan

# class Ngay_Lop_Hoc(models.Model):
#     ngay = models.CharField(max_length=255,choices=[('Thứ 2', 'Thứ 2'),('Thứ 3', 'Thứ 3'),('Thứ4', 'Thứ 4'),('Thứ 5', 'Thứ 5'),('Thứ 6', 'Thứ 6'),('Thứ 7', 'Thứ 7'),('Chử Nhật','Chử Nhật')], default='Chủ Nhật')
#     lopHoc_id = models.ManyToManyField(LopHoc)

#     def __str__(self):
#         return self.ngay
# class NgayHoc(models.Model):
#     ngay = models.CharField(max_length=255,choices=[('Thứ 2', 'Thứ 2'),('Thứ 3', 'Thứ 3'),('Thứ4', 'Thứ 4'),('Thứ 5', 'Thứ 5'),('Thứ 6', 'Thứ 6'),('Thứ 7', 'Thứ 7'),('Chử Nhật','Chử Nhật')], default='Chủ Nhật')

#     def __str__(self):
#         return self.ngay

# class NgayLopHoc(models.Model):
#     ngayHoc = models.ManyToManyField(NgayHoc)
#     lopHoc_id = models.ForeignKey(LopHoc, on_delete=models.SET_NULL, null=True)

#     def __str__(self):
#         return self.ngayHoc
#     def get_NgayHoc(self):
#         return "\n".join([p.ngay for p in self.ngayHoc.all()])

class NgayHoc(models.Model):
    ngay = models.CharField(max_length=255,choices=[('Thứ 2', 'Thứ 2'),('Thứ 3', 'Thứ 3'),('Thứ4', 'Thứ 4'),('Thứ 5', 'Thứ 5'),('Thứ 6', 'Thứ 6'),('Thứ 7', 'Thứ 7'),('Chủ Nhật','Chủ Nhật')], default='Chủ Nhật')
    def __str__(self):
        return self.ngay
