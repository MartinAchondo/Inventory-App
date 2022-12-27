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
    codigo,
    tipo,
    descripcion,
    color,
    costo,
    precio,
    cantidad,
    preciotienda,
    cantidadcasa,
    cantidadtienda
) 
VALUES(
    :codigo,
    :tipo,
    :descripcion,
    :color,
    :costo,
    :precio,
    :cantidad,
    :preciotienda,
    :cantidadcasa,
    :cantidadtienda
); 

INSERT INTO ventas(
    codigo,
    fecha,
    cantidad,
    lugar,
    precioventa,
    precioreal,
    descuento
) 
VALUES(
    :codigo,
    :fecha,
    :cantidad,
    :lugar,
    :precioventa,
    :precioreal,
    :descuento
); 

INSERT INTO historial(
    codigo,
    tipo,
    fecha,
    descripcion
) 
VALUES(
    :codigo,
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