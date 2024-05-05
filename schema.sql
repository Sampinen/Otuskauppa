
CREATE TABLE public.creatureprices (
    id serial PRIMARY KEY,
    type text,
    price integer DEFAULT 99999 NOT NULL
);

CREATE TABLE public.registered (
    id serial PRIMARY KEY,
    username text NOT NULL UNIQUE,
    password text,
    money integer DEFAULT 100 NOT NULL
);


CREATE TABLE public.creatures (
    id serial PRIMARY KEY,
    type text,
    owner text,
    name character varying(20) DEFAULT 'Creature'::character varying NOT NULL
);



CREATE TABLE public.forumposts (
   id serial PRIMARY KEY,
    content text NOT NULL,
    username text NOT NULL
);



CREATE TABLE public.giftcodes (
    id serial PRIMARY KEY,
    code text NOT NULL,
    claimed boolean DEFAULT false NOT NULL,
    reclaimable boolean DEFAULT false NOT NULL,
    money integer DEFAULT 0 NOT NULL
);

INSERT INTO public.creatureprices (type,price) VALUES ("haukerias",50);
INSERT INTO public.creatureprices (type,price) VALUES ("lohari",45);




