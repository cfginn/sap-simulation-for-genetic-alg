from pysapets.animal import Animal
import pysapets.constants as constants
import random


# define ant class to inherit from animal class

class Ant(Animal):
  # base health and attack values
  BASE_HEALTH = 1
  BASE_ATTACK = 2
  
  def __init__(self, addAttack = 0, addHealth = 0):
    # ability: upon death, randomly give a friend a buff acording to level
    # lvl 1: +2 attack, +1 health
    # lvl 2: +4 attack, +2 health
    # lvl 3: +6 attack, +3 health
    def _run_effect(self, friends):
      if all(friend.dead for friend in friends):
        print("{}".format(constants.ERROR_ALL_FRIENDS_DEAD))

      elif self.dead:
        # select random friend not dead
        friend = random.choice([f for f in friends if not f.dead and f != self])
        attack_buff = self.level * 2
        health_buff = self.level

        # apply buff
        friend.add_attack(attack_buff)
        friend.add_health(health_buff)

      else:
        print("{}".format(constants.ERROR_STILL_ALIVE))
    
    # create ability
    self.ability = Animal.Ability(self, constants.FAINT, constants.SELF, _run_effect)

    super().__init__(addAttack + self.BASE_ATTACK, addHealth + self.BASE_HEALTH, animalType = constants.ANT, tier = 1, ability=self.ability)

