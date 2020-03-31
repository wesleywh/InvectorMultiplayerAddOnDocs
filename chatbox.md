[Back To Index](index.md)

# Core Object: ChatBox  
<p align="center">
	<img src="https://i.imgur.com/0hAlLrB.jpg">
</p>
<br/>

### Sound Options
<img src="https://i.imgur.com/IRLvxBt.jpg">
<br/>

| Variable Name | Type | Description |
|:--- |:---:|:---|
| Source | AudioSource | The audiosource that will play chat notification sounds |
| Chat Notification | AudioClip | The sound that will play when you receive a new chat message |
| Notification Volume | Range[0,1] | The volume that the `Chat Notification` will be played at |

### Animation Options
<img src="https://i.imgur.com/QW6HfRn.jpg">
<br/>

| Variable Name | Type | Description |
|:--- |:---:|:---|
| Chat Anim | Animator | The animator component that has the `Slide In` and `Slide Out` animations |
| Slide In | string | The name of the animation to play in the animator component when you want to slide in the chatbox for use |
| Slide Out | string | The name of the animation to play in the animator component when you want to slide out the chatbox to not use it |

### ChatBox GameObject Parts Options
<img src="https://i.imgur.com/8qMEwEl.jpg">
<br/>

| Variable Name | Type | Description |
|:--- |:---:|:---|
| Parent Chat Obj | GameObject | The gameobject to disable/enable when you call enable chatbox function |
| Msg Input | InputField | The input field to read when you want to send a message. Will extract that text and send it across the network |
| Connection Status | Text | The text component to display the current `NetworkManager` connection status
| Message Obj | GameObject | The gameobject that will be the parent to all the message objects that are received from the network |
| Scroll Rect | ScrollView | The scrollbar to manipulate from the chatbox help actions |
| New Message Icon | GameObject | The icon to enable/disable when you receive a chat message |
| Only When Window Closed | bool | Only display the `New Message Icon` if the chatbox is closed when you receive a new message from the network |

### External Object References Options
<img src="https://i.imgur.com/viMxC8m.jpg">
<br/>

| Variable Name | Type | Description |
|:--- |:---:|:---|
| nm | NetworkManager | The `NetworkManager` component to read from. This is automatically populate if not supplied. |

### Connection Settings Options
<img src="https://i.imgur.com/wazLO3T.jpg">
<br/>

| Variable Name | Type | Description |
|:--- |:---:|:---|
| Protocol | string | The network protocol to use when sending message across the network. |
| Region | string | The photon server region to connect your chatbox to |
| Auth Type | Photon Auth Type | Read the photon documentation on auth types here: [Steam Authentication](https://doc.photonengine.com/en-us/chat/current/connection-and-authentication/authentication/steam-auth) |

### Input Settings Options
<img src="https://i.imgur.com/53isUO7.jpg">
<br/>

| Variable Name | Type | Description |
|:--- |:---:|:---|
| Open Chat Window On Press | string | The project settings key to press in order to open the chatbox. |
| Close Chat Window On Press | string | The project settings key to press in order to close the chatbox |
| Send Chat On Press | string | The project settings key to press to send whatever is in your `Msg Input` across the network |

### Helpful ChatBox Actions Options
<img src="https://i.imgur.com/P5uHh5m.jpg">
<br/>

| Variable Name | Type | Description |
|:--- |:---:|:---|
| Auto Scroll | bool | Will automatically scroll to the bottom of the scroll rect when you receive a new chat message. |
| Start Enabled | bool | Will enable the chatbox when the scene loads. |
| Enable On Connect | bool | Will enable the chatbox when you successfully connect to the chat server |
| Debugging | bool | (Disable for production release) Will verbose log everything to the unity console |

### Events

#### Data Events
<img src="https://i.imgur.com/P5uHh5m.jpg">
<br/>

| UnityEvent | Description |
|:--- |:---|
| OnReceiveBroadcastMessage | When the chatbox received a `BroadCastMessage` event this is called with that BroadCast Message |
| OnYouSubscribeToDataChannel | When you have successfully subscribed to the `Data` channel for this session. |
| OnUserSubscribedToDataChannel | When another person has successfully subscribed to the `Data` channel for this session. |
| OnUserUnSubscribeToDataChannel | When another person has unsubscribed from the `Data` channel for this session. |

#### Subscribe Events
<img src="https://i.imgur.com/9tPaB8W.jpg">
<br/>

| UnityEvent | Description |
|:--- |:---|
| OnYouSubscribeToAnyChannel | When you have successfully subscribed to any chat channel. |
| OnYouUnSubscribeToAnyChannel | When you have successfully un-subscribed to any chat channel. |

#### Subscribe Events
<img src="https://i.imgur.com/9tPaB8W.jpg">
<br/>

| UnityEvent | Description |
|:--- |:---|
| OnYouSubscribeToAnyChannel | When you have successfully subscribed to any chat channel. |
| OnYouUnSubscribeToAnyChannel | When you have successfully un-subscribed to any chat channel. |

#### Message Events
<img src="https://i.imgur.com/YcDsufg.jpg">
<br/>

| UnityEvent | Description |
|:--- |:---|
| ReceivedAnyChatMessage | Called when you receive any chat message (not a data message) |
| ReceivedOtherPlayerChatMessage | Called when you receive another players chat message (not a data message) |

#### Enable Events
<img src="https://i.imgur.com/4wwVVJv.jpg">
<br/>

| UnityEvent | Description |
|:--- |:---|
| ChatEnabled | Called when you enable the chatbox |
| ChatDisabled | Called when you disable the chatbox |