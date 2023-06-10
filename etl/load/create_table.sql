create table if not exists public.f_internet (
          index_num int
        , entity varchar(120)
        , code varchar(50)
        , date_year int 
        , cellulars int
        , percent_users decimal(15,2)
        , users int 
        , broadband int
);