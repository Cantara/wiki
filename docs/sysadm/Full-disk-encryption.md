# Full disk encryption

This will not be another howto for encrypting your harddrive, because there is a enough of good howtoes on the subject already (see links in the [security:resouces](Resources.md) section). However it is interesting to know which encryption schemes are preferred and why and in which configuration they apply.

## Why?

Since the audience for this wiki are mostly developers this will be the angle for describing why encryption is important.

Firstly, unless you are developing on a open-source project, the code itself are not public domain and needs to be protected. A search on Google for "source code leaked" gives 22000 hits. Secondly, the code also often comes with database connection strings and internal IP addressees which should not be exposed. 

Thirdly, you might install a local database with live data to test the application. If this database contains personal information about real customers or organizations you definitely want some protection. Encrypting sensitive information has been done for a long time and is a perfect means to protect data from exposure when the medium on which it is stored is lost or stolen. However you cannot run a database server from a file stored in an encrypted folder. You can however from a encrypted disk drive, which to the operating system is just another partition with a file system.

Encrypting drives makes some sense for work stations, but they make a whole lot more sense for a laptop that you take with you all the time, both for work and other events. A developers laptop should therefore use an encrypted drive where work can be safely stored.

## How?

There are dozens of ways to encrypt files and folder on your laptop, so I'll describe my favourite ones and why:
- Full system disk encryption
- Full disk encryption
- Virtual encrypted partion

### System disk encryption

I prefer to use system disk encryption instead of encrypting single files, folders or even non<sub>~system partitions. The reason for this is that if you encrypt only selected parts of your file system it is easy to forget some piece of data that should have been encrypted which are not (for instance if your database stores data in /var/lib/ or your text editor auto</sub>~saves files in /tmp). Also, you would like to encrypt your home folder which on Vista cannot (to my knowledge) be a separate partition mounted after login. If your a little paranoid (and you should be) you should go for a encryption scheme that is active before you log in.

To fully encrypt a Linux system you need to reinstall the OS. Not because that is strictly necessary, but because there is no script or program that does it automatically and the number of corner cases to handle makes in unsuitable for a simple howto. I only use Debian GNU Linux or Ubuntu. The Debian installer has a separate choice for encrypted root partition using LVM, dm-crypt and LUKS. For Ubuntu there is a similar choice, but only on the alternate install ISO.

