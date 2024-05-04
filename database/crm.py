from tortoise.models import Model
from tortoise import fields
from status.orm_models import *

# 全量客户表
class CrmMember(Model): # member表
    id = fields.IntField(pk=True, description='自增主键', auto_increment=True)
    ## 不可为空
    member = fields.CharField(max_length=32, description='会员卡号或者档案号')
    created = fields.DatetimeField(description='首次开卡日期 or 档案号创建日期')
    ## 可以为空
    # 如果是会员卡，则显示卡主手机号，如果是客户，则显示档案号手机号
    phone = fields.CharField(max_length=16, description='手机号', null=True)
    life_type = fields.CharField(max_length=32, description='生命周期分类', null=True)

    # 本次卡生效日期
    begin_date = fields.DatetimeField(description='本次开卡日期', null=True)
    # 卡到期日期
    end_date = fields.DatetimeField(description='会员卡到期日期', null=True)
    # 会员卡类型
    card_type = fields.CharField(max_length=64, description='最新会员卡类型', null=True)
    # 本次开卡方式
    open_type = fields.IntField(description='开卡方式', null=True)
    # 本次操作员工
    create_user = fields.CharField(max_length=32, description='本次开卡操作员工', null=True)
    # TG类型
    tg = fields.CharField(max_length=16, description='TG类型', null=True)
    # 定位城市
    gps_city = fields.CharField(max_length=32, description='定位城市', null=True)
    # 选择的服务城市
    server_city = fields.CharField(max_length=32, description='服务城市', null=True)
    # 首诊城市
    first_city = fields.CharField(max_length=32, description='首诊城市', null=True)
    # 首诊日期
    first_date = fields.DatetimeField(null=True, description='首诊日期')
    # 首诊科室
    first_dep = fields.CharField(max_length=32, description='首诊科室', null=True)
    # 最后一次就诊城市
    last_city = fields.CharField(max_length=32, description='最后一次就诊城市', null=True)
    # 最后一次就诊日期
    last_date = fields.DatetimeField(null=True, description='最后一次就诊日期')
    # 最后一次就诊科室
    last_dep = fields.CharField(max_length=32, description='最后一次就诊科室', null=True)

    # 归属状态，默认为正常状态
    owner_status = fields.CharEnumField(ChangeStatus, default=ChangeStatus.NORMAL)

    class Meta:
        table = 'crm_member'

class MemUser(Model): # 客户归属管家表
    id = fields.IntField(pk=True, description='自增主键', auto_increment=True)
    create_at = fields.DatetimeField(auto_now_add=True, description='创建日期')
    member = fields.CharField(max_length=32, description='会员卡号或者档案号')
    user_id = fields.IntField(description='员工表ID')
    update_at = fields.DatetimeField(auto_now=True, description='更新日期')

    class Meta:
        table = 'crm_member_user'

class MemSea(Model): # 客户公海表
    id = fields.IntField(pk=True, description='自增主键', auto_increment=True)
    create_at = fields.DatetimeField(auto_now_add=True, description='创建日期')
    member = fields.CharField(max_length=32, description='会员卡号或者档案号')
    sea_id = fields.IntField(description='公海')
    update_at = fields.DatetimeField(auto_now=True, description='更新日期')

    class Meta:
        table = 'crm_member_sea'

class CrmSea(Model): # 公海表
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=32, description='公海名称', null=True)

    class Meta:
        table = 'crm_sea'

    def __str__(self):
        self.name

# 转移日志表
class ChangeUserLog(Model): # 归属转移log
    id = fields.IntField(pk=True, auto_increment=True)
    create_at = fields.DatetimeField(auto_now_add=True, description='创建日期')

    # 操作的客户
    member = fields.CharField(max_length=32, description='会员卡号或者档案号')

    # 对应操作的用户
    performed_by = fields.ForeignKeyField('models.CrmUser', related_name='assignment_user_user')
    # 旧员工
    old_user = fields.ForeignKeyField('models.CrmUser', related_name='old_user')
    # 新员工
    new_user = fields.ForeignKeyField('models.CrmUser', related_name='new_user')

    update_at = fields.DatetimeField(auto_now=True, description='更新日期')

    class Meta:
        table = 'crm_change_user_log'

class ChangeSeaLog(Model): # 公海变更log
    id = fields.IntField(pk=True, auto_increment=True)
    create_at = fields.DatetimeField(auto_now_add=True, description='创建日期')

    # 操作的客户
    member = fields.CharField(max_length=32, description='会员卡号或者档案号')

    # 对应操作的用户
    performed_by = fields.ForeignKeyField('models.CrmUser', related_name='assignment_sea_user')
    # 旧公海
    old_sea = fields.ForeignKeyField('models.CrmSea', related_name='old', null=True)
    # 新公海
    new_sea = fields.ForeignKeyField('models.CrmSea', related_name='new', null=True)

    update_at = fields.DatetimeField(auto_now=True, description='更新日期')

    class Meta:
        table = 'crm_change_sea_log'

# 用户表
class CrmUser(Model): # 员工表
    id = fields.IntField(pk=True, auto_increment=True)
    username = fields.CharField(max_length=32, description='账号')
    pwd = fields.CharField(max_length=32, description='密码')
    name_cn = fields.CharField(max_length=32, description='中文名')
    title = fields.CharField(max_length=32, description='岗位')

    wechat_username = fields.CharField(max_length=32, description='企微账号', null=True)
    wechat_nickname = fields.CharField(max_length=64, description='企微昵称', null=True)

    # 1对多关系
    department = fields.ForeignKeyField('models.CrmDepartments', description='对应部门', related_name='employees')

    # 默认状态
    status = fields.CharEnumField(STATUS, default=STATUS.ACTIVE)

    class Meta:
        table = 'crm_user'

    def __str__(self):
        return self.username


class CrmDepartments(Model): # 部门表
    id = fields.IntField(pk=True, auto_increment=True)
    name = fields.CharField(max_length=100)
    parent_department = fields.ForeignKeyField('models.CrmDepartments', null=True, description='上级部门', related_name='sub_departments')

    # 层级表示法
    level = fields.IntField(default=0)

    # 或者使用路径表示法
    path = fields.TextField(null=True)

    # 部门默认状态
    status = fields.CharEnumField(STATUS, default=STATUS.ACTIVE)

    class Meta:
        table = 'crm_department'
        ordering = ["level"]

    def __str__(self):
        return self.name