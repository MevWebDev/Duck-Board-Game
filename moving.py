
from init import ladder_sound,wind_sound,rip_sound,x2_sound
def checkSquare(player_pos,dice_number):
   if player_pos in [7, 24, 35, 48, 62]:
      x2_sound.play()
      player_pos += dice_number
      if player_pos > 68:
          player_pos = 68
   if player_pos == 61:
       player_pos = 0
       rip_sound.play()
       return player_pos
   if player_pos == 47:
       ladder_sound.play()
       player_pos = 65
       return player_pos
   if player_pos == 15:
       wind_sound.play()
       player_pos = 10
       return player_pos
   return player_pos