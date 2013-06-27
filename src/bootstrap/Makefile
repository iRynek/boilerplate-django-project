BOOTSTRAP_DIR = ./
BOOTSTRAP_OUTPUT_DIR = ../../apps/core/static/core/lib/bootstrap/
CUSTOM_DIR = ${BOOTSTRAP_DIR}less/custom/
CUSTOM_BASE_LESS = ${CUSTOM_DIR}base.less
CUSTOM_BASE = ../../apps/core/static/core/css/base.css
BOOTSTRAP = ${BOOTSTRAP_OUTPUT_DIR}css/bootstrap.css
BOOTSTRAP_LESS = ${BOOTSTRAP_DIR}less/bootstrap.less
BOOTSTRAP_RESPONSIVE = ${BOOTSTRAP_OUTPUT_DIR}css/bootstrap-responsive.css
BOOTSTRAP_RESPONSIVE_LESS = ${BOOTSTRAP_DIR}less/responsive.less
DATE=$(shell date +%I:%M%p)
CHECK=\033[32m✔\033[39m
HR=\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#

#
# BUILD
#

build:
	@echo "\n${HR}"
	@echo "Building Bootstrap..."
	@echo "${HR}\n"
	@${BOOTSTRAP_DIR}node_modules/.bin/recess --compile ${BOOTSTRAP_LESS} > ${BOOTSTRAP}
	@${BOOTSTRAP_DIR}node_modules/.bin/recess --compile ${BOOTSTRAP_RESPONSIVE_LESS} > ${BOOTSTRAP_RESPONSIVE}
	@${BOOTSTRAP_DIR}node_modules/.bin/recess --compile ${CUSTOM_BASE_LESS} > ${CUSTOM_BASE}
	@echo "Compiling LESS with Recess...               ${CHECK} Done"
	@cp ${BOOTSTRAP_DIR}img/* ${BOOTSTRAP_OUTPUT_DIR}img/
	@cd ${BOOTSTRAP_DIR}; cat js/bootstrap-transition.js js/bootstrap-alert.js js/bootstrap-button.js js/bootstrap-carousel.js js/bootstrap-collapse.js js/bootstrap-dropdown.js js/bootstrap-modal.js js/bootstrap-tooltip.js js/bootstrap-popover.js js/bootstrap-scrollspy.js js/bootstrap-tab.js js/bootstrap-typeahead.js js/bootstrap-affix.js > js/bootstrap.js
	@cp ${BOOTSTRAP_DIR}js/*.js ${BOOTSTRAP_OUTPUT_DIR}js/
	@echo "/**\n* Bootstrap.js v2.3.2 by @fat & @mdo\n* Copyright 2012 Twitter, Inc.\n* http://www.apache.org/licenses/LICENSE-2.0.txt\n*/" > ${BOOTSTRAP_OUTPUT_DIR}js/copyright.js
	@echo "Bootstrap successfully built at ${DATE}."
	@echo "${HR}\n"
	@echo "Thanks for using Bootstrap,"
	@echo "<3 @mdo and @fat + @iRynek\n"

install:
	cd ${BOOTSTRAP_DIR}; npm install; pip install watchdog
watch:
	echo "Watching less files...";
	cd ${BOOTSTRAP_DIR};watchmedo shell-command \
	--pattern="*.less" \
        --recursive \
	--command='make' \
	-w

