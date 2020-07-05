[Back To Index](../../index.md)

# VoiceChat

[Jump To Parameters](#parameter-definitions)<br/>
[Jump To Function Definitions](#functions-definitions)<br/>

--------------------------------------------------------
## Parameter Definitions<a name="parameter-definitions"></a>

Select the parameter name from below to jump directly to it on this page.

[buttonToPress](#parameter-buttonToPress)<br>
[connectionStatus](#parameter-connectionStatus)<br>
[debugging](#parameter-debugging)<br>
[ifOnTeam](#parameter-ifOnTeam)<br>
[isPlayer](#parameter-isPlayer)<br>
[pushToTalk](#parameter-pushToTalk)<br>
[recordingImage](#parameter-recordingImage)<br>
[speakerImage](#parameter-speakerImage)<br>

------------------
### buttonToPress<a name="parameter-buttonToPress"></a>

> Button press to enable voice transmittion.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |string|None

[Back To Top](#)

------------------
### connectionStatus<a name="parameter-connectionStatus"></a>

> Hidden variable. Shows the current voice connection status as an easy to reference string.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |string|""

[Back To Top](#)

------------------
### debugging<a name="parameter-debugging"></a>

> Verbose console logging to help you while you debug.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|private |bool|false

[Back To Top](#)

------------------
### ifOnTeam<a name="parameter-ifOnTeam"></a>

> Will only enable the voice chat indicator if you're on the target team. " <br>If left blank will always enable when talking across the network, no matter " <br>what team your on.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |string|""

[Back To Top](#)

------------------
### isPlayer<a name="parameter-isPlayer"></a>

> This component is for the player or not.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|private |bool|false

[Back To Top](#)

------------------
### pushToTalk<a name="parameter-pushToTalk"></a>

> Automatically record voice when speaking or require a button to be pushed.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|private |bool|false

[Back To Top](#)

------------------
### recordingImage<a name="parameter-recordingImage"></a>

> The image to show when you are recording your voice

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |GameObject|null

[Back To Top](#)

------------------
### speakerImage<a name="parameter-speakerImage"></a>

> The image to show when voice is being played through the speaker.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |GameObject|null

[Back To Top](#)

## Function Definitions<a name="functions-definitions"></a>

Select the function name from below to jump directly to it on this page.

[Awake](#Awake)<br>
[CalibrateVoiceDetector](#CalibrateVoiceDetector)<br>
[ConnectToVoiceServer](#ConnectToVoiceServer)<br>
[DisconnectFromVoiceServer](#DisconnectFromVoiceServer)<br>
[EnableEncryptedAudioStream](#EnableEncryptedAudioStream)<br>
[EnableLoopAudioPlayback](#EnableLoopAudioPlayback)<br>
[EnableMuteSpeaker](#EnableMuteSpeaker)<br>
[EnablePushToTalk](#EnablePushToTalk)<br>
[EnableRecorderReliableMode](#EnableRecorderReliableMode)<br>
[EnableTransmitVoice](#EnableTransmitVoice)<br>
[EnableVoiceDetection](#EnableVoiceDetection)<br>
[EnableVoiceEcho](#EnableVoiceEcho)<br>
[GetCurrentMicrophone](#GetCurrentMicrophone)<br>
[GetIntresetGroup](#GetIntresetGroup)<br>
[InitializeRecorder](#InitializeRecorder)<br>
[RecorderIsRecording](#RecorderIsRecording)<br>
[RecorderIsTransmitting](#RecorderIsTransmitting)<br>
[SetIntrestGroup](#SetIntrestGroup)<br>
[SetMicrophoneDevice](#SetMicrophoneDevice)<br>
[SetSpeakerPrefab](#SetSpeakerPrefab)<br>
[Start](#Start)<br>
[StartRecording](#StartRecording)<br>
[Update](#Update)<br>
[VoiceClientStateChanged](#VoiceClientStateChanged)<br>

------------------
### public virtual void Awake()<a name="Awake"></a>

>   Immediately turns off the is speaking and is recording images. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### public virtual void CalibrateVoiceDetector(int howLong)<a name="CalibrateVoiceDetector"></a>

>   Initializes the record if not already initalized. Call this to set the `PrimaryRecorder` into calibration mode and for how long. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|howLong|int type, how long to wait until calibration is completed.|

[Back To Top](#)

------------------
### public virtual void ConnectToVoiceServer()<a name="ConnectToVoiceServer"></a>

>   Will connect to the voice chat server. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### public virtual void DisconnectFromVoiceServer()<a name="DisconnectFromVoiceServer"></a>

>   Will disconnect from the voice chat server. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### public virtual void EnableEncryptedAudioStream(bool enabled)<a name="EnableEncryptedAudioStream"></a>

>   Enable encryption of audio streams. Heavier on network traffic but more secure (if worried about that sort of thing). 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|enabled|bool type, encrypt audio traffic?|

[Back To Top](#)

------------------
### public virtual void EnableLoopAudioPlayback(bool enabled)<a name="EnableLoopAudioPlayback"></a>

>   Will loop the voice on play back or not. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|enabled|bool type, you want the played voice to continue looping?|

[Back To Top](#)

------------------
### public virtual void EnableMuteSpeaker(bool enabled)<a name="EnableMuteSpeaker"></a>

>   Will turn the audio source volume to zero or back to it's `originalAudioVolume` parameter setting based on the input value that you pass in. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|enabled|bool type, mute audio source or not?|

[Back To Top](#)

------------------
### public virtual void EnablePushToTalk(bool enabled)<a name="EnablePushToTalk"></a>

>   Will immediately stop recording and set the Push-To-Talk value to whatever you pass in. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|enabled|bool type, enable Push-To-Talk or not?|

[Back To Top](#)

------------------
### public virtual void EnableRecorderReliableMode(bool enabled)<a name="EnableRecorderReliableMode"></a>

>   Set the `PrimaryRecorder` to be in `ReliableMode` or not. Read more about this on the photon documentation here: https://doc.photonengine.com/en-us/voice/current/getting-started/recorder 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|enabled|bool type, make the recorder reliable or not|

[Back To Top](#)

------------------
### public virtual void EnableTransmitVoice(bool enabled)<a name="EnableTransmitVoice"></a>

>   Allow the `PrimaryRecorder` to send the recorded voice over the network or not 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|enabled|bool type, send voice over network?|

[Back To Top](#)

------------------
### public virtual void EnableVoiceDetection(bool enabled)<a name="EnableVoiceDetection"></a>

>   Will initialize the recorder if not. Will set the `PrimaryRecorder` to filter recorded sound and transmit only when a predefined threshold of signal level is exceeded. Read more about voice detection here: https://doc.photonengine.com/en-us/voice/current/getting-started/recorder 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|enabled|bool type, enable Voice detection?|

[Back To Top](#)

------------------
### public virtual void EnableVoiceEcho(bool enabled)<a name="EnableVoiceEcho"></a>

>   Play your recorded voice locally. Excellent for debugging purposes. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|enabled|bool type, enable voice playback?|

[Back To Top](#)

------------------
### public virtual string GetCurrentMicrophone()<a name="GetCurrentMicrophone"></a>

>   Get a list of detected microphone devices   Get the current actively used microphone. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True| A list of detected mics Current active mic|

**No parameters**

[Back To Top](#)

------------------
### public virtual byte GetIntresetGroup()<a name="GetIntresetGroup"></a>

>   The current voice group to listen and receive transmissions from. (0 means everyone.) Read more about this here: https://doc.photonengine.com/en-us/voice/current/getting-started/recorder 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True| Your current group|

**No parameters**

[Back To Top](#)

------------------
### public virtual void InitializeRecorder()<a name="InitializeRecorder"></a>

>   Performs initializations on the recorder. Read more from the getting started guide in photon: https://doc.photonengine.com/en-US/voice/current/getting-started/voice-for-pun 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### public virtual bool RecorderIsRecording()<a name="RecorderIsRecording"></a>

>   Returns true or false if the `PrimaryRecorder` is recording voice or not. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True| True of False, is recording right now?|

**No parameters**

[Back To Top](#)

------------------
### public virtual bool RecorderIsTransmitting()<a name="RecorderIsTransmitting"></a>

>   Returns true or false if the `PrimaryRecorder` is currently transmitting the recorded voice over the network or not. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True| |

**No parameters**

[Back To Top](#)

------------------
### public virtual void SetIntrestGroup(byte group)<a name="SetIntrestGroup"></a>

>   Set what group you would like to receive transmissions from. (0 means everyone.) Read more about this here: https://doc.photonengine.com/en-us/voice/current/getting-started/recorder 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|group|byte type, the group to listen to|

[Back To Top](#)

------------------
### public virtual void SetMicrophoneDevice(string deviceName)<a name="SetMicrophoneDevice"></a>

>   Set the active microphone device to be whatever you pass in. The name must match what is currently known. Can call `GetAllMicrophoneDevices` to know what is currently known. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|deviceName|string type, the name of the microphone device to set your active device to|

[Back To Top](#)

------------------
### public virtual void SetSpeakerPrefab(GameObject target)<a name="SetSpeakerPrefab"></a>

>   Sets the target of the `SpeakerPrefab`. Read the photon documentation for more about this: https://doc.photonengine.com/en-US/voice/current/getting-started/voice-for-pun 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|target|The GameObject to set as the `SpeakerPrefab`|

[Back To Top](#)

------------------
### public virtual void Start()<a name="Start"></a>

>   Enables/Disables recording based on the settings in this component. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### public virtual void StartRecording(bool enabled)<a name="StartRecording"></a>

>   Makes the `PrimaryRecorder` start recording or not. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|enabled|bool type, start recording voice or not|

[Back To Top](#)

------------------
### protected virtual void Update()<a name="Update"></a>

>   Will record based on inputs or record based on voice levels. This is all based on the settings on this component. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### protected virtual void VoiceClientStateChanged(Photon.Realtime.ClientState fromState, Photon.Realtime.ClientState toState)<a name="VoiceClientStateChanged"></a>

>   Callback method. Called whenever the state of the voice client changes. This is used to set the `connectionStatus` status variable. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|fromState|Photon.Realtime.ClientState type, the state you were in|
|toState|Photon.Realtime.ClientState type, the state your now in|

[Back To Top](#)

