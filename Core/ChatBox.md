[Back To Index](../index.md)

# ChatBox

[Jump To Parameters](#parameter-definitions)<br/>
[Jump To Delegates](#delegate-definitions)<br/>
[Jump To Function Definitions](#functions-definitions)<br/>

--------------------------------------------------------
## Parameter Definitions<a name="parameter-definitions"></a>

Select the parameter name from below to jump directly to it on this page.

[ChatDisabled](#parameter-ChatDisabled)<br>
[ChatEnabled](#parameter-ChatEnabled)<br>
[OnReceiveBroadcastMessage](#parameter-OnReceiveBroadcastMessage)<br>
[OnUserSubscribedToDataChannel](#parameter-OnUserSubscribedToDataChannel)<br>
[OnUserUnSubscribedToDataChannel](#parameter-OnUserUnSubscribedToDataChannel)<br>
[OnYouSubscribeToAnyChannel](#parameter-OnYouSubscribeToAnyChannel)<br>
[OnYouSubscribeToDataChannel](#parameter-OnYouSubscribeToDataChannel)<br>
[OnYouUnSubscribeFromAnyChannel](#parameter-OnYouUnSubscribeFromAnyChannel)<br>
[OnYouUnSubscribeToDataChannel](#parameter-OnYouUnSubscribeToDataChannel)<br>
[ReceivedAnyChatMessage](#parameter-ReceivedAnyChatMessage)<br>
[ReceivedOtherPlayerChatMessage](#parameter-ReceivedOtherPlayerChatMessage)<br>
[authType](#parameter-authType)<br>
[autoScroll](#parameter-autoScroll)<br>
[chatAnim](#parameter-chatAnim)<br>
[chatChannel](#parameter-chatChannel)<br>
[chatNotification](#parameter-chatNotification)<br>
[closeWindowOnPress](#parameter-closeWindowOnPress)<br>
[connectionStatus](#parameter-connectionStatus)<br>
[enableOnConnect](#parameter-enableOnConnect)<br>
[messagesObj](#parameter-messagesObj)<br>
[msgInput](#parameter-msgInput)<br>
[newMessageIcon](#parameter-newMessageIcon)<br>
[nm](#parameter-nm)<br>
[notificationVolume](#parameter-notificationVolume)<br>
[onlyWhenWindowClose](#parameter-onlyWhenWindowClose)<br>
[openChatWindowOnPress](#parameter-openChatWindowOnPress)<br>
[otherChatMessage](#parameter-otherChatMessage)<br>
[parentChatObj](#parameter-parentChatObj)<br>
[protocol](#parameter-protocol)<br>
[region](#parameter-region)<br>
[scrollRect](#parameter-scrollRect)<br>
[sendChatOnPress](#parameter-sendChatOnPress)<br>
[slideIn](#parameter-slideIn)<br>
[slideOut](#parameter-slideOut)<br>
[source](#parameter-source)<br>
[startEnabled](#parameter-startEnabled)<br>
[yourChatMessage](#parameter-yourChatMessage)<br>

------------------
 ### ChatDisabled<a name="parameter-ChatDisabled"></a>
> UnityEvent. Called when you disable the chatbox.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |UnityEvent|None

[Back To Top](#)

------------------
 ### ChatEnabled<a name="parameter-ChatEnabled"></a>
> UnityEvent. Called when you enable the chatbox.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |UnityEvent|None

[Back To Top](#)

------------------
 ### OnReceiveBroadcastMessage<a name="parameter-OnReceiveBroadcastMessage"></a>
> UnityEvent. Called when you receive a Broadcast data message type.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |BroadCastUnityEvent|None

[Back To Top](#)

------------------
 ### OnUserSubscribedToDataChannel<a name="parameter-OnUserSubscribedToDataChannel"></a>
> UnityEvent. Called when another player subscribes to the data chat channel.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |StringUnityEvent|None

[Back To Top](#)

------------------
 ### OnUserUnSubscribedToDataChannel<a name="parameter-OnUserUnSubscribedToDataChannel"></a>
> UnityEvent. Called when another player un-subscribes from the data chat channel.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |StringUnityEvent|None

[Back To Top](#)

------------------
 ### OnYouSubscribeToAnyChannel<a name="parameter-OnYouSubscribeToAnyChannel"></a>
> UnityEvent. Called when YOU as the owner subscribe to a any new chat channel.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |StringUnityEvent|None

[Back To Top](#)

------------------
 ### OnYouSubscribeToDataChannel<a name="parameter-OnYouSubscribeToDataChannel"></a>
> UnityEvent. Called when YOU as the owner subscribe to the data chat channel.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |UnityEvent|None

[Back To Top](#)

------------------
 ### OnYouUnSubscribeFromAnyChannel<a name="parameter-OnYouUnSubscribeFromAnyChannel"></a>
> UnityEvent. Called when YOU as the owner un-subscribe from any chat channel.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |StringUnityEvent|None

[Back To Top](#)

------------------
 ### OnYouUnSubscribeToDataChannel<a name="parameter-OnYouUnSubscribeToDataChannel"></a>
> UnityEvent. Called when YOU as the owner un-subscribe from the data chat channel.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |UnityEvent|None

[Back To Top](#)

------------------
 ### ReceivedAnyChatMessage<a name="parameter-ReceivedAnyChatMessage"></a>
> UnityEvent. Called whenever ANY chat message is received.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |SentChatUnityEvent|None

[Back To Top](#)

------------------
 ### ReceivedOtherPlayerChatMessage<a name="parameter-ReceivedOtherPlayerChatMessage"></a>
> UnityEvent. Called whenver you receive a chat message from someone else.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |SentChatUnityEvent|None

[Back To Top](#)

------------------
 ### authType<a name="parameter-authType"></a>
> What type of authenication you want to use with this chat.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|None|CustomAuthenticationType|Photon.Chat.CustomAuthenticationType.None

[Back To Top](#)

------------------
 ### autoScroll<a name="parameter-autoScroll"></a>
> Whether or not you want to automatically scroll to the bottom when a new message comes in.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |bool|true

[Back To Top](#)

------------------
 ### chatAnim<a name="parameter-chatAnim"></a>
> The animator that controls the slide in/out actions of the chatbox.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |Animator|null

[Back To Top](#)

------------------
 ### chatChannel<a name="parameter-chatChannel"></a>
> The default channel to subscribe to if you don't set the channel in other ways.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |string|"worldChat"

[Back To Top](#)

------------------
 ### chatNotification<a name="parameter-chatNotification"></a>
> The notification sound you want to play

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |AudioClip|null

[Back To Top](#)

------------------
 ### closeWindowOnPress<a name="parameter-closeWindowOnPress"></a>
> The buttons that are responsible for closing the chat window

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |List<string>|new List<string>()

[Back To Top](#)

------------------
 ### connectionStatus<a name="parameter-connectionStatus"></a>
> The text element that will display the connection status.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |Text|null

[Back To Top](#)

------------------
 ### enableOnConnect<a name="parameter-enableOnConnect"></a>
> When successfully connected display the chatbox.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |bool|true

[Back To Top](#)

------------------
 ### messagesObj<a name="parameter-messagesObj"></a>
> The object that will hold all the generate message objects.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |GameObject|null

[Back To Top](#)

------------------
 ### msgInput<a name="parameter-msgInput"></a>
> The input field where you can type a chat message.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |InputField|null

[Back To Top](#)

------------------
 ### newMessageIcon<a name="parameter-newMessageIcon"></a>
> The icon that will appear when a new message is recieved.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |GameObject|null

[Back To Top](#)

------------------
 ### nm<a name="parameter-nm"></a>
> The network manager to reference. This will be things like the game version.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |NetworkManager|null

[Back To Top](#)

------------------
 ### notificationVolume<a name="parameter-notificationVolume"></a>
> How loud you want to play the notification sound.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |float|0.5f

[Back To Top](#)

------------------
 ### onlyWhenWindowClose<a name="parameter-onlyWhenWindowClose"></a>
> Only display the new message icon when the chat window is closed.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |bool|true

[Back To Top](#)

------------------
 ### openChatWindowOnPress<a name="parameter-openChatWindowOnPress"></a>
> The buttons that are responsible for opening the chat window

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |List<string>|new List<string>()

[Back To Top](#)

------------------
 ### otherChatMessage<a name="parameter-otherChatMessage"></a>
> The gameobject holding the \"ChatMessage\" component that will be generated when someone else sends you a message.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |GameObject|null

[Back To Top](#)

------------------
 ### parentChatObj<a name="parameter-parentChatObj"></a>
> The object that holds everything for your chat UI.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |GameObject|null

[Back To Top](#)

------------------
 ### protocol<a name="parameter-protocol"></a>
> The protocol to use for your chat client

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |ConnectionProtocol|ConnectionProtocol.Udp

[Back To Top](#)

------------------
 ### region<a name="parameter-region"></a>
> The region you want to have this chat client be in.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |PhotonChatRegions|PhotonChatRegions.US

[Back To Top](#)

------------------
 ### scrollRect<a name="parameter-scrollRect"></a>
> The scroll rect that controls the scrolling of the chatbox.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |ScrollRect|null

[Back To Top](#)

------------------
 ### sendChatOnPress<a name="parameter-sendChatOnPress"></a>
> Send your message on this keyboard press.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |List<string>|new List<string>()

[Back To Top](#)

------------------
 ### slideIn<a name="parameter-slideIn"></a>
> The name of the animation to play when the chat box is enabled. If you have a chatAnim component supplied.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |string|"Slide_In"

[Back To Top](#)

------------------
 ### slideOut<a name="parameter-slideOut"></a>
> The name of the animation to play when the chat box is disabled. If you have a chatAnim component supplied.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |string|"Slide_Out"

[Back To Top](#)

------------------
 ### source<a name="parameter-source"></a>
> Where the sound clip will play from.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |AudioSource|null

[Back To Top](#)

------------------
 ### startEnabled<a name="parameter-startEnabled"></a>
> Start with the chatbox out and selected.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |bool|false

[Back To Top](#)

------------------
 ### yourChatMessage<a name="parameter-yourChatMessage"></a>
> The gameobject holding the \"ChatMessage\" component that will be generated when you send a message.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |GameObject|null

[Back To Top](#)

## Delegate Definitions<a name="delegate-definitions"></a>

Select the delegate name from below to jump directly to it on this page.

[OnConnectedToChat](#delegate-OnConnectedToChat)<br>
[OnHideChatBox](#delegate-OnHideChatBox)<br>
[OnRecieveData](#delegate-OnRecieveData)<br>
[OnRecieveMessage](#delegate-OnRecieveMessage)<br>
[OnShowChatBox](#delegate-OnShowChatBox)<br>
[OnSubscribedToChannles](#delegate-OnSubscribedToChannles)<br>
[OnUnSubscribedFromChannels](#delegate-OnUnSubscribedFromChannels)<br>
[OnUserSubToChannel](#delegate-OnUserSubToChannel)<br>
[OnUserUnSubFromChannel](#delegate-OnUserUnSubFromChannel)<br>

------------------
 ### public BasicDelegate OnConnectedToChat<a name="delegate-OnConnectedToChat"></a>

>   Called when you have successfully connected to the chat server. 

**No parameters**

[Back To Top](#)

------------------
 ### public BasicDelegate OnHideChatBox<a name="delegate-OnHideChatBox"></a>

>   Called when you hide/slide out the chatbox. 

**No parameters**

[Back To Top](#)

------------------
 ### public ChatDataMessage OnRecieveData<a name="delegate-OnRecieveData"></a>

>   Called when you receive a data message in the chat. 

| Parameter Name | Description
|:---|:---|
|type|System.Type type, The system type of this serialized data.|
|incomingData|string type, Serialized dictionary data to be parsed by the data channel.|

[Back To Top](#)

------------------
 ### public SentChatMessageDelegate OnRecieveMessage<a name="delegate-OnRecieveMessage"></a>

>   Called when you receive a any message, data or chat. 

| Parameter Name | Description
|:---|:---|
|message|string type, SentChatMessage type which consists of the player name and the message.|

[Back To Top](#)

------------------
 ### public BasicDelegate OnShowChatBox<a name="delegate-OnShowChatBox"></a>

>   Called when you show/slide in the chatbox. 

**No parameters**

[Back To Top](#)

------------------
 ### public ChatSubChannels OnSubscribedToChannles<a name="delegate-OnSubscribedToChannles"></a>

>   Called when you unsubscribe from any channel. 

| Parameter Name | Description
|:---|:---|
|channels|string[] type, The chat channels that you want to subscribe to|
|results|bool[] type, If subscription was successful or not.|

[Back To Top](#)

------------------
 ### public ChatChannels OnUnSubscribedFromChannels<a name="delegate-OnUnSubscribedFromChannels"></a>

>   Called when you subscribe to any channel. 

| Parameter Name | Description
|:---|:---|
|channels|string[] type, the channels that you have unsubscribed from|

[Back To Top](#)

------------------
 ### public ChatUserChannel OnUserSubToChannel<a name="delegate-OnUserSubToChannel"></a>

>   Called when another user subscribes to any channel you're in. 

| Parameter Name | Description
|:---|:---|
|channel|string type, the channel the user has subscribe to|
|user|string type, the user that has subscribed|

[Back To Top](#)

------------------
 ### public ChatUserChannel OnUserUnSubFromChannel<a name="delegate-OnUserUnSubFromChannel"></a>

>   Delegate. Called when another user un-subscribes to any channel you're in. 

| Parameter Name | Description
|:---|:---|
|channel|string type, the channel the user has subscribe to|
|user|string type, the user that has subscribed|

[Back To Top](#)

## Function Definitions<a name="functions-definitions"></a>

Select the function name from below to jump directly to it on this page.

[AutoScrollToBottom](#AutoScrollToBottom)<br>
[Awake](#Awake)<br>
[BroadcastData](#BroadcastData)<br>
[Connect](#Connect)<br>
[DebugReturn](#DebugReturn)<br>
[Disconnect](#Disconnect)<br>
[Disconnect](#Disconnect)<br>
[DisplayNewChatIcon](#DisplayNewChatIcon)<br>
[EnableChat](#EnableChat)<br>
[EnableVisualBox](#EnableVisualBox)<br>
[FindPlayerCam](#FindPlayerCam)<br>
[GetUserId](#GetUserId)<br>
[IsConnectedToDataChannel](#IsConnectedToDataChannel)<br>
[IsDictionary](#IsDictionary)<br>
[IsEnabled](#IsEnabled)<br>
[IsPressingButton](#IsPressingButton)<br>
[OnApplicationQuit](#OnApplicationQuit)<br>
[OnChatStateChange](#OnChatStateChange)<br>
[OnConnected](#OnConnected)<br>
[OnDestroy](#OnDestroy)<br>
[OnDisconnected](#OnDisconnected)<br>
[OnGetMessages](#OnGetMessages)<br>
[OnPrivateMessage](#OnPrivateMessage)<br>
[OnStatusUpdate](#OnStatusUpdate)<br>
[OnSubscribed](#OnSubscribed)<br>
[OnUnsubscribed](#OnUnsubscribed)<br>
[OnUserSubscribed](#OnUserSubscribed)<br>
[OnUserUnsubscribed](#OnUserUnsubscribed)<br>
[PlayChatNotificationSound](#PlayChatNotificationSound)<br>
[ReceiveData](#ReceiveData)<br>
[ReceiveNewMessage](#ReceiveNewMessage)<br>
[SceneLoaded](#SceneLoaded)<br>
[SendMessage](#SendMessage)<br>
[SetActiveChannel](#SetActiveChannel)<br>
[SetActiveRoomAsChannelName](#SetActiveRoomAsChannelName)<br>
[SetMyPlayer](#SetMyPlayer)<br>
[Start](#Start)<br>
[SubscribeToChannel](#SubscribeToChannel)<br>
[UnSubscribeToChannel](#UnSubscribeToChannel)<br>
[Update](#Update)<br>

------------------
 ### public virtual void AutoScrollToBottom()<a name="AutoScrollToBottom"></a>
>   Make the scroll view of the chatbox scroll to the bottom. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### protected virtual void Awake()<a name="Awake"></a>
>   Used to unlock the mouse and make the mouse cursor visible. Also generates your players unique hash for the chat. Finally makes sure the chat icon is turned off. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### public virtual void BroadcastData(string channelName, object data)<a name="BroadcastData"></a>
>   Call this function to send data to a channel name to every player subscribed to that channel. Call 'BuildDataObj' function to format and build the serialized data string to send. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|channelName|string type, The name of the channel to send data over, must be subscribed to it.|
|data|object type, the data to send in the channelName|

[Back To Top](#)

------------------
 ### public virtual void Connect()<a name="Connect"></a>
>   Connect to the chat server. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### public virtual void DebugReturn(DebugLevel level, string message)<a name="DebugReturn"></a>
>   For debugging purposes only. Used to debug information 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|level|DebugLevel type|
|message|string type, the message that was recieved|

[Back To Top](#)

------------------
 ### public virtual void Disconnect(string placeholder = "")<a name="Disconnect"></a>
>   Disconnect from the chat server. This is only used in scenarios with things that need a string input. Simply calls the Disconnect() function. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|placeholder|Empty placeholder, does nothing.|

[Back To Top](#)

------------------
 ### public virtual void Disconnect()<a name="Disconnect"></a>
>   Disconnect from the chat server. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### public virtual void DisplayNewChatIcon(bool enabled)<a name="DisplayNewChatIcon"></a>
>   Enable or disable the chat icon. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|enabled|bool type, true = on/enabled|

[Back To Top](#)

------------------
 ### public virtual void EnableChat(bool enabled)<a name="EnableChat"></a>
>   Enable/Disable the chatbox, Lock/Unlock the mouse, Hide/Show the mouse, Lock/Unlock camera movement, slide in/slide out the chatbox and selects/ deselects the inputfield. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|enabled|***No found decription**|

[Back To Top](#)

------------------
 ### public virtual void EnableVisualBox(bool enabled)<a name="EnableVisualBox"></a>
>   Hide/Show the actual chatbox (not sliding in or out), actually enable of disable the object itself. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|enabled|***No found decription**|

[Back To Top](#)

------------------
 ### protected virtual void FindPlayerCam()<a name="FindPlayerCam"></a>
>   Find the camera that you use to look around with your player. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### public virtual string GetUserId()<a name="GetUserId"></a>
>   Returns your unique userid for the chatbox 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True| your unique user id|

**No parameters**

[Back To Top](#)

------------------
 ### public virtual bool IsConnectedToDataChannel()<a name="IsConnectedToDataChannel"></a>
>   Returns the subscribers of this channel.   Returns true or false if you're currently subscribed to the data channel. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True| list of users currently subscribed to this channel |

| Parameter Name | Description |
|:---|:---|
|channel|string type, the channel name|

[Back To Top](#)

------------------
 ### public virtual bool IsDictionary(object o)<a name="IsDictionary"></a>
>   Internal used function, true or false if the passed in object is a dictionary or not. Used as part of the data channel parsing. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True| true if dictionary, false if not|

| Parameter Name | Description |
|:---|:---|
|o|object type, the object to check|

[Back To Top](#)

------------------
 ### public virtual bool IsEnabled()<a name="IsEnabled"></a>
>   Returns true or false if the chatbox is active 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True| True or False, The chatbox is active?|

**No parameters**

[Back To Top](#)

------------------
 ### private bool IsPressingButton(List<string> codes)<a name="IsPressingButton"></a>
>   Returns true if pressing one of the passed in button names. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|private|False| true if pressing any one of these passed in button codes|

| Parameter Name | Description |
|:---|:---|
|codes|List of strings type, The button codes to check|

[Back To Top](#)

------------------
 ### public virtual void OnApplicationQuit()<a name="OnApplicationQuit"></a>
>   To avoid that the Editor becomes unresponsive, disconnect all Photon connections in OnApplicationQuit. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### public virtual void OnChatStateChange(ChatState state)<a name="OnChatStateChange"></a>
>   Callback method. Called whenever your connection status changes 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|state|ChatState type, the current connection state|

[Back To Top](#)

------------------
 ### public virtual void OnConnected()<a name="OnConnected"></a>
>   Callback method. Called when you are connected to the chat server 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### public virtual void OnDestroy()<a name="OnDestroy"></a>
>   To avoid that the Editor becoming unresponsive, disconnect all Photon connections in OnDestroy. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### public virtual void OnDisconnected()<a name="OnDisconnected"></a>
>   Callback method. Called when you get disconnected from the chat server 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### public virtual void OnGetMessages(string channelName, string[] senders, object[] messages)<a name="OnGetMessages"></a>
>   Callback method. Called whenever you receive a new message on ANY subscribed channel 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|channelName|string type, The channel name that is receiving the message|
|senders|string type, Who is sending the message|
|messages|string type, The actual string message|

[Back To Top](#)

------------------
 ### public virtual void OnPrivateMessage(string sender, object message, string channelName)<a name="OnPrivateMessage"></a>
>   Callback method. Called whenever you receive a private message 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|sender|string type, Who is sending the mesage|
|message|string type, The actual message|
|channelName|string type, The channel name receiving the message|

[Back To Top](#)

------------------
 ### public virtual void OnStatusUpdate(string user, int status, bool gotMessage, object message)<a name="OnStatusUpdate"></a>
>   Callback method. Called when a user's status has updated. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|user|string type, the user that updated|
|status|int type, the users current status|
|gotMessage|bool type, recieved the message|
|message|object type, the messsage that was sent|

[Back To Top](#)

------------------
 ### public virtual void OnSubscribed(string[] channels, bool[] results)<a name="OnSubscribed"></a>
>   Callback method. Called when you subscribed to a channel. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|channels|Array type, All the channels you tried subscribed to|
|results|Array type, the success or failure of this subscription|

[Back To Top](#)

------------------
 ### public virtual void OnUnsubscribed(string[] channels)<a name="OnUnsubscribed"></a>
>   Callback method. Called when you unsubscribe from a channel 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|channels|Array type, channel that were un-subscribed from|

[Back To Top](#)

------------------
 ### public virtual void OnUserSubscribed(string channel, string user)<a name="OnUserSubscribed"></a>
>   Callback method. Called when another user subscribes to a channel. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|channel|string type, the channel that was subscribed to|
|user|string type, the user that subscribed|

[Back To Top](#)

------------------
 ### public virtual void OnUserUnsubscribed(string channel, string user)<a name="OnUserUnsubscribed"></a>
>   Callback method. Called when another user un-subscribes from a channel. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|channel|string type, the channel that was unsubscribed from|
|user|string type, the user that unsubscribed|

[Back To Top](#)

------------------
 ### public virtual void PlayChatNotificationSound()<a name="PlayChatNotificationSound"></a>
>   Play the notification sound from the specific sound source in the parameters. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### public virtual void ReceiveData(Type type, string incomingData)<a name="ReceiveData"></a>
>   Use to receive serialized data convert it back to its original type and call an action based on the type of data that was recieved. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|type|System.Type type, The type of data object this is|
|incomingData|string type, The serialized data|

[Back To Top](#)

------------------
 ### public virtual void ReceiveNewMessage(SentChatMessage incoming)<a name="ReceiveNewMessage"></a>
>   Receive a message that was sent by another player and instantiate a new line in the chatbox with this information. Then trigger to display the chat icon. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|incoming|SentChatMessage type, consists of a player name and the message|

[Back To Top](#)

------------------
 ### protected virtual void SceneLoaded(Scene scene, LoadSceneMode mode)<a name="SceneLoaded"></a>
>   Callback method. Called when a scene has successfully loaded. This will call 'FindPlayerCam' function. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|scene|Scene type|
|mode|LoadSceneMode type|

[Back To Top](#)

------------------
 ### public virtual void SendMessage(string channelName, string message)<a name="SendMessage"></a>
>   Take an object and return a serialized version of it to send in data chatbox channels.   Send a string message to a channel name  that you're already subscribed to. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True| Serialized data that is compatible with the chatbox's data channel|

| Parameter Name | Description |
|:---|:---|
|data|object type, the data you want to serialize|
|channelName|string type, the channel name you want to send a message to.|
|message|string type, the actual message to send.|

[Back To Top](#)

------------------
 ### public virtual void SetActiveChannel(string newChannel)<a name="SetActiveChannel"></a>
>   Returns a list of all the channel names that you're subscribed to   Un-subscribe from the previous 'active' channel and subscribe to this channel, making it your currently active one. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True| List of channel names your subscribed to|

| Parameter Name | Description |
|:---|:---|
|newChannel|string type, the channel name.|

[Back To Top](#)

------------------
 ### public virtual void SetActiveRoomAsChannelName()<a name="SetActiveRoomAsChannelName"></a>
>   Unsubscribe from the previous 'active' channel and subscribe to a channel name that is the same as the current Photon Room you're in. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### protected virtual void SetMyPlayer()<a name="SetMyPlayer"></a>
>   Finds your player and populates internal variables so the chatbox can enable or disable various aspects of your character when the box is open or closed. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### protected virtual void Start()<a name="Start"></a>
>   Used to setup various settings in the chatbox like chat length, chat app settings, authentication values, finding player camera, finding your player, etc. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### public virtual void SubscribeToChannel(string channelName)<a name="SubscribeToChannel"></a>
>   The channel name you want to subscribe to. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|channelName|string type, the name of the channel|

[Back To Top](#)

------------------
 ### public virtual void UnSubscribeToChannel(string channelName)<a name="UnSubscribeToChannel"></a>
>   The channel name you want to un-subscribe from. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|channelName|string type, the name of the channel|

[Back To Top](#)

------------------
 ### protected virtual void Update()<a name="Update"></a>
>   Used to constantly ping the chat master server to keep that chatbox alive and capture new messages. Also watches for player input to enable/disable the chatbox. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

