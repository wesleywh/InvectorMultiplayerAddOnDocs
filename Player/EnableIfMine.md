[Back To Index](../index.md)

# EnableIfMine

[Jump To Parameters](#parameter-definitions)<br/>
[Jump To Function Definitions](#functions-definitions)<br/>

--------------------------------------------------------
## Parameter Definitions<a name="parameter-definitions"></a>

Select the parameter name from below to jump directly to it on this page.

[targets](#parameter-targets)<br>

------------------
 ### targets<a name="parameter-targets"></a>
> The list of gameobjects to enable if you are the " <br>owner player or not.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |GameObject[]|new GameObject[] { }

[Back To Top](#)

## Function Definitions<a name="functions-definitions"></a>

Select the function name from below to jump directly to it on this page.

[EnableTargets](#EnableTargets)<br>
[Start](#Start)<br>

------------------
 ### protected virtual void EnableTargets(bool isEnabled)<a name="EnableTargets"></a>
>   Loops through the `targets` and disables/enables them based on the input value. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|isEnabled|bool type, enable or disable the targets?|

[Back To Top](#)

------------------
 ### protected virtual void Start()<a name="Start"></a>
>   Enables/Disables the list of `targets` if you're the owner or not. This is done by calling the `EnableTargets` function. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

