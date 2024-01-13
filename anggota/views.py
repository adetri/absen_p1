# yourappname/views.py
from django.shortcuts import render, redirect
from .models import *
from django.http import JsonResponse


def index(request):
    return render(request, 'numpad.html', {})


def absen_page(request):
    context = {
        'variable1': 'Value 1',
        'variable2': 'Value 2',
        # Add more key-value pairs as needed
    }
    return render(request, 'absen.html', context)


def absen(request, pan):
    absen = Member.objects.get(pan_number=pan)

    context = {
        'variable1': 'Value 1',
        'variable2': 'Value 2',
        'data_member': absen,
        # Add more key-value pairs as needed
    }
    print(absen)
    return render(request, 'absen.html', context)


def absen2(request, pan):
    absen = Member.objects.get(pan_number=pan)

    context = {
        'nama': absen.name,
        'pan_num': absen.pan_number,


        # Add more key-value pairs as needed
    }
    # print(absen)
    return JsonResponse(context)


def absen3(request):
    member = Member.objects.get(pan_number=request.POST['pan'])
    aben = Absen(member=member, amal=request.POST['amal'])
    aben.save()
    context = {
        'msg': "absen berhasil",
        # 'pan_num': absen.pan_number,


        # Add more key-value pairs as needed
    }
    # print(absen)
    return JsonResponse(context)


def data_anggota(request):
    anggota = Member.objects.all()
    context = {
        'anggota': anggota
    }
    return render(request, 'anggota.html', context)


def tambah_anggota(request):

    if request.method == 'POST':

        print(request.POST)

        member = Member(name=request.POST['name'],
                        pan_number=request.POST['pan_number'])
        member.save()
        context = {
            "status req": 1,
        }
        return render(request, 'form_anggota.html', context)

    else:

        context = {
            "status req": 0,
        }

        return render(request, 'form_anggota.html', context)


def delete_anggota(request, pk):
    try:
        anggota = Member.objects.get(pk=pk)
        anggota.delete()

    except:
        pass

    return redirect('/anggota/')
