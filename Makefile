BMM_GH="git@github.com:rainbow-mind-machine/boring-mind-machine.git"
BMM_CMR="ssh://git@git.charlesreid1.com:222/bots/boring-mind-machine.git"
MKM_CMR="ssh://git@git.charlesreid1.com:222/charlesreid1/mkdocs-material.git"

initialize: site mkdocs_material cmr_remote

deploy: site
	rm -rf site/*
	mkdocs build
	cd site; git add -A .; git commit -a -m 'Updating gh-pages site'; git push origin gh-pages; git push cmr gh-pages

mkdocs_material:
	git submodule add $(MKM_CMR)
	git add mkdocs-material .gitmodules
	git commit mkdocs-material .gitmodules -m 'Initializing mkdocs-material submodule'
	git push origin

site:
	git clone -b gh-pages $(BMM_GH) site
	cd site; git remote add cmr $(BMM_CMR)

cmr_remote:
	git remote add cmr $(BMM_CMR)

test:
	nosetests -v
