[Back To Index](../../../index.md)

# GenericCountDown

[Jump To Parameters](#parameter-definitions)<br/>
[Jump To Function Definitions](#functions-definitions)<br/>

--------------------------------------------------------
## Parameter Definitions<a name="parameter-definitions"></a>

Select the parameter name from below to jump directly to it on this page.

[OnNumberChange](#parameter-OnNumberChange)<br>
[OnStartCounting](#parameter-OnStartCounting)<br>
[OnStopCounting](#parameter-OnStopCounting)<br>
[OnZero](#parameter-OnZero)<br>
[countSpeed](#parameter-countSpeed)<br>
[debugging](#parameter-debugging)<br>
[ifIsOwner](#parameter-ifIsOwner)<br>
[numberType](#parameter-numberType)<br>
[soundSource](#parameter-soundSource)<br>
[startTime](#parameter-startTime)<br>
[startType](#parameter-startType)<br>
[syncWithPhotonServer](#parameter-syncWithPhotonServer)<br>
[texts](#parameter-texts)<br>
[tickClip](#parameter-tickClip)<br>
[useRoomOwnerShip](#parameter-useRoomOwnerShip)<br>

------------------
### OnNumberChange<a name="parameter-OnNumberChange"></a>

> UnityEvent. Called when the current number the counter is at changes.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |FloatUnityEvent|new FloatUnityEvent()

[Back To Top](#)

------------------
### OnStartCounting<a name="parameter-OnStartCounting"></a>

> UnityEvent. Called when the counting starts.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |UnityEvent|new UnityEvent()

[Back To Top](#)

------------------
### OnStopCounting<a name="parameter-OnStopCounting"></a>

> UnityEvent. Called when the countind stops.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |UnityEvent|new UnityEvent()

[Back To Top](#)

------------------
### OnZero<a name="parameter-OnZero"></a>

> UnityEvent. Called when the current number reaches zero.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |UnityEvent|new UnityEvent()

[Back To Top](#)

------------------
### countSpeed<a name="parameter-countSpeed"></a>

> How fast to count down? Higher = faster, Lower = Slower

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |float|1.0f

[Back To Top](#)

------------------
### debugging<a name="parameter-debugging"></a>

> If you want verbose logging into the console as to what is happening in this script.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |bool|false

[Back To Top](#)

------------------
### ifIsOwner<a name="parameter-ifIsOwner"></a>

> If you are the owner then only perform the OnZero event.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |bool|false

[Back To Top](#)

------------------
### numberType<a name="parameter-numberType"></a>

> How do you want the number to be displayed? \n" <br>WholeNumber = Display in integer format\n\n" <br>FullTime = Display like 00:00:00\n\n" <br>AbbreviatedTime = Display like 00:00\n\n" <br>Raw = Display the raw float value

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |NumberType|NumberType.WholeNumber

[Back To Top](#)

------------------
### soundSource<a name="parameter-soundSource"></a>

> (Optional) The audio source to play the tick clip sound.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |AudioSource|null

[Back To Top](#)

------------------
### startTime<a name="parameter-startTime"></a>

> The time the timer will start counting down from.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |float|6.0f

[Back To Top](#)

------------------
### startType<a name="parameter-startType"></a>

> When do you want to start counting?\n" <br>Immediately=The OnStart call will trigger the counting sequence.\n" <br>OnCall=An outside source will have to call the StartCounting function.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |CounterStartType|CounterStartType.OnCall

[Back To Top](#)

------------------
### syncWithPhotonServer<a name="parameter-syncWithPhotonServer"></a>

> If you want to countdown based off the time on the photon server. Great for " <br>having everyone keep the same time. However this is not responsible for starting " <br>everyone at the same time. Just counting down at the same speed!

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |bool|false

[Back To Top](#)

------------------
### texts<a name="parameter-texts"></a>

> (Optional)Texts to overwrite and show the current counted number.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |Text[]|new Text[] { }

[Back To Top](#)

------------------
### tickClip<a name="parameter-tickClip"></a>

> (Optional) The audio clip to play every time a whole number goes down by 1.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |AudioClip|null

[Back To Top](#)

------------------
### useRoomOwnerShip<a name="parameter-useRoomOwnerShip"></a>

> Only perform the UnityEvents if you are the owner/not the owner.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |bool|false

[Back To Top](#)

## Function Definitions<a name="functions-definitions"></a>

Select the function name from below to jump directly to it on this page.

[OnRoomPropertiesUpdate](#OnRoomPropertiesUpdate)<br>
[PlayAudioClip](#PlayAudioClip)<br>
[RemoveRoomProperties](#RemoveRoomProperties)<br>
[SetAudioSource](#SetAudioSource)<br>
[SetClip](#SetClip)<br>
[SetStartTime](#SetStartTime)<br>
[SetTexts](#SetTexts)<br>
[SetTime](#SetTime)<br>
[Start](#Start)<br>
[StartCounting](#StartCounting)<br>
[StopCounting](#StopCounting)<br>
[SubtractTime](#SubtractTime)<br>
[TimerEnded](#TimerEnded)<br>
[Update](#Update)<br>

------------------
### protected virtual void OnRoomPropertiesUpdate(Hashtable propertiesThatChanged)<a name="OnRoomPropertiesUpdate"></a>

>   Callback method. This is called when the properties of the current room have changed. Will start the timer and set the sync values based on what is received. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|propertiesThatChanged|***No found decription**|

[Back To Top](#)

------------------
### protected virtual void PlayAudioClip()<a name="PlayAudioClip"></a>

>   Start playing the `soundSource`. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### public virtual void RemoveRoomProperties()<a name="RemoveRoomProperties"></a>

>   Removes all the custom room properties that this component has added to sync the times. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### public virtual void SetAudioSource(AudioSource source)<a name="SetAudioSource"></a>

>   Sets the `soundSource`. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|source|AudioSource type, the audiosource to use.|

[Back To Top](#)

------------------
### public virtual void SetClip(AudioClip clip)<a name="SetClip"></a>

>   Sets the `tickClip`. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|clip|AudioClip type, the tick clip to use.|

[Back To Top](#)

------------------
### public virtual void SetStartTime(float timeToStart)<a name="SetStartTime"></a>

>   The time that the timer should start at when first starting to count down. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|timeToStart|float type, the start counting from time.|

[Back To Top](#)

------------------
### protected virtual void SetTexts(string value)<a name="SetTexts"></a>

>   Set the `texts` values to be whatever the input string is. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|value|string type, the string to display|

[Back To Top](#)

------------------
### public virtual void SetTime(float incomingTime)<a name="SetTime"></a>

>   Set the current time number the counter is at. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|incomingTime|float type, the current time number to set.|

[Back To Top](#)

------------------
### protected virtual void Start()<a name="Start"></a>

>   If the `startType` is `Immediately` it will call the `StartCounting` function. Also sets the `tickClip` if there is a `soundSource` and a `tickClip` specified. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### public virtual void StartCounting()<a name="StartCounting"></a>

>   Start the countdown. Calls `OnStartCounting` UnityEvent. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### public virtual void StopCounting()<a name="StopCounting"></a>

>   Stop the countdown. Calls `OnStopCounting` UntiyEvent. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### public virtual void SubtractTime(float subtractTime)<a name="SubtractTime"></a>

>   Remove time from the current countdown time. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|subtractTime|float type, the amount of time to subtract.|

[Back To Top](#)

------------------
### protected virtual void TimerEnded()<a name="TimerEnded"></a>

>   This is called when the timer reachs zero. It will call the `RemoveSyncTime` function and the `OnZero` UnityEvent. It also resets this timer so it can be used again. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### protected virtual void Update()<a name="Update"></a>

>   Responsible for subtracting time from the current time in an settings the display value parameter based on the `numberType` parameter. Also calls the `PlayAudioClip` function when the time changes. It also calls the `SetTexts` function to set the display counting values. Finally it calls the `OnZero` UnityEvent when reacing zero and the `StopCounting` function when it reaches zero. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

