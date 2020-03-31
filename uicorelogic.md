[Back To Index](index.md)

# Core Object: UICoreLogic  

[Jump To Core Options](#core-options)<br/>
[Jump To Sound Options](#sound-options)<br/>
[Jump To Loading Page Options](#loading-page-options)<br/>
[Jump To Start Events](#start-events)<br/>
[Jump To Loading Events](#loading-events)<br/>
[Jump To Naming Events](#naming-events)<br/>
[Jump To Error Events](#error-events)<br/>
[Jump To Room Events](#start-events)<br/>
[Jump To Public Functions](#functions)<br/>

<p align="center">
	<img src="https://i.imgur.com/TYHRbXn.jpg">
</p>
<br/>

### Core Options<a name="core-options"></a>
<img src="https://i.imgur.com/EkUtI9Q.jpg">
<br/>

| Variable Name | Type | Description |
|:--- |:---:|:---|
| DefaultLevelIndex | int | The default level to load if one isn't ever specified |
| SelectablePlayers | GameObject[] | The list of players that people are allowed to select from |
| SceneList | SceneOption[] | All of the scene names and sprites to use in a scene voting system |
| Debugging | bool | Will load everything this is doing to the console (disable for a production release) |

### Sound Options<a name="sound-options"></a>
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

### Loading Page Options<a name="loading-page-options"></a>
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

#### Start Events<a name="start-events"></a>
<img src="https://i.imgur.com/38x0E1v.jpg">
<br/>

| UnityEvent | Description |
|:--- |:---|
| OnStart | This is a one time event that is triggered when this component is started up for the first time |

#### Loading Events<a name="loading-events"></a>
<img src="https://i.imgur.com/7Nl0P1N.jpg"><br/>
<img src="https://i.imgur.com/aWkmDXc.jpg"><br/>
<img src="https://i.imgur.com/0I8CHMs.jpg"><br/>
<br/>

| UnityEvent | Description |
|:--- |:---|
| OnSceneLoaded | When a new unity scene has finished loading this is called. |
| OnStartLoading | When the loading page is first triggered to start loading this is called. |
| OnCompleteLevelLoading | When the loading bar indicates that is has completed loading this is called. |

#### Naming Events<a name="naming-events"></a>
<img src="https://i.imgur.com/fT1SMAW.jpg"><br/>
<br/>

| UnityEvent | Description |
|:--- |:---|
| OnNameEnterFailed | Called when you attempt to input an invalid player name. |
| OnNameEnterSuccess | Called when you successfully input a player name. |

#### Error Events<a name="error-events"></a>
<img src="https://i.imgur.com/P3CNpm3.jpg"><br/>
<br/>

| UnityEvent | Description |
|:--- |:---|
| OnNetworkError | Called when you call the "NetworkErrorOccured" function. |

#### Room Events<a name="start-events"></a>
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

## Public Functions<a name="functions"></a>

| Function | What It Does |
|:---|:---|
| void RestartMusic() | Will restart the current music selection |
| void StopMusic() | Will stop playing the current music selection |
| void PlayMusic() | Will play the current music selection |
| void EnableMusic(bool isEnabled) | Will enable/disable the music sound source |
| void FadeMusic(bool fadeOut) | Fade In/Out the music |
| void PlayMouseEnter() | Play the `MouseEnter` sound from the sound source |
| void PlayMouseExit() | Play the `MouseExit` sound from the sound source |
| void PlayMouseClick() | Play the `MouseClick` sound from the sound source |
| void PlayFinalClick() | Play the `FinalClick` sound from the sound source |
| void LoopMusic(bool setLooping) | Set the looping value on the music source |
| void SetMusicVolume(float volume) | Set the volume of the music source |
| void SetMusicAudio(AudioClip clip) | Set the music clip on the music source |
| void KickPlayer(string userId) | Get the photon player from the photon room |
| GameObject GetSetPlayer() | Returns the value of the `playerPrefab` in your NetworkManager component |
| void SetPlayer(int index) | Get the Gameobject at index from the `selectablePlayers` array and set that as the `playerPrefab` in the NetworkManager component |
| void SubmitSavedPlayerName() | Get the saved player name and attempt to set that via the NetworkManager |
| void SavePlayerName(string playerName) | Save the player name locally but don't submitted it yet |
| void SetMyTeamName(string teamName) | Set the NetworkManager teamName |
| string GetMyTeamName() | Get the NetworkManager teamName |
| string GetUserTeamName(string userId) | Get a different players teamName |
| Dictionary<string, string> GetTeamData() | Returns a dictionary of userIds and the team they're on |
| void AddToTeamData(string userId, string teamName) | Add a photon player to a team |
| void ClearTeamData() | Delete the team data dictionary |
| void SendReadyState(bool isReady) | Notifies everyone in a photon room the ready state of yourself |
| void ClearPlayerReadyDict() | Deletes the dictionary holding the information about the players that are ready or not |
| Dictionary<string, bool> GetPlayersReadyDict() | Returns a dictionary of userIds and if they are ready or not |
| bool PlayerIsReady(string userId) | Returns true if that particular user has indicated they were ready |
| bool AllPlayersReady() | Returns true if every player is ready |
| bool PlayerInReadyDict(string userId) | Returns true if a player is found in the current ready dictionary |
| void AddNewPlayerToPlayerReadyList(Photon.Realtime.Player player) | Adds a player to the ready dictionary |
| void RemovePlayerToPlayerReadyList(Photon.Realtime.Player player) | Removed a player from the ready dictionary |
| void JoinLobby() | Calls the network manager to join the photon lobby |
| void SaveRoomName(string roomName) | Save a local copy of the photon room name |
| void JoinRoom(string roomname) | Calls the Networkmanager to join a particular photon room |
| void JoinSavedRoomName(bool useSavedPassword) | Join the room name that you saved earlier, can include a saved password as well |
| void JoinPrivateRoom() | Join a private room using the saved room name |
| void JoinRandomPublicRoomOrCreateOne() | Will join any public open photon room |
| void SaveRoomPassword(string password) | Save the password to use for later |
| void ClearSavedRoomPassword() | Remove the saved password |
| void SetRoomIsJoinable(bool isJoinable) | Call the network manager to set the open state of the photon room |
| void SetRoomVisibility(bool isVisible) | Call the network manager to set the photon room visibility |
| void SendStartCountdown(float amount) | Start a countdown across the network starting at a specified time |
| void SendStopCountdown() | Stop the countdown across the network |
| void SendSceneVote(int sceneIndex) | Send your scene vote across the network |
| int GetSceneVotes(int sceneIndex) | Get the current amount of votes for a scene at the scene index |
| void ClearSceneVoteList() | Clear the vote list |
| void CreateRandomSceneList() | Randomize the SceneList and save that random copy locally |
| void SetRandomSceneList(List<SceneOption> randomRoomList) | Set the saved random scene list according to your input |
| void SendCreatedRandomSceneList() | Send your random scene list across the network for others to set |
| SceneOption GetRandomSceneNumber(int value) | Return the data at index from the randomly generated scene list that was saved earlier |
| SceneOption GetSceneNumber(int value) | Return the data at index for the original sceneList |
| void SaveRoomList() | Save the list of photon rooms that was returned from the NetworkManager |
| Dictionary<string, RoomInfo> GetRoomList() | Get the current list of photon rooms from the NetworkManager |
| void EnableRoomNameChecking(bool isEnabled) | Enable checking for valid rooms names |
| void CreateSessionWithSavedRoomName(bool useSavedPassword=false) | Create a photon room name from the saved room name. Make the room type public |
| void CreatePrivateSession() | Create a photon room from the saved room name and include a password. Also make the room type private |
| void Disconnect() | Call disconnect on the network manager |
| void NetworkErrorOccured(string errorMessage) | Display the network error page with the message |
| void SendStartSession() | Make everyone load the saved scene name and start the match |
| void SendEnableAutoSpawn(bool enableSpawn) | Set `autoPlayerSpawn` option in the NetworkManager |
| string GetSavedSceneToLoadName() | Get the saved scene name |
| SendSceneChangeInfo(string sceneName, int index) | Make everyone over the network change there saved scene name (and index) |
| void SaveSceneToLoad(string levelName) | Save the scene name (for later loading) |
| void SaveSceneToLoad(int levelIndex) | Save the scene index (converted to name) for later loading |
| void LoadSavedLevel() | Load the saved scene name |
| void EveryoneLoadSavedLevel() | Make everyone over the network load their saved scene name |
| void EveryoneLoadLevel(string levelName) | Call the networkmanager to load the level name for everyone |
| void EveryoneLoadLevel(int levelIndex) | Call the network manager to load the level index for everyone |
| void EnablePlayerAutoSpawn(bool setActive) | Set the `autoPlayerSpawn` settings on the networkmanager |
| void EnableLoadingPage(bool isEnabled) | Enable the loading page |
| void ResetLoadingBar() | Set the loading bar value back to zero |
| void QuitGame() | Quit the game |
| void EnableChatboxSlideOut(bool isEnabled) | Make the `ChatBox` slide in or out |
| void EnableChatBoxVisibility(bool isEnabled) | Make the `ChatBox` visible or not |
| void EnableSavedPlayerUI(bool isEnabled) | Enable/Disable previously saved Invector UI elements |
| void SavePlayerUIs() | Save the invector UI elements for later manipulation |
| void ClearPlayerUIs() | Remove the saved player UI list |
| void RefreshPlayerUIs() | Calls `ClearPlayerUIs` and `SavePlayerUIs` |
| void EnableMouseMovement(bool isEnabled) | Enable/Disable mouse movement |
| void EnableMouseVisibility(bool isVisible) | Enable/Disable mouse visibility |
| void MouseSelect(GameObject target) | Make the mouse select a target |
