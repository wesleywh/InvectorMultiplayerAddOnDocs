[Back To Index](../index.md)

# SyncObject

[Jump To Parameters](#parameter-definitions)<br/>
[Jump To Function Definitions](#functions-definitions)<br/>

--------------------------------------------------------
## Parameter Definitions<a name="parameter-definitions"></a>

Select the parameter name from below to jump directly to it on this page.

[isLeftHanded](#parameter-isLeftHanded)<br>
[isWeaponHolder](#parameter-isWeaponHolder)<br>
[syncDestroy](#parameter-syncDestroy)<br>
[syncDisable](#parameter-syncDisable)<br>
[syncEnable](#parameter-syncEnable)<br>
[syncImmediateChildren](#parameter-syncImmediateChildren)<br>
[view](#parameter-view)<br>

------------------
### isLeftHanded<a name="parameter-isLeftHanded"></a>

> NOTE: This only matters when \"syncImmediateChildren\" is enabled \n\nIs a left handed weapon? If the correct one is not selected could produce incorrect positioning when syncing across the network.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |bool|false

[Back To Top](#)

------------------
### isWeaponHolder<a name="parameter-isWeaponHolder"></a>

> NOTE: This only matters when \"syncImmediateChildren\" is enabled \n\nIs this a weapon holder? If the correct one is not selected could produce incorrect positioning when syncing across the network.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |bool|false

[Back To Top](#)

------------------
### syncDestroy<a name="parameter-syncDestroy"></a>

> When this object is destroyed, sync across the network using the selected PhotonView.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |bool|true

[Back To Top](#)

------------------
### syncDisable<a name="parameter-syncDisable"></a>

> When this object is disabled, sync across the network using the selected PhotonView.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |bool|true

[Back To Top](#)

------------------
### syncEnable<a name="parameter-syncEnable"></a>

> When this object is enabled, sync across the network using the selected PhotonView.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |bool|true

[Back To Top](#)

------------------
### syncImmediateChildren<a name="parameter-syncImmediateChildren"></a>

> Important Note: Used ONLY for items!  \n\n When child objects are added or removed, sync across the network using the selected PhotonView. This will only sync immediate child transforms of this object, no nested transforms. This is a limitation of the unity engine.\n\n Will sync: Enables, Destorys, Disables, and Instantiate items from the item data.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |bool|true

[Back To Top](#)

------------------
### view<a name="parameter-view"></a>

> The photon view to use when making rpc calls. If not populated will use the root object or if this object contains a photonview component will use it.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |PhotonView|null

[Back To Top](#)

## Function Definitions<a name="functions-definitions"></a>

Select the function name from below to jump directly to it on this page.

[AddThisComponent](#AddThisComponent)<br>
[Awake](#Awake)<br>
[GOInList](#GOInList)<br>
[IsInChildrenStatsList](#IsInChildrenStatsList)<br>
[OnDestroy](#OnDestroy)<br>
[OnDisable](#OnDisable)<br>
[OnEnable](#OnEnable)<br>
[OnTransformChildrenChanged](#OnTransformChildrenChanged)<br>

------------------
### protected virtual void AddThisComponent(GameObject child)<a name="AddThisComponent"></a>

>   Calls to add the `SyncObject` component to the passed in gameobject. Also sets the settings as though this is a child of this component. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|child|The GameObject to add the `SyncObject` component to|

[Back To Top](#)

------------------
### protected virtual void Awake()<a name="Awake"></a>

>   Builds the index tree to the root of this tree and finds the parent `PhotonView` component. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### protected virtual bool GOInList(GameObject go, List<ChildrenStates> children)<a name="GOInList"></a>

>   Checks to see if the passed in GameObject is is currently in this components known list of gameObjects. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True| True or False, is already in the known list.|

| Parameter Name | Description |
|:---|:---|
|go|The gameobject to check if its in the list|

[Back To Top](#)

------------------
### protected virtual bool IsInChildrenStatsList(GameObject go)<a name="IsInChildrenStatsList"></a>

>   Checks to see if the passed in GameObject is is currently in this components known list of gameObjects. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True| True or False, is already in the known list.|

| Parameter Name | Description |
|:---|:---|
|go|The gameobject to check if its in the list|

[Back To Top](#)

------------------
### protected virtual void OnDestroy()<a name="OnDestroy"></a>

>   Calls the `Item_NetworkDestroy` RPC which destroys this object for everyone on the network, not including yourself. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### protected virtual void OnDisable()<a name="OnDisable"></a>

>   Will call the `NetworkSetActive` RPC which will disable this object for everyone on the network, not including yourself. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### protected virtual void OnEnable()<a name="OnEnable"></a>

>   Will call the `NetworkSetActive` RPC which will enable this object for everyone on the network, not including yourself. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### protected virtual void OnTransformChildrenChanged()<a name="OnTransformChildrenChanged"></a>

>   Called when a child object is added or removed from this object. Will detect if the object is added or removed and call the `Item_NetworkDestroy` or `NetworkSetActive` RPC to enable/disable or destroy this object over the network. This makes the networked players mimic what the owner's state currently is. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

