from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import TodolistSerializer
from .models import Todolist

# GET Data
@api_view(['GET'])
def all_todolist(request):
    alltodolist = Todolist.objects.all() #ดึงข้อมูลจาก model Todolist
    serializer = TodolistSerializer(alltodolist,many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# POST Data (save data to database)
@api_view(['POST'])
def post_todolist(request):
    if request.method == 'POST':
        serializer = TodolistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)



@api_view(['PUT'])
def update_todolist(request,TID):
    # localhost:8000/api/update-todolist/13
    todo = Todolist.objects.get(id=TID)

    if request.method == 'PUT':
        data = {}
        serializer = TodolistSerializer(todo,data=request.data)
        if serializer.is_valid():
            serializer.save()
            data['status'] = 'updated'
            return Response(data=data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_todolist(request,TID):
    todo = Todolist.objects.get(id=TID)

    if request.method == 'DELETE':
        delete = todo.delete()
        data = {}
        if delete:
            data['status'] = 'deleted'
            statuscode = status.HTTP_200_OK
        else:
            data['status'] = 'failed'
            statuscode = status.HTTP_400_BAD_REQUEST

        return Response(data=data, status=statuscode)



data = [
    {
        "title":"Laptop คืออะไร?",
        "subtitle":"คอมพิวเตอร์ คือ อุปกรณ์ที่ใช้สำหรับการคำนวณและทำงานอื่นๆ?",
        "image_url":"https://raw.githubusercontent.com/UncleEngineer/BasicAPI/main/computer.jpg",
        "detail":"คอมพิวเตอร์ (อังกฤษ: computer) หรือศัพท์บัญญัติราชบัณฑิตยสภาว่า คณิตกรณ์[2][3] เป็นเครื่องจักรแบบสั่งการได้ที่ออกแบบมาเพื่อดำเนินการกับลำดับตัวดำเนินการทางตรรกศาสตร์หรือคณิตศาสตร์ โดยอนุกรมนี้อาจเปลี่ยนแปลงได้เมื่อพร้อม ส่งผลให้คอมพิวเตอร์สามารถแก้ปัญหาได้มากมาย\n\nคอมพิวเตอร์ถูกประดิษฐ์ออกมาให้ประกอบไปด้วยความจำรูปแบบต่าง ๆ เพื่อเก็บข้อมูล อย่างน้อยหนึ่งส่วนที่มีหน้าที่ดำเนินการคำนวณเกี่ยวกับตัวดำเนินการทางตรรกศาสตร์ และตัวดำเนินการทางคณิตศาสตร์ และส่วนควบคุมที่ใช้เปลี่ยนแปลงลำดับของตัวดำเนินการโดยยึดสารสนเทศที่ถูกเก็บไว้เป็นหลัก อุปกรณ์เหล่านี้จะยอมให้นำเข้าข้อมูลจากแหล่งภายนอก และส่งผลจากการคำนวณตัวดำเนินการออกไป"
        
    },
    {
        "title":"Flutter 2 คือ?",
        "subtitle":"Tools สำหรับออกแบบ UI ของ Google ",
        "image_url":"https://raw.githubusercontent.com/UncleEngineer/BasicAPI/main/mobileapp.jpg",
        "detail":"Flutter 2 สร้างโดย Google บริษัทเทคโนโลยีอันดับต้นๆของโลก ที่มาพร้อมกับความสวยงาม อลังการ พาไปวัดไปวาแบบไม่ต้องอายใคร 55 อีกทั้งสามารถเขียนโปรแกรมครั้งเดียวด้วยภาษา Dart ที่ถูกออกแบบมาให้เขียนง่าย เข้าใจได้ไม่ยาก เขียนแค่ครั้งเดียว ส่งไปใช้งานได้ทุกแพลตฟอร์ม ไม่ว่าจะเป็น Android, iOS, Web Application, Windows, Linux, MacOS เรียกได้ว่าเขียนครั้งเดียวจบ ส่งไปใช้งานได้เลย"
    },
    {
        "title":"Python คือ?",
        "subtitle":"ภาษาเขียนโปรแกรมชนิดหนึ่ง สร้างขึ้นเมื่อ 1991",
        "image_url":"https://raw.githubusercontent.com/UncleEngineer/BasicAPI/main/coding.jpg",
        "detail":"ภาษาไพทอน (Python programming language) หรือที่มักเรียกกันว่าไพทอน เป็นภาษาระดับสูงซึ่งสร้างโดยคีโด ฟัน โรสซึม โดยเริ่มในปีพ.ศ. 2533 การออกแบบของภาษาไพทอนมุ่งเน้นให้ผู้โปรแกรมสามารถอ่านชุดคำสั่งได้โดยง่ายผ่านการใช้งานอักขระเว้นว่าง (whitespaces) จำนวนมาก นอกจากนั้นการออกแบบภาษาไพทอนและการประยุกต์ใช้แนวคิดการเขียนโปรแกรมเชิงวัตถุในตัวภาษายังช่วยให้นักเขียนโปรแกรมสามารถเขียนโปรแกรมที่เป็นระเบียบ อ่านง่าย มีขนาดเล็ก และง่ายต่อการบำรุง[3]"
    }

]

def Home(request):
    return JsonResponse(data=data,safe=False,json_dumps_params={'ensure_ascii': False})