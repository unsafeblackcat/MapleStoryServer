-- ���ļ����Գ�ʼ��ִ�У�Ҳ���Բ�ִ�У����û�����ű������Զ�����
create table if not exists db_update_log (
    id int(11) not null auto_increment comment '����id',
    version varchar(10) default null comment '�汾��',
    file_name varchar(50) default null comment '�ļ���',
    update_time datetime default null comment '����ʱ��',
    primary key(id)
) default charset=gbk;