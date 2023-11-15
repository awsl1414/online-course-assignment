from tortoise import fields
from tortoise.models import Model


class OriginClass(Model):
    # 主键，当表里所有属性都没设置pk时，默认生成一个IntField类型 id 的主键
    # id = fields.UUIDField(pk=True)
    teacherName = fields.CharField(max_length=255, null=False, description="教师姓名")
    teacherRoom = fields.CharField(max_length=255, null=False, description="教研室")
    courseName = fields.CharField(max_length=255, null=False, description="课程名称")
    className = fields.CharField(max_length=255, null=False, description="班级名称")
    population = fields.IntField(null=False, description="班级人数")
    software = fields.CharField(max_length=255, null=False, description="软件")
    cycle = fields.CharField(max_length=255, null=False, description="周期")
