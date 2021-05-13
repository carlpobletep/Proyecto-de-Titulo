from django.db import models
from ckeditor.fields import RichTextField


class ModeloBase(models.Model):
    id = models.AutoField(primary_key = True)
    estado = models.BooleanField('Estado',default = True)
    fecha_creacion = models.DateField('Fecha de Creación',auto_now = False, auto_now_add = True)
    fecha_modificacion = models.DateField('Fecha de Modificación',auto_now = True, auto_now_add = False)
    fecha_eliminacion = models.DateField('Fecha de Eliminación',auto_now = True, auto_now_add = False)

    class Meta:
        abstract = True

    def __str__(self):
         return f'{self.number}. {self.category} with {self.beds} for {self.capacity} people'

class Categoria(ModeloBase):
    nombre = models.CharField('Nombre de la Categoría', max_length = 100, unique = True)
    imagen_referencial = models.ImageField('Imagen Referencial',upload_to = 'categoria/')

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return self.nombre

class Cliente(ModeloBase):
    nombre = models.CharField('Nombres',max_length = 100)
    apellidos = models.CharField('Apellidos',max_length = 120)
    usuario = models.CharField('Usuario',max_length=120)
    contraseña = models.CharField('Contraseña',max_length=120)
    direccion = models.CharField('direccion',max_length=120)
    email = models.EmailField('Correo Electrónico', max_length = 200)
    facebook = models.URLField('Facebook', null = True, blank = True)
    twitter = models.URLField('Twitter', null = True, blank = True)
    instagram = models.URLField('Instagram', null = True, blank = True)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return '{0},{1}'.format(self.apellidos,self.nombre,self.usuario,self.contraseña)

class Empleado(ModeloBase):
    nombre = models.CharField('Nombres',max_length = 100)
    apellidos = models.CharField('Apellidos',max_length = 120)
    usuario = models.CharField('Usuario',max_length=120)
    contraseña = models.CharField('Contraseña',max_length=120)
    direccion = models.CharField('direccion',max_length=120)
    email = models.EmailField('Correo Electrónico', max_length = 200)

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

    def __str__(self):
        return '{0},{1}'.format(self.apellidos,self.nombre,self.usuario,self.contraseña)

class Administrador(ModeloBase):
    nombre = models.CharField('Nombres',max_length = 100)
    apellidos = models.CharField('Apellidos',max_length = 120)
    usuario = models.CharField('Usuario',max_length=120)
    contraseña = models.CharField('Contraseña',max_length=120)
    direccion = models.CharField('direccion',max_length=120)
    email = models.EmailField('Correo Electrónico', max_length = 200)

    class Meta:
        verbose_name = 'Administrador'
        verbose_name_plural = 'Administradores'

    def __str__(self):
        return '{0},{1}'.format(self.apellidos,self.nombre,self.usuario,self.contraseña)

class Proveedor(ModeloBase):
    nombre = models.CharField('Nombres',max_length = 100)
    apellidos = models.CharField('Apellidos',max_length = 120)
    usuario = models.CharField('Usuario',max_length=120)
    contraseña = models.CharField('Contraseña',max_length=120)
    rubro = models.CharField('Contraseña',max_length=120)
    direccion = models.CharField('direccion',max_length=120)
    email = models.EmailField('Correo Electrónico', max_length = 200)

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'

    def __str__(self):
        return '{0},{1}'.format(self.apellidos,self.nombre,self.usuario,self.contraseña)

class Habitacion(ModeloBase):
    nombre_habitacion = models.CharField('Nombre Habitacion ',max_length = 150, unique = True)
    numero_habitacion = models.CharField('Numero Habitacion', max_length = 150, unique = True)
    descripcion = models.TextField('Descripción')
    cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)
    contenido = RichTextField()
    imagen_referencial = models.ImageField('Imagen Referencial', upload_to = 'imagenes/', max_length = 255)
    publicado = models.BooleanField('Publicado / No Publicado',default = False)
    fecha_publicacion = models.DateField('Fecha de Publicación')

    class Meta:
        verbose_name = 'Habitacion'
        verbose_name_plural = 'Habitaciones'

    def __str__(self):
        return self.modelo

