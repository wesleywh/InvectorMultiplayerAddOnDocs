[Back To Index](index.md)

# Core Object: UICoreLogic  
<p align="center">
	<img src="https://i.imgur.com/TYHRbXn.jpg">
</p>
<br/>

### Core Options
<img src="https://i.imgur.com/EkUtI9Q.jpg">
<br/>

| Variable Name | Type | Description |
|:--- |:---:|:---|
| DefaultLevelIndex | int | The default level to load if one isn't ever specified |
| SelectablePlayers | GameObject[] | The list of players that people are allowed to select from |
| SceneList | SceneOption[] | All of the scene names and sprites to use in a scene voting system |
| Debugging | bool | Will load everything this is doing to the console (disable for a production release) |

### Sound Options
<img src="https://i.imgur.com/HUVKCbL.jpg">
<br/>

| Variable Name | Type | Description |
|:--- |:---:|:---|
| MusicSource | AudioSource | The audiosource that will play the music for the UI |
| SoundSource | AudioSource | The audiosource that will play the ui sound effects |
| MouseEnter | AudioClip | The sound to play when you call the "PlayMouseEnter" function |
| MouseEnterVolume | Range(0,1) | How loud to player the `MouseEnter` sound |
| MouseExit | AudioClip | The sound to play when you call the "PlayMouseExit" function |
| MouseExitVolume | Range(0,1) | How loud to player the `MouseExit` sound |
| MouseClick | AudioClip | The sound to play when you call the "PlayMouseClick" function |
| MouseClickVolume | Range(0,1) | How loud to player the `MouseClick` sound |
| FinalClick | AudioClip | The sound to play when you call the "PlayFinalClick" function |
| StartVolume | Range(0,1) | What volume to set the musicSource at |
| FadeInAudio | bool | If you want to slowly fade in the music in the MusicSource |
| FadeInSpeed | float | How fast to fade in the musicSource |

### Loading Page Options
<img src="https://i.imgur.com/XglpZ1x.jpg">
<br/>

| Variable Name | Type | Description |
|:--- |:---:|:---|
| LoadingParent | GameObject | The object that holds everything for the loading page. This object will be enable/disabled when starting/stopping loading |
| LoadingImages | Sprite[] | The images to cycle through when on the loading page |
| LoadingImageDisplayTime | float | How long to show a image before cycling to the next in the `LoadingImages` array |
| LoadingImageFadeSpeed | float | How fast to fade in each `LoadingImage` |
| LoadingTitle | string | The title of the loading page |
| LoadingDesc | string[] | Descriptions to cycle through when loading a page |
| MainLoadingImage | Image | The image component that is responsible for displaying the main loading image displayed on the loading page |
| LoadingTitleText | Text | The text component that is responsible for displaying the loading title. |
| LoadingDescText | Text | The text component that is responsible for displaying the description text. |
| LoadingBar | Image | The image that will have the fill value change from 0 to 1 based on the Photon networks loading status |

### UI Events

#### Start Events
<img src="https://i.imgur.com/38x0E1v.jpg">
<br/>

| UnityEvent | Description |
|:--- |:---|
| OnStart | This is a one time event that is triggered when this component is started up for the first time |

#### Loading Events
<img src="https://i.imgur.com/7Nl0P1N.jpg"><br/>
<img src="https://i.imgur.com/aWkmDXc.jpg"><br/>
<img src="https://i.imgur.com/0I8CHMs.jpg"><br/>
<br/>

| UnityEvent | Description |
|:--- |:---|
| OnSceneLoaded | When a new unity scene has finished loading this is called. |
| OnStartLoading | When the loading page is first triggered to start loading this is called. |
| OnCompleteLevelLoading | When the loading bar indicates that is has completed loading this is called. |

#### Naming Events
<img src="https://i.imgur.com/fT1SMAW.jpg"><br/>
<br/>

| UnityEvent | Description |
|:--- |:---|
| OnNameEnterFailed | Called when you attempt to input an invalid player name. |
| OnNameEnterSuccess | Called when you successfully input a player name. |

#### Error Events
<img src="https://i.imgur.com/P3CNpm3.jpg"><br/>
<br/>

| UnityEvent | Description |
|:--- |:---|
| OnNetworkError | Called when you call the "NetworkErrorOccured" function. |

#### Room Events
<img src="https://i.imgur.com/aK6tnoS.jpg"><br/>
<img src="https://i.imgur.com/FzVCu4G.jpg"><br/>
<br/>

| UnityEvent | Description |
|:--- |:---|
| OnCreateRoomFailed | When you failed to create a photon room. |
| OnCreateRoomSuccess | When you successfully created a photon room. |
| OnWaitToJoinPhotonRoomsLobby | When you're in the photon lobby waiting to join a photon room. |
| OnStartSession | Called when you run the "SendStartSession" function |
| OnCountdownStart | Called when you receive a PhotonRaise Event of type "CB_EVENT_STARTCOUNTDOWN". This is enabled by calling the "SendStartCountdown" function |
| OnCountdownStop | Called when you receive a PhotonRaise Event of type "CB_EVENT_STARTCOUNTDOWN". This is enabled by calling the "SendStopCountdown" function |