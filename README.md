En Argentina, los precios fluctúan constantemente debido a la inflación. Este proyecto tiene como objetivo recopilar diariamente el precio de la Cajita Feliz de McDonald's para utilizarlo como un indicador en futuros análisis estadísticos. Los datos estarán disponibles a través de una URL, lo que permitirá un acceso fácil y directo para su consulta y análisis.

Descripción técnica:

Extracción de datos: Utilizamos Python y Selenium para realizar el scraping diario del precio de la Cajita Feliz desde el sitio web de McDonald's.
Contenedorización y despliegue: El proyecto se empaqueta en una imagen Docker que se sube al repositorio de imágenes en AWS ECR (Elastic Container Registry).
Ejecución automatizada: Desde una instancia EC2 en AWS, se accede a la imagen Docker y se programa su ejecución diaria mediante Cron Jobs.
Almacenamiento de datos: Los datos recopilados se almacenan en una base de datos DynamoDB en AWS, garantizando un almacenamiento seguro y escalable.
Exposición de datos: Un segundo contenedor Docker, también desplegado en EC2, expone los datos recopilados a través de una API basada en Flask, permitiendo el acceso a los datos mediante un endpoint público.

Lista de herramientas:

Python: lenguaje de programación principal.
Selenium: herramienta de automatización para la extracción de datos web.
Flask: framework web para construir la API.
Boto3: SDK de AWS para interactuar con DynamoDB y otros servicios.
Docker: contenedorización del proyecto para un despliegue consistente.
Cron Jobs: programación de tareas automáticas en el servidor.
AWS ECR: almacenamiento de la imagen Docker en la nube.
AWS EC2: instancia de servidor en la nube para ejecutar los contenedores.
AWS DynamoDB: base de datos NoSQL para almacenar los datos recopilados.

Este proyecto permite poner en práctica una variedad de herramientas y tecnologías clave en el desarrollo de software y la infraestructura en la nube. Es un ejemplo claro de cómo una idea simple puede convertirse en una oportunidad para aprender y aplicar conocimientos en un entorno real.

URL de acceso a los datos (Endpoint API): http://3.134.245.1/prices
URL del proyecto en github: https://github.com/Abareil/happy-meal-project

