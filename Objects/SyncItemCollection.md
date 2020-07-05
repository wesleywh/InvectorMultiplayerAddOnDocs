[Back To Index](../index.md)

# SyncItemCollection

[Jump To Parameters](#parameter-definitions)<br/>
[Jump To Function Definitions](#functions-definitions)<br/>

--------------------------------------------------------
## Parameter Definitions<a name="parameter-definitions"></a>

Select the parameter name from below to jump directly to it on this page.

[OnPressActionInput](#parameter-OnPressActionInput)<br>
[OnSceneEnterUpdate](#parameter-OnSceneEnterUpdate)<br>
[holder](#parameter-holder)<br>
[onPressActionDelay](#parameter-onPressActionDelay)<br>
[onPressActionInputWithTarget](#parameter-onPressActionInputWithTarget)<br>
[references](#parameter-references)<br>
[resourcesPrefab](#parameter-resourcesPrefab)<br>
[skipStartCheck](#parameter-skipStartCheck)<br>
[syncCreateDestroy](#parameter-syncCreateDestroy)<br>
[syncCrossScenes](#parameter-syncCrossScenes)<br>

------------------
### OnPressActionInput<a name="parameter-OnPressActionInput"></a>

> UnityEvent, called when you press the action button.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |UnityEvent|None

[Back To Top](#)

------------------
### OnSceneEnterUpdate<a name="parameter-OnSceneEnterUpdate"></a>

> UnityEvent, call when you first enter a room and the `DoScenesReplay` " <br>from the NetworkManager indicates this object has had actions performed on it " <br>by another player previously.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |UnityEvent|None

[Back To Top](#)

------------------
### holder<a name="parameter-holder"></a>

> This is only important if \"syncCrossScenes\" is true. \n\nThe object you want to track " <br>the position of. When trying to sync this item across the scene it uses it's name and this " <br>holder position to try and figure out what object to update.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |Transform|null

[Back To Top](#)

------------------
### onPressActionDelay<a name="parameter-onPressActionDelay"></a>

> This should be copied exactly from vItemCollection.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |float|None

[Back To Top](#)

------------------
### onPressActionInputWithTarget<a name="parameter-onPressActionInputWithTarget"></a>

> UnityEvent, called when you press the action button with a gameobject.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |OnDoActionWithTarget|None

[Back To Top](#)

------------------
### references<a name="parameter-references"></a>

> The list of items this object has.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|None|List<ItemReference>|new List<ItemReference>()

[Back To Top](#)

------------------
### resourcesPrefab<a name="parameter-resourcesPrefab"></a>

> Only matters if \"Sync Cross Scenes\" is true.\n\n" <br>The prefab name in the resources folder that corresponds to this object. Must be exact in " <br>order to spawn from the resources folder.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |string|null

[Back To Top](#)

------------------
### skipStartCheck<a name="parameter-skipStartCheck"></a>

> If false, will check to make sure this has been instantiated with item data via the network call. " <br>If not it will destroy itself in favor of another ItemCollection. Enable this ONLY if you DON'T dynamically " <br>add items to the ItemCollection component.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |bool|false

[Back To Top](#)

------------------
### syncCreateDestroy<a name="parameter-syncCreateDestroy"></a>

> Only matters if \"Sync Cross Scenes\" is true.\n\n" <br>Enable if this object is dynamically added to the scene. Will instantiate/destroy this object across " <br>Unity Scenes and for all networked players.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |bool|false

[Back To Top](#)

------------------
### syncCrossScenes<a name="parameter-syncCrossScenes"></a>

> Whether or not you want this to be a globally updated item. (EX: If a player " <br>in scene 1 collects this then when other players enter this scene they will see " <br>this as already collected.)

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |bool|true

[Back To Top](#)

## Function Definitions<a name="functions-definitions"></a>

Select the function name from below to jump directly to it on this page.

[ChatBoxBroadCastCollect](#ChatBoxBroadCastCollect)<br>
[Collect](#Collect)<br>
[Collect](#Collect)<br>
[E_OnPressAction](#E_OnPressAction)<br>
[EnableVItemCollection](#EnableVItemCollection)<br>
[ItemWrapper](#ItemWrapper)<br>
[SceneCollected](#SceneCollected)<br>
[Start](#Start)<br>
[UpdateDatabase](#UpdateDatabase)<br>
[UpdateScenesDatabase](#UpdateScenesDatabase)<br>

------------------
### public virtual void ChatBoxBroadCastCollect()<a name="ChatBoxBroadCastCollect"></a>

>   Sends data via the data channel in the chatbox to everyone in the session to tell them that this item has been collected when they entire this unity scene. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### public virtual void Collect()<a name="Collect"></a>

>   This is designed to be called from the vItemCollection OnPress* UnityEvent. This calls `NetworkCollect` RPC and broadcasts the collect command via the Chatbox to all those in the session (via `ChatBoxBroadCastCollect` function). 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### public virtual void Collect(GameObject target = null)<a name="Collect"></a>

>   This is designed to be called from the vItemCollection OnPress* UnityEvent. This calls `NetworkCollect` RPC and broadcasts the collect command via the Chatbox to all those in the session (via `ChatBoxBroadCastCollect` function). 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### protected virtual IEnumerator E_OnPressAction(GameObject target = null, bool sendNetwork = true)<a name="E_OnPressAction"></a>

>   Used to call the `NetworkDestroySelf` RPC, which destroys this object for everyone currently in the scene and everyone going to enter this scene. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True| |

| Parameter Name | Description |
|:---|:---|
|target|***No found decription**|
|sendNetwork|***No found decription**|

[Back To Top](#)

------------------
### public virtual void EnableVItemCollection(bool isEnabled)<a name="EnableVItemCollection"></a>

>   Enables/Disables the `vItemCollection` component on this object. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|isEnabled|***No found decription**|

[Back To Top](#)

------------------
### ItemWrapper wrapper = new ItemWrapper(items);<a name="ItemWrapper"></a>

>   Takes a list of `ItemReference`'s and serializes that list and returns it. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|private|False| A serialized version of the input list|

| Parameter Name | Description |
|:---|:---|
|items|List<ItemReference> type, the list of items you want to serialize.|

[Back To Top](#)

------------------
### public virtual void SceneCollected()<a name="SceneCollected"></a>

>   Calls the `NetworkSceneCollected` RPC for everyone. This calls the `E_OnPressAction` function for everyone. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### protected virtual void Start()<a name="Start"></a>

>   Wehn first started will check to see if this has been instantiated from the owning player with item data. If not it will destroy this object because it was instantiated from Invector and not photon. This is to prevent duplicates appearing for the player that originally dropped this. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### public virtual void UpdateDatabase(List<ItemReference> items)<a name="UpdateDatabase"></a>

>   Takes a serialized List<ItemReference> and converts it back to a list from a string.   Calls the `UpdateScenesDatabase` IEnumerator function. This will send the item update information over the ChatBox data channel so others entering this scene will see the updates to this list of items. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True| returns the original List<ItemReference>|

| Parameter Name | Description |
|:---|:---|
|serializedItems|***No found decription**|
|items|List<ItemReference> type, The list of items to set on this itemCollection|

[Back To Top](#)

------------------
### protected virtual IEnumerator UpdateScenesDatabase(List<ItemReference> items)<a name="UpdateScenesDatabase"></a>

>   Send this item and its item list to all other players in the session so when they join this scene they will have an up to date accurate item in the scene. Done via sending this information over the data channel on the chatbox. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|items|List<ItemReference> type, the list of items to add to this object|

[Back To Top](#)

