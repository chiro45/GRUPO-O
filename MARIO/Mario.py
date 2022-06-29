
import arcade

#CONSTANTES

#Constantes para la ventana del juego

ANCHO_PANTALLA = 800

ALTO_PANTALLA = 600

TITULO_PANTALLA = "Super MARIO BROS ARCADE"

#Constantes para escalar los sprites (hojas png)
ESCALA_PERSONAJE = 0.20

ESCALA_TERRENO = 0.20

ESCALA_TUBERIA = 0.32

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
		self.sonido_base = arcade.load_sound("Sonidos\sonido_base.ogg")
		self.sonido_salto = arcade.load_sound("Sonidos\salto.ogg")
		#Variable del sprite jugador
		self.jugador_sprite = None

		# se usa para realizar un seguimiento de nuestro desplazamiento
		self.vista_inferior = 0
		
		self.vista_izquierda = 0
  
	def setup(self):
		self.lista_jugador = arcade.SpriteList()
		self.lista_muro = arcade.SpriteList(use_spatial_hash=True)
		self.lista_moneda = arcade.SpriteList()
		self.sonido_base = arcade.Sound("Sonidos/sonido_base.ogg",True)
		self.sonido_base.play(volume=0.4)

		#Crea el jugador
		fuente_imagen = "marioCar.png"
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

							[604, 135],
							[650, 135],
							[714, 135],
							[778, 135], #tuberia
							[842, 270],
							[906, 270],
							[970, 270],
							[1034, 270],
							[1098, 135],
							[1162, 135],
							[1226, 135], 
							             #tuberia
							[1482, 135],
							[1546, 135],
							[1610, 135],
							[1674, 135],
							[1738, 135],
							[1802, 265],#tuberia
							[1866, 265],
							[1930, 160],
							[1994, 160],
							[2058, 160],
							            #salto
							[2250, 120],
							            #tuberia
							[2506, 180],
						    [2602, 70],#tuberia y bloque
							[2666, 70],#tuberia y bloque
							[2762, 230],
							[2858, 70],#tuberia y bloque
							[2922, 70],#tuberia y bloque
							[3018, 180],
							           #tuberia
							[3274, 120]
			]
		

		for coordenadas in coordenadas_bloqueTierra:
			# añade en el terreno creado
			muro = arcade.Sprite("terreno.png", ESCALA_TERRENO)
			muro.position = coordenadas
			self.lista_muro.append(muro)

		#TUBERIAS
		coordenadas_tuberia = [ 
							#horizontal vertical

							
							[938, 120],
							[1354,120],
							[1834,365],
							[2378,120],
							[2634,170],
							[2890,170],
							[3146,120]
							
							
			]
		

		for coordenadas in coordenadas_tuberia:
			# añade las tuberias entre los bloques de terreno
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
        
		#COORDENADAS MASTIL
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


		#COORDENADAS NUBES
		coordenadas_nubes = [ 
							#horizontal vertical

							[300,  500],
							[800, 600],
							[1200, 550],
							[1600, 620],
							[2100, 600],
							[2500, 620],
							[2780, 530],       							
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
				self.sonido_salto = arcade.Sound("Sonidos/salto.ogg",True)
				self.sonido_salto.play(volume=0.4)
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
