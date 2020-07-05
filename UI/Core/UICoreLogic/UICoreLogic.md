[Back To Index](../../../index.md)

# UICoreLogic

[Jump To Parameters](#parameter-definitions)<br/>
[Jump To Function Definitions](#functions-definitions)<br/>

--------------------------------------------------------
## Parameter Definitions<a name="parameter-definitions"></a>

Select the parameter name from below to jump directly to it on this page.

[OnCompleteLevelLoading](#parameter-OnCompleteLevelLoading)<br>
[OnCountdownStarted](#parameter-OnCountdownStarted)<br>
[OnCountdownStopped](#parameter-OnCountdownStopped)<br>
[OnCreateRoomFailed](#parameter-OnCreateRoomFailed)<br>
[OnCreateRoomSuccess](#parameter-OnCreateRoomSuccess)<br>
[OnNameEnterFailed](#parameter-OnNameEnterFailed)<br>
[OnNameEnterSuccess](#parameter-OnNameEnterSuccess)<br>
[OnNetworkError](#parameter-OnNetworkError)<br>
[OnReceiveRoundTime](#parameter-OnReceiveRoundTime)<br>
[OnResetEverything](#parameter-OnResetEverything)<br>
[OnSceneLoaded](#parameter-OnSceneLoaded)<br>
[OnStart](#parameter-OnStart)<br>
[OnStartLoading](#parameter-OnStartLoading)<br>
[OnStartSession](#parameter-OnStartSession)<br>
[OnWaitToJoinPhotonRoomsLobby](#parameter-OnWaitToJoinPhotonRoomsLobby)<br>
[debugging](#parameter-debugging)<br>
[defaultLevelIndex](#parameter-defaultLevelIndex)<br>
[fadeInAudio](#parameter-fadeInAudio)<br>
[fadeInSpeed](#parameter-fadeInSpeed)<br>
[finalClick](#parameter-finalClick)<br>
[finalClickVolume](#parameter-finalClickVolume)<br>
[loadingBar](#parameter-loadingBar)<br>
[loadingDesc](#parameter-loadingDesc)<br>
[loadingDescText](#parameter-loadingDescText)<br>
[loadingImageDisplayTime](#parameter-loadingImageDisplayTime)<br>
[loadingImages](#parameter-loadingImages)<br>
[loadingPageFadeSpeed](#parameter-loadingPageFadeSpeed)<br>
[loadingParent](#parameter-loadingParent)<br>
[loadingTitle](#parameter-loadingTitle)<br>
[loadingTitleText](#parameter-loadingTitleText)<br>
[mainLoadingImage](#parameter-mainLoadingImage)<br>
[mouseClick](#parameter-mouseClick)<br>
[mouseClickVolume](#parameter-mouseClickVolume)<br>
[mouseEnter](#parameter-mouseEnter)<br>
[mouseEnterVolume](#parameter-mouseEnterVolume)<br>
[mouseExit](#parameter-mouseExit)<br>
[mouseExitVolume](#parameter-mouseExitVolume)<br>
[musicSource](#parameter-musicSource)<br>
[sceneList](#parameter-sceneList)<br>
[selectablePlayers](#parameter-selectablePlayers)<br>
[soundSource](#parameter-soundSource)<br>
[startVolume](#parameter-startVolume)<br>
[teamsUpdated](#parameter-teamsUpdated)<br>
[voiceViewUpdated](#parameter-voiceViewUpdated)<br>

------------------
 ### OnCompleteLevelLoading<a name="parameter-OnCompleteLevelLoading"></a>
> UnityEvent. Called when you have completely loaded a unity scene.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |UnityEvent|None

[Back To Top](#)

------------------
 ### OnCountdownStarted<a name="parameter-OnCountdownStarted"></a>
> UnityEvent. Called when you receive a start countdown PhotonEvent.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |FloatUnityEvent|None

[Back To Top](#)

------------------
 ### OnCountdownStopped<a name="parameter-OnCountdownStopped"></a>
> UnityEvent. Called when you receive a stop countdown PhotonEvent.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |UnityEvent|None

[Back To Top](#)

------------------
 ### OnCreateRoomFailed<a name="parameter-OnCreateRoomFailed"></a>
> UnityEvent. Called when creating a photon room fails.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |StringUnityEvent|None

[Back To Top](#)

------------------
 ### OnCreateRoomSuccess<a name="parameter-OnCreateRoomSuccess"></a>
> UnityEvent. Called when creating a photon room succeeds.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |UnityEvent|None

[Back To Top](#)

------------------
 ### OnNameEnterFailed<a name="parameter-OnNameEnterFailed"></a>
> UnityEvent. Called when entering a name for your player fails.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |StringUnityEvent|None

[Back To Top](#)

------------------
 ### OnNameEnterSuccess<a name="parameter-OnNameEnterSuccess"></a>
> UnityEvent. Called when entering a name for your player succeeds.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |UnityEvent|None

[Back To Top](#)

------------------
 ### OnNetworkError<a name="parameter-OnNetworkError"></a>
> UnityEvent. Called when you receive a network error.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |StringUnityEvent|None

[Back To Top](#)

------------------
 ### OnReceiveRoundTime<a name="parameter-OnReceiveRoundTime"></a>
> UnityEvent. Called when you receive an update round time PhotonEvent.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |FloatUnityEvent|None

[Back To Top](#)

------------------
 ### OnResetEverything<a name="parameter-OnResetEverything"></a>
> UnityEvent. Called when you want to reset the UI back to it's default state.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |UnityEvent|None

[Back To Top](#)

------------------
 ### OnSceneLoaded<a name="parameter-OnSceneLoaded"></a>
> UnityEvent. Called everytime when a unity scene is first loaded.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |SceneEvent|new SceneEvent()

[Back To Top](#)

------------------
 ### OnStart<a name="parameter-OnStart"></a>
> UnityEvent. Called only once in the `OnStart` method of this component.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |UnityEvent|new UnityEvent()

[Back To Top](#)

------------------
 ### OnStartLoading<a name="parameter-OnStartLoading"></a>
> UnityEvent. Called when you have just started loading a unity scene.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |UnityEvent|None

[Back To Top](#)

------------------
 ### OnStartSession<a name="parameter-OnStartSession"></a>
> Called when you successfully create a new session.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |UnityEvent|None

[Back To Top](#)

------------------
 ### OnWaitToJoinPhotonRoomsLobby<a name="parameter-OnWaitToJoinPhotonRoomsLobby"></a>
> UnityEvent. Called right after you attempt to join the photon lobby.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |UnityEvent|None

[Back To Top](#)

------------------
 ### debugging<a name="parameter-debugging"></a>
> Log everything that happens to the unity console.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |bool|false

[Back To Top](#)

------------------
 ### defaultLevelIndex<a name="parameter-defaultLevelIndex"></a>
> If you don't set the scene to load this is the default level index it will use.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |int|0

[Back To Top](#)

------------------
 ### fadeInAudio<a name="parameter-fadeInAudio"></a>
> When first loading the UI, fade in the audio.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |bool|false

[Back To Top](#)

------------------
 ### fadeInSpeed<a name="parameter-fadeInSpeed"></a>
> If fading out your music how to fast to fade out. Higher values will fade out faster.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |float|0.25f

[Back To Top](#)

------------------
 ### finalClick<a name="parameter-finalClick"></a>
> The sound that will be played when you call the \"PlayerFinalClick\" function.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |AudioClip|null

[Back To Top](#)

------------------
 ### finalClickVolume<a name="parameter-finalClickVolume"></a>
> How loud to play the \"finalClick\" sound.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |float|0.5f

[Back To Top](#)

------------------
 ### loadingBar<a name="parameter-loadingBar"></a>
> The loading bar.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |Image|null

[Back To Top](#)

------------------
 ### loadingDesc<a name="parameter-loadingDesc"></a>
> The description text that will be set when the loading screen is displayed.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |List<string>|new List<string>()

[Back To Top](#)

------------------
 ### loadingDescText<a name="parameter-loadingDescText"></a>
> The text object that will be used to display your loading description text.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |Text|null

[Back To Top](#)

------------------
 ### loadingImageDisplayTime<a name="parameter-loadingImageDisplayTime"></a>
> How long to display each image before fading to the next one.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |float|8.0f

[Back To Top](#)

------------------
 ### loadingImages<a name="parameter-loadingImages"></a>
> The image that will display when loading the screen.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |List<Sprite>|new List<Sprite>()

[Back To Top](#)

------------------
 ### loadingPageFadeSpeed<a name="parameter-loadingPageFadeSpeed"></a>
> How fast to fade the images in and out.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |float|0.25f

[Back To Top](#)

------------------
 ### loadingParent<a name="parameter-loadingParent"></a>
> The Parent Object that holds all of the loading page transforms.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |GameObject|null

[Back To Top](#)

------------------
 ### loadingTitle<a name="parameter-loadingTitle"></a>
> The title text that will be set when the loading screen is displayed

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |string|""

[Back To Top](#)

------------------
 ### loadingTitleText<a name="parameter-loadingTitleText"></a>
> The text object that will be used to display your loading title text.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |Text|null

[Back To Top](#)

------------------
 ### mainLoadingImage<a name="parameter-mainLoadingImage"></a>
> The image that will be displaying your main loading sprite

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |Image|null

[Back To Top](#)

------------------
 ### mouseClick<a name="parameter-mouseClick"></a>
> The sound that will be played when you call the \"PlayerMouseClick\" function.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |AudioClip|null

[Back To Top](#)

------------------
 ### mouseClickVolume<a name="parameter-mouseClickVolume"></a>
> How loud to play the \"mouseClick\" sound.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |float|0.5f

[Back To Top](#)

------------------
 ### mouseEnter<a name="parameter-mouseEnter"></a>
> The sound that will be played when you call the \"PlayerMouseEnter\" function.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |AudioClip|null

[Back To Top](#)

------------------
 ### mouseEnterVolume<a name="parameter-mouseEnterVolume"></a>
> How loud to play the \"mouseEnter\" sound.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |float|0.5f

[Back To Top](#)

------------------
 ### mouseExit<a name="parameter-mouseExit"></a>
> The sound that will be played when you call the \"PlayerMouseExit\" function.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |AudioClip|null

[Back To Top](#)

------------------
 ### mouseExitVolume<a name="parameter-mouseExitVolume"></a>
> How loud to play the \"mouseExit\" sound.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |float|0.5f

[Back To Top](#)

------------------
 ### musicSource<a name="parameter-musicSource"></a>
> The audio source that will play your menu music.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |AudioSource|null

[Back To Top](#)

------------------
 ### sceneList<a name="parameter-sceneList"></a>
> A list of `SceneOptions` to choose from when you want to implement " <br>a way for players to select the scene they would like to join.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |List<SceneOption>|new List<SceneOption>()

[Back To Top](#)

------------------
 ### selectablePlayers<a name="parameter-selectablePlayers"></a>
> The complete list of players that are selectable to the end user.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |GameObject[]|new GameObject[] { }

[Back To Top](#)

------------------
 ### soundSource<a name="parameter-soundSource"></a>
> The audio source that will play your menu sounds.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |AudioSource|null

[Back To Top](#)

------------------
 ### startVolume<a name="parameter-startVolume"></a>
> How loud to set your audio to.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |float|0.5f

[Back To Top](#)

------------------
 ### teamsUpdated<a name="parameter-teamsUpdated"></a>
> Delegate. Called when any player on a team is added or removed.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |BasicDelegate|None

[Back To Top](#)

------------------
 ### voiceViewUpdated<a name="parameter-voiceViewUpdated"></a>
> Delegate. Called when the voice view is updated.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |BasicDelegate|None

[Back To Top](#)

## Function Definitions<a name="functions-definitions"></a>

Select the function name from below to jump directly to it on this page.

[AddNewPlayerToPlayerReadyList](#AddNewPlayerToPlayerReadyList)<br>
[AddToTeamData](#AddToTeamData)<br>
[AllPlayersReady](#AllPlayersReady)<br>
[ClearPlayerReadyDict](#ClearPlayerReadyDict)<br>
[ClearPlayerUIs](#ClearPlayerUIs)<br>
[ClearSavedRoomPassword](#ClearSavedRoomPassword)<br>
[ClearSceneVoteList](#ClearSceneVoteList)<br>
[ClearTeamData](#ClearTeamData)<br>
[CreatePrivateSession](#CreatePrivateSession)<br>
[CreateRandomSceneList](#CreateRandomSceneList)<br>
[CreateSessionWithSavedRoomName](#CreateSessionWithSavedRoomName)<br>
[Disconnect](#Disconnect)<br>
[EnableChatBoxVisibility](#EnableChatBoxVisibility)<br>
[EnableChatboxSlideOut](#EnableChatboxSlideOut)<br>
[EnableLoadingPage](#EnableLoadingPage)<br>
[EnableMouseMovement](#EnableMouseMovement)<br>
[EnableMouseVisibility](#EnableMouseVisibility)<br>
[EnableMusic](#EnableMusic)<br>
[EnablePlayerAutoSpawn](#EnablePlayerAutoSpawn)<br>
[EnableRoomNameChecking](#EnableRoomNameChecking)<br>
[EnableSavedPlayerUI](#EnableSavedPlayerUI)<br>
[EveryoneLoadLevel](#EveryoneLoadLevel)<br>
[EveryoneLoadLevel](#EveryoneLoadLevel)<br>
[EveryoneLoadSavedLevel](#EveryoneLoadSavedLevel)<br>
[FadeMusic](#FadeMusic)<br>
[GetMyTeamName](#GetMyTeamName)<br>
[GetPlayerVoiceView](#GetPlayerVoiceView)<br>
[GetRandomSceneNumber](#GetRandomSceneNumber)<br>
[GetSavedSceneToLoadName](#GetSavedSceneToLoadName)<br>
[GetSceneNumber](#GetSceneNumber)<br>
[GetSceneVotes](#GetSceneVotes)<br>
[GetSetPlayer](#GetSetPlayer)<br>
[GetSetPlayerIndex](#GetSetPlayerIndex)<br>
[GetUserTeamName](#GetUserTeamName)<br>
[JoinLobby](#JoinLobby)<br>
[JoinPrivateRoom](#JoinPrivateRoom)<br>
[JoinRandomPublicRoomOrCreateOne](#JoinRandomPublicRoomOrCreateOne)<br>
[JoinRoom](#JoinRoom)<br>
[JoinSavedRoomName](#JoinSavedRoomName)<br>
[KickPlayer](#KickPlayer)<br>
[LoadSavedLevel](#LoadSavedLevel)<br>
[LoopMusic](#LoopMusic)<br>
[MouseSelect](#MouseSelect)<br>
[MouseSelectHandle](#MouseSelectHandle)<br>
[MouseSelectTarget](#MouseSelectTarget)<br>
[NetworkErrorOccured](#NetworkErrorOccured)<br>
[PhotonEvent_AUTOSPAWN](#PhotonEvent_AUTOSPAWN)<br>
[PhotonEvent_KICKPLAYER](#PhotonEvent_KICKPLAYER)<br>
[PhotonEvent_MAPCHANGE](#PhotonEvent_MAPCHANGE)<br>
[PhotonEvent_RANDOMSCENELIST](#PhotonEvent_RANDOMSCENELIST)<br>
[PhotonEvent_READUP](#PhotonEvent_READUP)<br>
[PhotonEvent_ROUNDTIME](#PhotonEvent_ROUNDTIME)<br>
[PhotonEvent_SCENEVOTE](#PhotonEvent_SCENEVOTE)<br>
[PhotonEvent_STARTCOUNTDOWN](#PhotonEvent_STARTCOUNTDOWN)<br>
[PhotonEvent_STARTSESSION](#PhotonEvent_STARTSESSION)<br>
[PhotonEvent_TEAMCHANGE](#PhotonEvent_TEAMCHANGE)<br>
[PhotonEvent_VOICEVIEW](#PhotonEvent_VOICEVIEW)<br>
[PlayFinalClick](#PlayFinalClick)<br>
[PlayMouseClick](#PlayMouseClick)<br>
[PlayMouseEnter](#PlayMouseEnter)<br>
[PlayMouseExit](#PlayMouseExit)<br>
[PlayMusic](#PlayMusic)<br>
[PlayerInReadyDict](#PlayerInReadyDict)<br>
[PlayerIsReady](#PlayerIsReady)<br>
[QuitGame](#QuitGame)<br>
[RecievedPhotonEvent](#RecievedPhotonEvent)<br>
[RefreshPlayerUIs](#RefreshPlayerUIs)<br>
[RemovePlayerToPlayerReadyList](#RemovePlayerToPlayerReadyList)<br>
[ResetEverything](#ResetEverything)<br>
[ResetLoadingBar](#ResetLoadingBar)<br>
[RestartMusic](#RestartMusic)<br>
[SavePlayerName](#SavePlayerName)<br>
[SavePlayerUIs](#SavePlayerUIs)<br>
[SaveRoomList](#SaveRoomList)<br>
[SaveRoomName](#SaveRoomName)<br>
[SaveRoomPassword](#SaveRoomPassword)<br>
[SaveSceneToLoad](#SaveSceneToLoad)<br>
[SaveSceneToLoad](#SaveSceneToLoad)<br>
[SceneLoaded](#SceneLoaded)<br>
[SendCreatedRandomSceneList](#SendCreatedRandomSceneList)<br>
[SendEnableAutoSpawn](#SendEnableAutoSpawn)<br>
[SendReadyState](#SendReadyState)<br>
[SendRoundTime](#SendRoundTime)<br>
[SendSceneChangeInfo](#SendSceneChangeInfo)<br>
[SendSceneVote](#SendSceneVote)<br>
[SendStartCountdown](#SendStartCountdown)<br>
[SendStartSession](#SendStartSession)<br>
[SendStopCountdown](#SendStopCountdown)<br>
[SendUpdateVoiceView](#SendUpdateVoiceView)<br>
[SetFadeToVolume](#SetFadeToVolume)<br>
[SetMusicAudio](#SetMusicAudio)<br>
[SetMusicVolume](#SetMusicVolume)<br>
[SetMyTeamName](#SetMyTeamName)<br>
[SetPlayer](#SetPlayer)<br>
[SetRandomSceneList](#SetRandomSceneList)<br>
[SetRoomIsJoinable](#SetRoomIsJoinable)<br>
[SetRoomVisibility](#SetRoomVisibility)<br>
[Start](#Start)<br>
[StopMusic](#StopMusic)<br>
[SubmitSavedPlayerName](#SubmitSavedPlayerName)<br>
[Update](#Update)<br>
[VisualKickPlayer](#VisualKickPlayer)<br>
[WaitForRandomJoin](#WaitForRandomJoin)<br>

------------------
 ### public virtual void AddNewPlayerToPlayerReadyList(Photon.Realtime.Player player)<a name="AddNewPlayerToPlayerReadyList"></a>
>   Takes a Photon.Realtime.Player input and extracts the user id of that player and adds it to the player ready dictionary as not ready. If that player's user id already exists in the dictionary it will make it be marked as not ready. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|player|Photon.Realtime.Player type, player to put into the dictionary|

[Back To Top](#)

------------------
 ### public virtual void AddToTeamData(string userId, string teamName)<a name="AddToTeamData"></a>
>   Returns the entire team data dictionary. This dictionary is a list of users ids and the teams those ids are on.   Adds the user id to the team name. If that user id is already in the dictionary it will move that user id to the new team name. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True| Dictionary of team data|

| Parameter Name | Description |
|:---|:---|
|userId|string type, Photon user id|
|teamName|string type, name of the team to join|

[Back To Top](#)

------------------
 ### public virtual bool AllPlayersReady()<a name="AllPlayersReady"></a>
>   Checks all the user ids in the player ready dictionary and sees if they have been marked as ready or not. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True| True if all user ids in the player ready dictionary are makrs as ready, otherwise false|

**No parameters**

[Back To Top](#)

------------------
 ### public virtual void ClearPlayerReadyDict()<a name="ClearPlayerReadyDict"></a>
>   Erases the entire dictionary of what players are ready. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### public virtual void ClearPlayerUIs()<a name="ClearPlayerUIs"></a>
>   Remove all saved player UIs from local manipulation. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### public virtual void ClearSavedRoomPassword()<a name="ClearSavedRoomPassword"></a>
>   Clears the `_roomPassword` internal variable. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### public virtual void ClearSceneVoteList()<a name="ClearSceneVoteList"></a>
>   Clears the `_sceneVotes` dictionary so it no longer has ANY votes in it. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### public virtual void ClearTeamData()<a name="ClearTeamData"></a>
>   Erases the entire team data dictionary. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### public virtual void CreatePrivateSession()<a name="CreatePrivateSession"></a>
>   Attempts to create a photon room with the saved `_roomName` and `_roomPassword` variables. Calls the `OnCreateRoomFailed` or `OnCreateRoomSuccess` UnityEvents if the room creation was successfull or not. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### public virtual void CreateRandomSceneList()<a name="CreateRandomSceneList"></a>
>   Populates the `_randomSceneList` list. This is used for players to cast votes as to what scene they would like to play at. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### public virtual void CreateSessionWithSavedRoomName(bool useSavedPassword = false)<a name="CreateSessionWithSavedRoomName"></a>
>   Create the initial photon room that will become the session name for your session. If you want to create a password protected room pass in true. Also will perform checks on the room name to make sure it's valid if you have enabled the `_roomNameChecking` variable to be true. Calls the `NetworkManager`'s `CreateRoom` function to create the Photon room. Finally calls `OnCreateRoomSuccess` UnityEvent if the room creation was successfull, or calls `OnCreateRoomFailed` if it was not. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|useSavedPassword|***No found decription**|

[Back To Top](#)

------------------
 ### public virtual void Disconnect()<a name="Disconnect"></a>
>   Calls the `NetworkManager`'s `Disconnect` function to disconnect from the photon room. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### public virtual void EnableChatBoxVisibility(bool isEnabled)<a name="EnableChatBoxVisibility"></a>
>   Make the chatbox inactive or not. True = Can see chatbox, False = Can NOT see chatbox 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|isEnabled|bool type, make the chatbox visible or not?|

[Back To Top](#)

------------------
 ### public virtual void EnableChatboxSlideOut(bool isEnabled)<a name="EnableChatboxSlideOut"></a>
>   Make the chatbox slide in or out. True = Slide out(visible), False = Slide in(not visible) 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|isEnabled|bool type, True = Slide Out|

[Back To Top](#)

------------------
 ### public virtual void EnableLoadingPage(bool isEnabled)<a name="EnableLoadingPage"></a>
>   Display the loading page UI or not. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|isEnabled|bool type, show the loading page?|

[Back To Top](#)

------------------
 ### public virtual void EnableMouseMovement(bool isEnabled)<a name="EnableMouseMovement"></a>
>   Allow the mouse to be moved around or not. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|isEnabled|bool type, true = can move, false = cannot move|

[Back To Top](#)

------------------
 ### public virtual void EnableMouseVisibility(bool isVisible)<a name="EnableMouseVisibility"></a>
>   Hide or show the mouse. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|isVisible|bool type, true = show, false = hide|

[Back To Top](#)

------------------
 ### public virtual void EnableMusic(bool isEnabled)<a name="EnableMusic"></a>
>   Disables/Enables the `musicSource` component based on the input value. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|isEnabled|bool type, Enable or Disable `musicSource` component.|

[Back To Top](#)

------------------
 ### public virtual void EnablePlayerAutoSpawn(bool setActive)<a name="EnablePlayerAutoSpawn"></a>
>   Sets the `NetworkManager`'s `autoSpawnPlayer` value to whatever input value you use. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|setActive|bool type, make the players auto spawn?|

[Back To Top](#)

------------------
 ### public virtual void EnableRoomNameChecking(bool isEnabled)<a name="EnableRoomNameChecking"></a>
>   Returns the internal variable `_rooms`. This is just a list of potential photon rooms.   Turn on valid room name checking. This makes it so rooms names can't have invalid characters or be blank. If this is on and rooms have these it will throw an error. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True| Dictionary of photon rooms|

| Parameter Name | Description |
|:---|:---|
|isEnabled|bool type, ensure valid room names.|

[Back To Top](#)

------------------
 ### public virtual void EnableSavedPlayerUI(bool isEnabled)<a name="EnableSavedPlayerUI"></a>
>   Find all of the UI's that invector provides and enable them or not. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|isEnabled|bool type, disable or enable the Invector provided UIs?|

[Back To Top](#)

------------------
 ### public virtual void EveryoneLoadLevel(string levelName)<a name="EveryoneLoadLevel"></a>
>   Calls the `NetworkManager`'s `NetworkLoadLevel` with the `sendEveryone` value as true. It will load the unity scene based on the input value's index. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|levelName|string type, the scene name to find the index for|

[Back To Top](#)

------------------
 ### public virtual void EveryoneLoadLevel(int levelIndex)<a name="EveryoneLoadLevel"></a>
>   Calls the `NetworkManager`'s `NetworkLoadLevel with the `sendEveryone` value as true. It will load the unity scene based on the index you pass in. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|levelIndex|int type, the scene index to load|

[Back To Top](#)

------------------
 ### public virtual void EveryoneLoadSavedLevel()<a name="EveryoneLoadSavedLevel"></a>
>   Calls the `NetworkManager`'s `NetworkLoadLevel` function with the sendEveryone variable as true. It uses the previously saved level name's index. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### public virtual void FadeMusic(bool fadeOut)<a name="FadeMusic"></a>
>   Fade the `musicSource` in or out based on the input value. True = Fade Out, False = Fade In 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|fadeOut|bool type, fade music in or out?|

[Back To Top](#)

------------------
 ### public virtual string GetMyTeamName()<a name="GetMyTeamName"></a>
>   Returns the string value that is stored in the `NetworkManager`'s `teamName` parameter. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True| string value in the `teamName` parameter of the NetworkManager component|

**No parameters**

[Back To Top](#)

------------------
 ### public virtual int GetPlayerVoiceView(string UserId)<a name="GetPlayerVoiceView"></a>
>   Get the voice view of the passed in photon user id. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True| The photon voice view of the user id|

| Parameter Name | Description |
|:---|:---|
|UserId|string type, the photon user id|

[Back To Top](#)

------------------
 ### public virtual SceneOption GetRandomSceneNumber(int value)<a name="GetRandomSceneNumber"></a>
>   Returns an amount of random `SceneOption`'s from the `_randomSceneList` list. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True| Specified number of `SceneOption`'s|

| Parameter Name | Description |
|:---|:---|
|value|int type, number of `SceneOption`'s to return|

[Back To Top](#)

------------------
 ### public virtual string GetSavedSceneToLoadName()<a name="GetSavedSceneToLoadName"></a>
>   Returns the previously saved level name 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True| the previously saved level name|

**No parameters**

[Back To Top](#)

------------------
 ### public virtual SceneOption GetSceneNumber(int value)<a name="GetSceneNumber"></a>
>   Extracts the `SceneOption` value from the `sceneList` list at the specified index. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True| A `SceneOption` value|

| Parameter Name | Description |
|:---|:---|
|value|int type, the index to pull from|

[Back To Top](#)

------------------
 ### public virtual int GetSceneVotes(int sceneIndex)<a name="GetSceneVotes"></a>
>   Returns the entire `_sceneVotes` dictionary which contains all the votes that people have currently cast for a scene index. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True| |

| Parameter Name | Description |
|:---|:---|
|sceneIndex|int type, the scene index to see how many votes it has|

[Back To Top](#)

------------------
 ### public virtual GameObject GetSetPlayer()<a name="GetSetPlayer"></a>
>   Get the `playerPrefab` from the network manager. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True| GameObject of the player that you have set in the `NetworkManager`|

**No parameters**

[Back To Top](#)

------------------
 ### public virtual int GetSetPlayerIndex()<a name="GetSetPlayerIndex"></a>
>   Returns the current selected player index that will be used to select a player later. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True| |

**No parameters**

[Back To Top](#)

------------------
 ### public virtual string GetUserTeamName(string userId)<a name="GetUserTeamName"></a>
>   Finds the team name that the photon user id is a part of. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True| the string team name that the user id is a part of|

| Parameter Name | Description |
|:---|:---|
|userId|string type, the photon user id|

[Back To Top](#)

------------------
 ### public virtual void JoinLobby()<a name="JoinLobby"></a>
>   Calls the instanced `NetworkManager`'s `JoinLobby` function. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### public virtual void JoinPrivateRoom()<a name="JoinPrivateRoom"></a>
>   Calls the instance'd `NetworkManager`'s `JoinRandomRoom` function with the previous set internal variables `_roomName` and `_roomPassword` parameters. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### public virtual void JoinRandomPublicRoomOrCreateOne()<a name="JoinRandomPublicRoomOrCreateOne"></a>
>   Calls the `WaitForRandomJoin` IEnumerator. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### public virtual void JoinRoom(string roomname)<a name="JoinRoom"></a>
>   Calls the instanceds `NetworkManager`'s `JoinRoom` function with the input value and immediately calls the `OnWaitToJoinPhotonRoomsLobby` UnityEvent. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|roomname|string type, the name of the photon room to join|

[Back To Top](#)

------------------
 ### public virtual void JoinSavedRoomName(bool useSavedPassword)<a name="JoinSavedRoomName"></a>
>   Calls the instance'd `NetworkManager`'s `JoinRandomRoom` function with the `_roomName` internal variable that was saved from the `SaveRoomName` function. Also uses the saved `_roomPassword` is the input value is true. Immediately calls the `OnWaitToJoinPhotonRoomsLobby` UnityEvent. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|useSavedPassword|bool type, use the previously set room password or join without a password?|

[Back To Top](#)

------------------
 ### public virtual void KickPlayer(string userId)<a name="KickPlayer"></a>
>   Calls the `VisualKickPlayer` IEnumerator wit the `userId`. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|userId|string type, the photon user id to boot from the photon room.|

[Back To Top](#)

------------------
 ### public virtual void LoadSavedLevel()<a name="LoadSavedLevel"></a>
>   Calls the `NetworkManager`'s `NetworkLoadLevel` function with the previously saved level name's index. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### public virtual void LoopMusic(bool setLooping)<a name="LoopMusic"></a>
>   Set the `musicSource` loop value. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|setLooping|bool type, loop the `musicSource` or not?|

[Back To Top](#)

------------------
 ### public virtual void MouseSelect(GameObject target)<a name="MouseSelect"></a>
>   Calls the `MouseSelectHandle` IEnumerator 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|target|***No found decription**|

[Back To Top](#)

------------------
 ### IEnumerator MouseSelectHandle(GameObject target)<a name="MouseSelectHandle"></a>
>   Sets the target the mouse will select based on the input target. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|private|False|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|target|GameObject type, the target for the mouse to select|

[Back To Top](#)

------------------
 ### protected virtual void MouseSelectTarget(GameObject target)<a name="MouseSelectTarget"></a>
>   Have the mouse select the target gameobect 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|target|Gameobject type, the gameobject for the mouse to select|

[Back To Top](#)

------------------
 ### public virtual void NetworkErrorOccured(string errorMessage)<a name="NetworkErrorOccured"></a>
>   Calls the `OnNetworkError` UnityEvent with the passed in string 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|errorMessage|string type, the error message to display|

[Back To Top](#)

------------------
 ### protected virtual void PhotonEvent_AUTOSPAWN(object[] data)<a name="PhotonEvent_AUTOSPAWN"></a>
>   Calls the `SendEnableAutoSpawn` function. This is a received Photon Event. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|data|***No found decription**|

[Back To Top](#)

------------------
 ### protected virtual void PhotonEvent_KICKPLAYER(object[] data)<a name="PhotonEvent_KICKPLAYER"></a>
>   Makes the receiver of this event leave the photon room with an error message. This is a received photon event. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|data|***No found decription**|

[Back To Top](#)

------------------
 ### protected virtual void PhotonEvent_MAPCHANGE(object[] data)<a name="PhotonEvent_MAPCHANGE"></a>
>   Makes the receiver change the saved leve name and index. This is a received photon event. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|data|***No found decription**|

[Back To Top](#)

------------------
 ### protected virtual void PhotonEvent_RANDOMSCENELIST(object[] data)<a name="PhotonEvent_RANDOMSCENELIST"></a>
>   Makes the receiver set their `_randomSceneList` variable to whatever is received. This is a received photon event. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|data|***No found decription**|

[Back To Top](#)

------------------
 ### protected virtual void PhotonEvent_READUP(object[] data)<a name="PhotonEvent_READUP"></a>
>   Makes the user id ready up. This is a received PhotonEvent message. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|data|***No found decription**|

[Back To Top](#)

------------------
 ### protected virtual void PhotonEvent_ROUNDTIME(object[] data)<a name="PhotonEvent_ROUNDTIME"></a>
>   Sets the round time to be whatever is received. This is a received photon event. This also calls the `OnReceiveRoundTime` UnityEvent. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|data|***No found decription**|

[Back To Top](#)

------------------
 ### protected virtual void PhotonEvent_SCENEVOTE(object[] data)<a name="PhotonEvent_SCENEVOTE"></a>
>   Adds or removes a vote to the scene vote index. This is a received photon event. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|data|***No found decription**|

[Back To Top](#)

------------------
 ### protected virtual void PhotonEvent_STARTCOUNTDOWN(object[] data)<a name="PhotonEvent_STARTCOUNTDOWN"></a>
>   Makes the receiver call the `OnCountdownStarted` or `OnCountdownStopped` UnityEvents based on the received value. This is a received photon event. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|data|***No found decription**|

[Back To Top](#)

------------------
 ### protected virtual void PhotonEvent_STARTSESSION(object[] data)<a name="PhotonEvent_STARTSESSION"></a>
>   Makes everyone start the session and this will make it so the `RecievedPhotonEvent` function will not be called anymore when receiving events from the network. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|data|***No found decription**|

[Back To Top](#)

------------------
 ### protected virtual void PhotonEvent_TEAMCHANGE(object[] data)<a name="PhotonEvent_TEAMCHANGE"></a>
>   Makes a user id change to a new team. This is a received PhotonEvent message. Also executes the `teamsUpdated` delegate. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|data|***No found decription**|

[Back To Top](#)

------------------
 ### protected virtual void PhotonEvent_VOICEVIEW(object[] data)<a name="PhotonEvent_VOICEVIEW"></a>
>   Sets the voice view id for the user id for later referencing. Also calls the `voiceViewUpdated` delegate. This is a received photon event. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|data|***No found decription**|

[Back To Top](#)

------------------
 ### public virtual void PlayFinalClick()<a name="PlayFinalClick"></a>
>   Play the `finalClick` audio clip from the `soundSource` 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### public virtual void PlayMouseClick()<a name="PlayMouseClick"></a>
>   Play the `mouseClick` audio clip from the `soundSource` 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### public virtual void PlayMouseEnter()<a name="PlayMouseEnter"></a>
>   Play the `mouseEnter` audio clip from the `soundSource` 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### public virtual void PlayMouseExit()<a name="PlayMouseExit"></a>
>   Play the `mouseExit` audio clip from the `soundSource` 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### public virtual void PlayMusic()<a name="PlayMusic"></a>
>   Starts playing the audio clip on the `musicSource`. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### public virtual bool PlayerInReadyDict(string userId)<a name="PlayerInReadyDict"></a>
>   Returns true if the user id is already in the player read dictionary. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True| true if that id is in the player ready dictionary, otherwise false.|

| Parameter Name | Description |
|:---|:---|
|userId|string type, photon user id|

[Back To Top](#)

------------------
 ### public virtual bool PlayerIsReady(string userId)<a name="PlayerIsReady"></a>
>   Returns the dictionary of users ids and if they're ready or not   Checks to see if that user id is marked as ready by looking it up in the player ready dictionary. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True| player ready dictionary true if the player is marked as ready in the player ready dictionary, otherwise false.|

| Parameter Name | Description |
|:---|:---|
|userId|string type, the photon user id|

[Back To Top](#)

------------------
 ### public virtual void QuitGame()<a name="QuitGame"></a>
>   Quit the unity application. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### protected virtual void RecievedPhotonEvent(EventData obj)<a name="RecievedPhotonEvent"></a>
>   Called when ANY photon event is received. Will find out what type of event it is and call that function. (EX: If receiving `CB_EVENT_STARTSESSION` photon event it will call the `PhotonEvent_STARTSESSION` function) 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|obj|***No found decription**|

[Back To Top](#)

------------------
 ### public virtual void RefreshPlayerUIs()<a name="RefreshPlayerUIs"></a>
>   Rebuilds the saved player UIs list. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### public virtual void RemovePlayerToPlayerReadyList(Photon.Realtime.Player player)<a name="RemovePlayerToPlayerReadyList"></a>
>   Takes a Photon.Realtime.Player input and extracts the user id of that player, finds that user id in the player ready dictionary and removes it from the dictionary. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|player|Photon.Realtime.Player type, the player to remove|

[Back To Top](#)

------------------
 ### public virtual void ResetEverything()<a name="ResetEverything"></a>
>   Called when you want to reset the UI back to its default state. Will clear all parameters and attempt to reset this component back to its starting values. Also calls `OnResetEverything` UnityEvent for additional user-defined actions. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### public virtual void ResetLoadingBar()<a name="ResetLoadingBar"></a>
>   Sets the `loadingBar` to zero. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### public virtual void RestartMusic()<a name="RestartMusic"></a>
>   Will start the audio clip from the beginning again on the `musicSource`. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### public virtual void SavePlayerName(string playerName)<a name="SavePlayerName"></a>
>   Saves the input string as a future player name that will be used by the \ `SubmitSavedPlayerName` function. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|playerName|string type, the player name to potentially use.|

[Back To Top](#)

------------------
 ### public virtual void SavePlayerUIs()<a name="SavePlayerUIs"></a>
>   Find all the objects tagged with `PlayerUI` and save them for later manipulation. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### public virtual void SaveRoomList()<a name="SaveRoomList"></a>
>   Populates the internal variable `_rooms` based on the `cachedRoomList` value in the `NetworkManager` component. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### public virtual void SaveRoomName(string roomName)<a name="SaveRoomName"></a>
>   Stores the room name input for future use into the `_roomName` internal variable. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|roomName|string type, the name of the photon room to save.|

[Back To Top](#)

------------------
 ### public virtual void SaveRoomPassword(string password)<a name="SaveRoomPassword"></a>
>   Saves the input string into the `_roomPassword` internal variable for later use. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|password|string type, the password you want to include when joining/creating rooms.|

[Back To Top](#)

------------------
 ### public virtual void SaveSceneToLoad(string levelName)<a name="SaveSceneToLoad"></a>
>   Calls `SendSceneChangeInfo` function with the extracted index of the scene name that you input and the scene name. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|levelName|string type, the scene name to have everyone set their map choice to|

[Back To Top](#)

------------------
 ### public virtual void SaveSceneToLoad(int levelIndex)<a name="SaveSceneToLoad"></a>
>   Calls `SendSceneChangeInfo` with the extracts name of the scene index that you input and the index. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|levelIndex|***No found decription**|

[Back To Top](#)

------------------
 ### protected virtual void SceneLoaded(Scene scene, LoadSceneMode mode)<a name="SceneLoaded"></a>
>   Callback method. This is called when a new Unity scene is loaded. This calls the `OnSceneLoaded` UnityEvent. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|scene|Scene type, the Scene that was loaded|
|mode|LoadSceneMode type, how this scene was loaded|

[Back To Top](#)

------------------
 ### public virtual void SendCreatedRandomSceneList()<a name="SendCreatedRandomSceneList"></a>
>   Calls the `CB_EVENT_RANDOMSCENELIST` PhotonEvent which will make everyone set their `_randomSceneList` list to the value that you currently have set in your own `_randomSceneList` list. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### public virtual void SendEnableAutoSpawn(bool enableSpawn)<a name="SendEnableAutoSpawn"></a>
>   Calls the `CB_EVENT_AUTOSPAWN` Photon Event. This will make it so autospawn is enabled when a new Unity scene is loaded. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|enableSpawn|bool type, enable auto spawn?|

[Back To Top](#)

------------------
 ### public virtual void SendReadyState(bool isReady)<a name="SendReadyState"></a>
>   Calls the `CB_EVENT_READYUP` PhotonEvent. This event will make your user id be marked as ready or not based on the input value. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|isReady|bool type, you're ready?|

[Back To Top](#)

------------------
 ### public virtual void SendRoundTime(float roundTime)<a name="SendRoundTime"></a>
>   Calls the `CB_EVENT_ROUNDTIME` PhotonEvent to set the round time to whatever number is passed into this function for everyone in the photon room. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|roundTime|float type, the amount of time to set the round to|

[Back To Top](#)

------------------
 ### protected virtual void SendSceneChangeInfo(string sceneName, int index)<a name="SendSceneChangeInfo"></a>
>   Calls the `CB_EVENT_MAPCHANGE` photon event. Sets the scene name and index for all players in the photon room. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|sceneName|string type, the scene name to set to|
|index|int type, the index of this scene name|

[Back To Top](#)

------------------
 ### public virtual void SendSceneVote(int sceneIndex)<a name="SendSceneVote"></a>
>   Calls the `CB_EVENT_SCENEVOTE` PhotonEvent which will add one to all players `_sceneVotes` at the index key you have specified. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|sceneIndex|int type, the scene index to vote for. |

[Back To Top](#)

------------------
 ### public virtual void SendStartCountdown(float amount)<a name="SendStartCountdown"></a>
>   Calls the `CB_EVENT_STARTCOUNTDOWN` PhotonEvent, which will trigger the countdown to start. This will trigger the `OnCountdownStarted` UnityEvent for all players that receive this event, including yourself. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|amount|float type, countdown amount|

[Back To Top](#)

------------------
 ### public virtual void SendStartSession()<a name="SendStartSession"></a>
>   Calls the `CB_EVENT_STARTSESSION` photon event. Which makes everyone start the photon session. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### public virtual void SendStopCountdown()<a name="SendStopCountdown"></a>
>   Calls the `CB_EVENT_STARTCOUNTDOWN` PhotonEvent which will make all players, including yourself, stop the countdown process. This all triggers the `OnCountdownStopped` UnityEvent for everyone, including yourself. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### public virtual void SendUpdateVoiceView(string UserId, int ViewId)<a name="SendUpdateVoiceView"></a>
>   Calls the `CB_EVENT_VOICEVIEW` PhotonEvent. This eventually will execute the `voiceViewUpdated` delegate. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|UserId|***No found decription**|
|ViewId|***No found decription**|

[Back To Top](#)

------------------
 ### public virtual void SetFadeToVolume(float fadeToVolume)<a name="SetFadeToVolume"></a>
>   Set the music to fade to the selected volume next time you trigger a fade music. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|fadeToVolume|float type, the volume to set the music to fade to|

[Back To Top](#)

------------------
 ### public virtual void SetMusicAudio(AudioClip clip)<a name="SetMusicAudio"></a>
>   Set the `musicSource` audio clip. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|clip|AudioClip type, the clip to set the `musicSource` to.|

[Back To Top](#)

------------------
 ### public virtual void SetMusicVolume(float volume)<a name="SetMusicVolume"></a>
>   Immediately set the `musicSource` volume level. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|volume|float type, the volume level to set the music to|

[Back To Top](#)

------------------
 ### public virtual void SetMyTeamName(string teamName = "")<a name="SetMyTeamName"></a>
>   Calls the `CB_EVENT_TEAMCHANGE` PhotonEvent. This will set your photon user id to be on the team name that matches the input value. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|teamName|string type, what team to join.|

[Back To Top](#)

------------------
 ### public virtual void SetPlayer(int index)<a name="SetPlayer"></a>
>   Will set the player according to the input index. Will choose the player to set as the `playerPrefab` in the NetworkManager from the `selectablePlayers` list. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|index|int type, the index to choose from the `selectablePlayers` list.|

[Back To Top](#)

------------------
 ### public virtual void SetRandomSceneList(List<SceneOption> randomRoomList)<a name="SetRandomSceneList"></a>
>   Receives as scene list and sets it to the `_randomSceneList` list. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|randomRoomList|***No found decription**|

[Back To Top](#)

------------------
 ### public virtual void SetRoomIsJoinable(bool isJoinable)<a name="SetRoomIsJoinable"></a>
>   Calls the `NetworkManager`'s `SetRoomIsOpen` function with whatever value you have specified in this function. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|isJoinable|bool type, make this photon room joinable?|

[Back To Top](#)

------------------
 ### public virtual void SetRoomVisibility(bool isVisible)<a name="SetRoomVisibility"></a>
>   Make this photon room visible or not. Calls the `NetworkManager`'s `SetRoomVisibility` function with the input value specified here. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|isVisible|bool type, make the photon room be in the list when people list rooms.|

[Back To Top](#)

------------------
 ### protected virtual void Start()<a name="Start"></a>
>   Sets the music volume, Adds the `AddNewPlayerToPlayerReadyList` and `RemovePlayerToPlayerReadyList` functions to the `OnPlayerJoinedCurrentRoom` and `OnPlayerLeftCurrentRoom` delegates of the `NetworkManager` component. Also sets up the `SceneLoaded` function to be called when a new scene is loaded. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### public virtual void StopMusic()<a name="StopMusic"></a>
>   Stops playing the audio clip on the `musicSource` 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### public virtual void SubmitSavedPlayerName()<a name="SubmitSavedPlayerName"></a>
>   Calls the `OnNameEnterFailed` or `OnNameEnterSuccess` UnityEvents if the player name that was saved previously passes the tests or not. If it passes the tests it will send this player name to the NetworkManager's `SetPlayerName` function. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### protected virtual void Update()<a name="Update"></a>
>   Controls music volumes, loading bars, load images, loading titles, and loading descriptions. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### IEnumerator VisualKickPlayer(string userId)<a name="VisualKickPlayer"></a>
>   Calls the `CB_EVENT_KICKPLAYER` PhotonEvent. Which will force the owner of photon user id to leave the photon room. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|private|False|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|userId|string type, the owner's user id to boot from the photon room.|

[Back To Top](#)

------------------
 ### IEnumerator WaitForRandomJoin()<a name="WaitForRandomJoin"></a>
>   Joins the Photon Lobby and attempts to find an open room that isn't at capacity yet. If one isn't found it will generate a new room with a random hash room name. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|private|False|Does not return anything|

**No parameters**

[Back To Top](#)

