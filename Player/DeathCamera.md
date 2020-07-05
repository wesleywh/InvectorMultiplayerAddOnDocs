[Back To Index](../index.md)

# DeathCamera

[Jump To Parameters](#parameter-definitions)<br/>
[Jump To Function Definitions](#functions-definitions)<br/>

--------------------------------------------------------
## Parameter Definitions<a name="parameter-definitions"></a>

Select the parameter name from below to jump directly to it on this page.

[OnDisableSwitching](#parameter-OnDisableSwitching)<br>
[OnEnableSwitching](#parameter-OnEnableSwitching)<br>
[deathVisual](#parameter-deathVisual)<br>
[keyToSwitchNext](#parameter-keyToSwitchNext)<br>
[keyToSwitchPrevious](#parameter-keyToSwitchPrevious)<br>

------------------
### OnDisableSwitching<a name="parameter-OnDisableSwitching"></a>

> UnityEvent. Called when you disallow the owner player to switch camera targets.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |UnityEvent|new UnityEvent()

[Back To Top](#)

------------------
### OnEnableSwitching<a name="parameter-OnEnableSwitching"></a>

> UnityEvent. Called when you allow the owner player to switch camera targets.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |UnityEvent|new UnityEvent()

[Back To Top](#)

------------------
### deathVisual<a name="parameter-deathVisual"></a>

> (Optional)The UI GameObject to enable when you die.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |GameObject|null

[Back To Top](#)

------------------
### keyToSwitchNext<a name="parameter-keyToSwitchNext"></a>

> The key to press in order to have the camera switch to a new player " <br>target if \"allowSwitching\" is true.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |string|""

[Back To Top](#)

------------------
### keyToSwitchPrevious<a name="parameter-keyToSwitchPrevious"></a>

> The key to press in order to have the camera switch to a new player " <br>target if \"allowSwitching\" is true.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |string|""

[Back To Top](#)

## Function Definitions<a name="functions-definitions"></a>

Select the function name from below to jump directly to it on this page.

[Awake](#Awake)<br>
[EnableSwitching](#EnableSwitching)<br>
[SelectNextTarget](#SelectNextTarget)<br>
[SelectPreviousTarget](#SelectPreviousTarget)<br>
[SwitchCameraTarget](#SwitchCameraTarget)<br>
[Update](#Update)<br>

------------------
### protected virtual void Awake()<a name="Awake"></a>

>   Makes sure the death visual is inactive by default. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### public virtual void EnableSwitching(bool isEnabled)<a name="EnableSwitching"></a>

>   Allow the owner player to switch the camera target. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|isEnabled|bool type, allow camera switching?|

[Back To Top](#)

------------------
### public virtual void SelectNextTarget()<a name="SelectNextTarget"></a>

>   Sets the potential next target the camera can switch to. Does not switch the camera target. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### public virtual void SelectPreviousTarget()<a name="SelectPreviousTarget"></a>

>   Sets the potential next target the camera can switch to. Does not switch the camera target. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### public virtual bool SwitchCameraTarget(Transform target)<a name="SwitchCameraTarget"></a>

>   Changes the invector camera target to target another player in the room. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True| true|

| Parameter Name | Description |
|:---|:---|
|target|Transform type, the transform that you want the camera to target|

[Back To Top](#)

------------------
### protected virtual void Update()<a name="Update"></a>

>   If switching is allowed, this will capture the owner input and switch the camera to target another player when the owner presses the `keyToSwitchPrevious` or `keyToSwitchNext` parameter value. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

