using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.IO;

public class determinePlayer : MonoBehaviour
{

    int player = 0;

    // Use this for initialization
    void Start()
    {
        StreamReader reader = new StreamReader("players.txt");
        player = System.Convert.ToInt32(reader.ReadLine());
        

    }

    // Update is called once per frame
    void Update()
    {

    }
}
