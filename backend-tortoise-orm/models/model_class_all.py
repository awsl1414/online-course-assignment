from tortoise import fields

from tortoise.models import Model


class FinalClass(Model):
    teacherName = fields.CharField(max_length=255, null=False, description="教师姓名")
    teacherRoom = fields.CharField(max_length=255, null=False, description="教研室")
    courseName = fields.CharField(max_length=255, null=False, description="课程名称")
    className = fields.CharField(max_length=255, null=False, description="班级名称")
    population = fields.IntField(null=False, description="班级人数")
    software = fields.CharField(max_length=255, null=False, description="软件")
    computerRoomName = fields.CharField(max_length=255, null=False, description="机房名称")
    week = fields.IntField(null=False, description="周次")
    weekDay = fields.IntField(null=False, description="星期")
    lesson = fields.CharField(max_length=255, null=False, description="节次")
    cycle = fields.CharField(max_length=255, null=False, description="周期")
