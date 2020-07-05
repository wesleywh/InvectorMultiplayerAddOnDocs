[Back To Index](../index.md)

# NetworkBreakObject

[Jump To Parameters](#parameter-definitions)<br/>
[Jump To Function Definitions](#functions-definitions)<br/>

--------------------------------------------------------
## Parameter Definitions<a name="parameter-definitions"></a>

Select the parameter name from below to jump directly to it on this page.

[dropPoint](#parameter-dropPoint)<br>
[dropPrefab](#parameter-dropPrefab)<br>
[holder](#parameter-holder)<br>
[prefabName](#parameter-prefabName)<br>
[syncCrossScenes](#parameter-syncCrossScenes)<br>

------------------
 ### dropPoint<a name="parameter-dropPoint"></a>
> Used by 'DropObject' function. Will drop the networked object at this position and rotation

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |Transform|null

[Back To Top](#)

------------------
 ### dropPrefab<a name="parameter-dropPrefab"></a>
> Whether or not you want to drop a network prefab from the 'Resources' folder when this is broken.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |bool|false

[Back To Top](#)

------------------
 ### holder<a name="parameter-holder"></a>
> The object to track the position of.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |Transform|null

[Back To Top](#)

------------------
 ### prefabName<a name="parameter-prefabName"></a>
> The name of the prefab that lives in the resources folder that you want to drop.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |string|""

[Back To Top](#)

------------------
 ### syncCrossScenes<a name="parameter-syncCrossScenes"></a>
> Whether or not you want to sync the break object action across unity scenes.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |bool|true

[Back To Top](#)

## Function Definitions<a name="functions-definitions"></a>

Select the function name from below to jump directly to it on this page.

[BreakObject](#BreakObject)<br>
[DropObject](#DropObject)<br>
[SceneBreak](#SceneBreak)<br>

------------------
 ### public virtual void BreakObject()<a name="BreakObject"></a>
>   Will sent the `SceneBreak` function and `BroadcastData` fucntion to everyone that enters this photon room that joins the photon session. This makes it a persistant action that spans across all Unity scenes. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### protected virtual void DropObject()<a name="DropObject"></a>
>   Calls the `NetworkInstantiatePersistantPrefab` from the NetworkManager to instantiate a prefab from the `Resources` folder for everyone in the Photon room. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### public virtual void SceneBreak()<a name="SceneBreak"></a>
>   Sends the `SendNetworkBreakObject` RPC as buffered to everyone, including yourself. (Breaks the object) 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

