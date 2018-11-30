using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class pawn : basePiece, pieceMoves{


    bool hasMoved = false;

    public void checkMove(int movedToX, int movedToY)
    {
        if(color == 'b')
        {
            //minus 2 for being on blacks side
            if(movedToY == currentColPos - 2 && hasMoved == true)
            {
                board.boardTiles[currentColPos, currentRowPos].GetComponent<tile>().pieceOnTile = this;
            }
            if(movedToY == currentColPos - 1)
            {
                board.boardTiles[currentColPos, currentRowPos].GetComponent<tile>().pieceOnTile = this;

            }

        }
        if(color == 'w')
        {
            if(movedToX == currentRowPos + 1 && board.boardTiles[movedToY, movedToX].GetComponent<tile>().pieceOnTile != null)
            {
                board.boardTiles[currentColPos, currentRowPos].GetComponent<tile>().pieceOnTile = this;

            }
            else
            {

                //invalid move
            }
        }


    }

	void Start () {
		
	}

    void checkMoves()
    {

    }
	

	void Update () {
		
	}
}
