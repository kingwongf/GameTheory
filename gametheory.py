import numpy as np

## Problem Statement 
# A game involves a player and the house who play either "H" or "T" and each round. 
# Player's payoff HH = 3, HT/TH = -2 and TT = 1
# Find the optimal strategy for 1. the player 2. the house

## let P_player_H be the probability of the player playing "H" , P_house_H be the probability of the house playing "H" and B be the number of rounds 
class Game():
	def __init__(self, P_house_H, P_player_H, B):

		self.player_wealth = 0
		self.house_wealth = 0
		self.P_player_H = P_player_H
		self.P_house_H = P_house_H
		self.B = B


	def game(self,player, house):
		
		for i in range(self.B):
			if player[i] == 'T' == house[i]:
				self.player_wealth+= 1
				self.house_wealth-=1
			elif player[i] == 'H' == house[i]:
				self.player_wealth+=3
				self.house_wealth-=3
			else:
				self.player_wealth-=2
				self.house_wealth+=2

	def main(self):

		player = np.random.choice(['H', 'T'], self.B, p=[self.P_player_H, 1-self.P_player_H])
		house = np.random.choice(['H', 'T'], self.B, p=[self.P_house_H,1-self.P_house_H])

		self.game(player,house)

		print("player's wealth ", self.player_wealth, "house's wealth ", self.house_wealth)

# if __name__ == "__main__":
# 	A = Game(0, 0, 1000)
# 	A.main()

