CREATE TABLE IF NOT EXISTS inventario (
    id integer PRIMARY KEY,
    codigo text NOT NULL,
    tipo text NOT NULL,
    descripcion text NOT NULL,
    color text NOT NULL,
    costo integer NOT NULL,
    precio integer NOT NULL,
    cantidad integer NOT NULL,
    preciotienda integer NOT NULL,
    cantidadcasa integer NOT NULL,
    cantidadtienda integer NOT NULL
);
 
CREATE TABLE IF NOT EXISTS codigos (
    id integer PRIMARY KEY,
    codigo text NOT NULL,
    tipo text NOT NULL,
    descripcion text NOT NULL,
    color text NOT NULL
);
 
CREATE TABLE IF NOT EXISTS historial (
    id integer PRIMARY KEY,
    codigo text NOT NULL,
    tipo text NOT NULL,
    fecha text NOT NULL,
    descripcion text NOT NULL
);

CREATE TABLE IF NOT EXISTS colores (
    id integer PRIMARY KEY,
    numero integer NOT NULL,
    color text NOT NULL
);

CREATE TABLE IF NOT EXISTS tipos (
    id integer PRIMARY KEY,
    sigla text NOT NULL,
    tipo text NOT NULL
);

CREATE TABLE IF NOT EXISTS ventas (
    id integer PRIMARY KEY,
    codigo text NOT NULL,
    fecha text NOT NULL,
    cantidad integer NOT NULL,
    lugar text NOT NULL,
    precioventa integer NOT NULL,
    precioreal integer NOT NULL,
    descuento text NOT NULL
);

CREATE TABLE IF NOT EXISTS id_fotos (
    id_foto text PRIMARY KEY,
    codigo text NOT NULL
)