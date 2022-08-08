import pygame


kernal = 3
display_dim = (450, 450)
default_font = 'freesansbold.ttf'

# interface infos Initialisations phase :
# ALWAYS: x_axis / y_axis


def intit_squares(sq_on_axis, margin=3, dim=display_dim):
    width, height = dim
    x_axis_sq, y_axis_sq = sq_on_axis  # squares on x/Y axis
    # available width/height (3px margin)
    av_width = width - ((x_axis_sq+1)*margin)
    av_height = height - ((y_axis_sq+1)*margin)
    # squares width/height :
    sq_width = av_width // x_axis_sq
    sq_height = av_height // y_axis_sq
    # return (width, height), (x_axis_sq, y_axis_sq), (sq_width, sq_height)
    return (sq_on_axis), (sq_width, sq_height), margin


sq_on_axis, sq_dim, margin = intit_squares((kernal, kernal), 3)


def draw_squares(display, grid, grids_dict, margin, nbr_square, sq_dim, colors, font):
    x_axis_sq, y_axis_sq = nbr_square
    sq_width, sq_height = sq_dim
    font_color, font_bg_color = colors['white'], colors['tumblr']
    square_color, empty_square_color = colors['yahoo'], colors['white']
    squares = []
    for y in range(y_axis_sq):
        for x in range(x_axis_sq):
            x_offset = margin*(1+x) + sq_width*x
            y_offset = margin*(1+y) + sq_height*y
            square = [x_offset, y_offset,
                      sq_width, sq_height
                      ]
            # squares.append(squar)
            # # since we put <pygame.draw.rect> then no need to store them

            grids_dict[str(y)+str(x)] = square
            if grid[y][x]:
                # draw...(....., [x, y, width, height])
                pygame.draw.rect(display, square_color, square)
                # Font #
                # create a text surface object,
                # on which text is drawn on it.
                text = font.render('{}'.format(
                    grid[y][x]), True, font_color, font_bg_color)
                # create a rectangular object for the
                # text surface object
                textRect = text.get_rect()
                # set the center of the rectangular object.
                textRect.center = (x_offset + sq_width // 2,
                                   y_offset + sq_height // 2)
                # copying the text surface object
                # to the display surface object
                # at the center coordinate.
                display.blit(text, textRect)
            else:
                pygame.draw.rect(display, empty_square_color, square)


def get_mouse_coord(mouse_pos, grids_dict):
    x_pos, y_pos = mouse_pos
    for index, square in grids_dict.items():
        line, column = int(index[0]), int(index[1])
        x_begin, y_begin, x_end, y_end, = square
        x_end += x_begin
        y_end += y_begin
        if x_begin <= x_pos <= x_end and y_begin <= y_pos <= y_end:
            return (line, column)


def init_font(font, font_size=32):
    return pygame.font.Font(font, font_size)
