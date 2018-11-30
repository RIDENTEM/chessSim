using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class basePiece {

    Sprite pieceSprite;
    string pieceType;
    public int currentRowPos;
    public int currentColPos;
    protected int movedToRowPos;
    protected int movedToColPos;
    bool validMove;
    //if color = w, white
    //if color = b, black
   protected char color;

    

    
    

    

	// Use this for initialization
	void Start () {
		
	}
	
	// Update is called once per frame
	void Update () {
		
	}
}
