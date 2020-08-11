from game_class import *

g = game()
g.start_screen()
while g.running:
    g.new()
    g.game_over_screen()

pygame.quit()
print('Game closed')
