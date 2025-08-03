# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

# Define a timeout value
TIMEOUT       = 2

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Remove all auto-generated files
clean:
	@echo "Removing auto-generated files..."
	@if [ -d "$(BUILDDIR)" ]; then \
		echo "Removing $(BUILDDIR) directory..."; \
		rm -rf "$(BUILDDIR)"; \
		sleep $(TIMEOUT); \
	fi
	@echo "Removing API Reference toctree sections..."
	@python remove_api_toctrees.py
	@sleep $(TIMEOUT)
	@if [ -d "$(SOURCEDIR)/api" ]; then \
		echo "Removing $(SOURCEDIR)/api directory..."; \
		rm -rf "$(SOURCEDIR)/api"; \
		sleep $(TIMEOUT); \
	fi
	@if [ -d "downloads" ]; then \
		echo "Removing downloads directory..."; \
		rm -rf "downloads"; \
		sleep $(TIMEOUT); \
	fi

# Fetch repositories
fetch_repos:
	@echo "Fetching repositories..."
	@python fetch_repos.py
	@sleep $(TIMEOUT)

# Generate the API index file
make_api_index:
	@echo "Generating API index..."
	@python make_api_index.py
	@sleep $(TIMEOUT)

# Generate the API toctrees
generate_api_toctrees:
	@echo "Generating API toctrees..."
	@python generate_api_toctrees.py
	@sleep $(TIMEOUT)

# Default target to build the documentation
all: fetch_repos make_api_index generate_api_toctrees
	@$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: all
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
