# How To Upgrade from a very old version to a new version

If you're upgrading from a very old version of the package to the newest release it's a good idea to first reset all your files by running the following menu items in Unity:

1. Window > Reset > Invector Files
(If you have any addons enabled)
2. Window > Reset > Shooter Template 
... etc
3. Click out of Unity and back in to let it recompile

Now delete the entire `InvectorMultiplayer` directory (that's correct, delete it.) Now from the asset store Import the package again. With the package imported enable everything you had before:

1. CB Games > Convert > Invector Files
2. Click out of Unity and back in to let it recompile
(If you have any add-ons imported into your project)
3. CB Games > Enable Support > Enable Shooter Template Add-On
...etc
4. Click out of Unity and back in to let it recompile

You should now have all the new code. There may be likely a few things that have been deleted from the project between versions so just make sure you're prefabs don't include any removed components. Then your done!

# How To Upgrade From Just The Previous Release To The Newest Release

This is more simple than the previous approach. It's best to reset the files prior to importing but if you're reading this you probably didn't do that. So run the following menus:

1. Window > Reset > Invector Files
(If you have any addons enabled)
2. Window > Reset > Shooter Template 
... etc
3. Click out of Unity and back in to let it recompile

When done reseting the files, import the new code from either github or the asset store. Then the new code has finished importing into the project run through the following menus:

1. CB Games > Convert > Invector Files
2. Click out of Unity and back in to let it recompile
(If you have any add-ons imported into your project)
3. CB Games > Enable Support > Enable Shooter Template Add-On
..etc
4. Click out of Unity and back in to let it recompile

That should be it.