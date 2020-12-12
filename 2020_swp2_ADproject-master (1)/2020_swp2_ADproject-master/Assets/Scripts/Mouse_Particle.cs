using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Mouse_Particle : MonoBehaviour {

    public GameObject Pt;
	// Update is called once per frame
	void Update ()
    {
		if(Input.GetMouseButton(0))
        {
            Vector3 vec = Camera.main.ScreenToWorldPoint(Input.mousePosition);
            vec.z = Pt.transform.position.z;
            Pt.transform.localPosition = vec;
        

        }
    }

   
}
