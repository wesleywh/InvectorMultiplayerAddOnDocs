[Back To Index](../../../index.md)

# EnableIfAllPlayersReady

[Jump To Parameters](#parameter-definitions)<br/>
[Jump To Function Definitions](#functions-definitions)<br/>

--------------------------------------------------------
## Parameter Definitions<a name="parameter-definitions"></a>

Select the parameter name from below to jump directly to it on this page.

[mustBeOnwer](#parameter-mustBeOnwer)<br>
[targets](#parameter-targets)<br>

------------------
 ### mustBeOnwer<a name="parameter-mustBeOnwer"></a>
> Will only be enabled if you're also the MasterClient of the photon room.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |bool|false

[Back To Top](#)

------------------
 ### targets<a name="parameter-targets"></a>
> The list of GameObjects to enable or disable.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |GameObject[]|new GameObject[] { }

[Back To Top](#)

## Function Definitions<a name="functions-definitions"></a>

Select the function name from below to jump directly to it on this page.

[EnableTargets](#EnableTargets)<br>
[FixedUpdate](#FixedUpdate)<br>

------------------
 ### protected virtual void EnableTargets(bool isEnabled)<a name="EnableTargets"></a>
>   Enable or disable all the `targets` based on the input value. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|isEnabled|***No found decription**|

[Back To Top](#)

------------------
 ### protected virtual void FixedUpdate()<a name="FixedUpdate"></a>
>   Will constantely set all the targets to be active based on the return value from the `UICoreLogic`'s `AllPlayersReady` function. Calls `EnableTargets` to enable or disable all the targets 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

