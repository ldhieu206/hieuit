from django.shortcuts import render

# Create your views here.
from mailer import Mailer
from django.shortcuts import render
import datetime
# Create your views here.
from unicodedata import name
from django.shortcuts import render
from django.http.response import *
from django.http import *
from django.shortcuts import redirect
from .models import *
import hashlib
from datetime import date
# Create your views here.

def indexAdmin(request):
    return render(request, 'home/admin/indexAdmin.html')

def index(request):
    return render(request, 'home/index.html')


def indexGV(request):
    try:
        maGV = request.session['giaoVien']
        giaoVien = GiaoVien.objects.get(maGV=maGV)
    except KeyError:
        return redirect('/loginGV')
    return render(request, 'home/giaoVien/indexGV.html')


def indexHV(request):
    try:
        maHV = request.session['hocVien']
        hocVien = HocVien.objects.get(maHV=maHV)
    except KeyError:
        return redirect('/login')
    return render(request, 'home/hocVien/indexHV.html')


def login(request):
    try:
        maHV = request.session['hocVien']
        return redirect('/indexHV')
    except KeyError:
        pass
    if request.method == 'POST':
        maHV = request.POST['maHV']
        password = request.POST['password']
        try:
            hocVien = HocVien.objects.get(maHV=maHV, password=password)
            request.session['hocVien'] = hocVien.maHV
            return redirect('/indexHV')
        except HocVien.DoesNotExist:
            return render(request, 'home/hocVien/login.html', {'result': 'incorrect', 'maHV': maHV})
    return render(request, 'home/hocVien/login.html', {'result': None})


def loginGV(request):
    try:
        maGV = request.session['giaoVien']
        return redirect('/indexGV')
    except KeyError:
        pass
    if request.method == 'POST':
        maGV = request.POST['maGV']
        password = request.POST['password']
        try:
            giaoVien = GiaoVien.objects.get(maGV=maGV, password=password)
            request.session['giaoVien'] = giaoVien.maGV
            return redirect('/indexGV')
        except GiaoVien.DoesNotExist:
            return render(request, 'home/giaoVien/loginGV.html', {'result': 'incorrect', 'maGV': maGV})
    return render(request, 'home/giaoVien/loginGV.html', {'result': None})


def logout(request):
    try:
        del request.session['hocVien']
    except KeyError:
        pass
    return redirect('/')


def logoutGV(request):
    try:
        del request.session['giaoVien']
    except KeyError:
        pass
    return redirect('/')



def account(request):
    try:
        maHV = request.session['hocVien']
        hocVien = HocVien.objects.get(maHV=maHV)
    except KeyError:
        return redirect('/login')
    lopHocs = [x.lopHoc_id for x in HocVien_LopHoc.objects.filter(
        hocVien_id=hocVien.maHV)]
    phuHuynhs = PhuHuynh.objects.filter(hocVien_id=hocVien.maHV)
    hocPhis =  HocPhi_HocVien.objects.filter(hocVien_id= hocVien.maHV)
    data = {
        'hocVien': hocVien,
        'lopHocs': lopHocs,
        'phuHuynhs': phuHuynhs,
        'hocPhis': hocPhis,
    }
    return render(request, 'home/hocVien/account.html', data)




def accountGV(request):
    try:
        maGV = request.session['giaoVien']
        giaoVien = GiaoVien.objects.get(maGV=maGV)
    except KeyError:
        return redirect('/loginGV')
    lopHocs = LopHoc.objects.filter(giaoVien_id=giaoVien.maGV)
    luongGVs = LuongGV.objects.filter(giaoVien_id=giaoVien.maGV)
    data = {
        'giaoVien': giaoVien,
        'lopHocs': lopHocs,
        'luongGVs': luongGVs
    }
    return render(request, 'home/giaoVien/accountGV.html', data)

def lopHocPhuTrach(request):
    try:
        maGV = request.session['giaoVien']
        giaoVien = GiaoVien.objects.get(maGV=maGV)
    except KeyError:
        return redirect('/loginGV')
    lopHocs = LopHoc.objects.filter(giaoVien_id=maGV)
    data = {
        'giaoVien': giaoVien,
        'lopHocs': lopHocs
    }
    return render(request, 'home/giaoVien/lopHocPhuTrach.html', data)

