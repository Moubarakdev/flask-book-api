--
-- PostgreSQL database dump
--

-- Dumped from database version 11.14
-- Dumped by pg_dump version 11.14

-- Started on 2022-05-15 11:52:56

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 197 (class 1259 OID 33050)
-- Name: categorie; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.categorie (
    id integer NOT NULL,
    name character varying NOT NULL,
    description character varying NOT NULL
);


ALTER TABLE public.categorie OWNER TO postgres;

--
-- TOC entry 196 (class 1259 OID 33048)
-- Name: categorie_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.categorie_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.categorie_id_seq OWNER TO postgres;

--
-- TOC entry 2832 (class 0 OID 0)
-- Dependencies: 196
-- Name: categorie_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.categorie_id_seq OWNED BY public.categorie.id;


--
-- TOC entry 199 (class 1259 OID 33061)
-- Name: livre; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.livre (
    id integer NOT NULL,
    isbn integer NOT NULL,
    titre character varying NOT NULL,
    date_publication date NOT NULL,
    auteur character varying NOT NULL,
    editeur character varying NOT NULL,
    categorie_id integer
);


ALTER TABLE public.livre OWNER TO postgres;

--
-- TOC entry 198 (class 1259 OID 33059)
-- Name: livre_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.livre_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.livre_id_seq OWNER TO postgres;

--
-- TOC entry 2833 (class 0 OID 0)
-- Dependencies: 198
-- Name: livre_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.livre_id_seq OWNED BY public.livre.id;


--
-- TOC entry 2693 (class 2604 OID 33053)
-- Name: categorie id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.categorie ALTER COLUMN id SET DEFAULT nextval('public.categorie_id_seq'::regclass);


--
-- TOC entry 2694 (class 2604 OID 33064)
-- Name: livre id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.livre ALTER COLUMN id SET DEFAULT nextval('public.livre_id_seq'::regclass);


--
-- TOC entry 2824 (class 0 OID 33050)
-- Dependencies: 197
-- Data for Name: categorie; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.categorie (id, name, description) FROM stdin;
1	Science-fiction humouristique	un sous-genre de la science-fiction qui exploite les ressorts de l'humour
2	Fable	un court récit en vers ou en prose qui vise à donner de façon plaisante une leçon de vie
3	Tragédie	un genre théâtral dont l’origine remonte au théâtre grec antique
4	Roman policier	un roman relevant du genre policier
\.


--
-- TOC entry 2826 (class 0 OID 33061)
-- Dependencies: 199
-- Data for Name: livre; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.livre (id, isbn, titre, date_publication, auteur, editeur, categorie_id) FROM stdin;
1	1111	Martiens, Go Home!	1954-09-01	Fredric Brown	Astounding	1
2	2222	Le corbeau et le renard	1954-09-01	Jean de La Fontaine	Desaint & Saillant	2
3	3333	Roméo et Juliette	1597-01-01	William Shakespeare	John Danter	3
5	4444	Séquences mortelles	2021-03-01	Michael Connelly	null	4
\.


--
-- TOC entry 2834 (class 0 OID 0)
-- Dependencies: 196
-- Name: categorie_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.categorie_id_seq', 4, true);


--
-- TOC entry 2835 (class 0 OID 0)
-- Dependencies: 198
-- Name: livre_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.livre_id_seq', 5, true);


--
-- TOC entry 2696 (class 2606 OID 33058)
-- Name: categorie categorie_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.categorie
    ADD CONSTRAINT categorie_pkey PRIMARY KEY (id);


--
-- TOC entry 2698 (class 2606 OID 33071)
-- Name: livre livre_isbn_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.livre
    ADD CONSTRAINT livre_isbn_key UNIQUE (isbn);


--
-- TOC entry 2700 (class 2606 OID 33069)
-- Name: livre livre_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.livre
    ADD CONSTRAINT livre_pkey PRIMARY KEY (id);


--
-- TOC entry 2701 (class 2606 OID 33072)
-- Name: livre livre_categorie_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.livre
    ADD CONSTRAINT livre_categorie_id_fkey FOREIGN KEY (categorie_id) REFERENCES public.categorie(id);


-- Completed on 2022-05-15 11:52:57

--
-- PostgreSQL database dump complete
--

