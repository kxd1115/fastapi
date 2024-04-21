from tortoise.models import Model
from tortoise import fields
from datetime import datetime


# 全量客户表
class Member(Model):
    id = fields.IntField(pk=True, auto_increment=True)
    member_type = fields.CharField(max_length=32, description='客户类型')           # 会员 or 客户
    member = fields.CharField(max_length=32, description='会员卡号')
    card_life_type = fields.CharField(max_length=32, description='生命周期分类')
    card_id = fields.IntField(description='卡ID', default='')
    created = fields.DatetimeField(description='首次开卡日期')
    begin_date = fields.DatetimeField(description='本次开卡日期')
    end_date = fields.DatetimeField(description='会员卡到期日期')
    card_type = fields.IntField(description='最新会员卡类型')                      # 会员卡类型
    phone = fields.CharField(max_length=16, description='手机号')                 # 如果是会员卡，则显示卡主手机号，如果是客户，则显示档案号手机号

    owner_user = fields.ForeignKeyField('crm.User', description='归属管家', related_name='member')
    owner_cm = fields.ForeignKeyField('crm.User', description='归属CM', related_name='member')
    owner_ci = fields.ForeignKeyField('crm.User', description='归属商保', related_name='member')

# 客户类型
class Member_Type(Model):
    id = fields.IntField(pk=True, auto_increment=True)

# 转移日志表
class ChangeUserLog(Model):
    id = fields.IntField(pk=True, auto_increment=True)
    change_time = fields.DatetimeField(
        default=datetime.now,
        null=True,
        blank=True,
        verbose_name="变更日期"
    )

    # 对应操作的用户
    create_user = fields.ForeignKeyField('crm.User', description='操作用户', related_name='changeuserlog')
    old_user = fields.ForeignKeyField('crm.User', description='目前归属', related_name='changeuserlog')
    new_user = fields.ForeignKeyField('crm.User', description='调整后归属', related_name='changeuserlog')

    update_at = fields.DatetimeField(auto_now=True, description='实例更新日期', verbose_name='最后更新日期')

# 用户表
class User(Model):
    id = fields.IntField(pk=True, auto_increment=True)
    username = fields.CharField(max_length=32, description='账号')
    pwd = fields.CharField(max_length=32, description='密码')
    name_cn = fields.CharField(max_length=32, description='中文名')