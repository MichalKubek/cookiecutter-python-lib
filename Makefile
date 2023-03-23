BAKE_OPTIONS=--no-input

help:
	@echo "bake 	generate project using defaults"
	@echo "watch 	generate project using defaults and watch for changes"
	@echo "replay 	replay last cookiecutter run and watch for changes"
	@echo "init	Prepare working eviroment"

init:
	pip install -r requirements.txt
bake:
	cookiecutter $(BAKE_OPTIONS) . --overwrite-if-exists

watch: bake
	watchmedo shell-command -p '*.*' -c 'make bake -e BAKE_OPTIONS=$(BAKE_OPTIONS)' -W -R \{{cookiecutter.namespace}}-{{cookiecutter.project_name}}/

replay: BAKE_OPTIONS=--replay
replay: watch
	;
