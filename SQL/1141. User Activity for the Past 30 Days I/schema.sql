create table If Not Exists Activity (
    user_id int,
    session_id int,
    activity_date date,
    activity_type ENUM('open_session', 'end_session', 'scroll_down', 'send_message')
);

truncate table Activity;

insert into Activity (user_id, session_id, activity_date, activity_type)
values ('1', '1', '2019-07-20', 'open_session');

insert into Activity (user_id, session_id, activity_date, activity_type)
values ('1', '1', '2019-07-20', 'scroll_down');

insert into Activity (user_id, session_id, activity_date, activity_type)
values ('1', '1', '2019-07-20', 'end_session');

insert into Activity (user_id, session_id, activity_date, activity_type)
values ('2', '4', '2019-07-20', 'open_session');

insert into Activity (user_id, session_id, activity_date, activity_type)
values ('2', '4', '2019-07-21', 'send_message');

insert into Activity (user_id, session_id, activity_date, activity_type)
values ('2', '4', '2019-07-21', 'end_session');

insert into Activity (user_id, session_id, activity_date, activity_type)
values ('3', '2', '2019-07-21', 'open_session');

insert into Activity (user_id, session_id, activity_date, activity_type)
values ('3', '2', '2019-07-21', 'send_message');

insert into Activity (user_id, session_id, activity_date, activity_type)
values ('3', '2', '2019-07-21', 'end_session');

insert into Activity (user_id, session_id, activity_date, activity_type)
values ('4', '3', '2019-06-25', 'open_session');

insert into Activity (user_id, session_id, activity_date, activity_type)
values ('4', '3', '2019-06-25', 'end_session');
