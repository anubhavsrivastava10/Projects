# Rock Paper Scissor

Rock Paper Scissor is a classic old school hand game which is usally played between two people since i couldn't find myself anyone to play this with me in this quarantine I made my coputer play it with me.

## Three shapes with an outstreched hand :

**_Rock_** : Denoted by a closed fist.
**_Paper_** : Denoted by a flat hand.
**_Scissor_** : Denoted by a fist with the index finger and middle finger extended, forming a V.

## Rules

1. Rock wins over Scissor but looses over Paper.
2. Scissor wins over Paper but looses over Rock.
3. Paper wins over Rock but looses over Scissor.

Player who wins the round gets one point and incase of the same show of hands no one gets a point.
Player with the maximum point wins.

## Code Base

The code is simple and illustrates the basic if else condition for all the cases formed in the game conditions.

Input by the player are given in the form of words : like "Rock".

The player input for the choice from Rock, Paper, Scissor is taken through getpass class imported from getpass module which hides the input being taken from the screen(basically how you take password).
Then the computer chooses a compeletly random element from the list of Rock, Paper, Scissor with the help of the random module imported.
Then according to the both the input the if conditions are being checked and the scores are awarded likewise.

After every round the scores are revealed to know who is winning.

To end the game play the Player enters the "end" input which declares who scored how many points and who won by how much point difference.