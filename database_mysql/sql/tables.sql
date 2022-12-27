----
CREATE TABLE IF NOT EXISTS codigos (
    id_codigo INTEGER AUTO_INCREMENT,
    codigo TEXT NOT NULL,
    tipo TEXT NOT NULL,
    descripcion TEXT NOT NULL,
    color TEXT NOT NULL,
    PRIMARY KEY (id_codigo)
);

----
CREATE TABLE IF NOT EXISTS inventario (
    id_codigo INTEGER NOT NULL,
    cantidad INTEGER NOT NULL,
    cantidadcasa INTEGER NOT NULL,
    cantidadtienda INTEGER NOT NULL,
    PRIMARY KEY (id_codigo),
    FOREIGN KEY (id_codigo)
        REFERENCES codigos (id_codigo)
        ON DELETE CASCADE
);

----
CREATE TABLE IF NOT EXISTS precios (
    id_codigo INTEGER NOT NULL,
    costo INTEGER NOT NULL,
    preciocasa INTEGER NOT NULL,
    preciotienda INTEGER NOT NULL,
    PRIMARY KEY (id_codigo),
    FOREIGN KEY (id_codigo)
        REFERENCES codigos (id_codigo)
        ON DELETE CASCADE
);
 
----
CREATE TABLE IF NOT EXISTS historial (
    id INTEGER AUTO_INCREMENT,
    id_codigo INTEGER NOT NULL,
    tipo TEXT NOT NULL,
    fecha TEXT NOT NULL,
    descripcion TEXT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (id_codigo)
        REFERENCES codigos (id_codigo)
        ON DELETE CASCADE
);

----
CREATE TABLE IF NOT EXISTS colores (
    id INTEGER AUTO_INCREMENT,
    numero INTEGER NOT NULL,
    color TEXT NOT NULL,
    PRIMARY KEY (id)
);

----
CREATE TABLE IF NOT EXISTS tipos (
    id INTEGER AUTO_INCREMENT,
    sigla TEXT NOT NULL,
    tipo TEXT NOT NULL,
    PRIMARY KEY (id)
);

----
CREATE TABLE IF NOT EXISTS ventas (
    id INTEGER AUTO_INCREMENT,
    id_codigo INTEGER NOT NULL,
    fecha DATE NOT NULL,
    cantidad INTEGER NOT NULL,
    lugar TEXT NOT NULL,
    precioventa INTEGER NOT NULL,
    precioreal INTEGER NOT NULL,
    descuento TEXT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (id_codigo)
        REFERENCES codigos (id_codigo)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS id_fotos(
    id_foto TEXT NOT NULL,
    codigo TEXT NOT NULL,
    PRIMARY KEY(id_foto)
)