/*************************************************************************************************
 *                                                                                               *
 *                   Script Weather - Cria tabela public em SGBD PostgreSQL                      *	
 *                     2021 by Capano Wagner - Projeto Weather in Python                         *
 *                                                                                               *
 *************************************************************************************************/


CREATE SEQUENCE public.weather_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

	
CREATE TABLE weather(

	id INTEGER PRIMARY KEY NOT NULL DEFAULT nextval('weather_id_seq'::regclass),
	cidade varchar(120),
	created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
	info json, 
	service varchar(100)
)

