import arcade

ANCHO_PANTALLA = 1000
ALTO_PANTALLA = 500
TITULO_PANTALLA = "MUESTRA DEMO DE MARIO BROS"

#Constantes para escalar los sprites (hojas png)
ESCALA_PERSONAJE = 0.17
ESCALA_TERRENO = 0.20
ESCALA_TUBERIA = 0.20

#Velocidad del jugador
VELOCIDAD_MOVIMIENTO_JUGADOR = 5
GRAVEDAD = 1
VELOCIDAD_SALTO_JUGADOR = 20

# cuantos pixeles de margen como minimo entre el personaje
# y el borde de la pantalla.
MARGEN_VISTA_IZQUIERDO = 250
MARGEN_VISTA_DERECHO = 250
MARGEN_VISTA_INFERIOR = 50
MARGEN_VISTA_SUPERIOR = 100

class MiJuego(arcade.Window):

	def __init__(self):

		super().__init__(ANCHO_PANTALLA, ALTO_PANTALLA, TITULO_PANTALLA)

		arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

		self.lista_moneda = None
		self.lista_muro = None
		self.lista_jugador = None

		#Variable del sprite jugador
		self.jugador_sprite = None

		# se usa para realizar un seguimiento de nuestro desplazamiento
		self.vista_inferior = 0
		
		self.vista_izquierda = 0

