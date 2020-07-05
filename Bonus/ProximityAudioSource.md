[Back To Index](../index.md)

# ProximityAudioSource

[Jump To Parameters](#parameter-definitions)<br/>
[Jump To Function Definitions](#functions-definitions)<br/>

--------------------------------------------------------
## Parameter Definitions<a name="parameter-definitions"></a>

Select the parameter name from below to jump directly to it on this page.

[canPlay](#parameter-canPlay)<br>
[fadeIn](#parameter-fadeIn)<br>
[fadeSpeed](#parameter-fadeSpeed)<br>
[setVolume](#parameter-setVolume)<br>
[source](#parameter-source)<br>

------------------
 ### canPlay<a name="parameter-canPlay"></a>
> Can this audio source play sound?

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |bool|false

[Back To Top](#)

------------------
 ### fadeIn<a name="parameter-fadeIn"></a>
> Not modifiable in the inspector. If you want to start fading in or out the sound. True = Fade in, False = Fade out

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |bool|false

[Back To Top](#)

------------------
 ### fadeSpeed<a name="parameter-fadeSpeed"></a>
> How fast to fade in/out music. Higher values = Faster

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |float|0.25f

[Back To Top](#)

------------------
 ### setVolume<a name="parameter-setVolume"></a>
> Not modifiable in the inspector. This is modified by other scripts setting its starting volume.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |float|0

[Back To Top](#)

------------------
 ### source<a name="parameter-source"></a>
> The source where the sound will be played from.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |AudioSource|None

[Back To Top](#)

## Function Definitions<a name="functions-definitions"></a>

Select the function name from below to jump directly to it on this page.

[Start](#Start)<br>
[Update](#Update)<br>

------------------
 ### private void Start()<a name="Start"></a>
>   Automatically sets the AudioSource to loop its sound. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|private|False|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### private void Update()<a name="Update"></a>
>   Will fade in the sound if the setVolume is greater than zero and it is allowed to play. Will also fade out the sound if the setVolume is lower than the current volume and is allowed to player. Otherwise if it's zero it will stop the sound. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|private|False|Does not return anything|

**No parameters**

[Back To Top](#)

