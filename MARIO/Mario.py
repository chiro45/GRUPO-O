
import arcade

ANCHO_PANTALLA = 800

ALTO_PANTALLA = 600

TITULO_PANTALLA = "MUESTRA DEMO DE MARIO BROS"

#Constantes para escalar los sprites (hojas png)
ESCALA_PERSONAJE = 0.17

ESCALA_TERRENO = 0.20

ESCALA_TUBERIA = 0.20

#Velocidad del jugador
VELOCIDAD_MOVIMIENTO_JUGADOR = 8

GRAVEDAD = 1

VELOCIDAD_SALTO_JUGADOR = 20

# cuantos pixeles de margen como minimo entre el personaje
# y el borde de la pantalla.

MARGEN_VISTA_IZQUIERDA = 250

MARGEN_VISTA_DERECHA = 250

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
  
	def setup(self):
		self.lista_jugador = arcade.SpriteList()
		self.lista_muro = arcade.SpriteList(use_spatial_hash=True)
		self.lista_moneda = arcade.SpriteList()

		#Jugador
		fuente_imagen = "mario.png"
		self.jugador_sprite = arcade.Sprite(fuente_imagen, ESCALA_PERSONAJE)
		self.jugador_sprite.center_x = 120
		self.jugador_sprite.center_y = 300
		self.lista_jugador.append(self.jugador_sprite)
		#inicia el dibujado del suelo del juego por donde mario corre
		for x in range(0,4050, 64):
			muro = arcade.Sprite("terreno.png", ESCALA_TERRENO)
			muro.center_x = x
			muro.center_y = 20
			self.lista_muro.append(muro)

		coordinate_list = [ 
							#horizontal vertical

							[604, 140],
							[650, 140],
							[714, 140],
							[778, 140],
							[842, 300],
							[906, 300],
							[970, 300],
							[1034, 300],
							[1098, 140],
							[1162, 140],
							[1226, 140], #salto
							[1418, 140],
							[1482, 140],
							[1546, 140],
							[1610, 140],
							[1674, 140],
							[1738, 140],
							[1802, 300],
							[1866, 300],
							[1930, 300],
							[1994, 300],
							[2058, 140],
							[2122, 140],
							[2186, 140],
							[2150, 140],					
			]
		

		for coordinate in coordinate_list:
			# añade en el terreno creado
			muro = arcade.Sprite("tuberia.png", ESCALA_TUBERIA)
			muro.position = coordinate
			self.lista_muro.append(muro)



			# This shows using a coordinate list to place sprites
		coordinate_list2 = [ 
							#horizontal vertical

							[3000, 175]					
			]
		

		for coordinate in coordinate_list2:
			# Añade y crea el castillo en el terreno
			muro = arcade.Sprite("castillo.png", 0.2)
			muro.position = coordinate
			self.lista_muro.append(muro)
		coordinate_list3= [ 
							#horizontal vertical
							[0, 280],
							[2930, 280]					
			]
		

		for coordinate in coordinate_list3:
			# añade y crea el mastil
			muro = arcade.Sprite("mastil.png", 0.2)
			muro.position = coordinate
			self.lista_muro.append(muro)


		
		coordinate_list4 = [ 
							#horizontal vertical

							[1866, 3020],
							[1930, 3200],
							[1994, 3020],
							[2058, 140],
							[2122, 1420],
							[2186, 1420],
							[2150, 1420],				
			]
		

		for coordinate in coordinate_list4:
			# añade y crea las nubes
			muro = arcade.Sprite("nubes.png", 0.2)
			muro.position = coordinate
			self.lista_muro.append(muro)

		

		self.physics_engine = arcade.PhysicsEnginePlatformer(self.jugador_sprite, self.lista_muro, GRAVEDAD)
	
	def on_draw(self):
		arcade.start_render()
		self.lista_jugador.draw()
		self.lista_muro.draw()

	def on_key_press(self, llave, modificadores):
		"""Se llama cada vez que se presiona una tecla."""

		if llave == arcade.key.UP or llave == arcade.key.W:
			if self.physics_engine.can_jump():
				self.jugador_sprite.change_y = VELOCIDAD_SALTO_JUGADOR
		elif llave == arcade.key.LEFT or llave == arcade.key.A:
			self.jugador_sprite.change_x = -VELOCIDAD_MOVIMIENTO_JUGADOR
		elif llave == arcade.key.RIGHT or llave == arcade.key.D:
			self.jugador_sprite.change_x = VELOCIDAD_MOVIMIENTO_JUGADOR

	def on_key_release(self, llave, modificadores):
		"""Se llama cuando la usuario suelta una clave. """

		if llave == arcade.key.LEFT or llave == arcade.key.A:
			self.jugador_sprite.change_x  = 0
		elif llave == arcade.key.RIGHT or llave == arcade.key.D:
			self.jugador_sprite.change_x = 0

	def on_update(self, tiempo_delta):
		""" Movimiento y lógica de juego. """

		# Mueve al jugador con el motor de física engine

		self.physics_engine.update()

		# --- Administrar desplazamiento ---

        # Seguimiento si necesitamos cambiar la ventana gráfica

		cambiado = False

        # Desplazarse a la izquierda
		limite_izquierdo = self.vista_izquierda + MARGEN_VISTA_IZQUIERDA
		if self.jugador_sprite.left < limite_izquierdo:
			self.vista_izquierda -= limite_izquierdo - self.jugador_sprite.left
			cambiado = True

		# Desplazarse a la derecha
		limite_derecho = self.vista_izquierda + ANCHO_PANTALLA - MARGEN_VISTA_DERECHA
		if self.jugador_sprite.right > limite_derecho:
			self.vista_izquierda += self.jugador_sprite.right - limite_derecho
			cambiado = True

		# Desplazarse hacia arriba
		limite_superior = self.vista_inferior + ALTO_PANTALLA - MARGEN_VISTA_SUPERIOR
		if self.jugador_sprite.top > limite_superior:
			self.vista_inferior += self.jugador_sprite.top - limite_superior
			cambiado = True

        # Desplazarse hacia abajo
		limite_inferior = self.vista_inferior + MARGEN_VISTA_INFERIOR
		if self.jugador_sprite.bottom < limite_inferior:
			self.vista_inferior -= limite_inferior - self.jugador_sprite.bottom
			cambiado = True

		if cambiado:
			# Solo desplácese a números enteros. De lo contrario, terminaremos con píxeles que
			# no se alineen en la pantalla
			self.vista_inferior = int(self.vista_inferior)
			self.vista_izquierda = int(self.vista_izquierda)

			# Hace el desplazamiento
			arcade.set_viewport(self.vista_izquierda, ANCHO_PANTALLA + self.vista_izquierda, self.vista_inferior,ALTO_PANTALLA + self.vista_inferior)


def main():
	window = MiJuego()
	window.setup()
	arcade.run()
 
if __name__ == "__main__":
	main()
