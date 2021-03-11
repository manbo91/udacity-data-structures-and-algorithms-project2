import os


def find_files(suffix, path):
    if path is None or path == "":
        return None

    if os.path.isfile(path):
        if path.endswith(suffix):
            return [path]
        else:
            return None

    paths = list()

    for p in os.listdir(path):
        file_paths = find_files(suffix, f"{path}/{p}")

        if file_paths is not None:
            for file_path in file_paths:
                paths.append(file_path)

    return paths


if __name__ == "__main__":
    # this test is based on an example directory.
    """
    ./testdir
    ./testdir/subdir1
    ./testdir/subdir1/a.c
    ./testdir/subdir1/a.h
    ./testdir/subdir2
    ./testdir/subdir2/.gitkeep
    ./testdir/subdir3
    ./testdir/subdir3/subsubdir1
    ./testdir/subdir3/subsubdir1/b.c
    ./testdir/subdir3/subsubdir1/b.h
    ./testdir/subdir4
    ./testdir/subdir4/.gitkeep
    ./testdir/subdir5
    ./testdir/subdir5/a.c
    ./testdir/subdir5/a.h
    ./testdir/t1.c
    ./testdir/t1.h
    """

    # test case 1
    output_1 = find_files(".c", ".")
    print("Pass" if sorted(output_1) == sorted(["./testdir/subdir1/a.c",
                                                "./testdir/subdir3/subsubdir1/b.c",
                                                "./testdir/subdir5/a.c",
                                                "./testdir/t1.c"]) else "Fail")

    # test case 2
    output_2 = find_files(".h", ".")
    print("Pass" if sorted(output_2) == sorted(["./testdir/subdir1/a.h",
                                                "./testdir/subdir3/subsubdir1/b.h",
                                                "./testdir/subdir5/a.h",
                                                "./testdir/t1.h"]) else "Fail")

    # test case 3
    output_3 = find_files(".gitkeep", ".")
    print("Pass" if sorted(output_3) == sorted(["./testdir/subdir2/.gitkeep",
                                                "./testdir/subdir4/.gitkeep"]) else "Fail")

    # test case 4
    output_4 = find_files(".c", "")
    print("Pass" if output_4 == None else "Fail")