def luongGV(request):
    try:
        maGV = request.session['giaoVien']
        giaoVien = GiaoVien.objects.get(maGV=maGV)
    except KeyError:
        return redirect('/loginGV')
    luongGVs = LuongGV.objects.filter(giaoVien_id=maGV)
    data = {
        'giaoVien': giaoVien,
        'luongGVs': luongGVs
    }
    return render(request, 'home/giaoVien/luongGV.html', data)

def dsGiaoVien(request):
    Data = {'dsGiaoViens': GiaoVien.objects.all()}
    return render(request, 'home/giaoVien/dsGiaoVien.html', Data)


def dsHocVien(request):
    Data = {'dsHocViens': HocVien.objects.all()}
    return render(request, 'home/giaoVien/dsHocVien.html', Data)

def dsHocVienAdmin(request):
    Data = {'dsHocViens': HocVien.objects.all()}
    return render(request, 'home/admin/dsHocVien.html', Data)

def dsPhuHuynh(request):
    Data = {'dsPhuHuynhs': PhuHuynh.objects.all()}
    return render(request, 'home/admin/dsPhuHuynh.html', Data)


def dsLopHocHV(request):
    Data = {'dsLopHoc': LopHoc.objects.all().order_by('maLop')}
    return render(request, 'home/hocVien/dsLopHocHV.html', Data)

def dsLopHoc(request):
    Data = {'dsLopHocs': LopHoc.objects.all().order_by('maLop')}
    return render(request, 'home/giaoVien/dsLopHoc.html', Data)

def dsLopHocAdmin(request):
    Data = {'dsLopHocs': LopHoc.objects.all().order_by('maLop')}
    return render(request, 'home/admin/dsLopHoc.html', Data)

def dsKhoaHoc(request):
    Data = {'dsKhoaHocs': KhoaHoc.objects.all().order_by('maKH')}
    return render(request, 'home/admin/dsKhoaHoc.html', Data)

def dsHocVienLop(request, lopHoc_id):
    Data = {
        'dsHocVienLops': HocVien_LopHoc.objects.filter(
        lopHoc_id=lopHoc_id),
        'list_lophoc': LopHoc.objects.all()
        }
    return render(request, 'home/giaoVien/dsHocVienLop.html', Data)

def dsHocVienLopAdmin(request, lopHoc_id):
    Data = {
        'dsHocVienLops': HocVien_LopHoc.objects.filter(
        lopHoc_id=lopHoc_id),
        'list_lophoc': LopHoc.objects.all()
        }
    return render(request, 'home/admin/dsHocVienLop.html', Data)

def hienThiThongTinLopHoc(request, maLop):
    try:
        maHV = request.session['hocVien']
        hocVien = HocVien.objects.get(maHV=maHV)
    except KeyError:
        return redirect('/login')
    Data = {'hienThiThongTinLopHocs': LopHoc.objects.filter(maLop=maLop)}
    return render(request, 'home/hocVien/hienThiThongTinLopHoc.html', Data)



def hienThiThongTinPhuHuynh(request, hocVien_id):
    hocPhi = HocPhi_HocVien.objects.filter(hocVien_id=hocVien_id)
    phuHuynh = PhuHuynh.objects.filter(hocVien_id=hocVien_id)
    data = {
        'hocPhi': hocPhi,
        'phuHuynh': phuHuynh
    }
    return render(request, 'home/giaoVien/hienThiThongTinPhuHuynh.html', data)


def dsHocVienLopHoc(request):
    try:
        maHV = request.session['hocVien']
        hocVien = HocVien.objects.get(maHV=maHV)
    except KeyError:
        return redirect('/login')
    Data = {
        'dsHocVienLopHocs': LopHoc.objects.filter(
        dsHocVien=hocVien),
        'list_lophoc': LopHoc.objects.all()
        }
    return render(request, 'home/dsLopHocHocVien.html', Data)


def dsHocVienBuoiHocs(request):
    try:
        maHV = request.session['hocVien']
        hocVien = HocVien.objects.get(maHV=maHV)
    except KeyError:
        return redirect('/login')
    Data = {'dsHocVienBuoiHocs': HOCVIEN_buoihoc.objects.filter(
        dsHocVien=hocVien)}
    return render(request, 'home/giaoVien/dsHocVienBuoiHocs.html', Data)



