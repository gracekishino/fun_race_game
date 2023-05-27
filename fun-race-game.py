# Fun Race Game

# Created by Grace Kishino 2023/05/11

# Players take it in turns to 
# roll a dice and move forward the
# number of steps shown on the dice 

# The aim is for BOTH players to 
# reach the goal in as few gos as 
# possible!

import random

class Player:
  def __init__(self, game, number, name, footprint):
    self.game = game
    self.number = number
    self.position = 1
    self.name = self.set_name(name)
    self.footprint = self.set_footprint(footprint)

  def __repr__(self):
    return "{name} has a \"{footprint}\" footprint".format(name=self.name, footprint=self.footprint)
  
  def show_position(self):
    footprints = ""
    for i in range(0,self.position):
      footprints += self.footprint
    for i in range(0,self.game.total_steps-self.position):
      footprints += "→"
    footprints += "✨ " + self.name
    return footprints

  def set_footprint(self,footprint):
    formatted_fp = footprint.strip()
    if formatted_fp == "":
      formatted_fp = self.number
    else:
      formatted_fp = formatted_fp[0]
    return formatted_fp

  def set_name(self, name):
    formatted_name = name.strip()
    if formatted_name == "":
      formatted_name = "Player " + self.number
    return formatted_name

class Game:
  def __init__(self,name="Fun Race Game",steps=25):
    self.name = name
    self.total_steps = steps
    self.players = []
    self.finished = False
    self.quit = False
    self.gos = 0
  
  def __repr__(self):
    return "\n{name} has {steps} steps! \n\nThe aim is for BOTH players to reach \nthe goal in as few gos as possible. 💖💖 \n".format(name=self.name, steps=self.total_steps)

  def player_positions(self):
    player_positions = "\n"
    for player in self.players:
      player_positions += player.show_position() + "\n"
    return player_positions

  def player_footprints(self):
    player_footprints = "\n"
    for player in self.players:
      player_footprints += player.__repr__() + "\n"
    return player_footprints

  def play(self):
    # print game details
    print(self)

    # setup player 1
    p1_name = input("Player 1, please enter your name: ")
    if not p1_name: 
      p1_name = "Player 1"
    p1_footprint = input(p1_name + ", choose a single character footprint (e.g. #): ")
    player1 = Player(self, "1", p1_name, p1_footprint)
    self.players.append(player1)

    # setup player 2
    p2_name = input("Player 2, please enter your name: ")
    if not p2_name: 
      p2_name = "Player 2"
    p2_footprint = input(p2_name + ", choose a single character footprint (e.g. *): ")
    player2 = Player(self, "2", p2_name, p2_footprint)
    self.players.append(player2)

    # print game starting info
    print(self.player_footprints())
    print(self.player_positions())
    print(self.who_starts() + " goes first!")
    
    # players have gos until both the goal
    while not self.finished and not self.quit:
      for player in self.players:
          self.have_go(player)

    # end congrats message  
    if self.finished:        
      print("\nCongratulations!!! \nCompleted in " + str(self.gos) + " gos ✨")
    else:
      print("Let's play again soon!")

  # decide who starts
  def who_starts(self):
    random.shuffle(self.players)
    return self.players[0].name 
  
  # player has a go 
  def have_go(self, player):
    if not self.finished and not self.quit and player.position < self.total_steps:
      choice = input(player.name + ", it's your go! \nPress r to roll the dice, \nor q to quit the game: ")
      while choice != 'r' and choice != 'q':
        choice = input(player.name + ", it looks like you didn't choose 'r' or 'q'. Press r to roll the dice, or q to quit the game: ")
    
      if choice == 'q':
        self.quit = True
      elif choice == 'r':
        self.gos += 1
        roll = random.randint(1,6)
        print("\nYou rolled a " + str(roll) + "!")
        player.position += roll
        if player.position > self.total_steps:
          player.position = self.total_steps
        print(self.player_positions())

    # check if game is finished
    all_players_finished = True
    for player in self.players:
      if player.position < self.total_steps:
        all_players_finished = False
    if all_players_finished:
      self.finished = True

# set up games
game1 = Game()
game2 = Game("Win Together Game",50)

# Play games
game1.play()
game2.play()

  
    
