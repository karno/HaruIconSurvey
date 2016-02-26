package com.troidworks.bukkit.surveyor;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import org.bukkit.*;
import org.bukkit.block.Block;
import org.bukkit.block.BlockFace;
import org.bukkit.command.Command;
import org.bukkit.command.CommandSender;
import org.bukkit.entity.Player;
import org.bukkit.event.EventHandler;
import org.bukkit.event.EventPriority;
import org.bukkit.event.Listener;
import org.bukkit.event.server.PluginEnableEvent;
import org.bukkit.metadata.FixedMetadataValue;
import org.bukkit.metadata.MetadataValue;
import org.bukkit.plugin.java.JavaPlugin;
import org.bukkit.plugin.Plugin;
import org.bukkit.plugin.PluginManager;

import org.dynmap.DynmapAPI;
import org.dynmap.DynmapLocation;
import org.dynmap.markers.Marker;
import org.dynmap.markers.MarkerIcon;
import org.dynmap.markers.MarkerAPI;
import org.dynmap.markers.MarkerSet;
import org.dynmap.markers.PolyLineMarker;

import java.util.*;
import java.util.logging.Level;
import java.util.logging.Logger;
import org.dynmap.markers.impl.MarkerAPIImpl;

/**
 * Minecraft bukkit railroad Surveyor
 * Created by Karno on 2014/10/05.
 * Improved by hnakai on 2015/12/25.
 */
public class SurveyorPlugin extends JavaPlugin {
    static final String TICKET = "com.troidworks.bukkit.surveyor.Surveyor::SurveyorTicket";
    
    private static final String ARG_LABEL = "label";
    private static final String ARG_MARKUP = "markup";
    private static final String ARG_ID = "id";
    private static final String ARG_NEWID = "newid"; //original!
    private static final String ARG_TYPE = "type";
    private static final String ARG_NEWLABEL = "newlabel";
    private static final String ARG_FILE = "file";
    private static final String ARG_HIDE = "hide";
    private static final String ARG_ICON = "icon";
    private static final String ARG_DEFICON = "deficon";
    private static final String ARG_SET = "set";
    private static final String ARG_NEWSET = "newset";
    private static final String ARG_PRIO = "prio";
    private static final String ARG_MINZOOM = "minzoom";
    private static final String ARG_MAXZOOM = "maxzoom";
    private static final String ARG_STROKEWEIGHT = "weight";
    private static final String ARG_STROKECOLOR = "color";
    private static final String ARG_STROKEOPACITY = "opacity";
    private static final String ARG_FILLCOLOR = "fillcolor";
    private static final String ARG_FILLOPACITY = "fillopacity";
    private static final String ARG_YTOP = "ytop";
    private static final String ARG_YBOTTOM = "ybottom";
    private static final String ARG_RADIUSX = "radiusx";
    private static final String ARG_RADIUSZ = "radiusz";
    private static final String ARG_RADIUS = "radius";
    private static final String ARG_SHOWLABEL = "showlabels";
    private static final String ARG_X = "x";
    private static final String ARG_Y = "y";
    private static final String ARG_Z = "z";
    private static final String ARG_WORLD = "world";
    private static final String ARG_BOOST = "boost";
    private static final String ARG_DESC = "desc";
    
    private static Logger logger = null;

    final BlockFace[] faces = new BlockFace[]{BlockFace.NORTH, BlockFace.SOUTH, BlockFace.EAST, BlockFace.WEST};

    final Map<BlockFace, int[]> relativeBlocks = new HashMap<BlockFace, int[]>() {
        {
            put(BlockFace.NORTH_EAST, new int[]{0, 2});
            put(BlockFace.NORTH_WEST, new int[]{0, 3});
            put(BlockFace.SOUTH_EAST, new int[]{1, 2});
            put(BlockFace.SOUTH_WEST, new int[]{1, 3});
        }
    };
    
    private Plugin dynmap;
    private DynmapAPI dynmapapi;
    private MarkerAPI markerapi;
    
    private class OurServerListener implements Listener {
        @EventHandler(priority=EventPriority.MONITOR)
        public void onPluginEnable(PluginEnableEvent event) {
            Plugin p = event.getPlugin();
            String name = p.getDescription().getName();
            if(name.equals("dynmap")) {
                activate();
            }
        }
    }
    
