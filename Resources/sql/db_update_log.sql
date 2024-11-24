-- 该文件可以初始化执行，也可以不执行，如果没有这张表程序会自动创建
create table if not exists db_update_log (
    id int(11) not null auto_increment comment '自增id',
    version varchar(10) default null comment '版本号',
    file_name varchar(50) default null comment '文件名',
    update_time datetime default null comment '更新时间',
    primary key(id)
) default charset=gbk;