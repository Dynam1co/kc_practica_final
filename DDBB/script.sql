create table if not exists item
(
    id                integer not null,
    type              varchar not null,
    popularity        numeric,
    vote_count        integer,
    poster_path       varchar,
    adult             boolean,
    backdrop_path     varchar,
    original_language varchar,
    original_title    varchar,
    title             varchar,
    vote_average      numeric,
    overview          text,
    release_date      date,
    budget            integer,
    imdb_id           varchar,
    local_poster_path varchar,
    constraint item_pk
        primary key (type, id)
);

alter table item
    owner to fjasensi;

create table if not exists genre
(
    id   integer not null
        constraint genre_pk
            unique,
    name varchar
);

alter table genre
    owner to fjasensi;

create table if not exists item_genres
(
    type    varchar not null,
    iditem  integer not null,
    idgenre integer not null
        constraint item_genres_genre___fk
            references genre (id),
    constraint item_genres_pk
        unique (type, iditem, idgenre),
    constraint item_genres_item___fk
        foreign key (type, iditem) references item
);

alter table item_genres
    owner to fjasensi;

create table if not exists production_companies
(
    id   integer not null
        constraint production_companies_pk
            primary key,
    name varchar
);

alter table production_companies
    owner to fjasensi;

create table if not exists item_production_companies
(
    id     integer not null
        constraint item_production_companies_companies___fk
            references production_companies,
    iditem integer not null,
    name   varchar,
    type   varchar not null,
    constraint item_production_companies_pk
        primary key (type, iditem, id),
    constraint item_production_companies_item___fk
        foreign key (type, iditem) references item
);

alter table item_production_companies
    owner to fjasensi;

create table if not exists caracter
(
    id     integer not null
        constraint caracter_pk
            primary key,
    name   varchar,
    gender integer
);

alter table caracter
    owner to fjasensi;

create table if not exists item_caracter
(
    type   varchar not null,
    id     integer not null
        constraint item_caracter_caracter___fk
            references caracter,
    name   varchar,
    gender integer,
    iditem integer not null,
    constraint item_caracter_pk
        primary key (type, iditem, id),
    constraint item_caracter_item___fk
        foreign key (type, iditem) references item
);

alter table item_caracter
    owner to fjasensi;


