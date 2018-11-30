using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class rook : basePiece, pieceMoves {

    public int[] getValidXMoves()
    {
        int[] validX = new int[8];
        for(int i = 0; i < currentRowPos; i++)
        {
            
        }
        return validX;
    }

    public void checkMove(int movedToX, int movedToY)
    {
        
        if(color == 'b')
        {
            
        }
        if(color == 'w')
        {

        }
    }


    // Use this for initialization
    void Start () {
		
	}
	
	// Update is called once per frame
	void Update () {
		
	}
}