    /* from DynmapCore's MarkerAPIImpl.java */
     private static Map<String,String> parseArgs(String[] args, CommandSender snd) {
        HashMap<String,String> rslt = new HashMap<>();
        /* Build command line, so we can parse our way - make sure there is trailing space */
        String cmdline = "";
        for(int i = 1; i < args.length; i++) {
            cmdline += args[i] + " ";
        }
        boolean inquote = false;
        StringBuilder sb = new StringBuilder();
        String varid = null;
        for(int i = 0; i < cmdline.length(); i++) {
            char c = cmdline.charAt(i);
            if(inquote) {   /* If in quote, accumulate until end or another quote */
                if(c == '\"') { /* End quote */
                    inquote = false;
                    if(varid == null) { /* No varid? */
                        rslt.put(ARG_LABEL, sb.toString());
                    }
                    else {
                        rslt.put(varid, sb.toString());
                        varid = null;
                    }
                    sb.setLength(0);
                }
                else {
                    sb.append(c);
                }
            }
            else if(c == '\"') {    /* Start of quote? */
                inquote = true;
            }
            else if(c == ':') { /* var:value */
                varid = sb.toString();  /* Save variable ID */
                sb.setLength(0);
            }
            else if(c == ' ') { /* Ending space? */
                if(varid == null) { /* No varid? */
                    if(sb.length() > 0) {
                        rslt.put(ARG_LABEL, sb.toString());
                    }
                }
                else {
                    rslt.put(varid, sb.toString());
                    varid = null;
                }
                sb.setLength(0);
            }
            else {
                sb.append(c);
            }
        }
        if(inquote) {   /* If still in quote, syntax error */
            snd.sendMessage("Error: unclosed doublequote");
            return null;
        }
        return rslt;
    }
    
    @Override
    public void onEnable() {
        super.onEnable();
        logger = this.getLogger();
        PluginManager pm = getServer().getPluginManager();
        dynmap = pm.getPlugin("dynmap");
        if (dynmap == null){
            logger.log(Level.SEVERE, "Cannot find dynmap!");
            return;
        }
        dynmapapi = (DynmapAPI)dynmap;
        
        pm.registerEvents(new OurServerListener(), this);

        if (dynmap.isEnabled()){
            activate();
        }
        
        
    }

