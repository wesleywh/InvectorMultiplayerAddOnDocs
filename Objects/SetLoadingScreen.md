[Back To Index](../index.md)

# SetLoadingScreen

[Jump To Parameters](#parameter-definitions)<br/>
[Jump To Function Definitions](#functions-definitions)<br/>

--------------------------------------------------------
## Parameter Definitions<a name="parameter-definitions"></a>

Select the parameter name from below to jump directly to it on this page.

[LoadingDescriptions](#parameter-LoadingDescriptions)<br>
[LoadingImages](#parameter-LoadingImages)<br>
[LoadingTitle](#parameter-LoadingTitle)<br>

------------------
 ### LoadingDescriptions<a name="parameter-LoadingDescriptions"></a>
> The loading description to display while on the loading screen.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |List<string>|new List<string>()

[Back To Top](#)

------------------
 ### LoadingImages<a name="parameter-LoadingImages"></a>
> The images to cycle through while on the loading screen. Used in conjunction with the `UICoreLogic` component.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |List<Sprite>|new List<Sprite>()

[Back To Top](#)

------------------
 ### LoadingTitle<a name="parameter-LoadingTitle"></a>
> The load title to display while on the loading screen.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |string|""

[Back To Top](#)

## Function Definitions<a name="functions-definitions"></a>

Select the function name from below to jump directly to it on this page.

[EnableLoadingScreen](#EnableLoadingScreen)<br>
[SetLoadingScreenItems](#SetLoadingScreenItems)<br>

------------------
 ### public virtual void EnableLoadingScreen()<a name="EnableLoadingScreen"></a>
>   Calls `EnableLoadingPage` on `UICoreLogic` to enable the loading screen. Also calls `SetLoadingScreenItems` function to set the `UICoreLogic` values. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### public virtual void SetLoadingScreenItems()<a name="SetLoadingScreenItems"></a>
>   Sets the loading image, loading desc and load title on the UICoreLogic component. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

