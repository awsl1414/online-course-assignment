from fastapi import APIRouter, Depends, Query, File, UploadFile, Form
from typing import List, Optional
from sqlalchemy.orm import Session

from models import MainClass, OriginClass
from core import get_db, insert_origin_courses_from_xlsx
from crud import (
    get_origin_course,
    get_main_course,
    add_main_course,
    update_main_course,
    update_origin_course,
    delete_main_course,
    delete_origin_course,
)

from schemas import (
    Response200,
    Response400,
    OriginClassIn,
    MainClassIn,
    MainClassJsonIn,
    UpadateMainClassIn,
    UpadateOriginClassIn,
)

router_course = APIRouter(tags=["课程相关"])


@router_course.get("/get_origin_course", summary="原始课表查询")
def get_origin_course_api(
    db: Session = Depends(get_db),
    teacherName: Optional[str] = Query(None),
    teacherRoom: Optional[str] = Query(None),
    courseName: Optional[str] = Query(None),
    className: Optional[str] = Query(None),
    software: Optional[str] = Query(None),
    cycle: Optional[str] = Query(None),
):
    result = get_origin_course(
        db=db,
        teacherName=teacherName,
        teacherRoom=teacherRoom,
        courseName=courseName,
        className=className,
        software=software,
        cycle=cycle,
    )
    if not result:
        return Response400(msg="记录不存在")
    return result


@router_course.get("/get_main_course", summary="详细课表查询")
def get_main_course_api(
    db: Session = Depends(get_db),
    teacherName: Optional[str] = Query(None),
    teacherRoom: Optional[str] = Query(None),
    courseName: Optional[str] = Query(None),
    className: Optional[str] = Query(None),
    population: Optional[int] = Query(None),
    software: Optional[str] = Query(None),
    computerRoomName: Optional[str] = Query(None),
    week: Optional[int] = Query(None),
    weekDay: Optional[int] = Query(None),
    lesson: Optional[str] = Query(None),
    littleLesson: Optional[str] = Query(None),
    cycle: Optional[str] = Query(None),
):
    result = get_main_course(
        db=db,
        teacherName=teacherName,
        teacherRoom=teacherRoom,
        courseName=courseName,
        className=className,
        population=population,
        software=software,
        computerRoomName=computerRoomName,
        week=week,
        weekDay=weekDay,
        lesson=lesson,
        littleLesson=littleLesson,
        cycle=cycle,
    )
    if not result:
        return Response400(msg="记录不存在")
    return result


@router_course.post("/add_main_class", summary="添加详细课表")
def add_main_class_api(formData: MainClassIn, db: Session = Depends(get_db)):
    result = add_main_course(db=db, formData=formData)
    return result


@router_course.post("/add_origin_class_xlsx", summary="添加原始课表 by xlsx")
def add_origin_class_xlsx_api(
    mianClassXlsx: bytes = File(), db: Session = Depends(get_db)
):
    with open("backend/course_origin.xlsx", "wb") as f:
        f.write(mianClassXlsx)
    insert_origin_courses_from_xlsx(db=db)
    return Response200(msg="上传成功")


@router_course.post("/add_origin_class_json", summary="添加原始课表 by json")
def add_origin_class_json(formData: MainClassJsonIn, db: Session = Depends(get_db)):
    print(type(formData.data))
    print(formData.data[0])
    return formData.data


@router_course.put("/update_main_class", summary="更新详细课表")
def update_main_class_api(formData: UpadateMainClassIn, db: Session = Depends(get_db)):
    result = update_main_course(db=db, formData=formData)
    return result


@router_course.put("/update_origin_class", summary="更新原始课表")
def update_origin_class_api(
    formData: UpadateOriginClassIn, db: Session = Depends(get_db)
):
    result = update_origin_course(db=db, formData=formData)
    return result


@router_course.delete("/delete_main_class", summary="删除详细课表")
def delete_main_class_api(id: int, db: Session = Depends(get_db)):
    result = delete_main_course(db=db, id=id)
    return result


@router_course.delete("/delete_origin_class", summary="删除原始课表")
def delete_origin_class_api(id: int, db: Session = Depends(get_db)):
    result = delete_origin_course(db=db, id=id)
    return result


@router_course.get("/test", summary="测试接口")
def test(db: Session = Depends(get_db)):
    query = db.query(MainClass).get(1)
    print(query)
    return query