    @Override
    public boolean onCommand(CommandSender sender, Command command, String label, String[] args) {
        if (command.getName().equalsIgnoreCase("survey")) {
            if (!(sender instanceof Player)){
                // commands that console also can issue
                if (args[0].equalsIgnoreCase("renameid")) {
                    processRenameIDMarker(args, sender);
                    return true;
                }
                if (args[0].equalsIgnoreCase("addicons")) {
                    processAddIcons(args, sender);
                    return true;
                }
                sender.sendMessage("Command can only be used by player");
                return false;
            }
            // commands that only player can issue
            Player player = (Player) sender;
            if (args.length >= 1) {
                
                /*
                if (args[0].equalsIgnoreCase("mdebug")) {
                    String setid = "markers";
                    String id = "_spawn_world";
                    String label_ = null;
                    if((id == null) && (label_ == null)) {
                        player.sendMessage("<label> or id:<marker-id> required");
                        return true;
                    }
                    if(setid == null) {
                        setid = MarkerSet.DEFAULT;
                    }
                    MarkerSet set;
                    set = markerapi.getMarkerSet(setid);
                    if(set == null) {
                        player.sendMessage("Error: invalid set - " + setid);
                        return true;
                    }
                    Marker marker;
                    if(id != null) {
                        marker = set.findMarker(id);
                        if(marker == null) {    
                            player.sendMessage("Error: marker not found - " + id);
                            return true;
                        }
                    }
                    else {
                        marker = set.findMarkerByLabel(label_);
                        if(marker == null) {   
                            player.sendMessage("Error: marker not found - " + label_);
                            return true;
                        }
                    }
                    player.sendMessage("[found]: X:"+marker.getX());
                    return true;
                }
                */
                if (args[0].equalsIgnoreCase("begin")) {
                    if (args.length >= 3){
                        player.sendMessage(ChatColor.RED + "Too many arguments.(引数が多すぎます。)");  
                    }else{
                        Location location = player.getLocation();
                        beginSurvey(player, location);
                        return true;
                    }
                }
                if (args[0].equalsIgnoreCase("begin&add")) {
                    Location location = player.getLocation();
                    if (beginSurvey(player, location)){
                        //add marker
                    }
                    return true;
                }
                if (args[0].equalsIgnoreCase("end")) {
                    List<MetadataValue> metadata = player.getMetadata(TICKET);
                    if (metadata.isEmpty()) {
                        player.sendMessage(ChatColor.RED + "surveying is not started. ");
                        player.sendMessage(ChatColor.RED + "(測量がまだ開始されていません。)");
                        return true;
                    }
                    Location start = (Location) metadata.get(0).value();
                    if (!isRailBlock(start.getBlock())) {
                        player.sendMessage(ChatColor.RED + "starting block is not a rail (or destructed). ");
                        player.sendMessage(ChatColor.RED + "(開始地点がレールではなくなりました。)");
                        return true;
                    }
                    Block finishBlock = player.getLocation().getBlock();
                    if (!isRailBlock(finishBlock)) {
                        player.sendMessage(ChatColor.RED + "end surveying must be issued on the rail. ");
                        player.sendMessage(ChatColor.RED + "(測量の終了時には線路上に立っている必要があります。)");
                        return true;
                    }
                    Location finish = finishBlock.getLocation();
                    player.sendMessage(ChatColor.YELLOW + "finding path : " + toDisplayStr(start) + " -> " + toDisplayStr(finish));
                    long timestamp = System.currentTimeMillis();
                    
                    double result = getShortestTrail(start, finish, player);
                    
                    long duration = System.currentTimeMillis() - timestamp;
                    if (result >= 0) {
                        player.sendMessage(ChatColor.GREEN + "OK! (elapsed time :  " + duration + " ms)");
                        player.sendMessage(ChatColor.GREEN + "distance is " + result + "." );
                    } else {
                        player.sendMessage(ChatColor.RED + "could not reach the destination rail. ");
                        player.sendMessage(ChatColor.RED + "(経路を見つけられませんでした。)");
                    }

                    return true;
                }
                if (args[0].equalsIgnoreCase("help")) {
                    player.sendMessage(ChatColor.WHITE + "This plugin let you to survey rail distance between 2 points.");
                    player.sendMessage(ChatColor.WHITE + " 1. Go begin point and stand on the rail. ");
                    player.sendMessage(ChatColor.WHITE + " 2. enter command \"/survey begin\".");
                    player.sendMessage(ChatColor.WHITE + " 3. Go end point and stand on the rail.");
                    player.sendMessage(ChatColor.WHITE + " 4. enter command \"/survey end\".");
                    return true;
                }
            } else {
            }
            player.sendMessage(ChatColor.RED + "you must specify argument \"begin\" , \"end\" or \"help\". ");
            player.sendMessage(ChatColor.RED + "(\"begin\" , \"end\" または \"help\"の引数が必要です。)");
            return true;
        }
        return false;
    }

    private void activate(){
        markerapi = dynmapapi.getMarkerAPI();
        if(markerapi == null) {
            logger.log(Level.SEVERE , "Error loading Dynmap marker API!");
        }
    }
    
