def insert_origin_courses_from_xlsx(db: Session):
    # 导入一个工作簿
    wb = load_workbook("backend/course_origin.xlsx")
    # 获取当前活动的工作表
    ws = wb.active

    max_row = ws.max_row

    for rows in ws.iter_rows(min_row=1, max_row=max_row):
        origin_data = []
        for row in rows:
            origin_data.append(row.value)
        print(origin_data)
        if (
            not db.query(models.OriginClass)
            .filter(models.OriginClass.teacherName == origin_data[0])
            .filter(models.OriginClass.courseName == origin_data[1])
            .filter(models.OriginClass.className == origin_data[2])
            .first()
        ):
            OriginClass = models.OriginClass(
                teacherName=origin_data[0],
                courseName=origin_data[1],
                className=origin_data[2],
                population=origin_data[3],
                software=origin_data[4],
                week=origin_data[5],
                teacherRoom=origin_data[6],
                lesson=origin_data[7],
            )
            db.add(OriginClass)
            db.commit()
