import pygame
import sys

# Inicializar Pygame
pygame.init()

ANCHO = 800
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Jonatha Pertuz")

color_fondo = (70, 130, 180)
fuente = pygame.font.Font(None, 60)

# Variable para guardar el texto que escribas
texto_actual = ""
mensaje_ayuda = "Escribe y presiona ENTER para confirmar"

ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        
        # Cuando presionas una tecla
        if evento.type == pygame.KEYDOWN:
            # Si presionas ENTER → queda guardado
            if evento.key == pygame.K_RETURN:
                pass  # Solo deja el texto escrito
            # Si presionas BORRAR → elimina una letra
            elif evento.key == pygame.K_BACKSPACE:
                texto_actual = texto_actual[:-1]
            # Cualquier otra tecla → agrega la letra
            else:
                # Limitar a 30 caracteres máximo
                if len(texto_actual) < 30:
                    texto_actual += evento.unicode
    
    # Dibujar todo
    pantalla.fill(color_fondo)
    
    # Texto de ayuda arriba
    ayuda = fuente.render(mensaje_ayuda, True, (200, 200, 200))
    ayuda_rect = ayuda.get_rect(center=(ANCHO // 2, 80))
    pantalla.blit(ayuda, ayuda_rect)
    
    # Tu texto en el centro
    superficie_texto = fuente.render(texto_actual, True, (255, 255, 255))
    texto_rect = superficie_texto.get_rect(center=(ANCHO // 2, ALTO // 2))
    pantalla.blit(superficie_texto, texto_rect)
    
    pygame.display.flip()

pygame.quit()
sys.exit()