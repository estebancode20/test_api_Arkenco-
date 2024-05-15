1.Con el usuario "admin" y contraseña "1234" podrán acceder en la ruta http://127.0.0.1:8000/admin al panel donde podrán como administrador ingresar clientes(empresas).


2. Una vez registrado el id de una empresa. En la ruta http://127.0.0.1:8000/crud/v1/prospectos/ podran listar(GET) y ingresar(POST) los prospectos utilizando la api de djangorestframework, los campos sexo, estado y etapa están parametrizados.


3. Señalando en la ruta de la url el numero de registro, podran actualizar(PUT) y eliminar(DELETE) , los prospectos almacenados.   registro 1: http://127.0.0.1:8000/crud/v1/prospectos/1/
               registro 4:  http://127.0.0.1:8000/crud/v1/prospectos/4/


4. Construccion de la imagen:

docker build -t crmcrud .

docker images

OUTPUT:

REPOSITORY   TAG       IMAGE ID       CREATED          SIZE
crudcrm      latest    0b39286a8658   11 seconds ago   1.05GB


5. Ejecucion contenedores:

docker compose up

docker ps -a

OUTPUT:

REPOSITORY   TAG       IMAGE ID       CREATED          SIZE
crudcrm      latest    0b39286a8658   11 seconds ago   1.05GB