def hienThiThongTinGV(request, maGV):
    try:
        maGV = request.session['giaoVien']
        giaoVien = GiaoVien.objects.get(maGV=maGV)
    except KeyError:
        return redirect('/loginGV')
    Data = {'hienThiThongTinGV': GiaoVien.objects.filter(maGV=maGV)}
    return render(request, 'home/hocVien/hienThiThongTinGV.html', Data)


# jsonresponse
from django.http import JsonResponse
def send_email(request):
    if request.method == 'POST':
        maHV = request.POST['maHV']
        hocVien = HocVien.objects.get(maHV=maHV)
        phuHuynh = PhuHuynh.objects.get(hocVien_id=maHV)
        hocPhi = HocPhi_HocVien.objects.get(hocVien_id=maHV,phuHuynh_id=phuHuynh.maPH)

        receiver = phuHuynh.email
        sender = 'lehieu206201@gmail.com'
        password = 'usposcbumclsqebo'
        sender_name = 'ECenter'
        subject = 'Thông Báo Của ECenter'
        message = f"""
        <html>
            <head></head>
            <body style="font-size: 16px">
                <p>Học Viên: <b>{hocVien.name}</b>.</p>
                <p>Phụ Huynh: <b>{phuHuynh.tenPH}</b>.</p>
                <p>Học Phí: <b>{hocPhi.soTienDong}</b>.</p>
                <p>Ngày Đóng: <b>{hocPhi.ngay}</b>.</p>
                <p>Số Tiền Còn Phải Đóng: <b>{hocPhi.soChuaThanhToan}</b>.</p>
                <br>
            </body>
        </html>
        """

        mail = Mailer(email=sender, password=password)
        mail.settings(provider=mail.GMAIL)
        mail.send(sender_name=sender_name, receiver=receiver,
                subject=subject, message=message)
        return JsonResponse({
            "success": True,
            "message": "Email đã được gửi"
        })
        pass
    else:
        return JsonResponse({
            'success': False,
            'message': 'Method not allowed'
        })
def dangKyHoc(request):
    try:
        maHV = request.session['hocVien']
        hocVien = HocVien.objects.get(maHV=maHV)
    except KeyError:
        pass
    dsLopHoc = [x.lopHoc_id for x in HocVien_LopHoc.objects.filter(hocVien_id=hocVien)]
    phuHuynh_id = PhuHuynh.objects.get(hocVien_id=maHV)
    if request.method == 'POST':
        lopHoc_id = request.POST['maLop']
        lopHoc_id = LopHoc.objects.get(maLop=lopHoc_id)
        hocVien_id = HocVien.objects.get(maHV= maHV)
        ngay = datetime.now()
        dsLH = LopHoc.objects.filter(maLop = lopHoc_id)
        print(dsLH,"############")
        for x in dsLH:
            for y in x.lichHoc.split(','):
                for lopHoc in dsLopHoc:
                    for lh in lopHoc.lichHoc.split(','):
                        if y == lh:
                            return JsonResponse({
                                "success": False,
                                "message": "Lịch học trùng với lịch học của lớp học khác"
                            })
        try:
            if HocVien_LopHoc.objects.get(hocVien_id=hocVien_id, lopHoc_id=lopHoc_id):
                return JsonResponse({
                    "success": False,
                    "message": "Đã đăng ký lớp này rồi."
                }) 
            
        except HocVien_LopHoc.DoesNotExist:
            if lopHoc_id.soLuongHocVien >= lopHoc_id.soLuongHocVienMax:
                return JsonResponse({
                    "success": False,
                    "message": "Lớp đã đầy."
                })
            
            HocVien_LopHoc.objects.create(hocVien_id=hocVien_id, lopHoc_id=lopHoc_id)
            HocPhi_HocVien.objects.create(hocVien_id=hocVien_id, phuHuynh_id=phuHuynh_id,soChuaThanhToan=lopHoc_id.hocPhi_dot,ngay = ngay)
            lopHoc_id.soLuongHocVien += 1
            lopHoc_id.save()
            return JsonResponse({
                "success": True,
                "message": "Đăng ký thành công"
            })


