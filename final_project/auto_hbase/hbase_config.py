import xml.etree.ElementTree

def site_config(rootdir, master, cluster_distributed, zookeeper_quorum,
                 zookeeper_property_dataDir, zookeeper_session_timeout,
                 master_maxclockskew, hregion_max_filesize, master_loadbalance_bytable):
    # map the inputs to the function blocks
    options = \
        {
            'hbase.rootdir': rootdir,
            'hbase.master': master,
            'hbase.cluster.distributed': cluster_distributed,
            'hbase.zookeeper.quorum': zookeeper_quorum,
            'hbase.zookeeper.property.dataDir': zookeeper_property_dataDir,
            'zookeeper.session.timeout': zookeeper_session_timeout,
            'hbase.master.maxclockskew': master_maxclockskew,
            'hbase.hregion.max.filesize': hregion_max_filesize,
            'hbase.master.loadbalance.bytable': master_loadbalance_bytable
         }

    # Open original file
    et = xml.etree.ElementTree.parse('conf/hbase-site.xml')

    root = et.getroot()
    for property in root:
        value = options.get(property[0].text, None)
        if value:
            property[1].text = value

    # Write back to file
    et.write('hbase-site.xml')
    #et.write(sys.stdout)
