# FB_Code_TestScript
Script en Python para automatizar pruebas en FB y recuperar un código de seis dígitos utilizando una lista de números.

El script utiliza una lista de números de seis dígitos y los ingresa secuencialmente en la caja de código en la página de recuperacion de FB.
Después de cada intento, realiza un proceso de verificación buscando una cadena de texto específica en la respuesta del servidor de FB. 
Si la cadena de texto se encuentra, el código ingresado es el correcto y el proceso se detiene, mostrando el código recuperado.
