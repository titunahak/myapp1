# myapp1

# Libvirt plugin

This is a collectd python plugin to collect libvirt stats


1. Install the dependencies
===========================
Run
	#yum groupinstall 'Development Tools'
	#curl https://bootstrap.pypa.io/get-pip.py | python -
	#pip install setuptools
	#pip install libvirt-python==2.0.0
	#pip install collectd
	#pip install libvirt
	#pip install psutil


2. Install collectd
===================
Run
	#wget https://storage.googleapis.com/collectd-tarballs/collectd-5.6.1.tar.bz2
	#tar xf collectd-5.6.1.tar.bz2
	#cd collectd-5.6.1

	- copy below three files to collectd-5.6.1/src directory. These files are part of deepinsight project
	  and available under "deepInsight/collector/collectd/pplugins/writers/elasticsearch/" in github.com
	   - utils_format_json.c
	   - utils_format_json.h
	   - write_http.c

	Then run
	#./configure
	# make all install
	   
	Note: Make sure write_http and python module flag is yes (in the output list) when you run ./configure
		  write_http  . . . . . yes
		  python  . . . . . . . yes

	Now the collectd is installed in /opt/collectd directory


3. Copy plugin files to the machine :
=====================================
	Copy following plugin files to a directory.
	Example: Directory name: /PATH/TO/MODULE/DIRECTORY
		-	For libvirt plugin below files needs to be copied to the /PATH/TO/MODULE/DIRECTORY from https://github.com/pramurthy/deepInsight-Plugins
			 -	libvirt/libvirt_dynamic.py
			 -	libvirt/libvirt_static.py
			 -	libvirt/libvirt_utils.py
			 -	libvirt/libvirt_constants.py
			 
			Copy below files from deepInsight project reader plugin directory to /PATH/TO/MODULE/DIRECTORY. https://github.com/pramurthy/deepInsight/tree/master/collector/collectd/pplugins/readers
			-	utils.py
			-	constants.py
			-	write_json.py
		
3. Create entry for plugin data type dummy
=========================================
	In /opt/collectd/share/collectd/types.db file at the end of file add below

	"dummy 		value:GAUGE:0:U"

4. Collectd configuration changes
=================================
	- Uncomment below line form the /opt/collectd/etc/collectd.conf
		TypesDB     "/opt/collectd/share/collectd/types.db"
		LoadPlugin syslog
		LoadPlugin python
		LoadPlugin write_http
		
	- Add the following configuration
		-	For logfile
			-----------
			<Plugin logfile>
				LogLevel debug
				File "PATH_TO_CREATE_COLLECTD_LOG_FILE"  
				Timestamp true
				PrintSeverity false
			</Plugin>

		-	For libvirt static plugin
			-------------------------
			<Plugin python>
				ModulePath "/PATH/TO/MODULE/DIRECTORY"
				LogTraces true
				Interactive false
				Import "libvirt_static"
				<Module libvirt_static>
					interval 10
				</Module>
			</Plugin>
			
		-	For libvirt dynamic plugin
			--------------------------
			<Plugin python>
				ModulePath "/PATH/TO/MODULE/DIRECTORY"
				LogTraces true
				Interactive false
				Import "libvirt_dynamic"
				<Module libvirt_dynamic>
					interval 10
				</Module>
			</Plugin>
			
		-	For write_http plugin
			---------------------
			<Plugin write_http>
				<Node "example">
					URL "http://ELASTIC_SEARCH_IP:9200/<Index_Name>/<Table_Name>"
					Format "JSON"
				</Node>
			</Plugin>

5. Start the collectd
======================
	# /opt/collectd/sbin/collectd


