def draw_spiral():

    if (start == end) :

        return

    else:

        while(next_is_not_blocked):

            move_forward()

        turn_right()

        draw_spiral()

draw_spiral()
