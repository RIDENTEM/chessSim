using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class tile : MonoBehaviour
{

    public Collider2D tileCollider;
    public SpriteRenderer tileColor;
    public basePiece pieceOnTile = new basePiece();



    private void Awake()
    {
        tileCollider = GetComponent<Collider2D>();
        tileColor = GetComponent<SpriteRenderer>();
    }

    void onTileClick()
    {
        //  this.gameObject.GetComponent<Sprite>().texture.
    }

    private void OnGUI()
    {

    }

}
