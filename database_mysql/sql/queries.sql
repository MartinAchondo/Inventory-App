--pedir_codigo--
SELECT codigos.codigo, 
        codigos.tipo, 
        codigos.descripcion, 
        codigos.color,
        precios.costo,
        inventario.cantidad,
        precios.preciocasa,
        precios.preciotienda,
        inventario.cantidadcasa,
        inventario.cantidadtienda 
FROM codigos
INNER JOIN inventario
ON codigos.id_codigo = inventario.id_codigo
INNER JOIN precios
ON codigos.id_codigo = precios.id_codigo;

--pedir_codigos_en_casa--
SELECT codigos.codigo,codigos.descripcion,
FROM codigos
INNER JOIN inventario
ON codigos.id_codigo = inventario.id_codigos
WHERE inventario.cantidadcasa > 0;

--pedir_codigos_en_tienda--
SELECT codigos.codigo,codigos.descripcion,
FROM codigos
INNER JOIN inventario
ON codigos.id_codigo = inventario.id_codigos
WHERE inventario.cantidadtienda > 0;
