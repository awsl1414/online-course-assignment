from models import ModelsMainClass, ModelsOriginClass, ModelsComputerRoom, ModelsUser

model_mapping = {
    "ModelsMainClass": ModelsMainClass,
    "ModelsOriginClass": ModelsOriginClass,
    "ModelsComputerRoom": ModelsComputerRoom,
    "ModelsUser": ModelsUser,
}

computer_room_mapping = {
    "机房名称": "computer_room",
    "机房别名": "alias_name",
    "软件名称": "software_name",
}

origin_class_mapping = {
    "教师名": "teacher_name",
    "课程名": "course_name",
    "班级名": "class_name",
    "人数": "population",
    "软件名": "software_name",
    "周数": "cycle",
    "教研室": "teacher_room",
    "周课时": "week_lesson_times",
}


# excel表头映射
base_mapping = {
    "ModelsComputerRoom": computer_room_mapping,
    "ModelsOriginClass": origin_class_mapping,
}