For both Debian and Linux installing on an encrypted system disk is very easy. When setting up disks choose "Guided - Use entire disk and setup an encrypted LVM" or follow [this](http://learninginlinux.wordpress.com/2008/04/23/installing<sub>~ubuntu</sub><sub>804</sub><sub>with</sub><sub>full</sub><sub>disk</sub>~encryption/) howto to manually choose the partition to encrypt.

For Windows there is the open<sub>~source project [TrueCrypt](http://www.truecrypt.org/) which allow full disk encryption to be added on a installed system using a custom boot</sub>~loader which mounts the disk before the OS i started. The procedure is pretty straight forward and described in detail on the TrueCrypt web page. Before encrypting the drive the program will force you to burn a bootable CD with the TrueCrypt bootloader and some rescue applications. The system does encrypt the volume live and the operation can be rolled back (at any time) if you suddenly change your mind.

### Disk encryption

For non-system disk encryption all that's needed is an empty partition or disk to put data on. It will be formatted so should be empty or create a backup of the files somewhere else. If the system drive is not encrypted, all work related data should be placed on the encrypted drive. This can however not be enforced for all user files like browser cache and user specific settings, which will be placed in the users home folder. On Linux the actual partition holding the home folders can be encrypted solving this problem.

On Linux: [https://help.ubuntu.com/community/EncryptedFilesystemHowto](https://help.ubuntu.com/community/EncryptedFilesystemHowto) or [http://www.hermann<sub>~uwe.de/blog/howto</sub><sub>disk</sub><sub>encryption</sub><sub>with</sub><sub>dm</sub><sub>crypt</sub><sub>luks</sub><sub>and</sub><sub>debian](http://www.hermann</sub><sub>uwe.de/blog/howto</sub><sub>disk</sub><sub>encryption</sub><sub>with</sub><sub>dm</sub><sub>crypt</sub><sub>luks</sub><sub>and</sub>~debian)

On Windows: Use TrueCrypt and choose the partition to encrypt.

### Virtual encrypted partition

One feature of a virtual partition is that the partition is stored in a file on the original file system. This means that no changes has to be made on the partition table of your system and the partition can be added without any great risk or need to reinstall. Also, it would be a simple task to take an encrypted backup of the virtual drive, since the file can be sent to the backup server as it is (you should prefer a backup system which can do incremental backups on separate blocks instead of just files tough :-)

Virtual encrypted partitions is also the preferred way when using USB thumb drives which are even easier to loose.

On Linux: [https://help.ubuntu.com/community/EncryptedFilesystemHowto#Using%20losetup](https://help.ubuntu.com/community/EncryptedFilesystemHowto#Using%20losetup)

On Windows use TrueCrypt.

### Note

For a dual boot full system disk encryption scheme I found this [howto](http://ubuntuforums.org/showthread.php?t=761530) which seems straight forward and does just that. I have however not been able to test is yet. When I have and if it works it will however be my preferred setup for laptops. The scheme requires at least Linux to be reinstalled, since nobody has made a simple way of encrypting a running Linux installation (yet).

I use TrueCrypt in Windows allowing me to mount the NTFS partitions in Linux as well. However, several of the TrueCrypt features are Windows only and there are no (as of yet) 64 bit version that I know of. Therefore I use LUKS and dm-crypt for Linux. The fact that my Windows is unable to decrypt my LUKS encrypted Linux partitions doesn't bother me much since Vista isn't really interested in reading the Linux ext3 file systems anyway.

## Backup

**Important**: When using encryption you would also want backup\!

It's a well known fact that disk drives are unreliable at best, so it's a good rule to always back up your work. Nothing bothers me more than having to figure out what bugs I've already fixed once, but have to fix again because of lost work.

Adding disk encryption also adds a layer of complexity that might cause problems. The encryption schemes mentioned here are based on encrypting block for block using chaining. This means that bad blocks are more troublesome than on normal file systems. If you screw it up it's good to know that your data is available elsewhere. Using a real encryption schemes means that if you forget your pass phrase the data might as well have been shredded.

There are a lot of Open and commercial software for backing up your system. I personally use [BackupPC](http://backuppc.sourceforge.net/) running on a Linux server. If you don't have a personal server than have a look at [Jungle Disk](http://www.jungledisk.com/) which adds a layer of encryption on top of the Amazon S3 storage system. At $0.150 per GB it is very affordable (and highly secure).

### But want backing up my data contradict the reason for encrypting it in the first place?

Well, not really... (TODO)

## Resources

- (Re)install ubuntu 8.04 with full system disk encryption - [http://learninginlinux.wordpress.com/2008/04/23/installing<sub>~ubuntu</sub><sub>804</sub><sub>with</sub><sub>full</sub><sub>disk</sub><sub>encryption/](http://learninginlinux.wordpress.com/2008/04/23/installing</sub><sub>ubuntu</sub><sub>804</sub><sub>with</sub><sub>full</sub><sub>disk</sub>~encryption/)
- Dual boot full system disk encryption - [http://ubuntuforums.org/showthread.php?t=761530](http://ubuntuforums.org/showthread.php?t=761530)
- Back up securely using TrueCrypt - [http://www.truecrypt.org/docs/?s=how<sub>~to</sub><sub>back</sub><sub>up</sub><sub>securely](http://www.truecrypt.org/docs/?s=how</sub><sub>to</sub><sub>back</sub><sub>up</sub>~securely)
- Debian full system disk encryption without reinstall (technical) - [http://linuxgazette.net/140/kapil.html](http://linuxgazette.net/140/kapil.html)
- BackupPC backup utility system [http://backuppc.sourceforge.net/](http://backuppc.sourceforge.net/)
