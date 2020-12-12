using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class User
{
    public Vector2Int position;
    public GameObject[,] filedBlock;
    public int[,] filed;
    public bool[,] filedSelect;
    public int[] list;
    public int selectIndex;
    public int clear = 0;
    public int stack = 0;
    public GameObject selectBlock;
    public GameObject charater;
    public GameObject mask;
    public LineRenderer line;
    public ParticleSystem lineEffect;
    public SpriteRenderer background;
}

public class GameManager : MonoBehaviour
{
    [Range(0, 1)]
    public float value;
    public Material TransitionMaterial;
    //Sprite 
    public Sprite selectSprite;
    public Sprite[] block;

    //블럭
    private const float blockSize = 1.875f;

    [Header("Player")]
    public GameObject player;
    public User playerUser;

    [Header("Ai")]
    public GameObject computer;
    public User computerUser;

    //필드
    private Vector2 position = new Vector2(-300, 64);
    private Vector2Int filedSize = new Vector2Int(5, 14);
    private List<int[,]> fileds;
    public  List<Stack<Vector2Int>> nextMove;
    //입력
    private Vector2 begin;
    private Vector2 end;
    Color[,] colors = new Color[6, 2]
    {
        { Color.red, Color.white },
        { Color.yellow, Color.white },
        { Color.green, Color.white },
        { Color.blue, Color.white },
        { Color.magenta, Color.white },
        { Color.gray, Color.white }
    };

    //UI
    private bool playGame;
    private int comboBest;
    private int combo;
    private float comboTimer;
    private float time;
    private int score;

    public Image timerImage;
    public Image playerImage;
    public Image computerImage;
    [Header("Arcade")]
    public Sprite[] arcadeImage;
    public GameObject arcadeClear;

    [Header("Panel")]
    public Animator starAnimator;
    public GameObject pausePanel;
    public GameObject winPanel;
    public GameObject lostPanel;
    [Header("Text")]
    public Text comboText;
    public Text timeText;
    public Text clearText;

