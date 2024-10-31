# brainglobe-atlasapi

## Adding a new atlas
The details regarding packaging a new atlas can be found at 
[adding a new atlas](/documentation/brainglobe-atlasapi/adding-a-new-atlas). Here we outline the steps that follow once 
the new atlas pull request has been merged:

1. Run the atlas script to generate the new atlas, and double-check it passes our validation.
2. Upload the `tar.gz` archive to the [GIN atlas repository](https://gin.g-node.org/BrainGlobe/atlases).
3. Update the [`latest_versions.conf`](https://gin.g-node.org/BrainGlobe/atlases/src/master/last_versions.conf) file.
4. Add the atlas to the [atlas details](/documentation/brainglobe-atlasapi/usage/atlas-details) page of the website.
5. Add the atlas to the tables in:
   * The [BrainGlobe Atlas API documentation](/documentation/brainglobe-atlasapi/index)
   * The [BrainGlobe Atlas GitHub README](https://github.com/brainglobe/brainglobe-atlasapi/blob/main/README.md)
   * The [GIN atlas repository README](https://gin.g-node.org/BrainGlobe/atlases/src/master/README.md)
6. Write a [blog post](/blog/index) describing the new atlas. Make sure to highlight the original developers of the 
atlas (e.g. via the original publication) and the packager of the atlas if they are not in the core BrainGlobe team. 
Other details may include:
   * Background (e.g. why is this species important to study)
   * Details on the atlas
   * Images of the atlas
   * Any specific details about the atlas (e.g. a specific channel that should be used for registration)
   * Instructions for use (e.g. to visualise the atlas)
7. Inform the creators of the original atlas (if they did not package it), and offer to help them adopt BrainGlobe 
if this is of interest. Ideally this should be a follow up to an earlier message informing them of the effort to 
add the atlas.
8. Advertise the atlas by linking to the blog post. Where we advertise varies depending on the atlas, but will usually
include:
   * [Twitter/X](https://x.com/brain_globe)
   * [Mastodon](https://mastodon.online/@brainglobe)
   * [Bluesky](https://bsky.app/profile/brainglobe.bsky.social)
   * [BrainGlobe Zulip](https://brainglobe.zulipchat.com/)

In addition, we usually post about the atlas in any forum we think will find it useful, e.g. if we think there is a 
specific research community that may want to use the new atlas. 

