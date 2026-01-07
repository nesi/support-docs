---
created_at: '2020-01-14T22:10:50Z'
tags: []
---

Applying a *checksum function* to a file will return its *checksum*.
Checksum functions are a type of [hash function](https://en.wikipedia.org/wiki/Hash_function),
and will always return the same hash for any particular file contents, making them
useful for file validation. There are many different checksum functions.
The most commonly used are listed in the table below.

Checksums can be used to check for minor errors that may have been
introduced into a dataset. For example:

- After downloading a file (compare your generated checksum with the
    checksum provided by the vendor).
- When copying a file onto the cluster (generate a checksum on your
    local machine and another on the cluster).
- Verifying your results/workflow. (making a checksum of a results
    file can be a quick way to confirm nothing has changed).
- Corroborate files when working in a team.

While not necessary to do in every case, every time, file integrity
should be one of the first things you check when troubleshooting.

## Example

The file `corrupt.bin` has had 1 byte changed, yet on inspection would
appear identical.

``` out
-rw-rw-r--  1  393315  copy.bin
-rw-rw-r--  1  393315  corrupt.bin
-rw-rw-r--  1  393315  original.bin
```

By using a MD5 checksum (`md5sum *`) we can see that '`corrupt.bin`' has
diverged from the original, while '`copy.bin`' has not.

``` out
002c33835b3921d92d8074f3b392ef65 copy.bin
ef749eb4110c2a3b3c747390095d0b76 corrupt.bin
002c33835b3921d92d8074f3b392ef65 original.bin
```

Note that filename, path, permissions or any other metadata does not
affect the checksum.

!!! note
     Checksum functions are designed so that similar files *will not*
     produce similar hashes.
     You will only need to compare a few characters of the string to
     confirm validity.

## Commands

The checksum for file '*filename.txt*' can be found with the following
commands.

|         | Linux                    | Windows(CMD/Powershell)                  | Mac                          |
| ------- | ------------------------ | ---------------------------------------- | ---------------------------- |
| SHA-1   | `sha1sum filename.txt`   | `certUtil -hashfile filename.txt`        | `shasum filename.txt`        |
| SHA-256 | `sha256sum filename.txt` | `certUtil -hashfile filename.txt sha256` | `shasum -a 256 filename.txt` |
| MD5     | `md5sum filename.txt`    | `certUtil -hashfile filename.txt md5`    | `md5 filename.txt`           |
