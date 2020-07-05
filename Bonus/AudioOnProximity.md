[Back To Index](../index.md)

# AudioOnProximity

[Jump To Parameters](#parameter-definitions)<br/>
[Jump To Function Definitions](#functions-definitions)<br/>

--------------------------------------------------------
## Parameter Definitions<a name="parameter-definitions"></a>

Select the parameter name from below to jump directly to it on this page.

[distanceClip](#parameter-distanceClip)<br>
[distances](#parameter-distances)<br>

------------------
 ### distanceClip<a name="parameter-distanceClip"></a>
> The audio clip to fade in/out based on distance to the target.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|private |AudioClip|null

[Back To Top](#)

------------------
 ### distances<a name="parameter-distances"></a>
> At what distance should the sound source volume be set to?

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|private |DistanceVolume[]|new DistanceVolume[] { }

[Back To Top](#)

## Function Definitions<a name="functions-definitions"></a>

Select the function name from below to jump directly to it on this page.

[Update](#Update)<br>

------------------
 ### private void Update()<a name="Update"></a>
>   Will keep track of the target to the source. If it falls within the particular distances Array it will fade in the volume with the selected audio clip. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|private|False|Does not return anything|

**No parameters**

[Back To Top](#)