    private boolean processRenameIDMarker(String[] args, CommandSender sender){
        String id, newid, setid, label, markup, world;
        double x, y, z;
        MarkerIcon icon;
        int minzoom, maxzoom;
        if(args.length==1){
            sender.sendMessage(ChatColor.RED + "usage: /survey renameid id:[id] newid:[newid] (world:[world] set:[set])");
            return false;
        }
        Map<String,String> params = parseArgs(args, sender);
        if(params == null) return false;
        id = params.get(ARG_ID);
        newid = params.get(ARG_NEWID);
        setid = params.get(ARG_SET);
        world = params.get(ARG_WORLD);
        if(world != null) {
            if(getServer().getWorld(world) == null) {
                sender.sendMessage("Invalid world ID: " + world);
                return true;
            }
        }else{
            sender.sendMessage(" world:<world-id> required");
            return true;
        }

        if((id == null)) {
            sender.sendMessage(" id:<marker-id> required");
            return true;
        }
        if((newid == null)) {
            sender.sendMessage(" newid:<marker-id> required");
            return true;
        }
        if(setid == null) {
            setid = MarkerSet.DEFAULT;
        }
        MarkerSet set = markerapi.getMarkerSet(setid);
        if(set == null) {
            sender.sendMessage("Error: invalid set - " + setid);
            return true;
        }
        Marker marker, newmarker;
        marker = set.findMarker(id);
        if(marker == null) {    /* No marker */
            sender.sendMessage("Error: marker not found - " + id);
            return true;
        }
        minzoom = marker.getMinZoom();
        maxzoom = marker.getMaxZoom();
        label = marker.getLabel();
        markup = marker.getDescription();
        icon = marker.getMarkerIcon();
        x = marker.getX();
        y = marker.getY();
        z = marker.getZ();
        
        marker.deleteMarker();
        newmarker = set.createMarker(newid, label, "true".equals(markup),  world, x, y, z, icon, true);
        newmarker.setMinZoom(minzoom);
        newmarker.setMaxZoom(maxzoom);
        
        sender.sendMessage("Renamed marker id:" + marker.getMarkerID() + " (" + marker.getLabel() + ")");


        return true;
    } 
    
    private boolean processAddIcons(String[] args, CommandSender sender){
       String id, file, label;
        if(args.length > 1) {
            for(int i = 1; i < args.length; i++){
                id = args[i];
                label = args[i];
                file = "./tmp/"+args[i]+".png";

                MarkerIcon ico = markerapi.getMarkerIcon(id);
                if(ico != null) {
                    sender.sendMessage("Icon '" + id + "' already defined.");
                }else{
                    /* Open stream to filename */
                    File iconf = new File(file);
                    FileInputStream fis = null;
                    try {
                        fis = new FileInputStream(iconf);
                        /* Create new icon */
                        MarkerIcon mi = markerapi.createMarkerIcon(id, label, fis);
                        if(mi == null) {
                            sender.sendMessage("Error creating icon:"+id);
                        }else{
                            sender.sendMessage("Successfully created icon:"+id);
                        }
                    } catch (IOException iox) {
                        sender.sendMessage("Error loading icon file:" + id + " - " + iox);
                    } finally {
                        if(fis != null) {
                            try { fis.close(); } catch (IOException iox) {}
                        }
                    }
                }
            }
        } else {
            sender.sendMessage("args required");
        }
        return true;
    } 
    
    private boolean beginSurvey(Player player, Location location){
        // location.setY(location.getY() - 1);
        if (isRailBlock(location.getBlock())) {
            player.setMetadata(TICKET, new FixedMetadataValue(this, location));
            player.sendMessage(ChatColor.YELLOW + "Successfully started. ");
            player.sendMessage(ChatColor.YELLOW + "(測量の開始に成功しました。)");
            return true;
        } else {
            player.sendMessage(ChatColor.RED + "start surveying must be issued on the rail. ");
            player.sendMessage(ChatColor.RED + "(測量の開始時には線路上に立っている必要があります。)");
            return false;
        }   
    }
    
    private boolean addLine(List<Location> route){
        MarkerAPI api = markerapi;
        //DynmapLocation loc = null;
        List<DynmapLocation> ll = new ArrayList<>();
        double[] xx = new double[route.size()];
        double[] yy = new double[route.size()];
        double[] zz = new double[route.size()];
        String setid, id, label, markup;
        
        if((route.size() < 2)) {   /* Not enough points? */
            return false;
        }
        for(int i=0; i<route.size(); i++){
            Location location = route.get(i);
            xx[i] = location.getX();
            yy[i] = location.getY();
            zz[i] = location.getZ();
            ll.add(new DynmapLocation(location.getWorld().getName(),xx[i],yy[i],zz[i]));
            
        }
        /* Parse arguements */
        /*
        setid = parms.get(ARG_SET);
        id = parms.get(ARG_ID);
        label = parms.get(ARG_LABEL);
        markup = parms.get(ARG_MARKUP);
        */
        setid=null;
        id="hoge";
        label="ほげ";
        markup="";
        /* Fill in defaults for missing parameters */
        if(setid == null) {
            setid = MarkerSet.DEFAULT;
        }
        /* Add new marker */
        MarkerSet set = api.getMarkerSet(setid);
        if(set == null) {
            //sender.sendMessage("Error: invalid set - " + setid);
            return false;
        }
        /* Make poly-line marker */
        PolyLineMarker m = set.createPolyLineMarker(id, label, "true".equals(markup), ll.get(0).world, xx, yy, zz, true);
        if(m == null) {
            //sender.sendMessage("Error creating line");
            return false;
        }
        else {
            /* Process additional attributes, if any */
            //processPolyArgs(sender, m, parms);
            
            //sender.sendMessage("Added line id:'" + m.getMarkerID() + "' (" + m.getLabel() + ") to set '" + set.getMarkerSetID() + "'");
            
            /* Clear corner list */
        }
        return true;
    }
            
