import pygame
from sys import exit
from random import randint

def display_score():
    current_time = int(pygame.time.get_ticks()/1000) - start_time
    score_surf = test_font.render(f"SCORE : {current_time}", False, (64, 64, 64))
    score_rect = score_surf.get_rect(center = (400, 50))
    screen.blit(score_surf, score_rect)
    return current_time

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5

            if obstacle_rect.bottom == 300:
                screen.blit(snail_surface, obstacle_rect)
            else:
                screen.blit(fly_surface, obstacle_rect)
        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
        return obstacle_list
    else:
        return []

def collisions(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):
                return False
    return True

def player_animation():
    global player_surf, player_index
    if player_rect.bottom < 300:
        player_surf = player_jump
    else:
        player_index += 0.1
        player_surf = player_walk[int(player_index) % 2]
    # walking animation if player is on floor
    # jump animation if player is not on floor

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('PLATFORM JUMPER')
clock = pygame.time.Clock()
test_font = pygame.font.Font('fonts/Pixeltype.ttf', 50)
game_active = False
start_time = 0
score = 0

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

# score_surf = test_font.render('My Game', False, 'Black')
# score_rect = score_surf.get_rect(center = (400, 50))

# obstacles
snail_frame1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_frame2 = pygame.image.load('graphics/snail/snail2.png').convert_alpha()
snail_frames = [snail_frame1, snail_frame2]
snail_frame_index = 0
# snail_x_pos = 600
snail_surface = snail_frames[snail_frame_index]
# snail_rect = snail_surface.get_rect(midbottom = (snail_x_pos, 300))

fly_frame1 = pygame.image.load('graphics/fly/Fly1.png').convert_alpha()
fly_frame2 = pygame.image.load('graphics/fly/Fly2.png').convert_alpha()
fly_frame_index = 0
fly_frames = [fly_frame1, fly_frame2]
fly_surface = fly_frames[fly_frame_index]

obstacle_rect_list = []


player_walk_1 = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_walk_2 = pygame.image.load('graphics/player/player_walk_2.png').convert_alpha()
player_walk = [player_walk_1, player_walk_2]
player_index = 0
player_jump = pygame.image.load('graphics/player/jump.png').convert_alpha()
player_surf = player_walk[player_index]
player_rect = player_surf.get_rect(midbottom = (80, 300))
player_gravity = 0

# for game over menu
player_stand = pygame.image.load('graphics/player/player_stand.png').convert_alpha()
player_stand_scaled = pygame.transform.scale2x(player_stand)
player_stand_rect = player_stand_scaled.get_rect(center = (400, 200))

game_over_font = pygame.font.Font('fonts/Pixeltype.ttf', 60)
game_over_surf = game_over_font.render('PLATFORM JUMPER!', False, (111, 196, 169))
game_over_rect = game_over_surf.get_rect(center = (400, 60))

game_restart_font = pygame.font.Font('fonts/Pixeltype.ttf', 40)
game_restart_surf = game_restart_font.render('PRESS \'SPACE\' TO RESTART', False, (111, 196, 169))
game_restart_rect = game_restart_surf.get_rect(center=(400, 350))

# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500) # trigger obstacle timer at every 900 ms

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 500)
fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 200)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            # player jump
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom == 300:
                    player_gravity = -20
            # jump if mouse clicked on player
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == pygame.BUTTON_LEFT:
                    mouse_pos = pygame.mouse.get_pos()
                    if player_rect.collidepoint(mouse_pos) and player_rect.bottom == 300:
                        player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == K_SPACE:
                game_active = True
                # snail_rect.x = 800
                start_time = int(pygame.time.get_ticks() / 1000)
        if game_active:
            # obstacle timer
            if event.type == obstacle_timer:
                if randint(0, 2):
                    obstacle_rect_list.append(snail_surface.get_rect(bottomright = (randint(900, 1100), 300)))
                else:
                    obstacle_rect_list.append(fly_surface.get_rect(bottomright=(randint(900, 1100), 210)))
            # snail timer
            if event.type == snail_animation_timer:
                if snail_frame_index == 0: snail_frame_index = 1
                else: snail_frame_index = 0
                snail_surface = snail_frames[snail_frame_index]
            # fly timer
            if event.type == fly_animation_timer:
                if fly_frame_index == 0: fly_frame_index = 1
                else: fly_frame_index = 0
                fly_surface = fly_frames[fly_frame_index]



    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        # pygame.draw.rect(screen, '#c0e8ec', score_rect)
        # pygame.draw.rect(screen, '#c0e8ec', score_rect, 10)  # drawing a rect beneath the text
        # screen.blit(score_surf, score_rect)
        score = display_score()

        '''
        # snail
        snail_rect.x -= 5
        if snail_rect.right < 0:
            snail_rect.left = 800
        screen.blit(snail_surface, snail_rect)
        '''

        # player
        screen.blit(player_surf, player_rect)
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom > 300:
            player_rect.bottom = 300
        player_animation()

        # Obstacle movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        # collisions
        game_active = collisions(player_rect, obstacle_rect_list)
    else:
        player_rect.midbottom = (80, 300)
        player_gravity = 0
        obstacle_rect_list.clear()
        screen.fill((94, 129, 162))
        screen.blit(game_over_surf, game_over_rect)
        screen.blit(player_stand_scaled, player_stand_rect)
        screen.blit(game_restart_surf, game_restart_rect)
        score_message = test_font.render(f'Your Score : {score}', False, 'White')
        score_message_rect = score_message.get_rect(center=(400, 310))
        if score > 0:
            screen.blit(score_message, score_message_rect)




    # # Check for collision
    # # We just need to check if player-rect collides with the snail-rect using collide_rect method
    # if player_rect.colliderect(snail_rect):
    #     print('collisions')

    pygame.display.update()
    clock.tick(60)

