from math import sqrt


def balls_collide(ball_1, ball_2):
    if ball_1[3] < 0 or ball_2[3] < 0:
        raise ValueError("radius must be >= 0")
    length = sqrt((ball_1[0] - ball_2[0])**2 + (ball_1[1] - ball_2[1])**2 + (ball_1[2] - ball_2[2])**2)
    if length > ball_1[3] + ball_2[3]:
        return False
    else:
        return True
