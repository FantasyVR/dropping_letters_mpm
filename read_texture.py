from fileinput import filename
import imageio
import numpy as np


def exact_point(texture):
    w, h, d = texture.shape
    points = []
    for i in range(w):
        if texture[i].max() == 0:
            continue
        for j in range(h):
            if texture[i, j].max() == 0:
                continue
            points.append([i, j])
    return points


def compute_aabb(valid_points):
    min_x = min(valid_points[:, 0])
    min_y = min(valid_points[:, 1])
    max_x = max(valid_points[:, 0])
    max_y = max(valid_points[:, 1])
    print(f"bounding box: {min_x}, {min_y}, {max_x}, {max_y}")
    return [min_x, min_y, max_x, max_y]


def generate_random_points(texture, aabb_box):
    min_x, min_y, max_x, max_y = aabb_box
    len_x = max_x - min_x
    len_y = max_y - min_y
    scale_factor = 1.0 / max(len_x, len_y)

    num_rpoints = 10000
    rpoints = [None] * num_rpoints
    count = 0
    while (count < num_rpoints):
        rx = np.random.randint(min_x, max_x, size=num_rpoints)
        ry = np.random.randint(min_y, max_y, size=num_rpoints)
        for i in range(num_rpoints):
            if texture[rx[i], ry[i]].max() != 0 and count < num_rpoints:
                normal_point = np.array([ry[i] - min_y, min_x - rx[i]
                                         ]) * scale_factor
                rpoints[count] = normal_point + np.array([0.0, 1.0])
                print(f"{rpoints[count]}, {rx[i]},{ry[i]}")
                count += 1
    return np.asarray(rpoints)


def generate_random_samples_from_pixel_texture(file_name):
    texture = imageio.imread(file_name)
    print(f"image {file_name}'s shape: {texture.shape}")
    valid_points = np.asanyarray(exact_point(texture))
    print(f"valid number of letter points: {len(valid_points)}")
    aabb_box = compute_aabb(valid_points)
    random_points = generate_random_points(texture, aabb_box)
    print(f"num of rpoints: {random_points.shape}")
    return random_points


if __name__ == "__main__":
    texture = imageio.imread('T.png')
    print(f"image shape: {texture.shape}")
    w, h, d = texture.shape
    valid_points = np.asanyarray(exact_point(texture))
    print(f"valid number of letter points: {len(valid_points)}")
    aabb_box = compute_aabb(valid_points)
    rpoint = generate_random_points(texture, aabb_box)
    print(f"num of rpoints: {len(rpoint)}")
