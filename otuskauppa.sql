--
-- PostgreSQL database cluster dump
--

-- Started on 2024-04-20 19:37:12 EEST


--
-- TOC entry 208 (class 1259 OID 32868)
-- Name: creatureprices; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.creatureprices (
    id integer NOT NULL,
    type text,
    price integer DEFAULT 99999 NOT NULL
);


--
-- TOC entry 203 (class 1259 OID 16455)
-- Name: registered; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.registered (
    id integer NOT NULL,
    username text NOT NULL,
    password text,
    money integer DEFAULT 100 NOT NULL
);


--
-- TOC entry 202 (class 1259 OID 16453)
-- Name: registered_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.registered_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 2254 (class 0 OID 0)
-- Dependencies: 202
-- Name: registered_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.registered_id_seq OWNED BY public.registered.id;


--
-- TOC entry 204 (class 1259 OID 16476)
-- Name: creatures; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.creatures (
    id integer DEFAULT nextval('public.registered_id_seq'::regclass) NOT NULL,
    type text,
    owner text,
    name character varying(20) DEFAULT 'Creature'::character varying NOT NULL
);


--
-- TOC entry 209 (class 1259 OID 49245)
-- Name: forumposts; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.forumposts (
    id integer NOT NULL,
    content text NOT NULL,
    username text NOT NULL
);


--
-- TOC entry 207 (class 1259 OID 24668)
-- Name: giftcodes; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.giftcodes (
    id integer NOT NULL,
    code text NOT NULL,
    claimed boolean DEFAULT false NOT NULL
);


--
-- TOC entry 205 (class 1259 OID 16490)
-- Name: password_length; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.password_length
    START WITH 8
    INCREMENT BY 1
    MINVALUE 8
    MAXVALUE 30
    CACHE 1;


--
-- TOC entry 2255 (class 0 OID 0)
-- Dependencies: 205
-- Name: password_length; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.password_length OWNED BY public.registered.password;


--
-- TOC entry 206 (class 1259 OID 16492)
-- Name: username_length; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.username_length
    START WITH 2
    INCREMENT BY 1
    MINVALUE 2
    MAXVALUE 20
    CACHE 1;


--
-- TOC entry 2256 (class 0 OID 0)
-- Dependencies: 206
-- Name: username_length; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.username_length OWNED BY public.registered.username;


--
-- TOC entry 2105 (class 2604 OID 16458)
-- Name: registered id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.registered ALTER COLUMN id SET DEFAULT nextval('public.registered_id_seq'::regclass);


--
-- TOC entry 2119 (class 2606 OID 32876)
-- Name: creatureprices creatureprices_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.creatureprices
    ADD CONSTRAINT creatureprices_pkey PRIMARY KEY (id);


--
-- TOC entry 2115 (class 2606 OID 16483)
-- Name: creatures creatures_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.creatures
    ADD CONSTRAINT creatures_pkey PRIMARY KEY (id);


--
-- TOC entry 2121 (class 2606 OID 49252)
-- Name: forumposts forumposts_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.forumposts
    ADD CONSTRAINT forumposts_pkey PRIMARY KEY (id);


--
-- TOC entry 2117 (class 2606 OID 24676)
-- Name: giftcodes giftcodes_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.giftcodes
    ADD CONSTRAINT giftcodes_pkey PRIMARY KEY (id);


--
-- TOC entry 2112 (class 2606 OID 16463)
-- Name: registered registered_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.registered
    ADD CONSTRAINT registered_pkey PRIMARY KEY (id);


--
-- TOC entry 2113 (class 1259 OID 49244)
-- Name: unique_registered_username; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX unique_registered_username ON public.registered USING btree (username);


-- Completed on 2024-04-20 19:37:12 EEST

--
-- PostgreSQL database dump complete
--

-- Completed on 2024-04-20 19:37:12 EEST

--
-- PostgreSQL database cluster dump complete
--

