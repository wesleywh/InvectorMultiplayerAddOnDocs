[Back To Index](../index.md)

# SetWorldMusic

[Jump To Parameters](#parameter-definitions)<br/>
[Jump To Function Definitions](#functions-definitions)<br/>

--------------------------------------------------------
## Parameter Definitions<a name="parameter-definitions"></a>

Select the parameter name from below to jump directly to it on this page.

[randomMusic](#parameter-randomMusic)<br>
[volume](#parameter-volume)<br>

------------------
 ### randomMusic<a name="parameter-randomMusic"></a>
> The music clip to use.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|private |AudioClip[]|new AudioClip[] { }

[Back To Top](#)

------------------
 ### volume<a name="parameter-volume"></a>
> The volume to set the audio source to.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|private |float|0.5f

[Back To Top](#)

## Function Definitions<a name="functions-definitions"></a>

Select the function name from below to jump directly to it on this page.

[PlayWorldMusic](#PlayWorldMusic)<br>

------------------
 ### public void PlayWorldMusic()<a name="PlayWorldMusic"></a>
>   Will play the set audio clip at the set volume only after there is a found NetworkManager and UICoreLogic component attached to it in the scene. It will use the UICoreLogic functions to set the audio clip on the UICoreLogic component to the volume and audio clip to use. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|False|Does not return anything|

**No parameters**

[Back To Top](#)

