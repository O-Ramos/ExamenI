            *   *   *   Examen Parcial I - Cloud Computing  *   *   *

URL = "https://ptly9qxcx0.execute-api.us-east-1.amazonaws.com/prod/test"

- Funcionalidad -
La API es capaz de recibir un objecto imagen desde un servicio en S3
Realiza el analisis de la imagen mediante el servicio AWS Rekognition
Regresa un json con los resultados obtenidos tomando en cuenta el indice de confidencia

No recibe la entrada en el formato requerido

- Descripcion -
* Se monto un bucket en S3 con la finalidad de almacenar las imagenes durante las pruebas
* Se generó una lambda la cual se encarga de solicitar la imagen especificada al servicio de S3,
lo cual nos regresa la imagen como objecto.
* Esta misma lambda denominada rekognition_lambda tambien se encarga de llamar el servicio de
AWS Rekognition donde realizamos el analisis de las imagens para determinar las etiquetas y texto.
* De aqui se procesa el resultado para regresarse en un json file como respuesta al API gateway designado al evento.

- Codigo -
https://github.com/O-Ramos/ExamenI.git
