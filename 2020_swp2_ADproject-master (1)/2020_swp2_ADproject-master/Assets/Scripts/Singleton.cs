using System.Collections;
using System.Collections.Generic;
using UnityEngine;
public enum GameType
{
    Arcade,TimeAttack,Computer
}
public class Singleton  {
    public int selectLevel = 0;
    public int computerLevel = 0;
    public int maxSelectLevel = PlayerPrefs.GetInt("MaxSelectLevel");
    public int[] stageCombo = { 3, 5, 5, 6, 6 };
    public int[] stageTimer = { 20, 20, 25, 25, 25 };
    public GameType gameType=GameType.Computer;
    private static Singleton instance = null;

    public static Singleton Instance
    {
        get
        {
            if (instance == null)
                instance = new Singleton();
            return instance;
        }
    }
}
