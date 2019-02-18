create table mediaindex (filename varchar(255), filetype varchar(50), filesize bigint, filehash varchar(255))

create table goldenmedialist (filename varchar(255))
select * from mediaindex where filehash = 'a323ceccce70dd30bac1c5b83ac5e83ceb6b90126a6bb992f6899b669bd28892'
select count(*) from goldenmedialist
select count(*) from mediaindex
SELECT count(*) FROM mediaindex WHERE filehash = "b48cc336c335cdc3be6ec1891783687ae136969c969d9869ebd4942f42393dd0" AND filesize = 171
select filetype, count(*) from mediaindex group by filetype

select count(*) from mediaindex where filesize < 4000 

select * from mediaindex where filesize < 1000 limit 10

select filename, count(*) from mediaindex where filetype = "Video" group by filesize limit 10

select filename, filesize from mediaindex where filetype = "Video" order by filesize desc limit 100

select * from mediaindex where filename like '%IMG_0516%'
delete from mediaindex where filename like '%xili%'

select * from mediaindex where filetype = "Unknown"    
select filename, filehash, count(*) as dupcount from mediaindex group by filehash order by dupcount desc limit 1000
delete from mediaindex where filehash = 'ab2b8121d4f4d5d6aff0d4f0c0f1c30dfa5a815a955a94a7fec1d48b815e827c'
select filename from mediaindex where filehash = '866fe01bf20ff026aa956be55438d1aad3c5b5a1a7a5a18cff3fbe4f01928801'