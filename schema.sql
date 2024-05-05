
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




CREATE TABLE public.creatures (
    id integer DEFAULT nextval('public.registered_id_seq'::regclass) NOT NULL,
    type text,
    owner text,
    name character varying(20) DEFAULT 'Creature'::character varying NOT NULL
);



CREATE TABLE public.forumposts (
    id integer DEFAULT nextval('public.registered_id_seq'::regclass) NOT NULL,
    content text NOT NULL,
    username text NOT NULL
);



CREATE TABLE public.giftcodes (
    id integer DEFAULT nextval('public.registered_id_seq'::regclass) NOT NULL,
    code text NOT NULL,
    claimed boolean DEFAULT false NOT NULL,
    reclaimable boolean DEFAULT false NOT NULL,
    money integer DEFAULT 0 NOT NULL
);

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



