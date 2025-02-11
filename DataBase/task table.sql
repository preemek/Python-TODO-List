-- Table: public.task

-- DROP TABLE IF EXISTS public.task;

CREATE TABLE IF NOT EXISTS public.task
(
    id integer NOT NULL DEFAULT nextval('task_id_seq'::regclass),
    list_id integer NOT NULL,
    name character varying(50) COLLATE pg_catalog."default" NOT NULL,
    deadline date,
    priority character varying(20) COLLATE pg_catalog."default",
    status character varying(30) COLLATE pg_catalog."default",
    CONSTRAINT task_pkey PRIMARY KEY (id),
    CONSTRAINT fk_list FOREIGN KEY (list_id)
        REFERENCES public.list (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE CASCADE
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.task
    OWNER to avnadmin;