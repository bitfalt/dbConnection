> **Pooling Connection**
>
> El resultado mostrado en las siguientes imágenes es la carga en SQL
> Server, después de mandar el mismo query de 20 usuarios diferentes
> utilizando la herramienta JMeter.
>
> El pool size inicial es de 5 conexiones, con un máximo de 10
> conexiones al mismo tiempo.
>
> ![](media/image1.png){width="6.5111100174978125in"
> height="1.4375in"}

![](media/image2.png){width="6.715277777777778in"
height="1.3638877952755906in"}

> Sin embargo, cabe mencionar, aunque la configuración del pool no
> cambié la forma en
>
> la que maneja las conexiones pude variar, como se observa en la
> siguiente imagen. Se puede observar como se abrieron 9 conexiones en
> vez de 10, como la imagen de arriba.

![](media/image3.png){width="6.736111111111111in"
height="1.583332239720035in"}

![](media/image4.png){width="6.391666666666667in"
height="1.6041666666666667in"}

Como se puede observar los request, fueron exitosos y la base de datos
no tuvo problema manejando ninguna solicitud.

![](media/image5.png){width="5.872222222222222in"
height="1.0375in"}

Después de cierto tiempo de inactividad de request, en la imagen
anterior se puede observar como las conexiones del pool se reestablecen
a su minimo de 5.

**No Pooling Connection**

![](media/image6.png){width="6.5in"
height="1.3111111111111111in"}

![](media/image7.png){width="6.5in"
height="1.3027777777777778in"}

![](media/image8.png){width="6.5in"
height="0.8680544619422572in"}

En las imágenes anteriores, se puede observar como cambia el
comportamiento de las

conexiones al no usar un pool para manejar las conexiones, ya que, se
abren 20 conexiones diferentes para lograr realizar las consultas de los
20 usuarios.

Igualmente, no hay ningún inconveniente al tener esta cantidad de
conexiones abiertas para un query sencillo como el que se está
realizando.

![](media/image9.png){width="3.626388888888889in"
height="1.163888888888889in"}

A la izquierda se puede observar la cantidad de requests por segundo al
no utilizar pool (6 requests por segundo) y a la derecha la cantidad de
requests por segundo utilizando un pool (4 requests por segundo).

**Pooling Connection vs No Pooling Connection**

La implementación de un pool de conexiones puede potenciar el
rendimiento de una aplicación al permitir la reutilización de conexiones
existentes, en lugar de establecer una nueva conexión cada vez que un
usuario desea interactuar con la base de datos. Esto acelera la
interacción con la base de datos, optimizando la eficiencia de la
aplicación.

Además, el pool de conexiones establece límites a la cantidad de
conexiones abiertas en función de los parámetros predefinidos. A
diferencia de un sistema que abre una nueva conexión con cada usuario,
el pool de conexiones evita la sobrecarga que podría producirse con un
gran número de conexiones, preservando así el rendimiento y la eficacia
de la base de datos.

Es importante destacar que el pool de conexiones ofrece flexibilidad
para adaptarse al crecimiento futuro de la aplicación. A medida que
aumenta la cantidad de usuarios, se puede ajustar el número de
conexiones abiertas en el pool para satisfacer la demanda.

Por otro lado, en aplicaciones más pequeñas con una interacción menos
frecuente con la base de datos, podría ser preferible una conexión
directa. En estos casos, podría resultar más eficiente en términos de
recursos abrir conexiones de manera puntual, en lugar de mantener un
número fijo de conexiones abiertas cuando la demanda es baja. De esta
manera, se puede optimizar el uso de los recursos de acuerdo con las
necesidades específicas de la aplicación.
