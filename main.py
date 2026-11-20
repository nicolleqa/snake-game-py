import pygame
import random
import sys

# Inicializar Pygame
pygame.init()

# Configuración de pantalla y cuadrícula
ANCHO = 600
ALTO = 400
TAMANO_CELDA = 20
FPS_INICIAL = 6  # Velocidad inicial

# Colores (RGB)
NEGRO = (15, 15, 15)
BLANCO = (255, 255, 255)
VERDE = (46, 204, 113)
VERDE_OSCURO = (39, 174, 96)
ROJO = (231, 76, 60)
AMARILLO = (241, 196, 15)
GRIS = (40, 40, 40)

# Configurar ventana y reloj
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Snake Game")
reloj = pygame.time.Clock()
fuente = pygame.font.SysFont("arial", 22, bold=True)


def generar_comida(serpiente):
    """Genera coordenadas aleatorias alineadas a la cuadrícula fuera del cuerpo."""
    while True:
        x = random.randrange(0, ANCHO, TAMANO_CELDA)
        y = random.randrange(0, ALTO, TAMANO_CELDA)
        if (x, y) not in serpiente:
            return (x, y)


def dibujar_cuadricula():
    """Dibuja una cuadrícula sutil de fondo."""
    for x in range(0, ANCHO, TAMANO_CELDA):
        pygame.draw.line(pantalla, GRIS, (x, 0), (x, ALTO))
    for y in range(0, ALTO, TAMANO_CELDA):
        pygame.draw.line(pantalla, GRIS, (0, y), (ANCHO, y))


def mostrar_texto(texto, color, x, y, centrado=False):
    superficie = fuente.render(texto, True, color)
    rect = superficie.get_rect()
    if centrado:
        rect.center = (x, y)
    else:
        rect.topleft = (x, y)
    pantalla.blit(superficie, rect)


def juego():
    serpiente = [
        (ANCHO // 2, ALTO // 2),
        (ANCHO // 2 - TAMANO_CELDA, ALTO // 2),
        (ANCHO // 2 - 2 * TAMANO_CELDA, ALTO // 2),
    ]
    direccion = (TAMANO_CELDA, 0)
    comida = generar_comida(serpiente)
    
    puntuacion = 0
    nivel = 1
    fps_actual = FPS_INICIAL
    game_over = False

    while True:
        # 1. Manejo de eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:
                if game_over:
                    if evento.key == pygame.K_SPACE:
                        juego()
                    elif evento.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                else:
                    if evento.key == pygame.K_UP and direccion != (0, TAMANO_CELDA):
                        direccion = (0, -TAMANO_CELDA)
                    elif evento.key == pygame.K_DOWN and direccion != (0, -TAMANO_CELDA):
                        direccion = (0, TAMANO_CELDA)
                    elif evento.key == pygame.K_LEFT and direccion != (TAMANO_CELDA, 0):
                        direccion = (-TAMANO_CELDA, 0)
                    elif evento.key == pygame.K_RIGHT and direccion != (-TAMANO_CELDA, 0):
                        direccion = (TAMANO_CELDA, 0)

        if not game_over:
            # 2. Actualizar posición
            cabeza_x, cabeza_y = serpiente[0]
            nueva_cabeza = (cabeza_x + direccion[0], cabeza_y + direccion[1])

            # 3. Verificar colisiones
            if (
                nueva_cabeza[0] < 0
                or nueva_cabeza[0] >= ANCHO
                or nueva_cabeza[1] < 0
                or nueva_cabeza[1] >= ALTO
                or nueva_cabeza in serpiente
            ):
                game_over = True
            else:
                serpiente.insert(0, nueva_cabeza)

                # Verificar si comió
                if nueva_cabeza == comida:
                    puntuacion += 10
                    comida = generar_comida(serpiente)

                    # --- LÓGICA DE NIVELES Y VELOCIDAD ---
                    # Sube de nivel cada 50 puntos (5 comidas)
                    nuevo_nivel = (puntuacion // 20) + 1
                    if nuevo_nivel > nivel:
                        nivel = nuevo_nivel
                        fps_actual += 2  # Aumenta velocidad en 2 FPS por nivel
                else:
                    serpiente.pop()

        # 4. Dibujar en pantalla
        pantalla.fill(NEGRO)
        dibujar_cuadricula()

        # Dibujar comida
        pygame.draw.rect(
            pantalla, ROJO, (comida[0], comida[1], TAMANO_CELDA, TAMANO_CELDA), border_radius=5
        )

        # Dibujar serpiente
        for i, segmento in enumerate(serpiente):
            color = VERDE if i == 0 else VERDE_OSCURO
            pygame.draw.rect(
                pantalla, color, (segmento[0], segmento[1], TAMANO_CELDA, TAMANO_CELDA), border_radius=4
            )

        # Mostrar puntuación y nivel actual
        mostrar_texto(f"Puntos: {puntuacion}", BLANCO, 10, 10)
        mostrar_texto(f"Nivel: {nivel}", AMARILLO, ANCHO - 110, 10)

        if game_over:
            mostrar_texto("GAME OVER", ROJO, ANCHO // 2, ALTO // 2 - 30, centrado=True)
            mostrar_texto(
                f"Alcanzaste el Nivel {nivel} con {puntuacion} puntos",
                AMARILLO,
                ANCHO // 2,
                ALTO // 2 + 5,
                centrado=True,
            )
            mostrar_texto(
                "Presiona ESPACIO para reiniciar o 'ESC' para salir",
                BLANCO,
                ANCHO // 2,
                ALTO // 2 + 40,
                centrado=True,
            )

        pygame.display.flip()
        reloj.tick(fps_actual)  # Usa la velocidad dinámica


if __name__ == "__main__":
    juego()