def diemDanh(request):
    try:
        maGV = request.session['giaoVien']
        giaoVien = GiaoVien.objects.get(maGV=maGV)
    except KeyError:
        pass
    if request.method == 'POST':
        lopHoc_id = request.POST['lopHoc_id']
        lopHoc_id = LopHoc.objects.get(maLop=lopHoc_id)
        hocVien_id = request.POST['hocVien_id']
        hocVien_id = HocVien.objects.get(maHV=hocVien_id)
        print(hocVien_id)
        dongTien = True if request.POST['dongTien'] == 'true' else False
        ngay = datetime.now()
        try:
            HOCVIEN_buoihoc.objects.create( lopHoc_id=lopHoc_id,hocVien_id=hocVien_id,ngay= ngay,dongTien = dongTien, diemDanhHV=True)
            return JsonResponse({
                "success": True,
                "message": "Điểm danh thành công"
            })
        except HOCVIEN_buoihoc.DoesNotExist:
            return JsonResponse({
                "success": False,
                "message": "Điểm danh không thành công"
            })
    return JsonResponse({
        "success": False,
        "message": "Điểm danh không thành công"
    })

def searchDD(request):
    try:
        maGV = request.session['giaoVien']
        giaoVien = GiaoVien.objects.get(maGV=maGV)
    except KeyError:
        pass
    if request.method == 'POST':
        lopHoc_id = request.POST['lopHoc_id']
        ngay = request.POST['ngay']
    data = {
        'dsLopHoc':LopHoc.objects.all(),
        'dsDaDD':HOCVIEN_buoihoc.objects.filter(lopHoc_id = lopHoc_id,ngay = ngay)
    }
    return render(request, 'home/giaoVien/dsDaDD.html', data)


import xlwt
def export_excel(request):
    try:
        maGV = request.session['giaoVien']
        giaoVien = GiaoVien.objects.get(maGV=maGV)
    except KeyError:
        pass
    if request.method == 'POST':
        lopHoc_id = request.POST['lopHoc_id']
        ngay = request.POST['ngay']
        hvbh = HOCVIEN_buoihoc.objects.get(lopHoc_id = lopHoc_id,ngay = ngay)
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=HocVienBuoiHoc' +\
        str(datetime.now().date()) + '.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('HocVienBuoiHoc')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['Mã Lớp','Mã Học Viên','Đóng Tiền','Điểm Danh']
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    font_style = xlwt.XFStyle()
    rows = HOCVIEN_buoihoc.objects.all().values_list('lopHoc_id','hocVien_id','dongTien','diemDanhHV')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)
    wb.save(response)
    return response



def addLopHoc(request):
    data = {
        'dsLopHoc':LopHoc.objects.all(),
        'dsCaHoc':CaHoc.objects.all(),
        'dsNgayHoc':NgayHoc.objects.all(),
        'dsGiaoVien':GiaoVien.objects.all(),
        'range56':list(range(56)),
        'range7':list(range(7)),
        'range8':list(range(1,9)),
    }
    if request.method == 'POST':
        dslh = request.POST['dslh']
        maLop = request.POST['maLop']
        tenLop = request.POST['tenLop']
        giaoVien_id = request.POST['giaoVien_id']
        hocPhi_ca = request.POST['hocPhi_ca']
        ngayBatDau = request.POST['ngayBatDau']
        ngayKetThuc = request.POST['ngayKetThuc']
        traTheoKhoa = True if request.POST['traTheoKhoa'] == 'true' else False
        soLuongHocVienMax = request.POST['soLuongHocVienMax']
        hocPhi_dot = request.POST['hocPhi_dot']
        luongGV_ca = request.POST['luongGV_ca']
        gv = GiaoVien.objects.get(maGV=giaoVien_id)
        # dsLopHoc = LopHoc.objects.filter(giaoVien_id=giaoVien_id)
        dsLH = LopHoc.objects.filter(giaoVien_id=gv)

        try:

            lh = []
            for x in dslh.split(','):
                lh.append(int(x))
            for ds in dsLH:
                for d in ds.lichHoc.split(','):
                    if int(d) in lh:
                        return JsonResponse({
                            "success": False,
                            "message": "Giáo viên trùng lịch dạy!"
                        })
                        
            LopHoc.objects.get(maLop=maLop)
            return JsonResponse({
                "success": False,
                "message": "Lớp đã tồn tại"
            })
        except LopHoc.DoesNotExist:
            if ngayBatDau > ngayKetThuc:
                return JsonResponse({
                    "success": False,
                    "message": "Ngày bắt đầu phải trước ngày kết thúc"
                })
            
            LopHoc.objects.create(
                maLop=maLop,
                tenLop=tenLop,
                giaoVien_id=gv,
                hocPhi_ca=hocPhi_ca,
                ngayBatDau=ngayBatDau,
                ngayKetThuc=ngayKetThuc,
                traTheoKhoa=traTheoKhoa,
                soLuongHocVienMax=soLuongHocVienMax,
                hocPhi_dot=hocPhi_dot,
                luongGV_ca=luongGV_ca,
                lichHoc = str(dslh)
            )

            return JsonResponse({
                "success": True,
                "message": "Thêm lớp thành công"
            })
    return render(request, 'home/admin/addLopHoc.html',data)

