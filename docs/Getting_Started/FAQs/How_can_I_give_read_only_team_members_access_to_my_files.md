---
created_at: '2021-06-04T00:42:20Z'
tags: []
description: Instructions for giving read-only team members access to files
---

!!! tip "See also"
     [File permissions and
     groups](../../Storage/File_permissions_and_groups.md)

Not all projects have read-only groups created by default. If your
project has a read-only group created after the project itself was
created, you will need to add appropriate access control lists (ACLs) to
each of your files and directories within the project or nobackup
directory.

To do this, you can use the script `nn_add_to_acls_recursively`. The
following commands explain how to do this;  when running the commands,
replace `nesi12345` and `nesi12345r` with your project code and
read-only project code respectively.

!!! warning
     If this process is interrupted part-way through, for example due to
     your computer going to sleep and losing its connection to your NeSI
     terminal session, your files can end up in a bad way. For this reason
     please **run all the following commands in a `screen` or `tmux`
     session.**

1. Prepare a file containing the ACL to add. Ensure you include the
    `mask` line. Note that the script will not remove any of the
    existing ACL, except for overwriting existing lines that are the
    same, up to the second colon, as one of the new lines you ask to
    add.

    ```sh
    echo "mask::rwxc" > acl_to_add.txt
    echo "group:nesi12345r:r-x-" >> acl_to_add.txt
    ```

2. Check that the contents of the file are correct.

    ```sh
    cat acl_to_add.txt
    ```

3. Carry out the ACL change. You can specify a subdirectory instead if,
    as may well be the case, you don't want to trawl through the
    entirety of `/nesi/project/nesi12345` or `/nesi/nobackup/nesi12345`.

    ```sh
    nn_add_to_acls_recursively -f acl_to_add.txt /nesi/project/nesi12345
    ```

4. Check the resulting ACLs, for example:

    ```sh
    /usr/lpp/mmfs/bin/mmgetacl /nesi/project/nesi12345/some_dir
    /usr/lpp/mmfs/bin/mmgetacl -d /nesi/project/nesi12345/some_dir
    ```

    We suggest to check at least one subdirectory, at least one
    executable file (if there is one) and at least one non-executable
    file.

5. Repeat steps 3 and 4 for other directories within
    `/nesi/project/nesi12345` and `/nesi/nobackup/nesi12345`, with the
    necessary modifications.

6. Optionally, remove your ACL file.

    ```sh
    rm acl_to_add.txt
    ```

7. Optionally, exit the `screen` or `tmux` session when you are finished.
