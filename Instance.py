#Instance.py
#Created: 2 / 8 / 2022 (MM/DD/YYYY)
#Author: Robert B.
#Summary:
#The definition of an Instance: includes control logic for ensuring that the turn player is the only one who can
#change the state of the game.  Also defines the Player class, which simplifies how the system keeps track of each
#users' information in memory.

from Stones import SixteenStones
import random

class Instance:
	#The definition of an Instance.
	#Instances have 3 essential properties:
	#	1) The game itself.
	#	2) The players playing the game.
	#	3) A string output for each action.
	#
	#When initialized, an Instance must have 2 players (defined by thier Username & ID).
	#After an action has been performed through any of its functions (including its initializer), the 'outputString'
	#will be updated.  This value must be retreived after every action to show the game status.
	
	#Initializer
	def __init__(this,player1,player2):
		this.game=SixteenStones()
		this.players=[player1,player2]
		
		this.outputString="Game has started between ["+this.players[0].username+"] and ["+this.players[1].username+"]\n"
		this.outputString+=this.generateBoardGraphics()
	#end function __init__(self,Player,Player)

	#Internal Function(s)

	#self.generateBoardGraphics(self):
	#Creates the graphical output of the board.  Is called in other Instance functions to update the 'outputString' value.
	def generateBoardGraphics(this):
		returnThis=""
		
		if this.game.getBoardSum()!=1:
			returnThis+="Turn: "+str(this.game.getTurn())+", Player "+str(this.game.getTurnPlayer())+" ["+this.players[this.game.getTurnPlayer()-1].username+"], go.\n" 

		stones=["o","O","0"]
		
		rows=len(this.game.getBoard())
		
		for i in range(rows):
			returnThis+=str(i+1)+") "
			for j in range(this.game.getBoard()[i]):
				returnThis+=stones[1]+" "
			returnThis+="\n"
		
		return returnThis.strip()
	#end function generateBoardGraphics(self)
				
	#move(self,Player,int,int)
	#Much like the move function in the SixteenStones class, the move function of Instance attempts to make a
	#play for a user.  There are a few checks that occur here, such as the state of the game (finished or ongoing),
	#as well as which player in this instance is allowed to make a play.
	#
	#'player' refers to the player attempting to make a play.  'row' is the selected row that the player is choosing,
	#whereas 'num' is the amount of stones that they are attempting to take from the selected 'row'.
	def move(this,player,row,num):
		this.outputString=""
		
		turnPlayer=this.game.getTurnPlayer()-1

		if player.id!=this.players[turnPlayer].id:
			this.outputString+="It is not your turn, "+player.username+"."
		else:	
			result,resultMessage=this.game.move(row-1,num)	#The row input is supposed to be the index of the gameBoard
															#value in this game.  The player is expected to input a value
															#offset from the index by 1, thus the correction is made here.
			
			if this.game.getBoardSum()==1:
				this.outputString="Game over.\n["+this.players[turnPlayer].username+"] wins!\n"+this.generateBoardGraphics()
			else:			
				if result:
					this.outputString=this.generateBoardGraphics()
				else:
					this.outputString=resultMessage
	#end function move(self,Player,int,int)

	def hasPlayer(this,playerID):
		if playerID==this.player1.id or playerID==this.player2.id:
			return True
		else:
			return False
	#end function hasPlayer(int)
#END CLASS: Instance

class Player:
	#The definition of Player:
	#A player is composed of both the int userID and string username of a Discord user.  This exists to simplify how
	#an Instance stores the values of a player.

	#Initializer
	def __init__(this,id,username):
		this.id=id
		this.username=username
	#end __init__(self,int,string)

#END CLASS: Player

#EVERYTHING BELOW THIS LINE IS ONLY USED TO TEST THE CODE ABOVE.
#---------------------------------------------------------------

def main():
	print("Terst.\n")
	player1=Player(0,"xXplayer1Xx")
	player2=Player(1,"Player_2")
	
	runningInstance=Instance(player1,player2)
	
	print(runningInstance.outputString)
	
	move=[5,1]
	print(player1.username+": move "+str(move[0])+" "+str(move[1]))
	runningInstance.move(player1,move[0],move[1])
	print(runningInstance.outputString)
	
	move=[5,1]
	print(player1.username+": move "+str(move[0])+" "+str(move[1]))
	runningInstance.move(player1,move[0],move[1])
	print(runningInstance.outputString)
	
	move=[5,1]
	print(player2.username+": move "+str(move[0])+" "+str(move[1]))
	runningInstance.move(player2,move[0],move[1])
	print(runningInstance.outputString)
	
	move=[2,4]
	print(player2.username+": move "+str(move[0])+" "+str(move[1]))
	runningInstance.move(player2,move[0],move[1])
	print(runningInstance.outputString)
	
	runningInstance.move(player1,4,2)
	runningInstance.move(player2,1,6)
	
	print("\n...Some inputs later...\n")
	
	move=[2,-1]
	print(player1.username+": move "+str(move[0])+" "+str(move[1]))
	runningInstance.move(player1,move[0],move[1])
	print(runningInstance.outputString)
	
	move=[3,3]
	print(player1.username+": move "+str(move[0])+" "+str(move[1]))
	runningInstance.move(player1,move[0],move[1])
	print(runningInstance.outputString)
	
	move=[3,2]
	print(player1.username+": move "+str(move[0])+" "+str(move[1]))
	runningInstance.move(player1,move[0],move[1])
	print(runningInstance.outputString)
	
if __name__=="__main__":
	main()