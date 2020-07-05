[Back To Index](../../../index.md)

# EnableIfOwner

[Jump To Parameters](#parameter-definitions)<br/>
[Jump To Function Definitions](#functions-definitions)<br/>

--------------------------------------------------------
## Parameter Definitions<a name="parameter-definitions"></a>

Select the parameter name from below to jump directly to it on this page.

[isOwner](#parameter-isOwner)<br>
[targets](#parameter-targets)<br>

------------------
 ### isOwner<a name="parameter-isOwner"></a>
> The `targets` will only enable if you're the MasterClient or not.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |bool|true

[Back To Top](#)

------------------
 ### targets<a name="parameter-targets"></a>
> The list of gameobjects to enable or not if you're the MasterClient.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |GameObject[]|new GameObject[] { }

[Back To Top](#)

## Function Definitions<a name="functions-definitions"></a>

Select the function name from below to jump directly to it on this page.

[FixedUpdate](#FixedUpdate)<br>
[SetIsActive](#SetIsActive)<br>

------------------
 ### protected virtual void FixedUpdate()<a name="FixedUpdate"></a>
>   Enable or disables the targets based on if your the MasterClient, in a photon room, and have a `NetworkManager`. This is done by calling the `SetIsActive` function. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### protected virtual void SetIsActive(bool isActive)<a name="SetIsActive"></a>
>   Sets all the `targets` to be active or not based on the input value. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|isActive|bool type, enable all the targets?|

[Back To Top](#)