    private void Start()
    {
        playGame = true;
        playerUser = new User();
        StartGame(player, playerUser, new Vector2(position.x, position.y), 0);
        
        switch (Singleton.Instance.gameType) {
            case GameType.Arcade:
                comboText.gameObject.SetActive(true);
                timeText.gameObject.SetActive(true);
                clearText.gameObject.SetActive(false);
                LoadMap(playerUser);
                break;
            case GameType.TimeAttack:
                timerImage.transform.parent.gameObject.SetActive(true);
                timerImage.gameObject.SetActive(true);
                comboText.gameObject.SetActive(true);
                timeText.gameObject.SetActive(true);
                clearText.gameObject.SetActive(true);

                CreateMap(playerUser);
                break;
            case GameType.Computer:
                fileds = new List<int[,]>();

                nextMove = new List<Stack<Vector2Int>>();
                computerUser = new User();
                playerImage.transform.parent.gameObject.SetActive(true);
                playerImage.gameObject.SetActive(true);
                computerImage.gameObject.SetActive(true);
                computer.SetActive(true);

                StartGame(computer, computerUser,new Vector2(-position.x, position.y),filedSize.x-1);
                for (int a = 0; a < 32; a++)
                {
                    nextMove.Add(new Stack<Vector2Int>());
                    fileds.Add(new int[filedSize.y, filedSize.x]);
                    for (int i = 0; i < 10; i++)
                    {
                        int color = Random.Range(1, 7);

                        for (int j = 0; j < 3; j++)
                        {
                            int x, y = 1;

                            do
                            {
                                x = Random.Range(0, 5);
                                if (fileds[a][1, x] == 0)
                                    break;
                            }
                            while (true);

                            for (y = 1; y < filedSize.y - 1; y++)
                            {
                                if (fileds[a][y + 1, x] != 0)
                                {
                                    break;
                                }
                            }
                            nextMove[a].Push(new Vector2Int(x, y));
                            fileds[a][y, x] = color;
                        }
                    }
                }
                CreateMap(playerUser,0);
                CreateMap(computerUser,0);
                StartCoroutine("ComputerManager");
                break;
        };
        StartCoroutine("StartAnimation");
    }
    private void Update()
    {

        if (Input.GetKeyDown(KeyCode.Escape))
        {
            playGame = !playGame;
            pausePanel.SetActive(!playGame);
        }
        if (playGame)
        {
            playerUser.charater.transform.position = playerUser.filedBlock[playerUser.position.y, playerUser.position.x].transform.position;

            MouseClick();

            playerUser.position.x = Mathf.Clamp(playerUser.position.x, 0, 4);
            playerUser.line.SetPosition(1, playerUser.filedBlock[0, playerUser.position.x].transform.position);
            playerUser.line.SetPosition(0, playerUser.filedBlock[filedSize.y - 1, playerUser.position.x].transform.position);
            switch (Singleton.Instance.gameType)
            {
                case GameType.Arcade:
                    comboText.text = "Combo : " + combo;
                    timeText.text = "Time : " + (int)(time);
                    comboTimer += Time.deltaTime;
                    if(comboTimer>=3.5f)
                    {
                        combo = 0;
                    }
                    break;
                case GameType.TimeAttack:
                    comboText.text = "Combo : " + combo;
                    timeText.text = "Time : " + (int)((60 * 3) - time);
                    clearText.text = "Clear : " + score;
                    if (time >= 60 * 3)
                    {
                        PlayerPrefs.SetInt("BestScore", score);
                        playGame = false;
                        arcadeClear = winPanel.transform.Find("Stars").gameObject;
                        arcadeClear.SetActive(false);
                        winPanel.SetActive(true);
                        starAnimator.SetBool("Clear", true);
                        starAnimator.SetInteger("Star", 2);
                        for(int i=0;i<3;i++)
                        {
                            arcadeClear.transform.GetChild(0).transform.gameObject.SetActive(false);
                        }
                    }
                    timerImage.fillAmount = 1 - time / (60 * 3);
                    break;
                case GameType.Computer:
                    playerImage.fillAmount = (float)(playerUser.clear + 1) / ((computerUser.clear + 1) + (playerUser.clear + 1));
                    computerImage.fillAmount = (float)(computerUser.clear + 1) / ((computerUser.clear + 1) + (playerUser.clear + 1));
                    computerUser.position.x = Mathf.Clamp(computerUser.position.x, 0, 4);
                    computerUser.charater.transform.position = computerUser.filedBlock[computerUser.position.y, computerUser.position.x].transform.position;
                    computerUser.line.SetPosition(1, computerUser.filedBlock[0, computerUser.position.x].transform.position);
                    computerUser.line.SetPosition(0, computerUser.filedBlock[filedSize.y - 1, computerUser.position.x].transform.position);
                    if(playerUser.clear==5||computerUser.clear==5)
                    {
                        if(playerUser.clear == 5)
                        {
                            arcadeClear = winPanel.transform.Find("Stars").gameObject;
                            arcadeClear.SetActive(false);
                            winPanel.SetActive(true);
                            starAnimator.SetBool("Clear", true);
                            starAnimator.SetInteger("Star", 2);
                            for (int i = 0; i < 3; i++)
                            {
                                arcadeClear.transform.GetChild(0).transform.gameObject.SetActive(false);
                            }
                        }
                        else
                        {
                            arcadeClear = lostPanel.transform.Find("Stars").gameObject;
                            arcadeClear.SetActive(false);
                            lostPanel.SetActive(true);
                            for (int i = 0; i < 3; i++)
                            {
                                arcadeClear.transform.GetChild(0).transform.gameObject.SetActive(false);
                            }
                        }
                    }
                    break;
            };
            time += Time.deltaTime;
        }
    }
    private void StartGame(GameObject objects,User user,Vector2 position,int scale)
    {
        user.list = new int[3];
        user.filed = new int[filedSize.y, filedSize.x];
        user.filedSelect = new bool[filedSize.y, filedSize.x];
        user.filedBlock = new GameObject[filedSize.y, filedSize.x];

        user.position = new Vector2Int(2, 0);

        user.lineEffect = objects.gameObject.transform.Find("Effect").GetComponent<ParticleSystem>();
        user.charater = objects.gameObject.transform.Find("Charater").gameObject;
        user.selectBlock = objects.gameObject.transform.Find("SelectBlock").gameObject;
        user.line = user.charater.GetComponent<LineRenderer>();

        GameObject blocks = new GameObject("Blocks");
        blocks.transform.parent = objects.transform;
        GameObject selects = new GameObject("Selects");
        selects.transform.parent = objects.transform;
        selects.AddComponent<SpriteRenderer>().sprite = selectSprite;

        var offset = Camera.main.ScreenToWorldPoint(new Vector2(Screen.width / 2, Screen.height) - position);

        for (int y = 0; y < filedSize.y; y++)
        {
            for (int x = 0; x < filedSize.x; x++)
            {
                var curBlock = user.filedBlock[y, x] = new GameObject("Block_" + x.ToString() + "," + y.ToString());
                curBlock.transform.parent = blocks.transform;
                curBlock.transform.position = Vector3.Scale(block[0].bounds.size, new Vector3(blockSize * (x - scale), (blockSize / 2 + blockSize * y))) - offset;
                curBlock.transform.localScale = Vector3.one * blockSize;

                var spriteRenderer = curBlock.AddComponent<SpriteRenderer>();
                spriteRenderer.sprite = null;
                spriteRenderer.sortingOrder = 100;
                spriteRenderer.maskInteraction = SpriteMaskInteraction.None;
            }
        }
        selects.transform.position = (user.filedBlock[0, 0].transform.position + user.filedBlock[filedSize.y - 1, filedSize.x - 1].transform.position) / 2;
        selects.transform.localScale = Vector3.one * blockSize;

        var selectsSpriteRenderer = selects.GetComponent<SpriteRenderer>();
        selectsSpriteRenderer.drawMode = SpriteDrawMode.Tiled;
        selectsSpriteRenderer.size = new Vector2(selectSprite.bounds.size.x * filedSize.x, selectSprite.bounds.size.y * filedSize.y);
        selectsSpriteRenderer.sortingOrder = -25;

        user.mask = objects.gameObject.transform.Find("Mask").gameObject;
        user.mask.transform.position = user.filedBlock[filedSize.y / 2, filedSize.x / 2].transform.position - new Vector3(0, block[0].bounds.size.y * blockSize) / 2;
        user.mask.transform.localScale = Vector2.Scale((block[0].bounds.size * blockSize), filedSize);

        user.background = objects.gameObject.transform.Find("Background").GetComponent<SpriteRenderer>();
        Transform gamebackgroundRectTransform = user.background.GetComponent<Transform>();
        gamebackgroundRectTransform.localPosition = (user.filedBlock[0, 0].transform.position + user.filedBlock[filedSize.y - 1, filedSize.x - 1].transform.position) / 2;
        user.background.size = (Vector2.Scale((block[0].bounds.size * blockSize), filedSize));
        user.background.sortingOrder = -30;
    }
    private void LoadMap(User user)
    {
        TextAsset text = Resources.Load<TextAsset>("Stage_" + Singleton.Instance.selectLevel);
        string[] lines = text.text.Split('\n');
        for (int y = 0; y < filedSize.y; y++)
        {
            for (int x = 0; x < filedSize.x; x++)
            {
                int index = int.Parse(lines[filedSize.y - y - 1][x].ToString());
                SetBlock(user, x, y, index);
            }
        }

    }
    private void MouseClick()
    {
        if (Input.GetMouseButtonDown(0))
            begin = Input.mousePosition;
        else if (Input.GetMouseButtonUp(0))
        {
            end = Input.mousePosition;
            Vector2 diffend = end - begin;
            if (diffend.magnitude > 30 && Mathf.Abs(diffend.x) > Mathf.Abs(diffend.y))
            {
                if (diffend.x > 0)
                {
                    playerUser.position.x += 1;
                }
                else
                {
                    playerUser.position.x -= 1;
                }
            }
            else if (diffend.magnitude > 30)
            {
                if (diffend.y > 0)
                {
                    ClickBlock(playerUser, playerUser.position.x, 0);
                }
                else
                {
                    if(Singleton.Instance.gameType==GameType.TimeAttack)
                        CreateMap(playerUser);
                }
            }
        }

        if(Input.GetKeyDown(KeyCode.LeftArrow))
        {
            playerUser.position.x -= 1;
        }
        if (Input.GetKeyDown(KeyCode.RightArrow))
        {
            playerUser.position.x += 1;
        }
        if (Input.GetKeyDown(KeyCode.Space))
        {
            ClickBlock(playerUser, playerUser.position.x, 0);
        }
    }   
    private void CreateMap(User user)
    {
        user.stack = 0;
        for (int i = 0; i < user.list.Length; i++)
        {
            user.selectBlock.transform.GetChild(i).GetChild(0).gameObject.SetActive(false);
            user.list[i] = 0;
        }
        for (int i = 0; i < filedSize.y; i++)
        {
            for (int j = 0; j < filedSize.x; j++)
            {
                user.filedSelect[i, j] = false;
                RemoveBlock(user, j, i);
            }
        }
        for (int i = 0; i < 10; i++)
        {
            int color = Random.Range(1, 7);
            for (int j = 0; j < 3; j++)
            {
                int x, y = 1;
                do
                {
                    x = Random.Range(0, 5);
                    if (user.filed[1, x] == 0) break;
                }
                while (true);
                for (y = 1; y < filedSize.y - 1; y++)
                {
                    if (user.filed[y + 1, x] != 0) break;
                }
                SetBlock(user, x, y, color);

            }
        }
    }
    private void CreateMap(User user,int clearIndex)
    {
        user.stack = 0;
        for (int i = 0; i < user.list.Length; i++)
        {
            user.selectBlock.transform.GetChild(i).GetChild(0).gameObject.SetActive(false);
            user.list[i] = 0;
        }
        for (int i = 0; i < filedSize.y; i++)
        {
            for (int j = 0; j < filedSize.x; j++)
            {
                user.filedSelect[i, j] = false;
                RemoveBlock(user, j, i);
            }
        }
        for (int i=0;i<filedSize.y;i++)
        {
            for(int j=0;j<filedSize.x;j++)
            {
                user.filed[i,j] = fileds[clearIndex][i,j];
                SetBlock(user,j, i, user.filed[i, j]);
            }
        }
    }
    private void ClickBlock(User user, int x, int y)
    {
        for (int i = y; i < filedSize.y; i++)
        {
            if (user.filed[i, x] != 0 && user.filedSelect[i, x] == false)
            {
                SoundManager.Instance.PlayEffect("Hit");
                StartCoroutine(EnableBlock(user, x, i));
                user.list[user.selectIndex] = user.filed[i, x];
                user.filedSelect[i, x] = true;
                user.selectIndex += 1;
                SetEffectColor(user,user.filed[i,x]);
                RemoveBlock(user ,x, i);
                break;
            }
        }
        if (user.selectIndex == 3)
        {
            user.selectIndex = 0;
            comboTimer = 0;
            if (CheckSelectBlock(user))
            {
                combo += 1;
                for (int i = 0; i < filedSize.y; i++)
                {
                    for (int j = 0; j < filedSize.x; j++)
                    {
                        if (user.filed[i, j] != 0)
                        {
                            return;
                        }
                    }
                }
                switch (Singleton.Instance.gameType)
                {
                    case GameType.Arcade:
                        int starts = 0;
                        winPanel.SetActive(true);
                        playGame = false;

                        arcadeClear = winPanel.transform.Find("Stars").gameObject;
                        Singleton.Instance.maxSelectLevel = Mathf.Max(Singleton.Instance.selectLevel + 1, Singleton.Instance.maxSelectLevel);
                        PlayerPrefs.SetInt("MaxSelectLevel", Singleton.Instance.maxSelectLevel);
                        arcadeClear.transform.GetChild(0).transform.GetChild(1).GetComponent<Text>().text = "게임 클리어";
                        arcadeClear.transform.GetChild(1).transform.GetChild(1).GetComponent<Text>().text = string.Format("콤보 {0} 이상", Singleton.Instance.stageCombo[Singleton.Instance.selectLevel]);
                        arcadeClear.transform.GetChild(2).transform.GetChild(1).GetComponent<Text>().text = string.Format("{0}초 이내 클리어", Singleton.Instance.stageTimer[Singleton.Instance.selectLevel]);
                        arcadeClear.transform.GetChild(0).transform.GetChild(0).GetComponent<Image>().sprite = arcadeImage[1];
                        if (Singleton.Instance.stageCombo[Singleton.Instance.selectLevel] <= combo)
                        {
                            starts += 1;
                            arcadeClear.transform.GetChild(1).transform.GetChild(0).GetComponent<Image>().sprite = arcadeImage[1];
                        }
                        if (Singleton.Instance.stageTimer[Singleton.Instance.selectLevel] >= time)
                        {
                            starts += 1;
                            Debug.Log(arcadeClear.transform.GetChild(2).transform.GetChild(0).name);
                            arcadeClear.transform.GetChild(2).transform.GetChild(0).GetComponent<Image>().sprite = arcadeImage[1];
                        }
                        starAnimator.SetBool("Clear", true);
                        starAnimator.SetInteger("Star", starts);

                        break;
                    case GameType.TimeAttack:
                        score += 1;
                        CreateMap(playerUser);
                        break;
                    case GameType.Computer:

                        user.clear += 1;
                        CreateMap(user, user.clear);
                        if (user == computerUser)
                        {
                            StopCoroutine("ComputerManager");
                            StartCoroutine("ComputerManager");
                        }
                        break;
                };
      
                Debug.Log("All Clear");
            }
            else
            {
                switch (Singleton.Instance.gameType)
                {
                    case GameType.Arcade:
                        playGame = false;
                        lostPanel.SetActive(true);
                        arcadeClear = lostPanel.transform.Find("Stars").gameObject;
                        arcadeClear.transform.GetChild(0).transform.GetChild(1).GetComponent<Text>().text = "게임 클리어";
                        arcadeClear.transform.GetChild(1).transform.GetChild(1).GetComponent<Text>().text = string.Format("콤보 {0} 이상", Singleton.Instance.stageCombo[Singleton.Instance.selectLevel]);
                        arcadeClear.transform.GetChild(2).transform.GetChild(1).GetComponent<Text>().text = string.Format("{0}초 이내 클리어", Singleton.Instance.stageTimer[Singleton.Instance.selectLevel]);

                        arcadeClear.transform.GetChild(0).transform.GetChild(0).GetComponent<Image>().sprite = arcadeImage[0];
                        arcadeClear.transform.GetChild(1).transform.GetChild(0).GetComponent<Image>().sprite = arcadeImage[0];
                        arcadeClear.transform.GetChild(2).transform.GetChild(0).GetComponent<Image>().sprite = arcadeImage[0];
          
                        break;
                    case GameType.TimeAttack:
               
                        CreateMap(playerUser);
                        break;
                    case GameType.Computer:
                        CreateMap(user, user.clear);
                        break;
                };
            }
        }

    }
    private bool CheckSelectBlock(User user)
    {
        return (user.list[0] == user.list[1] && user.list[1] == user.list[2] && user.list[2] == user.list[0]);
    }
    private void SetBlock(User user, int x, int y, int number)
    {
        if (number != 0)
        {
            user.filed[y, x] = number;
            user.filedBlock[y, x].GetComponent<SpriteRenderer>().sprite = block[number - 1];
        }
        else
        {

            user.filed[y, x] = 0;
            user.filedBlock[y, x].GetComponent<SpriteRenderer>().sprite = null;
        }
    }
    private void RemoveBlock(User user, int x, int y)
    {
        user.filedBlock[y, x].GetComponent<SpriteRenderer>().sprite = null;
        user.filed[y, x] = 0;
    }
    IEnumerator ComputerManager()
    {
        float[] moveTime = { 1f, 0.75f, 0.5f };
        float[] attackTime = { 0.75f, 0.5f, 0.025f };
        while (true)
        {
            if (playGame)
            {
                Vector2Int v = nextMove[computerUser.clear].Pop();

                while (computerUser.position.x != v.x)
                {
                    if (computerUser.position.x > v.x) computerUser.position.x -= 1;
                    else computerUser.position.x += 1;
                    yield return new WaitForSeconds(moveTime[Singleton.Instance.computerLevel]);
                }
                ClickBlock(computerUser, computerUser.position.x, 0);
            }
            yield return new WaitForSeconds(attackTime[Singleton.Instance.computerLevel]);
        }
    }
    IEnumerator EnableBlock(User user,int x, int y)
    {
        int index = user.selectIndex;
        float timer = user.stack * -0.20f;
        GameObject image = user.selectBlock.transform.GetChild(index).GetChild(0).gameObject;
        GameObject sprite = new GameObject();
        Vector3 pos = user.selectBlock.transform.GetChild(index).position;
   
        sprite.AddComponent<SpriteRenderer>().sprite = user.filedBlock[y, x].GetComponent<SpriteRenderer>().sprite;
        sprite.transform.localScale = Vector3.one * blockSize;
        sprite.transform.position = user.filedBlock[y, x].transform.position;
        Destroy(sprite, 1);

        image.GetComponent<SpriteRenderer>().sprite = user.filedBlock[y, x].GetComponent<SpriteRenderer>().sprite;
        while (timer < 1)
        {
            timer += Time.deltaTime * 2;
            sprite.transform.position = Vector3.Lerp(user.filedBlock[y, x].transform.position, pos, timer);
            sprite.transform.localEulerAngles = Vector3.Lerp(Vector3.zero, Vector3.forward * 360, timer);

            yield return null;
        }
        user.stack += 1;
        image.gameObject.SetActive(true);

        yield return new WaitForSeconds(0.2f);
        if (user.stack >= 3)
        {
            user.stack = 0;
            for (int i = 0; i < 3; i++)
            {
                GameObject a = user.selectBlock.transform.GetChild(i).GetChild(0).gameObject;
                a.gameObject.SetActive(false);
            }
        }
    }
    IEnumerator StartAnimation()
    {
        float timer = 1;
        while (timer > 0)
        {
            value = timer;
            timer -= Time.deltaTime / 2;
            timer = Mathf.Clamp01(timer);
            yield return null;
        }
    }
    IEnumerator EndAnimation(int num)
    {
        float timer = 0;
        while (timer < 1)
        {
            value = timer;
            timer += Time.deltaTime / 2;
            timer = Mathf.Clamp01(timer);
            yield return null;
        }
        UnityEngine.SceneManagement.SceneManager.LoadScene(num);

    }
    public void CallMenu()
    {
        StartCoroutine(EndAnimation(0));
    }
    public void CallReGame()
    {
        StartCoroutine(EndAnimation(Application.loadedLevel));
    }
    public void CallNextGame()
    {
        Singleton.Instance.selectLevel += 1;
        StartCoroutine(EndAnimation(Application.loadedLevel));
    }
    public void SetEffectColor(User user,int num)
    {
        int y;
        num -= 1;
        var lineRenderer = user.charater.GetComponent<LineRenderer>();
        lineRenderer.startColor = colors[num, 0];
        lineRenderer.endColor = colors[num, 1];

        user.background.color = colors[num,0] * new Color(1f, 1f, 1f, 100f / 255f);

        for (y = 0; y < filedSize.y - 1; y++)
        {
            if (user.filed[y + 1, user.position.x] != 0)
                break;
        }

        var sh = user.lineEffect.shape;
        user.lineEffect.gameObject.transform.position = (user.filedBlock[0, user.position.x].transform.position);

        var a = user.lineEffect.main;
        a.startColor = new ParticleSystem.MinMaxGradient(colors[num, 0], colors[num, 1]);
        user.lineEffect.Play();
    }
    private void OnRenderImage(RenderTexture source, RenderTexture destination)
    {
        TransitionMaterial.SetFloat("_Cutoff", value);
        Graphics.Blit(source, destination, TransitionMaterial);
    }
}
