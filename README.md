# API proyecto de integración de plataformas: Caso FerreMas

FerreMas, empresa líder en ventas y distribución de productos de ferretería y construcción en Chile, busca expandir su negocio a través del comercio electrónico, lo que permitirá a la empresa llegar a un mayor número de clientes, incrementar sus ventas, ampliar su alcance y lograr un mejor posicionamiento en el mercado. Para ello, hemos desarrollado la siguiente API, que permitirá gestionar los productos, las categorías y las marcas con las que trabaja la empresa. Además, esta API permitirá en futuros proyectos la gestión de usuarios, posibilitando el inicio de sesión y el registro de los mismos. Finalmente, esta API proporciona las conexiones necesarias para la pasarela de pago de Transbank y permite obtener el valor del dólar actualizado al día, facilitando las transacciones y compras desde el extranjero con información actualizada desde la API del Banco Central. 

### Comandos necesarios para levantar la API
Instalación de los requerimientos necesarios:

`pip install -r requirements.txt`

Levantar servidor Django:

`py manage.py runserver`

### Documentación de la API FerreMas
### Gestión de Productos


- Obtener todos los productos:
  
  GET http://localhost:8000/api/productos/
![api_productos](https://github.com/nixtoon/api_integracion/assets/127158636/d5a9b905-86a0-4cf6-9fb3-457b828ae40d)


- Obtener producto por su id:
  
  GET http://localhost:8000/api/productos/get-producto/{id}
  ![api_productos_get_producto](https://github.com/nixtoon/api_integracion/assets/127158636/b262ff93-c623-4915-8a5b-b025c175dabc)


- Obtener producto según id categoria:

  GET   http://localhost:8000/api/productos/get-productos-categoria/{id}
  ![api_productos_get_productos_categoria](https://github.com/nixtoon/api_integracion/assets/127158636/37017a6b-1a94-4c35-8fe9-9b70939f8b56)


- Obtener producto según id de marca:
  
  GET   http://localhost:8000/api/productos/get-productos-marca/{id}
  ![api_productos_get_productos_marca](https://github.com/nixtoon/api_integracion/assets/127158636/2d034f87-e3c0-4c6e-85ba-5eca875832d7)


- Crear un nuevo producto:
  
  POST   http://localhost:8000/api/productos/create-producto/
  ![api_productos_create](https://github.com/nixtoon/api_integracion/assets/127158636/2a3fdcde-addf-4b61-a415-42e63f53901d)


- Editar un producto:
  
  PUT   http://localhost:8000/api/productos/update-producto/{id}
  ![api_productos_update](https://github.com/nixtoon/api_integracion/assets/127158636/caf650f0-6110-4b51-93f1-ba4b145e208a)


- Eliminar un producto
  
  DELETE   http://localhost:8000/api/productos/delete-producto/{id}
  ![api_productos_delete](https://github.com/nixtoon/api_integracion/assets/127158636/1197d82f-f5be-4083-8c45-1906ca5ce7a9)


### Gestión de marcas


- Obtener todas las marcas:

  GET   http://localhost:8000/api/productos/get-marcas
  ![api_productos_get_marcas](https://github.com/nixtoon/api_integracion/assets/127158636/51b02e6c-cf83-4ca7-9429-2b8a0ea9f8ac)


- Obtener marca según su id:

  GET   http://localhost:8000/api/productos/get-marca/{id}
  
  ![api_productos_get_marca](https://github.com/nixtoon/api_integracion/assets/127158636/4552786d-3458-4519-ad9d-79bae4446a10)


- Crear nueva marca:

  POST   http://localhost:8000/api/productos/create-marca/
  
  ![api_productos_create_marca](https://github.com/nixtoon/api_integracion/assets/127158636/e37d0fba-f865-4fea-9bb2-5a8250baf258)


- Editar Marca:
  
  PUT   http://localhost:8000/api/productos/update-marca/{id}
  
  ![api_productos_update_marca](https://github.com/nixtoon/api_integracion/assets/127158636/72e80770-e36f-41fa-b413-b2e99f532edc)


- Eliminar marca:
  
  DELETE   http://localhost:8000/api/productos/delete-marca/{id}
  
  ![api_productos_delete_marca](https://github.com/nixtoon/api_integracion/assets/127158636/11091c1b-79f0-464f-b238-bb8275e79450)


### Gestión de categorias

- Obtener todas las categorias:
  
  GET   http://localhost:8000/api/productos/get-categorias
  
  ![api_productos_get_categorias](https://github.com/nixtoon/api_integracion/assets/127158636/fe56a426-46a4-4099-90ad-f5d253aca853)


- Obtener Categoria según su id:
  
  GET   http://localhost:8000/api/productos/get-categoria/{id}
  
  ![api_productos_get_categoria](https://github.com/nixtoon/api_integracion/assets/127158636/d58d8857-adb8-4f28-9016-f5aacdbda0ae)


- Crear nueva categoria:
  
  POST   http://localhost:8000/api/productos/create-categoria/
  
  ![api_productos_create_categoria](https://github.com/nixtoon/api_integracion/assets/127158636/512fd04b-162d-47d0-bf29-a7c335d556e2)


- Editar categoria:

  PUT   http://localhost:8000/api/productos/update-categoria/{id}
  
  ![api_productos_update_categoria](https://github.com/nixtoon/api_integracion/assets/127158636/313cb42e-75f9-4194-9fa6-1a755e83b7ab)


- Eliminar categoria:

  DELETE   http://localhost:8000/api/productos/delete-categoria/{id}
  
  ![api_productos_delete_categoria](https://github.com/nixtoon/api_integracion/assets/127158636/f4e1633c-9f54-4727-a827-742ca65b66ec)


### Gestión de usuarios

- Iniciar sesión:
  
  POST   http://localhost:8000/api/accounts/login

  ![api_accounts_login](https://github.com/nixtoon/api_integracion/assets/127158636/c8f1b716-55c5-4db4-a47c-ebd245a561e8)

- Registrarse:

  POST   http://localhost:8000/api/accounts/register

  ![api_accounts_register](https://github.com/nixtoon/api_integracion/assets/127158636/841c457f-ae58-4427-9271-8efb52d91bcb)


### Pasarela de pago Transbank

- Crear nueva transacción:

  POST   http://localhost:8000/api/v1/transbank/transaction/create/

  ![transbank_transaction_create](https://github.com/nixtoon/api_integracion/assets/127158636/19b3468c-990b-4ccb-8cd5-3d2dba06abb3)


- Commit de la transacción:

  PUT   http://localhost:8000/api/v1/transbank/commit/{token}

  ![api_transbank_commit](https://github.com/nixtoon/api_integracion/assets/127158636/ac29c4b9-8811-4c4e-a974-1eb9fff58c84)


### API banco central

- Obtener valor actualizado del dolar

  GET   http://localhost:8000/api/v1/transbank/get-dollar-value

  ![api_transbank_get_dollar_value](https://github.com/nixtoon/api_integracion/assets/127158636/eb1f448b-4df2-43ce-9c4e-c83176cb9537)








    


  





  








