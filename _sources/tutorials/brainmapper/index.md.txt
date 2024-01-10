# Whole brain cell detection and registration with the `brainmapper` command line tool

:::{note}

`brainmapper` was previously called the `cellfinder` command-line interface tool.

This command-line tool was renamed with the release of `cellfinder` version `1.0.0`.
You can read about these changes [on our blog](/blog/version1/cellfinder_migration_live).

If you have previously been using the cellfinder command-line interface in your work, you'll most likely want to follow the links in the blog post to:

- Upgrade your version of the `cellfinder` package,
- Install `brainglobe-workflows` to get `brainmapper`, the same command-line tool but under it's new name.

:::

Although the `brainmapper` command line tool is designed to be easy to install and use, if you're coming to it with fresh eyes, it's not always clear where to start.
We provide an example brain to get you started, and also to illustrate how to play with the parameters to better suit your data.

:::{caution}
**The test dataset is large** $\approx 250$GB.
It is recommended that you try this tutorial out on the fastest machine you have, with the fastest hard drive possible (ideally SSD) and an NVIDIA GPU.
:::

## Tutorial

The tutorial is quite long, and is split into a number of sections.
Please be aware that downloading the data and running `brainmapper` may take a long time (e.g., overnight x2) if you don't have access to a particularly high-powered computer, or fast network connection.

Please go through the following sections in order:

```{toctree}
:maxdepth: 1
setting-up
running-brainmapper
visualising-the-results
exploring-the-numerical-results
visualising-your-data-in-brainrender
```
