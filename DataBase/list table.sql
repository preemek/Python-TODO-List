-- Table: public.list

-- DROP TABLE IF EXISTS public.list;

CREATE TABLE IF NOT EXISTS public.list
(
    id integer NOT NULL DEFAULT nextval('list_id_seq'::regclass),
    name character varying(50) COLLATE pg_catalog."default" NOT NULL,
    create_date date DEFAULT CURRENT_DATE,
    CONSTRAINT list_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.list
    OWNER to avnadmin;