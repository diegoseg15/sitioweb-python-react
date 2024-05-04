## Proyecto ReactPy con Tailwind CSS

Este proyecto demuestra cómo utilizar React con Python utilizando la biblioteca `ReactPy` junto con estilos de `Tailwind CSS`. A continuación, encontrarás detalles sobre cómo clonar el repositorio, los componentes utilizados y la información de la licencia.

### Clonar el Repositorio

Puedes clonar este repositorio utilizando Git:

```bash
git clone https://github.com/tu_usuario/tu_repositorio.git
cd tu_repositorio
```

### Componentes Utilizados

En este proyecto, se han utilizado los siguientes componentes:

- **HelloWorld**: Un componente simple que muestra "Hello World".
  
  ```python
  from reactpy import component, html

  @component
  def HelloWorld():
      return html.H1("Hello World")
  ```

- **Items**: Un componente para renderizar una lista de elementos.

  ```python
  from reactpy import component, html

  @component
  def Items():
      return html.Ul(
          html.Li("Item 1"),
          html.Li("Item 2"),
          html.Li("Item 3")
      )
  ```

### Estilos con Tailwind CSS

Este proyecto utiliza `Tailwind CSS` para estilizar los componentes. Se incluye el script de Tailwind en el HTML:

```python
from reactpy import html

# Script de Tailwind CSS
cdn_tailwind = html.script({"src": "https://cdn.tailwindcss.com"})
```

### Levantando el Servidor de Desarrollo

Para ejecutar la aplicación, utiliza `uvicorn`:

```bash
uvicorn Main:app --reload
```

Accede a [http://localhost:8000](http://localhost:8000) para ver la aplicación en funcionamiento.

### Licencia

Este proyecto está bajo la licencia MIT. Para más detalles, consulta el archivo `LICENSE` en el repositorio.
