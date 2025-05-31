# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Remove all generated files
clean:
	@echo "Removing auto-generated files..."
	rm -rf "$(BUILDDIR)"
	rm -rf "$(SOURCEDIR)/api"
	find "$(SOURCEDIR)/documentation" -type f -name 'api-reference.md' -delete

# Generate the API index file
make_api_index.py:
	@echo "Generating API index..."
	python make_api_index.py

# Generate the API toctrees
generate_api_toctrees.py:
	@echo "Generating API toctrees..."
	python generate_api_toctrees.py

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile make_api_index.py generate_api_toctrees.py
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
