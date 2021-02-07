# Glosario

## Django

- Model:
Un **Model** o **Modelo** es una manera de simplificar los recursos de datos. Estos modelos contienen los campos esenciales de la informacion que se va a manejar. Generalmente un modelo busca simplificar el mapeado de una tabla de una base de datos.
- Migration:
La **Migratacion** es la manera en la que **Django** realiza los cambios en los modelos (agregar o eliminar un campo, modelo, etc.) en su esquema de la base de datos. Normalmente son automaticos, pero Django necesita saber cuando realizar migraciones y cuando ejecutarlas.
- ORM:
Es el mapeador de objetos relaciones, el cual permite interactuar con la base de datos como si de SQL se tratase.
- QuerySet:
Basicamente es una lista con los campos u objetos de un modelo ya construido. Permite acceder a los datos de la base de datos relacionado con el modelo en cuestion.

## Django REST Framework

- Serializers:
Son clases que nos permiten convertir datos que se encuentran en formato propio de Django a formatos mas propios del entorno web, tales como **JSON** o **XML**.
- Viewsets:
- Mixins:

## RESTful

- JSON:
- Headers:
  - Content-Type:
  - Authorization:
  - Cookie:
  - Accept:
  - Content-Length:
  - Attachment:
- Parsers
- Renders
- Status codes
  - 200 OK:
  Es la respuesta estándar para peticiones correctas.
  - 201 Created:
  La petición ha sido completada y ha resultado en la creación de un nuevo recurso.
  - 202 Accepted:
  La petición ha sido aceptada para procesamiento, pero este no ha sido completado. La petición eventualmente pudiere no ser satisfecha, ya que podría ser no permitida o prohibida cuando el procesamiento tenga lugar.
  - 204 No Content:
  La petición se ha completado con éxito ,pero su respuesta no tiene ningún contenido (la respuesta puede incluir información en sus cabeceras HTTP).
  - 400 Bad Request:
  El servidor no procesará la solicitud, porque no puede, o no debe, debido a algo que es percibido como un error del cliente.
  - 401 Unauthorized:
  Similar al *403 Forbidden*, pero específicamente para su uso cuando la autentificación es posible pero ha fallado o aún no ha sido provista.
  - 403 Forbidden:
  La solicitud fue legal, pero el servidor rehúsa responderla dado que el cliente no tiene los privilegios para realizarla.
  - 404 Not Found:
  Recurso no encontrado. Se utiliza cuando el servidor web no encuentra la página o recurso solicitado.
  - 500 Internal Server Error:
  Es un código comúnmente emitido por aplicaciones empotradas en servidores web, mismas que generan contenido dinámicamente.
  - 504 Gateway Timeout:
  El servidor está actuando de proxy o gateway y no ha recibido a tiempo una respuesta del otro servidor, por lo que no puede responder adecuadamente a la petición del navegador.
    ...
- HTTP Methods:
  - GET:
  Solicita una representacion de un recurso especifico. Las peticiones que utilizan ***GET*** solo deben recuperar datos.
  - POST:
  Se utiliza para enviar una entidad a un recurso especifico, causando a menudo un cambio en el estado o efectos secundarios en el servidor.
  - PUT:
  El metodo ***PUT*** reemplaza todas las representaciones actuales del recurso de destino con la carga util de la peticion.
  - PATCH:
  Es utilizado para aplicar actualizaciones parciales a un recurso.
  - DELETE:
  Borra un recurso especifico.
  - HEAD:
  El metodo ***HEAD*** pide una respuesta identica a la de una peticion ***GET***, pero sin el cuerpo de la respuesta.
  - OPTIONS:
  Es usado para describir las opciones de comunicacion para el recurso destino.
  - CONNECT:
  Establece un tunel hacia el servidor identificado por el recurso.

## Otros conceptos

- CRUD:
Por sus siglas en ingles (**Create, Read, Update, Delete**) se refiere a un programa o aplicacion que tiene la funcion de *crear, listar o leer, actualizar o modificar, y eliminar* entidades de una base de datos o estructura de almacenamiento.
- JWT
  - Definition:
  - HS254:
- OpenAPI:
