import pygame
from game_lib import *
from game_interface import *
from time import time, sleep

# #########################################################
# The imported settings are: 
# from game_lib:
# pause, game_over, quit_game,
# computer_turn, waiting_time, colors

# from game_interface: 
# kernal, display_dim, default_fon, sq_on_axis, sq_dim, margin
# #########################################################
# Initialization :
grids_dict = {}
winner = None
action_index = 0

# Grid Initialisations phase :
initial_state = Grid.get_random_grid()
state = initial_state.copy()
print(state.grid)
starting_time = time()
path = solution(Node(initial_state.copy()))
print('Solution time:', time()-starting_time, ' Sec')
print('>> path:', path)

# ####################################################################
# Game Initialisations phase :
pygame.init()
display = pygame.display.set_mode(display_dim)  # I named this as display
# Game name (caption) and icon:
pygame.display.set_caption('8-Puzzle game')
pygame_icon = pygame.image.load('images/8-puzzle icon 3.png')
pygame.display.set_icon(pygame_icon)

display.fill(colors['white'])
pygame.display.flip()
# # Font Initialisations phase :
font = init_font(default_font)
draw_squares(display, initial_state.grid, grids_dict,
             margin, sq_on_axis, sq_dim, colors, font)
pygame.display.update()
# ####################################################################
starting_time = time()

# MAIN LOOP
while not game_over and not quit_game:
    draw_squares(display, state.grid, grids_dict, margin,

                 sq_on_axis, sq_dim, colors, font)
    pygame.display.update()

    if state.solved:
        game_over = True
        winner = 'COMPUTER' if computer_turn else 'PLAYER'
        break

    for event in pygame.event.get():
        # print(event)  # prints out all the actions that take place on the screen
        if event.type == pygame.KEYDOWN:
            # KEYDOWN EVENTS:
            # p ==> pause
            # t ==> computer/PLAYER turn
            # print(">> Random Key has been pressed <<")
            if event.key == pygame.K_p:
                print(">> PAUSE !!!")
                pause = not pause
            elif event.key == pygame.K_t:
                #
                if not computer_turn:
                    initial_state = Grid(state.grid)
                    path = solution(Node(initial_state))
                    action_index = 0
                #
                computer_turn = not computer_turn
                # we can put this line befor the if in here.

        if event.type == pygame.MOUSEBUTTONDOWN:
            # KEYDOWN EVENTS:
            if pause:
                print('>> GAME PAUSED !!')
            elif computer_turn:
                print('>> Computer turn !!')
            else:
                mouse_pos = pygame.mouse.get_pos()
                mouse_coord = get_mouse_coord(mouse_pos, grids_dict)
                if mouse_coord and state.can_move(mouse_coord):
                    print('>> IT CAN MOVE!')
                    state = state.make_move(None, mouse_coord)[0]
                else:
                    print('>> IT CAN\'T MOVE !!!')

    if event.type == pygame.QUIT:
        quit_game = True
    if pause:  # it need's to be here to catch KEYDOWN
        continue
    if computer_turn:
        state = state.make_action(path[action_index])
        action_index += 1
        pygame.time.wait(waiting_time)
        # grid = next_move(grid, path)
        # this used to consult the path and made the next move in it


print('Time ==>', time()-starting_time)
if quit_game:
    print('{:<5}{:<21}{:>21}'.format('', '>'*19, '<'*19))
    print('{:<5}{:<3}{:^36}{:>3}'.format('', '>>>', 'GAME QUITED!!', '<<<'))
    print('{:<5}{:<3}{:^36}{:>3}'.format(
        '', '>>>', 'BETTER LUCK NEXT TIME X)) !!!', '<<<'))
    print('{:<5}{:<21}{:>21}'.format('', '>'*19, '<'*19))
elif winner == 'COMPUTER':
    print('{:<5}{:<21}{:>21}'.format('', '>'*19, '<'*19))
    print('{:<5}{:<3}{:^36}{:>3}'.format(
        '', '>>>', 'COMPUTER HAVE WON !!!', '<<<'))
    print('{:<5}{:<3}{:^36}{:>3}'.format(
        '', '>>>', 'BETTER LUCK NEXT TIME X)) !!!', '<<<'))
    print('{:<5}{:<3}{:^36}{:>3}'.format(
        '', '>>>', 'number_of_steps: '+str(action_index), '<<<'))
    print('{:<5}{:<21}{:>21}'.format('', '>'*19, '<'*19))
else:
    print('{:<5}{:<21}{:>21}'.format('', '>'*19, '<'*19))
    print('{:<5}{:<3}{:^36}{:>3}'.format('', '>>>', 'YOU HAVE WON !!!', '<<<'))
    print('{:<5}{:<3}{:^36}{:>3}'.format('', '>>>', 'CONGRATS !!!', '<<<'))
    print('{:<5}{:<21}{:>21}'.format('', '>'*19, '<'*19))

sleep(4)
pygame.quit()
quit()