    private String toDisplayStr(Location location) {
        return "(" + location.getBlockX() + "," + location.getBlockY() + "," + location.getBlockZ() + ")";
    }

    // A* algorithm
    private double getShortestTrail(final Location origin, final Location destination, Player player) {
        if (origin.equals(destination)) {
            return 0.0;
        }

        Queue<TaggedLocation> open = new PriorityQueue<>(16, getTaggedLocationComparator());
        Map<Location, TaggedLocation> close = new HashMap<>();

        // initialize
        // start node is location == parent
        open.add(new TaggedLocation(origin, destination));

        while (!open.isEmpty()) {
            // poll shortest one from priority queue
            TaggedLocation poll = open.poll();
            Location pollLocation = poll.getLocation();

            if (pollLocation.equals(destination)) {
                // completed!
                
                // trace result route
                TaggedLocation tracer = poll;
                Boolean flag = false;
                Direction dir;
                Direction olddir = new Direction(BlockFace.SELF, -2); //dummy
                Location oldloc;
                List<TaggedLocation> route = new ArrayList<>();
                List<Location> simplifiedroute = new ArrayList<>();
                while(tracer.getParent() != tracer.getLocation()){
                    route.add(tracer);
                    tracer = close.get(tracer.getParent());
                }
                route.add(tracer);
                Collections.reverse(route);
                oldloc = route.get(0).getLocation();
                for(TaggedLocation tagged : route){
                    dir = tagged.getDirection();
                    if((dir.getFace()!=olddir.getFace()) || (dir.getYoffset()!=olddir.getYoffset())){
                        if(!flag){
                            simplifiedroute.add(oldloc);
                            //player.sendMessage(""+toDisplayStr(oldloc)
                            //    +" "+olddir.getFace().toString()+" "+olddir.getYoffset());
                        }
                        simplifiedroute.add(tagged.getLocation());
                        //player.sendMessage(""+toDisplayStr(tagged.getLocation())
                        //    +" "+dir.getFace().toString()+" "+dir.getYoffset());
                        flag = true;
                    }else{
                        flag = false;
                    }
                    olddir = dir;
                    oldloc = tagged.getLocation();
                }
                if(!flag){
                    simplifiedroute.add(oldloc);
                    //player.sendMessage(""+toDisplayStr(oldloc)
                    //    +" "+olddir.getFace().toString()+" "+olddir.getYoffset());
                }
                addLine(simplifiedroute); // add line to dmarker
                // return trail of current location.
                return poll.getDistance();
            }

            if (close.get(pollLocation) != null) {
                // this location has been observed
                continue;
            }

            close.put(pollLocation, poll);

            // continue to search trail.
            Map<Location, DirectionAndDistance> neighbor = getNeighborRail(pollLocation);
            for (Location loc : neighbor.keySet()) {
                // get tagged location of current.
                TaggedLocation old = close.get(loc);
                TaggedLocation tagged = new TaggedLocation(loc, destination,
                        poll.getDistance() + neighbor.get(loc).getDistance(), // g(pollLocation) + cost(pollLocation, loc)
                        pollLocation, neighbor.get(loc).getDirection());
                if (old != null) {
                    if (tagged.getDistance() >= old.getDistance()) {
                        continue;
                    }
                    close.remove(loc);
                }
                open.add(tagged);
                
            }
        }

        return -1;
    }

