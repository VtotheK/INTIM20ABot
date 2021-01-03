delimiter $$

drop procedure if exists deadlines_set;

create procedure deadlines_set(
	in _fromdiscord int, 
    _module varchar(50),
    _course varchar(50),
	_title varchar(1000),
    _summary varchar(1000),
    _userid bigint,
    _deadline datetime,
    _notifyfrom datetime
)
deadlines_set:begin

declare var_userid bigint;

if _deadline or _notifyfrom is null
then
	signal sqlstate '45000'
		set message_text = 'Deadline or notifyperiod is empty, please check the input.';
end if;

if _fromdiscord is null
then
	signal sqlstate '45000'
		set message_text = 'Fromdiscord flag is null.';
end if;
if arg_userid is not null
then
	select userid into var_userid from users where userid=arg_userid limit 1;
	if var_userid is null
	then
		leave deadlines_set;
    end if;
end if;

if _fromdiscord <> 1
then
	insert into deadlines(module,course,title,summary,userid,deadline,notifyfrom)
	values(_module,_course,_title,_summary,_userid,_deadline,_notifyfrom);
else
	insert into deadlines_staging(module,course,title,summary,userid,deadline,notifyfrom)
	values(_module,_course,_title,_summary,_userid,_deadline,_notifyfrom);
end if;
end $$

delimiter ;