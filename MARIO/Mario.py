
import arcade

#CONSTANTES

#Constantes para la ventana del juego

ANCHO_PANTALLA = 1200

ALTO_PANTALLA = 600

TITULO_PANTALLA = "MUESTRA DEMO DE MARIO BROS"

#Constantes para escalar los sprites (hojas png)
ESCALA_PERSONAJE = 0.15

ESCALA_TERRENO = 0.20

ESCALA_TUBERIA = 0.2

#Velocidad del jugador
VELOCIDAD_MOVIMIENTO_JUGADOR = 10

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

		#Crea el jugador
		fuente_imagen = "mario.png"
		self.jugador_sprite = arcade.Sprite(fuente_imagen, ESCALA_PERSONAJE)
		self.jugador_sprite.center_x = 120
		self.jugador_sprite.center_y = 300
		self.lista_jugador.append(self.jugador_sprite)
		
		#Crea el piso
		for x in range(0,6050, 64):
			muro = arcade.Sprite("terreno.png", ESCALA_TERRENO)
			muro.center_x = x
			muro.center_y = 20
			self.lista_muro.append(muro)
		#BLOQUE DE TIERRA AEREO
		coordenadas_bloqueTierra = [ 
							#horizontal vertical

							[604, 140],
							[650, 140],
							[714, 140],
							[778, 140],
							[842, 280],
							[906, 280],
							[970, 280],
							[1034, 280],
							[1098, 140],
							[1162, 140],
							[1226, 140], #salto
							[1418, 140],
							[1482, 140],
							[1546, 140],
							[1610, 140],
							[1674, 140],
							[1738, 140],
							[1802, 280],
							[1866, 280],
							[1930, 280],
							[1994, 280],
							[2058, 140],
							[2122, 140],
							[2186, 140],
							[2200, 140],
							[2236, 140],
							[2272, 140],
							[2308, 140],
							[2344, 140]
			]
		

		for coordenadas in coordenadas_bloqueTierra:
			# añade en el terreno creado
			muro = arcade.Sprite("tuberia.png", ESCALA_TUBERIA)
			muro.position = coordenadas
			self.lista_muro.append(muro)

			#Coordenadas DEL CASTillO
			coordenadasCastillo = [ 
							#horizontal vertical
							[6000, 175]					
			]
		

		for coordenadas in coordenadasCastillo:
			# Añade y crea el castillo en el terreno
			muro = arcade.Sprite("castillo.png", 0.2)
			muro.position = coordenadas
			self.lista_muro.append(muro)

		coordenadasMastil= [ 
							#horizontal vertical
							[0, 280],
							[5900, 280]					
			]
		

		for coordenadas in coordenadasMastil:
			# añade y crea el mastil
			muro = arcade.Sprite("mastil.png", 0.2)
			muro.position = coordenadas
			self.lista_muro.append(muro)


		
		coordenadas_nubes = [ 
							#horizontal vertical

							[500, 420],
							[1000, 600],
							[1200, 620],
							[1300, 620],
							[1400, 520],
							[2500, 620],
							[2580, 620],
							[2670, 620],
							[2720, 620],
							[2780, 530],
							[2800, 620],
							[2890, 620],
							[2930, 520],
							[2980, 620],       
							[3120, 430],
							[3250, 620],
							[3300, 620],      
							[3680, 620],      
							[3780, 620],       
							[3900, 620],       
							[4000, 520],       
							[4200, 620],       
							[4280, 620],
							[4360, 620],
							[4400, 620],
							[4520, 600],
							[4580, 620],
							[4640, 620],
							[4690, 620],
							[4750, 570],
							[4800, 620],
							[4820, 620],
							[4890, 420], 
							[5010, 620],
							[5110, 620],      
							[5190, 620],      
							[5250, 620],       
							[5300, 420],       
							[5360, 620],       
							[5390, 640],       
							[5400, 620],
							[5480, 420],
							[5560, 620],
							[5600, 620],
							[5640, 620],
							[5690, 620],
             
			]
		

		for coordenadas in coordenadas_nubes:
			# añade y crea las nubes
			muro = arcade.Sprite("nubes.png", 0.3)
			muro.position = coordenadas
			self.lista_muro.append(muro)

		
        #Motor de fisica
		self.physics_engine = arcade.PhysicsEnginePlatformer(self.jugador_sprite, self.lista_muro, GRAVEDAD)
	
	def on_draw(self):
		arcade.start_render()
		self.lista_jugador.draw()
		self.lista_muro.draw()

	def on_key_press(self, llave, modificadores):
		#Se llama cada vez que se presiona una tecla

		if llave == arcade.key.UP or llave == arcade.key.W:
			if self.physics_engine.can_jump():
				self.jugador_sprite.change_y = VELOCIDAD_SALTO_JUGADOR
		elif llave == arcade.key.LEFT or llave == arcade.key.A:
			self.jugador_sprite.change_x = -VELOCIDAD_MOVIMIENTO_JUGADOR
		elif llave == arcade.key.RIGHT or llave == arcade.key.D:
			self.jugador_sprite.change_x = VELOCIDAD_MOVIMIENTO_JUGADOR

	def on_key_release(self, llave, modificadores):
		#Se llama cuando el usuario suelta una clave

		if llave == arcade.key.LEFT or llave == arcade.key.A:
			self.jugador_sprite.change_x  = 0
		elif llave == arcade.key.RIGHT or llave == arcade.key.D:
			self.jugador_sprite.change_x = 0

	def on_update(self, tiempo_delta):
		#Movimiento y logica de juego

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

#main
def main():
	window = MiJuego()
	window.setup()
	arcade.run()
 
if __name__ == "__main__":
	main()
