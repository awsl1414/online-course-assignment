from tortoise import fields
from tortoise.models import Model


class User(Model):
    username = fields.CharField(max_length=255, null=False, description="用户名")
    job_number = fields.CharField(max_length=255, null=False, description="工号")
    hashed_password = fields.CharField(max_length=255, null=False, description="密码")
    permission = fields.IntField(null=False, description="权限")
