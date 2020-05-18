import numpy as np


def read_calib_file(path):
    # taken from https://github.com/hunse/kitti
    float_chars = set("0123456789.e+- ")
    data = {}
    with open(path, 'r') as f:
        for line in f.readlines():
            key, value = line.split(':', 1)
            value = value.strip()
            data[key] = value
            if float_chars.issuperset(value):
                # try to cast to float array
                try:
                    data[key] = np.array(value.split(' ')).astype(np.float)
                    print(np.array(value.split(' ')).astype(np.float))
                except ValueError:
                    # casting error: data[key] already eq. value, so pass
                    pass

    return data

def main():
    path = './dataset/depth_data/2011_09_26/calib_imu_to_velo.txt'
    data = read_calib_file(path)
    print(data['R'])

if __name__=='__main__':
    main()

