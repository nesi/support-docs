# Rclone

Rclone is available for those that need to transfer data from cloud
storage services like Google drive or OneDrive.

To use Rclone on Mahuika, you first need to module load it:

```bash
module load rclone
```

The basic command syntax of Rclone:

```bash
rclone subcommand options source:path dest:path
```

The most frequently used Rclone subcommands:

- `rclone copy` - Copy files from the source to the destination, skipping what has already been copied.
- `rclone sync` - Make the source and destination identical, modifying only the destination.
- `rclone move` - Move files from the source to the destination.
- `rclone delete` - Remove the contents of a path.

A more extensive list can be found in the [Rclone documentation](https://rclone.org/docs).
