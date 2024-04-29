
CREATE TABLE public.creatureprices (
    id integer NOT NULL,
    type text,
    price integer DEFAULT 99999 NOT NULL
);

CREATE TABLE public.registered (
    id integer NOT NULL,
    username text NOT NULL,
    password text,
    money integer DEFAULT 100 NOT NULL
);


CREATE SEQUENCE public.registered_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;



ALTER SEQUENCE public.registered_id_seq OWNED BY public.registered.id;



CREATE TABLE public.creatures (
    id integer DEFAULT nextval('public.registered_id_seq'::regclass) NOT NULL,
    type text,
    owner text,
    name character varying(20) DEFAULT 'Creature'::character varying NOT NULL
);

CREATE TABLE public.forumposts (
    id integer NOT NULL,
    content text NOT NULL,
    username text NOT NULL
);


CREATE TABLE public.giftcodes (
    id integer NOT NULL,
    code text NOT NULL,
    claimed boolean DEFAULT false NOT NULL
);

CREATE SEQUENCE public.password_length
    START WITH 8
    INCREMENT BY 1
    MINVALUE 8
    MAXVALUE 30
    CACHE 1;

ALTER SEQUENCE public.password_length OWNED BY public.registered.password;


CREATE SEQUENCE public.username_length
    START WITH 2
    INCREMENT BY 1
    MINVALUE 2
    MAXVALUE 20
    CACHE 1;


ALTER SEQUENCE public.username_length OWNED BY public.registered.username;


ALTER TABLE ONLY public.registered ALTER COLUMN id SET DEFAULT nextval('public.registered_id_seq'::regclass);


ALTER TABLE ONLY public.creatureprices
    ADD CONSTRAINT creatureprices_pkey PRIMARY KEY (id);



ALTER TABLE ONLY public.creatures
    ADD CONSTRAINT creatures_pkey PRIMARY KEY (id);



ALTER TABLE ONLY public.forumposts
    ADD CONSTRAINT forumposts_pkey PRIMARY KEY (id);




ALTER TABLE ONLY public.giftcodes
    ADD CONSTRAINT giftcodes_pkey PRIMARY KEY (id);




ALTER TABLE ONLY public.registered
    ADD CONSTRAINT registered_pkey PRIMARY KEY (id);


CREATE UNIQUE INDEX unique_registered_username ON public.registered USING btree (username);