def addCaHoc(request):
    if request.method == 'POST':
        gioBatDau = request.POST['gioBatDau']
        gioKetThuc = request.POST['gioKetThuc']
        ca = request.POST['ca']
        ghiChu = request.POST['ghiChu']
        try:
            CaHoc.objects.get(ca=ca)
            return JsonResponse({
                "success": False,
                "message": "Ca học đã tồn tại"
            })
        except CaHoc.DoesNotExist:
            CaHoc.objects.create(gioBatDau=gioBatDau, gioKetThuc=gioKetThuc, ca=ca, ghiChu=ghiChu)
            return JsonResponse({
                "success": True,
                "message": "Thêm ca học thành công",
            })
    return render(request, 'home/admin/addCaHoc.html')


def addHocVien(request):
    if request.method == 'POST':
        maHV = request.POST['maHV']
        name = request.POST['name']
        gioiTinh = request.POST['gioiTinh']
        ngaySinh = request.POST['ngaySinh']
        phone = request.POST['phone']
        email = request.POST['email']
        diaChi = request.POST['diaChi']
        password = request.POST['password']
        try:
            HocVien.objects.get(maHV=maHV)
            return JsonResponse({
                "success": False,
                "message": "Học viên đã tồn tại"
            })
        except HocVien.DoesNotExist:
            HocVien.objects.create(maHV=maHV, name=name, gioiTinh=gioiTinh, ngaySinh=ngaySinh, phone=phone, email=email, diaChi=diaChi, password=password)
            return JsonResponse({
                "success": True,
                "message": "Thêm học viên thành công",
            })
    return render(request, 'home/admin/addHocVien.html')

def addPhuHuynh(request):
    data = {
        'dsHocVien':HocVien.objects.all(),
    }
    if request.method == 'POST':
        maPH = request.POST['maPH']
        tenPH = request.POST['tenPH']
        hocVien_id = request.POST['hocVien_id']
        print(hocVien_id,"###################")
        mahv = HocVien.objects.get(maHV= hocVien_id)
        gioiTinh = request.POST['gioiTinh']
        ngaySinh = request.POST['ngaySinh']
        sdt1 = request.POST['sdt1']
        email = request.POST['email']
        soZalo = request.POST['soZalo']
        try:
            PhuHuynh.objects.get(maPH=maPH)
            return JsonResponse({
                "success": False,
                "message": "Phụ huynh đã tồn tại"
            })
        except PhuHuynh.DoesNotExist:
            PhuHuynh.objects.create(maPH=maPH, tenPH=tenPH, hocVien_id=mahv, gioiTinh=gioiTinh, ngaySinh=ngaySinh, sdt1=sdt1, email=email,soZalo = soZalo)
            return JsonResponse({
                "success": True,
                "message": "Thêm phụ huynh thành công",
            })
    return render(request, 'home/admin/addPhuHuynh.html',data)

def addGiaoVien(request):
    if request.method == 'POST':
        maGV = request.POST['maGV']
        tenGV = request.POST['tenGV']
        gioiTinh = request.POST['gioiTinh']
        ngaySinh = request.POST['ngaySinh']
        sdt = request.POST['sdt']
        email = request.POST['email']
        password = request.POST['password']
        luongNgay = request.POST['luongNgay']
        try:
            GiaoVien.objects.get(maGV=maGV)
            return JsonResponse({
                "success": False,
                "message": "Giáo viên đã tồn tại"
            })
        except GiaoVien.DoesNotExist:
            GiaoVien.objects.create(maGV=maGV, tenGV=tenGV, gioiTinh=gioiTinh, ngaySinh=ngaySinh, sdt=sdt, email=email, password=password, luongNgay=luongNgay)
            return JsonResponse({
                "success": True,
                "message": "Thêm giáo viên thành công",
            })
    return render(request, 'home/admin/addGiaoVien.html')