class Producto(ModeloBase):
    descrip_p = models.TextField('Descripción de Producto')
    precio_p = models.CharField('Precio Producto', max_length = 150, unique = True)
    stock_p = models.CharField('Stock Producto', max_length = 150, unique = True)
    stock_op = models.CharField('Stock op', max_length = 150, unique = True)
    proveedor = models.ForeignKey(Proveedor, on_delete = models.CASCADE)
    contenido = RichTextField()
    fecha_publicacion = models.DateField('Fecha de Publicación')

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.modelo

class Pedido(ModeloBase):
    descrip_p = models.TextField('Descripción de Pedido')
    empleado = models.ForeignKey(Empleado, on_delete = models.CASCADE)
    contenido = RichTextField()
    fecha_publicacion = models.DateField('Fecha de Publicación')

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    def __str__(self):
        return self.modelo

class OrdenPedido(ModeloBase):
    detalle_op = models.TextField('Detalle orden de Pedido')
    proveedor = models.ForeignKey(Proveedor, on_delete = models.CASCADE)
    administrador = models.ForeignKey(Administrador, on_delete = models.CASCADE)
    contenido = RichTextField()
    imagen_referencial = models.ImageField('Imagen Referencial', upload_to = 'imagenes/', max_length = 255)
    fecha_publicacion = models.DateField('Fecha de Publicación')

    class Meta:
        verbose_name = 'Ordenpedido'
        verbose_name_plural = 'Ordenespedidos'

    def __str__(self):
        return self.modelo


class OrdenCompra(ModeloBase):
    detalle_com = models.TextField('Detalle orden de Pedido')
    cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE)
    administrador = models.ForeignKey(Administrador, on_delete = models.CASCADE)
    contenido = RichTextField()
    imagen_referencial = models.ImageField('Imagen Referencial', upload_to = 'imagenes/', max_length = 255)
    fecha_publicacion = models.DateField('Fecha de Publicación')

    class Meta:
        verbose_name = 'Ordecompra'
        verbose_name_plural = 'OrdenCompras'

    def __str__(self):
        return self.modelo

class Comedor(ModeloBase):
    detalle_com = models.TextField('Detalle Comedor')
    cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE)
    ServicioG = models.ForeignKey(ServicioG, on_delete = models.CASCADE)
    ServicioE = models.ForeignKey(ServicioE, on_delete = models.CASCADE)
    ServicioEJ = models.ForeignKey(ServicioEJ, on_delete = models.CASCADE)
    contenido = RichTextField()

    class Meta:
        verbose_name = 'Comedor'
        verbose_name_plural = 'Comedores'

    def __str__(self):
        return self.modelo

class ServicioE(ModeloBase):
    minuta_s= models.TextField('Minuta Semanal')
    cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE)
    contenido = RichTextField()

    class Meta:
        verbose_name = 'ServicioE'
        verbose_name_plural = 'ServiciosE'

    def __str__(self):
        return self.modelo

class ServicioG(ModeloBase):
    minuta_s = models.TextField('Minuta semanal')
    cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE)
    contenido = RichTextField()

    class Meta:
        verbose_name = 'ServicioG'
        verbose_name_plural = 'ServiciosG'

    def __str__(self):
        return self.modelo

class ServicioEJ(ModeloBase):
    minuta_s = models.TextField('Minuta semanal')
    cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE)
    contenido = RichTextField()

    class Meta:
        verbose_name = 'ServicioEJ'
        verbose_name_plural = 'ServiciosEJ'

    def __str__(self):
        return self.modelo



class RedesSociales(ModeloBase):
    facebook = models.URLField('Facebook')
    twitter = models.URLField('Twitter')
    instagram = models.URLField('Instagram')

    class Meta:
        verbose_name = 'Red Social'
        verbose_name_plural = 'Redes Sociales'

    def __str__(self):
        return self.facebook

class Contacto(ModeloBase):
    nombre = models.CharField('Nombre', max_length = 100)
    apellidos = models.CharField('Apellidos', max_length = 150)
    correo = models.EmailField('Correo Electrónico', max_length = 200)
    asunto = models.CharField('Asunto', max_length = 100)
    mensaje = models.TextField('Mensaje')

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'

    def __str__(self):
        return self.asunto

