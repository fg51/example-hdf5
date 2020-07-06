# coding: utf-8
import h5py


def main():
    with h5py.File("sample.hdf5", "w") as fout:
        group = fout.create_group("/apple")

        dataset = group.create_dataset(
            name="2020-07-06",
            shape=(10000, 10),
            dtype="i8"
        )
        print(dataset)
        print(group)
        print(fout)



if __name__ == "__main__":
    main()
