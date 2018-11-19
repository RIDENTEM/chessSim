using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class board : MonoBehaviour
{

    [SerializeField] GameObject tile;

    void generateBoard()
    {
        float xPos = -3.0f;
        float yPos = 3.0f;
        Vector3 whereToSpawn;
        bool opp = false;
        for (int i = 0; i < 8; i++, yPos -= 0.5f)
        {
            for (int j = 0; j < 8; j++, xPos += 0.5f)
            {
                if (opp == false)
                {
                    if (j % 2 == 0)
                    {
                        tile.GetComponent<SpriteRenderer>().color = Color.white;
                    }
                    else
                        tile.GetComponent<SpriteRenderer>().color = Color.black;
                }
                else
                {
                    if (j % 2 == 0)
                    {
                        tile.GetComponent<SpriteRenderer>().color = Color.black;
                    }
                    else
                        tile.GetComponent<SpriteRenderer>().color = Color.white;


                }

                whereToSpawn = new Vector3(xPos, yPos, 0.0f);
                Instantiate(tile, whereToSpawn, Quaternion.identity);
            }
            xPos = -3.0f;
            if (opp == false)
                opp = true;
            else
                opp = false;

        }

    }


    // Use this for initialization
    void Start()
    {
        generateBoard();
    }

    // Update is called once per frame
    void Update()
    {

    }
}
