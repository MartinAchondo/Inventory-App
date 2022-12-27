INSERT INTO codigos(
    codigo,
    tipo,
    descripcion,
    color
) 
VALUES(
    :codigo,
    :tipo,
    :descripcion,
    :color
); 

INSERT INTO inventario(
    id_codigo,
    cantidad,
    cantidadcasa,
    cantidadtienda
) 
VALUES(
    :id_codigo,
    :cantidad,
    :cantidadcasa,
    :cantidadtienda
); 

INSERT INTO precios(
    id_codigo,
    costo,
    preciocasa,
    preciotienda
) 
VALUES(
    :id_codigo,
    :costo,
    :preciocasa,
    :preciotienda
); 

INSERT INTO ventas(
    id_codigo,
    fecha,
    cantidad,
    lugar,
    precioventa,
    precioreal,
    descuento
) 
VALUES(
    :id_codigo,
    :fecha,
    :cantidad,
    :lugar,
    :precioventa,
    :precioreal,
    :descuento
); 

INSERT INTO historial(
    id_codigo,
    tipo,
    fecha,
    descripcion
) 
VALUES(
    :id_codigo,
    :tipo,
    :fecha,
    :descripcion
); 

INSERT INTO tipos(
    sigla,
    tipo
) 
VALUES(
    :sigla,
    :tipo
); 

INSERT INTO colores(
    numero,
    color
) 
VALUES(
    :numero,
    :color
); 

INSERT INTO id_fotos(
    id_foto,
    codigo
)
VALUES(
    :id_foto,
    :codigo
);