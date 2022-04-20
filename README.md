# TOX

El objetivo de esta presentacion y mostrar como tomar un proyecto como este en un repositorio de GitHub como cualquier otro __(mostrar rapidamente el ejemplo)__ y convertirlo en un repositorio con una estructura que permita realizar pruebas unitarias automatizadas que cubran diferentes ambientes como OS y diferentes versiones de Python.

Para cada una de las pruebas se cuenta con un ambiente aislado donde se realiza una instalacion fresca del proyecto y verifica todo nuestro codigo. Ademas todo esto se ejecuta cada vez que se realiza un push al repositorio.

## Indice

1. Configuracion / re estructuracion del proyecto __(organizar el proyecto de forma que sea facilmente comprobable, ademas de la creacion de varios archivos de configuracion y para que se utilizan)__
2. Uso de Pytest / mypy / flake8 __(para ejecutar pruebas unitarias, para verficar sugerencias de tipado, para revisar la calidad de codigo)__
3. Multiples ambientes virtuales con TOX
4. GitHub Actions

> Cosas de los que no voy a hablar en esta presentacion, testing ya que es un tema muy amplio y se encuentra bajo el techo de la Integracion continua y depliegue continuo o implementacion continua.

> Tampoco se van a tocar temas de git Hooks

## 1. Configuracion / re estructuracion del proyecto

### * Separar `src` y `tests`
1. __Se explica por que se debe separar el proyecto en directorios__
### * Convertir el proyecto en un paquete instalable

## 2. Uso de Pytest / mypy / flake8
### * Configuracion de Pytest / mypy / flake8
   1. __Se explica a modo general como se configuran las herramientas utilizadas desde el `pyproject.toml` aclarando que hay otras alternativas__
   2. __Se muestra rapidamente un ejemplo de como se ejecuta cada una de estas herramientas de forma manual__
### * Caracteristicas generales de Pytest
   1. __Explicacion general de pytest__
      1. Pytest busca el directorio especificado en la configuracion, por defecto `tests`
      2. Pytest busca dentro del directorio cualquier modulo que comience con `test_`
      3. Pytest ejecuta cualquier metodo dentro del modulo que contenga en su nombre `test_`

## 3. Multiples ambientes virtuales con TOX
### * Configuracion y ejecucion de tox
   1. __Explicacion general de `tox.ini`__

## 4. GitHub Actions
### * Configuracion de GH actions en una accion de commit
   1. __Explicacion del directorio `.github/workflows`__
