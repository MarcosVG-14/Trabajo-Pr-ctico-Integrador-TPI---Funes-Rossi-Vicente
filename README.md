
# Trabajo Práctico Integrador - Funes - Rossi - Vicente

# FoodStore (Aplicación de gestión de pedidos y usuarios)

Esta es una aplicación interactiva desarrollada en Python y ejecutada a través de la consola, diseñada especialmente para gestionar pedidos en un E-Commerce (pedir, consultar, editar, eliminar), gestionar usuarios activos y roles de usuarios.

El programa utiliza una interfaz visual adaptada a la terminal mediante el uso de textos personalizados (caracteres ANSI), garantizando una experiencia de usuario intuitiva, prolija y ordenada, junto con persistencia de datos mediante archivos CSV.

## Características Principales

El sistema ofrece un sistema de inicio de sesión con control de roles y dos menús principales:

* **Menú de Administrador:** Permite gestionar de forma integral el catálogo (categorías y productos), administrar los usuarios registrados y supervisar o modificar el estado de los pedidos.
* **Menú de Usuario (Cliente):** Permite explorar el catálogo disponible, realizar nuevos pedidos, consultar el historial propio y gestionar los datos de su perfil.

## Menú Administrador

1. **Categorías:** Permite acceder a todas las funciones de administración sobre las categorías del sistema.
   * 1.1 ***Listar:*** Te permite listar todas las categorías que estén creadas y tengan el valor `eliminado = False`. En el caso de que la categoría esté creada y tenga el valor `eliminado = True`, la categoría no se mostrará.
   * 1.2 ***Crear:*** Te permite crear una categoría personalizada desde cero. Si alguno de los parámetros ingresados no pasa la capa de validaciones propuesta, el programa no se interrumpirá pero tampoco se creará la categoría.
   * 1.3 ***Editar:*** Te permite editar el nombre y la descripción anteriormente enunciados si se considera que alguno está mal ingresado. Mediante una búsqueda de `ID` de la categoría se encuentran los valores que se desean editar y, mediante una consulta de confirmación, se decide si cambiar los valores o dejar los que ya habían sido ingresados anteriormente.
   * 1.4 ***Eliminar:*** Te permite eliminar de manera lógica una categoría. Mediante una búsqueda de `ID` de la categoría se encuentra la entidad que se desea dar de baja; la función del programa cambia el valor de `eliminado = False` a `eliminado = True` tras una consulta de confirmación.
   * 1.5 ***Volver:*** Te permite retornar al menú principal para ver todas las acciones.
2. **Productos:** Permite gestionar el inventario de artículos disponibles en la tienda.
   * 2.1 ***Listar:*** Te permite listar todos los productos que estén creados y tengan el valor `eliminado = False`. En el caso de que el producto esté creado y tenga el valor `eliminado = True`, el producto no se mostrará.
   * 2.2 ***Crear:*** Te permite crear un producto personalizado desde cero (asignando nombre, precio, stock y categoría válida). Si alguno de los parámetros ingresados no pasa la capa de validaciones propuesta, el programa no se interrumpirá pero tampoco se creará el producto.
   * 2.3 ***Editar:*** Te permite editar los atributos del producto (nombre, descripción, precio, stock o categoría). Mediante una búsqueda de `ID` del producto se encuentran los valores que se desean editar y, mediante una consulta de confirmación, se decide si aplicar los cambios o conservar los datos anteriores.
   * 2.4 ***Eliminar:*** Te permite eliminar de manera lógica un producto. Mediante una búsqueda de `ID` del producto se encuentra el artículo que se desea dar de baja; la función cambia el valor de `eliminado = False` a `eliminado = True` previa confirmación.
   * 2.5 ***Volver:*** Te permite retornar al menú principal para ver todas las acciones.
3. **Usuarios:** Permite administrar las cuentas registradas en la plataforma.
   * 3.1 ***Listar:*** Muestra todos los usuarios activos en el sistema (`eliminado = False`), detallando su ID, nombre, correo electrónico y rol asignado.
   * 3.2 ***Crear:*** Permite registrar un nuevo usuario desde el panel de administración, validando el formato de los datos ingresados y evitando duplicados.
   * 3.3 ***Editar / Cambiar Rol:*** Mediante la búsqueda por `ID`, permite modificar los datos de un usuario existente o actualizar sus permisos (alternando entre rol de Administrador y Usuario estándar) tras confirmar la operación.
   * 3.4 ***Eliminar:*** Realiza una baja lógica del usuario seleccionado por `ID`, cambiando su estado a `eliminado = True` previa confirmación, impidiendo su acceso futuro sin perder el historial asociado.
   * 3.5 ***Volver:*** Permite retornar al menú principal del administrador.
4. **Pedidos:** Permite supervisar y gestionar todas las órdenes generadas en el E-Commerce.
   * 4.1 ***Listar:*** Muestra el listado completo de pedidos activos (`eliminado = False`), indicando el usuario asociado, los productos solicitados, el monto total y el estado actual del pedido.
   * 4.2 ***Consultar detalle / Filtrar:*** Permite buscar un pedido específico mediante su `ID` para visualizar el desglose completo de ítems y cantidades.
   * 4.3 ***Editar estado:*** Mediante la búsqueda por `ID`, permite actualizar el estado del pedido (por ejemplo:  *Pendiente* ,  *En preparación* ,  *Enviado* ,  *Entregado* ) previa confirmación.
   * 4.4 ***Eliminar / Cancelar:*** Permite dar de baja lógica un pedido (`eliminado = True`) mediante su `ID` y confirmación, restaurando el stock correspondiente si aplica.
   * 4.5 ***Volver:*** Permite retornar al menú principal del administrador.
5. **Cerrar sesión:** Finaliza la sesión actual del administrador de forma segura y retorna a la pantalla principal de inicio de sesión/registro.
6. **Salir:** Guarda los cambios pendientes en los archivos CSV y finaliza la ejecución del programa de manera ordenada.

## Menú Usuario (Cliente)

1. **Ver Catálogo:** Muestra las categorías y productos disponibles (`eliminado = False` y con stock disponible) para que el usuario pueda explorar la oferta de la tienda.
2. **Realizar Pedido:** Permite al usuario seleccionar productos mediante su `ID` y especificar cantidades. El sistema valida el stock disponible, calcula el total y registra el pedido asociándolo a su cuenta.
3. **Mis Pedidos:** Lista únicamente los pedidos realizados por el usuario autenticado, permitiendo consultar el estado y detalle de cada orden.
4. **Mi Perfil:** Permite visualizar los datos de la cuenta actual y editar información personal tras pasar las validaciones correspondientes.
5. **Cerrar sesión:** Cierra la sesión del usuario y regresa al menú de autenticación.
6. **Salir:** Cierra la aplicación por completo.

# Video de presentación y explicación del TPI
* https://youtu.be/eqa0Q_Q-uOc*
