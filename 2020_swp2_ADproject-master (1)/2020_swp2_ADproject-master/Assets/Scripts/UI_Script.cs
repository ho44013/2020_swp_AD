using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;
public class UI_Script : MonoBehaviour
{
    public GameObject stageButton;

    public int NowIndex;
    public Text bestScore;
    public Text[] mission_texts = new Text[3];
    private void Awake()
    {
        Screen.SetResolution(1280, 720, true);
        SoundManager.Instance.PlayBackground("Background");
    }
    private void Start()
    {
        for(int i=0;i<5;i++)
        {
            stageButton.transform.GetChild(i).GetChild(1).gameObject.SetActive(Singleton.Instance.maxSelectLevel < i);

        }
    }
    public void Go_Arcade_Mode()
    {
        Singleton.Instance.gameType = GameType.Arcade;
        Debug.Log("GO_ARCADE_MODE");
    }

    public void Go_VS_Computer_Mode()
    {
        Singleton.Instance.gameType = GameType.Computer;
        Debug.Log("GO_COMPUTER_MODE");
    }

    public void Go_TimeAttack_Mode()
    {
        Singleton.Instance.gameType = GameType.TimeAttack;
        bestScore.text = "Best Score : "+PlayerPrefs.GetInt("BestScore").ToString();
    }

    public void Exit()
    {
        Application.Quit();
    }

    public void Select_Mission(int index)
    {
        NowIndex = index;
        switch (index)
        {
            case 1:
                mission_texts[0].text = "Mission 1 : 게임 클리어";
                mission_texts[1].text = "mission 2 : 콤보 3 이상";
                mission_texts[2].text = "mission 3 : 20초 이내 클리어";
                break;
            case 2:
                mission_texts[0].text = "Mission 1 : 게임 클리어";
                mission_texts[1].text = "mission 2 : 콤보 5 이상";
                mission_texts[2].text = "mission 3 : 20초 이내 클리어";
                break;
            case 3:
                mission_texts[0].text = "Mission 1 : 게임 클리어";
                mission_texts[1].text = "mission 2 : 콤보 5 이상";
                mission_texts[2].text = "mission 3 : 25초 이내 클리어";
                break;
            case 4:
                mission_texts[0].text = "mission 4 text 0";
                mission_texts[1].text = "mission 4 text 1";
                mission_texts[2].text = "mission 4 text 2";
                break;
            case 5:
                mission_texts[0].text = "mission 5 text 0";
                mission_texts[1].text = "mission 5 text 1";
                mission_texts[2].text = "mission 5 text 2";
                break;
        }
      
    }

    public void Start_Mission()
    {
        if (Singleton.Instance.maxSelectLevel >= NowIndex - 1)
        {
            Singleton.Instance.selectLevel = NowIndex - 1;
            switch (NowIndex)
            {
                case 1:
                    Debug.Log("START_MISSION1111111111111");

                    break;
                case 2:
                    Debug.Log("START_MISSION22222222222");

                    break;
                case 3:
                    Debug.Log("START_MISSION333333333333");

                    break;
                case 4:
                    Debug.Log("START_MISSION444444444444");

                    break;
                case 5:
                    Debug.Log("START_MISSION5555555555");

                    break;
            }
            UnityEngine.SceneManagement.SceneManager.LoadScene(1);
        }
    }

    public void Start_TimeAttack()
    {
        UnityEngine.SceneManagement.SceneManager.LoadScene(1);
        Debug.Log("START_TIMEATTACK");
    }
    public void SetBackgroundVolume(Slider slider)
    {
        SoundManager.Instance.SetBackgroundVolume(slider.value);
    }
    public void SetEffectVolume(Slider slider)
    {
        SoundManager.Instance.SetEffectVolume(slider.value);
    }
}
