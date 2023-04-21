# Python

## Update cookiecutter-generated files with cruft

Ref: [original docs](https://cruft.github.io/cruft/) and [github repo](https://github.com/cruft/cruft).

First, `pip install cruft`. 
Then, you have to link your repo to the cookiecutter template by specifying its url.
You will also need to specify the cookiecutter commit hash, i.e. the version of cookiecutter you used to generate the repo. For now, we have to do this manually by comparing the history.
Once you have the hash, you can run `cruft link link.to.your.template`. This will create a `.cruft.json` file in your repo.

Now you can run `cruft diff` to see the changes between your repo and the template. If you are happy with the changes, you can run `cruft update` to update your repo. This will not overwrite all changes you have made, but only the files that have been changed in the template.

In the case `cruft update` is not able to apply all the changes, it will create a `.something.rej` file. You can then manually apply the changes to the files. This is a bit tedious, but it's the only way I have found to do it so far.

I have found that although the link to the repo is correct (`github_repository_url` field), the command `cruft diff` fails, so you might have to change it manually in the `.cruft.json` file to "provide later". 🤷🏻‍♀️

`cruft check` will check if your repo is up to date with the template, and basically will just give you a boolean response.

Once you are satisfied, commit the changes to a new branch and open a PR to merge it into `main`. 

Now, check if your GitHub actions fail... 🤦🏻‍♀️ If everything is fine, you can merge the PR. 🎉 If not, you will have to fix the errors and repeat the process. 😱
