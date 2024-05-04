# @Coding: utf-8
# @Time: 2024/5/2 14:26
# @User: Administrator


# 示例 在某种情况下 使用row_number会有更好的性能
'''
WITH RankedTable AS (
    SELECT *, ROW_NUMBER() OVER (ORDER BY 某列) AS RowNum
    FROM your_table
)
SELECT * FROM RankedTable
WHERE RowNum BETWEEN 起始行号 AND 结束行号;
'''

getMemCount = '''
        SELECT COUNT(DISTINCT m.member) mnum FROM crm_member m
        LEFT JOIN crm_member_user u1 ON m.member = u1.member
        LEFT JOIN crm_user u2 ON u1.user_id = u2.id
        WHERE u1.user_id = %s
        '''

getMemList = '''
        SELECT
        m.id, m.member
        , LEFT(CAST(m.created AS VARCHAR),10) created
        , m.phone, m.life_type
        , LEFT(CAST(m.begin_date AS VARCHAR),10) begin_date
        , LEFT(CAST(m.end_date AS VARCHAR),10) end_date
        , m.card_type, m.open_type
        , m.create_user, m.tg, m.gps_city, m.server_city
        , m.first_city
        , LEFT(CAST(m.first_date AS VARCHAR),19) first_date
        , m.first_dep
        , m.last_city
        , LEFT(CAST(m.last_date AS VARCHAR),19) last_date
        , m.last_dep, m.owner_status
        FROM crm_member m
        LEFT JOIN crm_member_user u1 ON m.member = u1.member
        LEFT JOIN crm_user u2 ON u1.user_id = u2.id
        WHERE u1.user_id = %s
        LIMIT %s OFFSET %s        
        '''