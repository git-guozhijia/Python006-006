-- 添加索引
-- ALTER TABLE `table_name` ADD PRIMARY KEY ( `id` )   -- 主键索引
-- ALTER TABLE `table_name` ADD UNIQUE ( `name` )  -- 添加唯一索引
ALTER TABLE table01 ADD INDEX id_index(id);
ALTER TABLE table01 ADD INDEX name_index(name);
ALTER TABLE table02 ADD INDEX id_index(id);
ALTER TABLE table02 ADD INDEX name_index(name);

-- 检查表内索引
SHOW INDEX FROM table01;
SHOW INDEX FROM table02;