    /**
     * get neighbor rails
     *
     * @param location source location
     * @return neighbor location and its distance
     */
    private Map<Location, DirectionAndDistance> getNeighborRail(Location location) {
        Map<Location, DirectionAndDistance> result = new HashMap<>();
        // y = -1
        result.putAll(getNeighborRailThisY(location, -1));
        // y = +1
        result.putAll(getNeighborRailThisY(location, +1));
        // y = 0
        result.putAll(getNeighborRailThisY(location, 0));
        return result;
    }

    /**
     * get neighbor rails in this Y value.
     *
     * @param location source location
     * @return neighbor location and its distance
     */
    private Map<Location, DirectionAndDistance> getNeighborRailThisY(Location origloc, int Yoffset) {
        Map<Location, DirectionAndDistance> result = new HashMap<>();
        double originalY = origloc.getY();
        Location location = origloc.clone();
        location.setY(originalY + Yoffset);
        Block block = location.getBlock();

        boolean[] relFlags = new boolean[4];
        for (int i = 0; i < 4; i++) {
            relFlags[i] = isRailBlock(block.getRelative(faces[i]));
            if (relFlags[i]) {
                Block rel = block.getRelative(faces[i]);
                if (isRailBlock(rel)) {
                    //if rail is not slant(ななめでない)  
                    result.put(rel.getLocation(), new DirectionAndDistance(
                            new Direction(faces[i], Yoffset), 1.0));
                }
            }
        }

        for (BlockFace face : relativeBlocks.keySet()) {
            boolean flag = false;
            for (int i : relativeBlocks.get(face)) {
                if (relFlags[i]) {
                    flag = true;
                }
            }
            if (flag) {
                Block rel = block.getRelative(face);
                if (isRailBlock(rel)) {
                    //if rail is slant(ななめ)
                    result.put(rel.getLocation(), new DirectionAndDistance(
                            new Direction(face, Yoffset), 1.0));
                }
            }
        }
        return result;
    }

    private boolean isRailBlock(Block block) {
        if (block == null) return false;
        Material material = block.getType();
        return material == Material.ACTIVATOR_RAIL ||
                material == Material.POWERED_RAIL ||
                material == Material.DETECTOR_RAIL ||
                material == Material.RAILS;
    }

    public static Comparator<TaggedLocation> getTaggedLocationComparator() {
        return new Comparator<TaggedLocation>() {
            @Override
            public int compare(TaggedLocation o1, TaggedLocation o2) {
                double value = o1.getCost() - o2.getCost();
                return value == 0 ? 0 : (value > 0 ? 1 : -1);
            }
        };
    }

    public class TaggedLocation {
        private Location location; // this node
        private double estimate; // heuristic cost
        private double distance; // actual cost
        private Location parent; // parent node
        private Direction direction;

        public TaggedLocation(Location location, Location target) {
            this(location, target, 0, location, new Direction(BlockFace.SELF, 0)); 
        }

        public TaggedLocation(Location location, Location target, double distance, Location parent, Direction direction) {
            this.location = location;
            this.estimate = Math.sqrt(Math.pow(location.getX() - target.getX(), 2) + Math.pow(location.getZ() - target.getZ(), 2));
            this.distance = distance;
            this.parent = parent;
            this.direction = direction;
        }

        public Location getLocation() {
            return location;
        }

        public double getDistance() {
            return distance;
        }

        public double getEstimate() {
            return estimate;
        }

        public Location getParent() {
            return parent;
        }
        
        public Direction getDirection() {
            return direction;
        }
        
        public double getCost() {
            return getDistance() + getEstimate();
        }

        @Override
        public boolean equals(Object obj) {
            return obj instanceof TaggedLocation && location.equals(((TaggedLocation) obj).location);
        }

        @Override
        public int hashCode() {
            return location.hashCode();
        }
    }
    
    public class DirectionAndDistance {
        private final Direction direction;
        private final double distance; // 脳髄からx3 分泌
        
        public DirectionAndDistance(Direction direction, double distance){
            this.direction = direction;
            this.distance = distance;
        }
        
        public Direction getDirection() {
            return direction;
        }

        public double getDistance() {
            return distance;
        }
    }
    
    public class Direction {
        private final BlockFace face;
        private final int Yoffset;
        
        public Direction(BlockFace face, int Yoffset) {
            this.face = face;
            this.Yoffset = Yoffset;
        }
        
        public BlockFace getFace() {
            return face;
        }

        public int getYoffset() {
            return Yoffset;
        }
    }

}

