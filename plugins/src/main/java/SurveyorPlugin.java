package com.troidworks.bukkit.surveyor;

import org.bukkit.*;
import org.bukkit.block.Block;
import org.bukkit.block.BlockFace;
import org.bukkit.command.Command;
import org.bukkit.command.CommandSender;
import org.bukkit.entity.Player;
import org.bukkit.metadata.FixedMetadataValue;
import org.bukkit.metadata.MetadataValue;
import org.bukkit.plugin.java.JavaPlugin;

import java.util.*;
import java.util.logging.Logger;

/**
 * Minecraft bukkit railroad Surveyor
 * Created by Karno on 2014/10/05.
 */
public class SurveyorPlugin extends JavaPlugin {
    static final String TICKET = "com.troidworks.bukkit.surveyor.Surveyor::SurveyorTicket";

    static Logger logger = null;

    final BlockFace[] faces = new BlockFace[]{BlockFace.NORTH, BlockFace.SOUTH, BlockFace.EAST, BlockFace.WEST};

    final Map<BlockFace, int[]> relativeBlocks = new HashMap<BlockFace, int[]>() {
        {
            put(BlockFace.NORTH_EAST, new int[]{0, 2});
            put(BlockFace.NORTH_WEST, new int[]{0, 3});
            put(BlockFace.SOUTH_EAST, new int[]{1, 2});
            put(BlockFace.SOUTH_WEST, new int[]{1, 3});
        }
    };

    @Override
    public void onEnable() {
        super.onEnable();
        logger = this.getLogger();
    }

    @Override
    public boolean onCommand(CommandSender sender, Command command, String label, String[] args) {
        if (command.getName().equalsIgnoreCase("survey") && sender instanceof Player) {
            Player player = (Player) sender;
            if (args.length == 1) {
                if (args[0].equalsIgnoreCase("begin")) {
                    Location location = player.getLocation();
                    // location.setY(location.getY() - 1);
                    if (isRailBlock(location.getBlock())) {
                        player.setMetadata(TICKET, new FixedMetadataValue(this, location));
                        player.sendMessage(ChatColor.YELLOW + "Successfully started. ");
                        player.sendMessage(ChatColor.YELLOW + "(測量の開始に成功しました。)");
                    } else {
                        player.sendMessage(ChatColor.RED + "start surveying must be issued on the rail. ");
                        player.sendMessage(ChatColor.RED + "(測量の開始時には線路上に立っている必要があります。)");
                    }
                    return true;
                }
                if (args[0].equalsIgnoreCase("end")) {
                    List<MetadataValue> metadata = player.getMetadata(TICKET);
                    if (metadata.size() == 0) {
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
                    long timestamp = System.currentTimeMillis();
                    player.sendMessage(ChatColor.YELLOW + "finding path : " + toDisplayStr(start) + " -> " + toDisplayStr(finish));
                    /*
                    HashMap<Location, Double> map = new HashMap<Location, Double>();
                    map.put(start, -1.0);
                    double result = getShortest(start.getBlock(), finish, map);
                    */
                    double result = getShortestTrail(start, finish);
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
            }
            player.sendMessage(ChatColor.RED + "you must specify argument \"begin\" , \"end\" or \"help\". ");
            player.sendMessage(ChatColor.RED + "(\"begin\" , \"end\" または \"help\"の引数が必要です。)");
            return true;
        }
        return false;
    }

    private String toDisplayStr(Location location) {
        return "(" + location.getBlockX() + "," + location.getBlockY() + "," + location.getBlockZ() + ")";
    }

    private double getShortestTrail(final Location origin, final Location destination) {
        if (origin.equals(destination)) {
            return 0.0;
        }

        Queue<TaggedLocation> open = new PriorityQueue<TaggedLocation>(16, getTaggedLocationComparator());
        Map<Location, TaggedLocation> close = new HashMap<Location, TaggedLocation>();

        // initialize
        open.add(new TaggedLocation(origin, destination));

        while (!open.isEmpty()) {
            // poll shortest one from priority queue
            TaggedLocation poll = open.poll();
            Location pollLocation = poll.getLocation();

            if (pollLocation.equals(destination)) {
                // completed!
                // return trail of current location.
                return poll.getDistance();
            }

            if (close.get(pollLocation) != null) {
                // this location has been observed
                continue;
            }

            close.put(pollLocation, poll);

            // continue to search trail.
            Map<Location, Double> neighbor = getNeighborRail(pollLocation);
            for (Location loc : neighbor.keySet()) {
                // get tagged location of current.
                TaggedLocation tagged = new TaggedLocation(loc, destination,
                        poll.getDistance() + neighbor.get(loc)); // g(pollLocation) + cost(pollLocation, loc)
                TaggedLocation old = close.get(loc);
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
    private Map<Location, Double> getNeighborRail(Location location) {
        Map<Location, Double> result = new HashMap<Location, Double>();
        double originalY = location.getY();
        // y = -1
        location.setY(originalY - 1);
        result.putAll(getNeighborRailThisY(location));
        // y = +1
        location.setY(originalY + 1);
        result.putAll(getNeighborRailThisY(location));
        // y = 0
        location.setY(originalY);
        result.putAll(getNeighborRailThisY(location));
        return result;
    }

    /**
     * get neighbor rails in this Y value.
     *
     * @param location source location
     * @return neighbor location and its distance
     */
    private Map<Location, Double> getNeighborRailThisY(Location location) {
        Block block = location.getBlock();
        Map<Location, Double> result = new HashMap<Location, Double>();

        boolean[] relFlags = new boolean[4];
        for (int i = 0; i < 4; i++) {
            relFlags[i] = isRailBlock(block.getRelative(faces[i]));
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
                    result.put(rel.getLocation(), 1.0); //if rail is slant(ななめ)
                }
            }
        }

        for (int i = 0; i < 4; i++) {
            if (relFlags[i]) {
                Block rel = block.getRelative(faces[i]);
                if (isRailBlock(rel)) {
                    result.put(rel.getLocation(), 1.0);
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

    class TaggedLocation {
        private Location location;
        private double estimate;
        private double distance;

        public TaggedLocation(Location location, Location target) {
            this(location, target, 0);
        }

        public TaggedLocation(Location location, Location target, double distance) {
            this.location = location;
            this.estimate = Math.sqrt(Math.pow(location.getX() - target.getX(), 2) + Math.pow(location.getZ() - target.getZ(), 2));
            this.distance = distance;
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
}

