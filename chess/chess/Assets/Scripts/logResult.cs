using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.IO;

public class logResult : MonoBehaviour
{


    void writeResult()
    {
        StreamWriter writer = new StreamWriter("results.txt");
        //if (white.checkmate)
            writer.WriteLine("True");
       // else
            writer.WriteLine("False");
    }

    // Use this for initialization
    void Start()
    {

    }

    // Update is called once per frame
    void Update()
    {

    }
}