def editCaHoc(request):
    data = {
        'dsCaHoc':CaHoc.objects.all(),
    }
    if request.method == 'POST':
        gioBatDau = request.POST['gioBatDau']
        gioKetThuc = request.POST['gioKetThuc']
        ca = request.POST['ca']
        ghiChu = request.POST['ghiChu']
        caHoc = CaHoc.objects.get(ca=ca)
        try:
            CaHoc.objects.get(gioBatDau=gioBatDau, gioKetThuc=gioKetThuc)
            return JsonResponse({
                "success": False,
                "message": "Ca học không có gì thay đổi"
            })
        except CaHoc.DoesNotExist:
            caHoc.gioBatDau = gioBatDau
            caHoc.gioKetThuc = gioKetThuc
            caHoc.ghiChu = ghiChu
            caHoc.save()

    return render(request, 'home/admin/editCaHoc.html',data)

import json

def lichHoc(request):
    try:
        maHV = request.session['hocVien']
        hocVien = HocVien.objects.get(maHV=maHV)
    except:
        return redirect('/')
    dsLopHoc = [x.lopHoc_id for x in HocVien_LopHoc.objects.filter(hocVien_id=hocVien)]
    dslh = {}
    for lopHoc in dsLopHoc:
        for lh in lopHoc.lichHoc.split(','):
            dslh[int(lh)] = lopHoc.maLop
    
    data = {
        'dsLopHoc': dsLopHoc,
        'dslh':dslh.items(),
        'range7':list(range(7)),
        'range8':list(range(1,9)),
        'range56':list(range(56)),
    }
    return render(request, 'home/hocVien/lichHoc.html',data)

def lichDay(request):
    try:
        maGV = request.session['giaoVien']
        giaoVien = GiaoVien.objects.get(maGV=maGV)
    except:
        return redirect('/')
    # dsLopHoc = [x.maLop for x in LopHoc.objects.filter(giaoVien_id=maGV)]
    dsLopHoc = LopHoc.objects.filter(giaoVien_id=maGV)
    print(dsLopHoc)
    dslh = {}
    for lopHoc in dsLopHoc:
        print(lopHoc.lichHoc)
        for lh in lopHoc.lichHoc.split(','):
            dslh[int(lh)] = lopHoc.maLop
    data = {
        'dsLopHoc': dsLopHoc,
        'dslh':dslh.items(),
        'range7':list(range(7)),
        'range8':list(range(1,9)),
        'range56':list(range(56)),
    }
    return render(request, 'home/giaoVien/lichDay.html',data)

def thongKe(request):
    hocPhiHV = HocPhi_HocVien.objects.all()
    luongGV = LuongGV.objects.all()
    chi = 0;
    thu= 0;
    for i in luongGV:
        chi += i.soTienNhan
    for k in hocPhiHV:
        thu += k.soTienDong
    data = {
        'hocPhiHV':hocPhiHV,
        'thu':thu,
        'chi':chi,
        'luongGV':luongGV,
    }
    return render(request, 'home/admin/thongKe.html',data)

import datetime as dt
from .resources import HocVienResource
from django.contrib import messages
from tablib import Dataset

def import_excel(request):              
    if request.method == 'POST' and request.FILES['myfile']:
        hocVien_resource = HocVienResource()
        dataset = Dataset()
        new_hocVien = request.FILES['myfile']

        if not new_hocVien.name.endswith('.xlsx'):
            messages.error(request, 'File không đúng định dạng')
            return redirect('home/admin/importexcel.html')
        imported_data = dataset.load(new_hocVien.read(),format='xlsx')
        for i in imported_data:
            value = HocVien(
                i[0],
                i[1],
                i[2],
                i[3],
                i[4],
                i[5],
                i[6],
                i[7],
            )
            value.save()
    return render(request, 'home/admin/importexcel.html')
