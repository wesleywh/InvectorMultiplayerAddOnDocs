[Back To Index](../../index.md)

# ExampleUI

[Jump To Parameters](#parameter-definitions)<br/>

--------------------------------------------------------
## Parameter Definitions<a name="parameter-definitions"></a>

Select the parameter name from below to jump directly to it on this page.

[AvailableRooms](#parameter-AvailableRooms)<br>
[AvailableScenes](#parameter-AvailableScenes)<br>
[ChooseRoomPage](#parameter-ChooseRoomPage)<br>
[HostGamePage](#parameter-HostGamePage)<br>
[JoinGamePage](#parameter-JoinGamePage)<br>
[LoadingBar](#parameter-LoadingBar)<br>
[LoadingDescriptionText](#parameter-LoadingDescriptionText)<br>
[LoadingPage](#parameter-LoadingPage)<br>
[LoadingPreviewImage](#parameter-LoadingPreviewImage)<br>
[LoadingPreviewImageTransitionSpeed](#parameter-LoadingPreviewImageTransitionSpeed)<br>
[LoadingTitleText](#parameter-LoadingTitleText)<br>
[LobbyPage](#parameter-LobbyPage)<br>
[MainPage](#parameter-MainPage)<br>
[NameErrorPage](#parameter-NameErrorPage)<br>
[NameInputField](#parameter-NameInputField)<br>
[NetworkErrorPage](#parameter-NetworkErrorPage)<br>
[NetworkErrorText](#parameter-NetworkErrorText)<br>
[PanelPage](#parameter-PanelPage)<br>
[PlayerCardAnimation](#parameter-PlayerCardAnimation)<br>
[PlayerCardPage](#parameter-PlayerCardPage)<br>
[PlayerCardText](#parameter-PlayerCardText)<br>
[PlayerNamePage](#parameter-PlayerNamePage)<br>
[PlayerPrefabSelectPage](#parameter-PlayerPrefabSelectPage)<br>
[RoomNameInput](#parameter-RoomNameInput)<br>
[connectionStatus](#parameter-connectionStatus)<br>
[createRoomButton](#parameter-createRoomButton)<br>
[effectChildren](#parameter-effectChildren)<br>
[fadeInAudio](#parameter-fadeInAudio)<br>
[fadeInUI](#parameter-fadeInUI)<br>
[fadeObjects](#parameter-fadeObjects)<br>
[fadeOutSpeed](#parameter-fadeOutSpeed)<br>
[finalClick](#parameter-finalClick)<br>
[finalClickVolume](#parameter-finalClickVolume)<br>
[loadImageDisplayTime](#parameter-loadImageDisplayTime)<br>
[lobbyIndex](#parameter-lobbyIndex)<br>
[lobbyOnlyRoomCreate](#parameter-lobbyOnlyRoomCreate)<br>
[mouseClick](#parameter-mouseClick)<br>
[mouseClickVolume](#parameter-mouseClickVolume)<br>
[mouseEnter](#parameter-mouseEnter)<br>
[mouseEnterVolume](#parameter-mouseEnterVolume)<br>
[mouseExit](#parameter-mouseExit)<br>
[mouseExitVolume](#parameter-mouseExitVolume)<br>
[musicSource](#parameter-musicSource)<br>
[playerCardDisplayTime](#parameter-playerCardDisplayTime)<br>
[players](#parameter-players)<br>
[roomButton](#parameter-roomButton)<br>
[soundSource](#parameter-soundSource)<br>
[startVolume](#parameter-startVolume)<br>
[successNameInputTravelTo](#parameter-successNameInputTravelTo)<br>
[titleImage](#parameter-titleImage)<br>
[uiFadeSpeed](#parameter-uiFadeSpeed)<br>

------------------
### AvailableRooms<a name="parameter-AvailableRooms"></a>

> The transform element in your UI that will be used as a parent object for your room button.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |GameObject|None

[Back To Top](#)

------------------
### AvailableScenes<a name="parameter-AvailableScenes"></a>

> The transform element in your UI that will be used as a parent object for your available scenes buttons. This is a child element of your \"ChooseRoomPage\

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |GameObject|None

[Back To Top](#)

------------------
### ChooseRoomPage<a name="parameter-ChooseRoomPage"></a>

> The page that is displayed when there is more than one available room to join.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |GameObject|None

[Back To Top](#)

------------------
### HostGamePage<a name="parameter-HostGamePage"></a>

> The gameobject that holds all the child elements that make up the host game page.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |GameObject|None

[Back To Top](#)

------------------
### JoinGamePage<a name="parameter-JoinGamePage"></a>

> The gameobject that holds all the child elements that make up the join game page.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |GameObject|None

[Back To Top](#)

------------------
### LoadingBar<a name="parameter-LoadingBar"></a>

> The loading bar to display when loading a page.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |Slider|None

[Back To Top](#)

------------------
### LoadingDescriptionText<a name="parameter-LoadingDescriptionText"></a>

> The loading page description text to display.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |Text|None

[Back To Top](#)

------------------
### LoadingPage<a name="parameter-LoadingPage"></a>

> The page to display when loading a scene.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |GameObject|None

[Back To Top](#)

------------------
### LoadingPreviewImage<a name="parameter-LoadingPreviewImage"></a>

> The loading page preview image to display.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |Image|None

[Back To Top](#)

------------------
### LoadingPreviewImageTransitionSpeed<a name="parameter-LoadingPreviewImageTransitionSpeed"></a>

> How fast to fade in and out the images on the loading page.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|private |float|0.5f

[Back To Top](#)

------------------
### LoadingTitleText<a name="parameter-LoadingTitleText"></a>

> The loading page title text to display.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |Text|None

[Back To Top](#)

------------------
### LobbyPage<a name="parameter-LobbyPage"></a>

> The page to display when you are connected to a lobby of a room (NOT A PHOTON LOBBY).

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |GameObject|None

[Back To Top](#)

------------------
### MainPage<a name="parameter-MainPage"></a>

> The gameobject that holds all the child elements that make up the main page.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |GameObject|None

[Back To Top](#)

------------------
### NameErrorPage<a name="parameter-NameErrorPage"></a>

> The gameobject to enable when the player attempts to input an invalid name.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |GameObject|None

[Back To Top](#)

------------------
### NameInputField<a name="parameter-NameInputField"></a>

> The input field element that will be used to set the player name.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |InputField|None

[Back To Top](#)

------------------
### NetworkErrorPage<a name="parameter-NetworkErrorPage"></a>

> The gameobject to enable when you wish to display a network error.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |GameObject|None

[Back To Top](#)

------------------
### NetworkErrorText<a name="parameter-NetworkErrorText"></a>

> The text element that will be used to display any network errors/events.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |Text|None

[Back To Top](#)

------------------
### PanelPage<a name="parameter-PanelPage"></a>

> The gameobject that holds everything, just in case you need to disable everything.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |GameObject|None

[Back To Top](#)

------------------
### PlayerCardAnimation<a name="parameter-PlayerCardAnimation"></a>

> The animation component to call to player slide in/out animations.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |Animation|None

[Back To Top](#)

------------------
### PlayerCardPage<a name="parameter-PlayerCardPage"></a>

> The gameobject to display a player card.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |GameObject|None

[Back To Top](#)

------------------
### PlayerCardText<a name="parameter-PlayerCardText"></a>

> The text to set to display the recently joined player.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |Text|None

[Back To Top](#)

------------------
### PlayerNamePage<a name="parameter-PlayerNamePage"></a>

> The gameobject that holds all the child elements to set a players name.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |GameObject|None

[Back To Top](#)

------------------
### PlayerPrefabSelectPage<a name="parameter-PlayerPrefabSelectPage"></a>

> The gameobject that holds all the child elements to allow a player to select their character(prefab).

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |GameObject|None

[Back To Top](#)

------------------
### RoomNameInput<a name="parameter-RoomNameInput"></a>

> The input field element that will be used to capture the room name to start.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |InputField|None

[Back To Top](#)

------------------
### connectionStatus<a name="parameter-connectionStatus"></a>

> String elements that will be populated by the network manager connection status.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |Text[]|None

[Back To Top](#)

------------------
### createRoomButton<a name="parameter-createRoomButton"></a>

> The gameobject that holds the \"Create Room\" button.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |GameObject|None

[Back To Top](#)

------------------
### effectChildren<a name="parameter-effectChildren"></a>

> When fading do you want to effect the parent object and all of its children?

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|private |bool|true

[Back To Top](#)

------------------
### fadeInAudio<a name="parameter-fadeInAudio"></a>

> When first loading the UI, fade in the audio.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|private |bool|false

[Back To Top](#)

------------------
### fadeInUI<a name="parameter-fadeInUI"></a>

> Fade in your UI when first loading it.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|private |bool|true

[Back To Top](#)

------------------
### fadeObjects<a name="parameter-fadeObjects"></a>

> When fading effect this object. If effect all children is selected it will effect this object and all of its children.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|private |GameObject[]|null

[Back To Top](#)

------------------
### fadeOutSpeed<a name="parameter-fadeOutSpeed"></a>

> If fading out your music how to fast to fade out. Higher values will fade out faster.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|private |float|0.25f

[Back To Top](#)

------------------
### finalClick<a name="parameter-finalClick"></a>

> The sound that will be played when you call the \"PlayerFinalClick\" function.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|private |AudioClip|null

[Back To Top](#)

------------------
### finalClickVolume<a name="parameter-finalClickVolume"></a>

> How loud to play the \"finalClick\" sound.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|private |float|0.5f

[Back To Top](#)

------------------
### loadImageDisplayTime<a name="parameter-loadImageDisplayTime"></a>

> How long to display the loading images on the loading page before begining the fade/out in process.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|private |float|5.0f

[Back To Top](#)

------------------
### lobbyIndex<a name="parameter-lobbyIndex"></a>

> The index of the scene that will act as your room's lobby. You can find this index in the Build Settings when you specify what scenes to build in your project.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |int|0

[Back To Top](#)

------------------
### lobbyOnlyRoomCreate<a name="parameter-lobbyOnlyRoomCreate"></a>

> You must be in the lobby for the \"Create Room\" button to be displayed.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|private |bool|true

[Back To Top](#)

------------------
### mouseClick<a name="parameter-mouseClick"></a>

> The sound that will be played when you call the \"PlayerMouseClick\" function.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|private |AudioClip|null

[Back To Top](#)

------------------
### mouseClickVolume<a name="parameter-mouseClickVolume"></a>

> How loud to play the \"mouseClick\" sound.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|private |float|0.5f

[Back To Top](#)

------------------
### mouseEnter<a name="parameter-mouseEnter"></a>

> The sound that will be played when you call the \"PlayerMouseEnter\" function.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|private |AudioClip|null

[Back To Top](#)

------------------
### mouseEnterVolume<a name="parameter-mouseEnterVolume"></a>

> How loud to play the \"mouseEnter\" sound.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|private |float|0.5f

[Back To Top](#)

------------------
### mouseExit<a name="parameter-mouseExit"></a>

> The sound that will be played when you call the \"PlayerMouseExit\" function.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|private |AudioClip|null

[Back To Top](#)

------------------
### mouseExitVolume<a name="parameter-mouseExitVolume"></a>

> How loud to play the \"mouseExit\" sound.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|private |float|0.5f

[Back To Top](#)

------------------
### musicSource<a name="parameter-musicSource"></a>

> The audio source that will play your menu music.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|private |AudioSource|None

[Back To Top](#)

------------------
### playerCardDisplayTime<a name="parameter-playerCardDisplayTime"></a>

> How long to show the player card before sliding out.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|private |float|10.0f

[Back To Top](#)

------------------
### players<a name="parameter-players"></a>

> All of the possible players that can be selected. Used in combination with " <br>the \"SelectPlayer\" function in this component. Call this function BEFORE attempting " <br>to spawn your player as the playerPrefab on the NetworkManager is set from this " <br>function.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |GameObject[]|null

[Back To Top](#)

------------------
### roomButton<a name="parameter-roomButton"></a>

> A prefab element that will be spawned in when a room is found from the server.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |GameObject|None

[Back To Top](#)

------------------
### soundSource<a name="parameter-soundSource"></a>

> The audio source that will play your menu sounds.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|private |AudioSource|None

[Back To Top](#)

------------------
### startVolume<a name="parameter-startVolume"></a>

> How loud to set your audio to.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|private |float|0.5f

[Back To Top](#)

------------------
### successNameInputTravelTo<a name="parameter-successNameInputTravelTo"></a>

> The gameobject to set active after successfully entering your player name. " <br>If not supplied will travel to PlayerPrefabPage

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |GameObject|null

[Back To Top](#)

------------------
### titleImage<a name="parameter-titleImage"></a>

> The gameobject that is the title image.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |GameObject|None

[Back To Top](#)

------------------
### uiFadeSpeed<a name="parameter-uiFadeSpeed"></a>

> How fast to fade in your UI. Higher values will fade in faster.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|private |float|1.0f

[Back To Top](#)

