----
DROP TRIGGER IF EXISTS insert_inventario;

----
CREATE TRIGGER insert_inventario BEFORE INSERT
ON inventario
FOR EACH ROW
SET NEW.cantidad=NEW.cantidadcasa+NEW.cantidadtienda;

----
DROP TRIGGER IF EXISTS update_inventario;

----
CREATE TRIGGER update_inventario BEFORE UPDATE
ON inventario
FOR EACH ROW
SET NEW.cantidad=NEW.cantidadcasa+NEW.cantidadtienda;


